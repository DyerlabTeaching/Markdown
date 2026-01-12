#!/usr/bin/env python3
"""
Generate a preview image of the title slide from slides.qmd
Requires: pip install playwright && playwright install chromium
"""

import subprocess
import sys
from pathlib import Path

def render_slides():
    """Render slides.qmd to HTML"""
    print("Rendering slides...")
    result = subprocess.run(["quarto", "render", "slides.qmd"],
                          capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error rendering slides: {result.stderr}")
        sys.exit(1)
    print("Slides rendered successfully")

def capture_screenshot_with_chrome(width=1280, height=720):
    """Capture screenshot using Chrome headless"""
    output_file = Path("media/slides-preview.png")
    slides_html = Path("docs/slides.html").absolute()

    if not slides_html.exists():
        print(f"Error: {slides_html} not found. Run quarto render first.")
        sys.exit(1)

    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        f"--screenshot={output_file}",
        f"--window-size={width},{height}",
        "--hide-scrollbars",
        "--force-device-scale-factor=1",
        f"file://{slides_html}#/title-slide"
    ]

    print(f"Capturing screenshot at {width}x{height}...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if output_file.exists():
        size_kb = output_file.stat().st_size / 1024
        print(f"Screenshot saved: {output_file} ({size_kb:.1f} KB)")
    else:
        print("Error: Screenshot not created")
        sys.exit(1)

def main():
    """Main function"""
    # Parse arguments
    width = int(sys.argv[1]) if len(sys.argv) > 1 else 1280
    height = int(sys.argv[2]) if len(sys.argv) > 2 else 720

    # Ensure media directory exists
    Path("media").mkdir(exist_ok=True)

    # Render and capture
    render_slides()
    capture_screenshot_with_chrome(width, height)

    print("\nCommon aspect ratios:")
    print("  16:9 HD:    ./capture-title-slide.py 1920 1080")
    print("  16:9 Web:   ./capture-title-slide.py 1280 720")
    print("  4:3:        ./capture-title-slide.py 1024 768")
    print("  Square:     ./capture-title-slide.py 1200 1200")

if __name__ == "__main__":
    main()
