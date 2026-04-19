#!/usr/bin/env bash
set -euo pipefail

echo "🔨 Building voice-input binary..."

# Detect OS
OS=$(uname -s)
ARCH=$(uname -m)
echo "📦 Building for: $OS ($ARCH)"

# Clean previous builds
rm -rf build dist

# Ensure PyInstaller is available
if ! uv run pyinstaller --version &>/dev/null; then
    echo "❌ PyInstaller not found. Installing..."
    uv add --dev pyinstaller
fi

# Build with verbose output
echo "📦 Running PyInstaller..."
uv run pyinstaller main.spec --clean --noconfirm

# Verify build
if [[ ! -f "dist/voice-input" ]]; then
    echo "❌ Build failed - binary not found"
    exit 1
fi

# Get binary size
SIZE=$(du -h dist/voice-input | cut -f1)
echo ""
echo "✅ Build complete!"
echo "📁 Binary: dist/voice-input ($SIZE)"
echo ""
echo "To test:"
echo "  ./dist/voice-input"
echo ""
echo "To install system-wide:"
echo "  cp dist/voice-input ~/.local/bin/"
