#!/bin/bash
# Capture title slide from slides.html
# Usage: ./capture-title-slide.sh [width] [height]

WIDTH=${1:-1920}
HEIGHT=${2:-1080}
ASPECT_RATIO="${WIDTH}x${HEIGHT}"

# Render the slides first
echo "Rendering slides..."
quarto render slides.qmd

# Capture screenshot using Chrome headless
echo "Capturing screenshot at ${ASPECT_RATIO}..."
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless \
  --disable-gpu \
  --screenshot="media/slides-preview.png" \
  --window-size=${ASPECT_RATIO} \
  --hide-scrollbars \
  --force-device-scale-factor=1 \
  "file://$(pwd)/docs/slides.html#/title-slide"

echo "Screenshot saved to media/slides-preview.png"

# Optional: Create a 16:9 aspect ratio version (common for embeds)
echo ""
echo "For 16:9 aspect ratio (1280x720), run:"
echo "./capture-title-slide.sh 1280 720"
