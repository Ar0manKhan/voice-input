.PHONY: all build clean install test dev

# Default target
all: build

# Development setup
dev:
	@echo "🐍 Setting up development environment..."
	uv sync --dev
	@echo "✅ Setup complete. Run with: uv run main.py"

# Build the binary
build:
	@echo "🔨 Building voice-input binary..."
	@bash build-binary.sh

# Quick build without cleaning (faster)
quick:
	@echo "🔨 Quick build (no clean)..."
	uv run pyinstaller main.spec --noconfirm
	@echo "✅ Build complete: dist/voice-input"

# Clean build artifacts
clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -rf build dist __pycache__ *.egg-info .pytest_cache .mypy_cache
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	@echo "✅ Clean complete"

# Install binary to ~/.local/bin
install: build
	@echo "📦 Installing to ~/.local/bin..."
	@mkdir -p ~/.local/bin
	cp dist/voice-input ~/.local/bin/
	@chmod +x ~/.local/bin/voice-input
	@echo "✅ Installed to ~/.local/bin/voice-input"
	@echo "   Make sure ~/.local/bin is in your PATH"

# Test run
test:
	@echo "🧪 Running application..."
	uv run main.py

# Run the built binary
test-binary: build
	@echo "🧪 Testing built binary..."
	./dist/voice-input

# Build for Linux (in Docker) - for distribution
build-linux:
	@echo "🐳 Building for Linux via Docker..."
	docker run --rm -v "$(PWD):/src" -w /src python:3.12-slim bash -c \
		"pip install uv && uv sync --dev && uv run pyinstaller main.spec"
	@echo "✅ Linux build complete"

# Release build (optimized, no debug)
release: clean
	@echo "🚀 Release build..."
	@OPTIMIZE=2 bash build-binary.sh
