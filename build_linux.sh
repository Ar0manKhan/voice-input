#!/usr/bin/env bash
# Legacy Linux build script using system pyinstaller
# Prefer: make build  or  bash build-binary.sh

set -euo pipefail

echo "⚠️  Warning: This script uses system pyinstaller"
echo "Recommended: make build  or  bash build-binary.sh"
echo ""

if ! command -v pyinstaller &> /dev/null; then
    echo "❌ Error: pyinstaller not found."
    echo "Install with: pip install pyinstaller"
    echo "Or use: uv add --dev pyinstaller"
    exit 1
fi

echo "📦 Building with system pyinstaller..."
rm -rf build dist
pyinstaller main.spec --clean --noconfirm

echo "✅ Build complete: dist/voice-input"
