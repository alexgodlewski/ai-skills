// paper_ocr.swift: reads text from scans on this Mac, using the text recognition built into macOS (Vision).
// Nothing is sent anywhere. Usage: paper_ocr <output-folder> <file> [<file> ...]
// Writes <output-folder>/<file name>.txt with a "=== Page N ===" line before each page.
import Foundation
import Vision
import PDFKit
import ImageIO
import CoreGraphics

func recognize(_ image: CGImage) -> String {
    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.automaticallyDetectsLanguage = true
    let handler = VNImageRequestHandler(cgImage: image, options: [:])
    do { try handler.perform([request]) } catch { return "[could not read this page: \(error.localizedDescription)]" }
    let obs = (request.results ?? []).sorted {
        // top to bottom, then left to right
        let a = $0.boundingBox, b = $1.boundingBox
        if abs(a.midY - b.midY) > 0.01 { return a.midY > b.midY }
        return a.minX < b.minX
    }
    return obs.compactMap { $0.topCandidates(1).first?.string }.joined(separator: "\n")
}

func render(_ page: PDFPage) -> CGImage? {
    let box = page.bounds(for: .mediaBox)
    let scale = 2200.0 / max(box.width, box.height)   // about 200 dpi on a letter page
    let w = Int(box.width * scale), h = Int(box.height * scale)
    guard let ctx = CGContext(data: nil, width: w, height: h, bitsPerComponent: 8, bytesPerRow: 0,
                              space: CGColorSpaceCreateDeviceRGB(),
                              bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue) else { return nil }
    ctx.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
    ctx.fill(CGRect(x: 0, y: 0, width: w, height: h))
    ctx.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: ctx)
    return ctx.makeImage()
}

let args = CommandLine.arguments
guard args.count >= 3 else { print("Usage: paper_ocr <output-folder> <file> [<file> ...]"); exit(1) }
let outDir = URL(fileURLWithPath: args[1])
try? FileManager.default.createDirectory(at: outDir, withIntermediateDirectories: true)

for path in args[2...] {
    let url = URL(fileURLWithPath: path)
    let outFile = outDir.appendingPathComponent(url.lastPathComponent + ".txt")
    var text = ""
    if url.pathExtension.lowercased() == "pdf" {
        guard let pdf = PDFDocument(url: url) else { print("SKIP (cannot open): \(path)"); continue }
        for i in 0..<pdf.pageCount {
            guard let page = pdf.page(at: i) else { continue }
            let embedded = (page.string ?? "").trimmingCharacters(in: .whitespacesAndNewlines)
            var body = embedded
            if embedded.count < 30, let img = render(page) { body = recognize(img) }   // a scan has no real text: read the picture
            text += "=== Page \(i + 1) ===\n\(body)\n\n"
        }
    } else {
        guard let src = CGImageSourceCreateWithURL(url as CFURL, nil) else { print("SKIP (cannot open): \(path)"); continue }
        let n = CGImageSourceGetCount(src)
        for i in 0..<max(n, 1) {
            // the thumbnail call applies the photo's rotation (phones store photos sideways)
            let opts: [CFString: Any] = [kCGImageSourceCreateThumbnailFromImageAlways: true,
                                         kCGImageSourceCreateThumbnailWithTransform: true,
                                         kCGImageSourceThumbnailMaxPixelSize: 4000]
            guard let img = CGImageSourceCreateThumbnailAtIndex(src, i, opts as CFDictionary) else { continue }
            text += "=== Page \(i + 1) ===\n\(recognize(img))\n\n"
        }
    }
    try? text.write(to: outFile, atomically: true, encoding: .utf8)
    print("OK \(url.lastPathComponent)")
}
