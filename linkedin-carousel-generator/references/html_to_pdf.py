#!/usr/bin/env python3
"""
html_to_pdf.py — render a carousel HTML file (one <section class="slide"> per slide,
built from html-boilerplate.html) into a LinkedIn-ready PDF, one square page per slide.

Fast path: a SINGLE headless Google Chrome launch prints the whole file to PDF, using an
injected print stylesheet that makes every slide its own 1080x1080 page with exact colors
and Google Fonts loaded. One Chrome start (a few seconds) instead of one per slide.

Usage:
    python3 html_to_pdf.py input.html [output.pdf]

If output.pdf is omitted, it is written next to the input with a .pdf extension.
Requirements (all already on this machine): Google Chrome. Pillow optional (only for the
PNG fallback). Falls back to a clear message if Chrome isn't found.
"""
import os
import re
import sys
import shutil
import tempfile
import subprocess

CHROME_CANDIDATES = [
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    shutil.which("google-chrome") or "",
    shutil.which("chromium") or "",
    shutil.which("chrome") or "",
]

# Injected just before </head>. Makes each .slide its own 1080x1080 print page,
# keeps background colors/images (paper + orange), strips the on-screen body chrome.
PRINT_CSS = """
<style id="__pdf_export__">
  @page { size: 1080px 1080px; margin: 0; }
  @media print {
    html, body { margin: 0 !important; padding: 0 !important; background: transparent !important; }
    body { display: block !important; gap: 0 !important; }
    * { -webkit-print-color-adjust: exact !important; print-color-adjust: exact !important; }
    .slide {
      width: 1080px !important; height: 1080px !important;
      margin: 0 !important; box-shadow: none !important;
      page-break-after: always; break-after: page;
    }
    .slide:last-child { page-break-after: auto; break-after: auto; }
  }
</style>
"""


def find_chrome():
    for c in CHROME_CANDIDATES:
        if c and os.path.exists(c):
            return c
    return None


def inject_print_css(html):
    if re.search(r"</head>", html, re.I):
        return re.sub(r"</head>", PRINT_CSS + "</head>", html, count=1, flags=re.I)
    return PRINT_CSS + html  # no <head>: prepend so it still applies


def page_count(pdf_path):
    """Cheap page count by scanning the PDF for /Type /Page objects."""
    try:
        with open(pdf_path, "rb") as f:
            data = f.read()
        return len(re.findall(rb"/Type\s*/Page[^s]", data)) or len(re.findall(rb"/Page\b", data))
    except Exception:
        return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 html_to_pdf.py input.html [output.pdf]")
        sys.exit(1)
    in_path = os.path.abspath(sys.argv[1])
    out_path = os.path.abspath(sys.argv[2]) if len(sys.argv) > 2 else os.path.splitext(in_path)[0] + ".pdf"

    chrome = find_chrome()
    if not chrome:
        print("ERROR: Google Chrome / Chromium not found. Manual fallback:")
        print("  open the HTML in a browser, screenshot each section at 1080x1080, merge to a PDF.")
        sys.exit(2)

    with open(in_path, encoding="utf-8") as f:
        html = f.read()
    n_slides = len(re.findall(r"<section\b", html, re.I))
    print_html = inject_print_css(html)

    workdir = tempfile.mkdtemp(prefix="carousel_pdf_")
    try:
        tmp_html = os.path.join(workdir, "print.html")
        with open(tmp_html, "w", encoding="utf-8") as f:
            f.write(print_html)
        cmd = [
            chrome,
            "--headless=new",
            "--disable-gpu",
            "--no-pdf-header-footer",
            "--no-margins",
            f"--user-data-dir={os.path.join(workdir, 'profile')}",
            "--virtual-time-budget=8000",     # one wait, for fonts + layout across all slides
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={out_path}",
            "file://" + tmp_html,
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if not os.path.exists(out_path):
            print("ERROR: Chrome did not produce a PDF.")
            print(res.stderr[-800:])
            sys.exit(2)
    finally:
        shutil.rmtree(workdir, ignore_errors=True)

    pages = page_count(out_path)
    suffix = f" ({pages} pages)" if pages else ""
    print(f"OK: {n_slides} slides -> {out_path}{suffix}")


if __name__ == "__main__":
    main()
