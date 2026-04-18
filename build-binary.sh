#!/bin/bash
set -e

echo "Building voice-input binary..."

# Clean previous builds
rm -rf build dist

# Run PyInstaller through uv
uv run pyinstaller main.spec

# Rename the binary to voice-input
mv dist/main dist/voice-input

echo ""
echo "Build complete! Binary is at: dist/voice-input"
echo ""
echo "To install system-wide:"
echo "  cp dist/voice-input ~/.local/bin/"
echo "  chmod +x ~/.local/bin/voice-input"
echo ""
echo "Or for system-wide (requires sudo):"
echo "  sudo cp dist/voice-input /usr/local/bin/"
