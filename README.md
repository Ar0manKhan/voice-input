# Voice Input

Speech-to-text transcription using Groq API. A simple, fast voice input application with a modern GUI.

> **Note:** Groq provides a generous **free usage tier** that's more than enough for typical personal use. No credit card is required to get started.

## Features

- 🎙️ One-click voice recording (Space bar to toggle)
- ⚡ Fast transcription using Groq's Whisper API
- 📋 Automatic clipboard copy of transcribed text
- 🖥️ Modern GUI with customtkinter
- 🔒 API key from environment variable or `.env` file

## Prerequisites

### 1. Install uv

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. System Dependencies (for PyAudio)

**Ubuntu/Debian:**
```bash
sudo apt-get install portaudio19-dev python3-pyaudio
```

**macOS:**
```bash
brew install portaudio
```

**Fedora/RHEL:**
```bash
sudo dnf install portaudio-devel
```

## Quick Start

One command to get everything running:

```bash
# Clone and setup
git clone https://github.com/arman-ar/voice-input.git
cd voice-input

# Install dependencies and run (uv handles everything!)
uv run --extra audio main.py
```

That's it! The application will start and you can begin recording.

## Setup API Key

The application needs a Groq API key. Set it via environment variable:

```bash
export GROQ_API_KEY="your_api_key_here"
```

Or create a `.env` file in the project root:

```bash
echo "GROQ_API_KEY=your_api_key_here" > .env
```

Get your API key at: https://console.groq.com/

## Development

### Install all dependencies (including dev)

```bash
uv sync --all-extras
```

### Run the application

```bash
uv run main.py
```

### Update dependencies

```bash
uv lock --upgrade
```

## Building a Binary Executable

Build a standalone binary that you can place in your `~/.local/bin` or `/usr/local/bin`:

```bash
# Build the binary
uv run build-binary.sh
```

This creates `dist/voice-input` which is a fully standalone executable.

### Install the binary system-wide

```bash
# Copy to local bin (user)
cp dist/voice-input ~/.local/bin/
chmod +x ~/.local/bin/voice-input

# Or system-wide (requires sudo)
sudo cp dist/voice-input /usr/local/bin/
```

Now you can run `voice-input` from anywhere!

## Usage

1. Start the application
2. Press **Space** to start recording
3. Speak your message
4. Press **Space** again to stop
5. The transcription is automatically copied to your clipboard
6. Press **Escape** to exit

## Project Structure

```
voice-input/
├── main.py              # Application entry point
├── audio_recorder.py    # Audio recording logic
├── groq_services.py     # Groq API integration
├── pyproject.toml       # Project configuration (uv)
├── uv.lock              # Locked dependency versions
└── build-binary.sh      # Script to build executable
```

## Troubleshooting

**PyAudio installation fails:**
- Make sure you installed the system dependencies (portaudio)
- On some systems, you may need to use `uv pip install pyaudio` separately

**API key not found:**
- Ensure `GROQ_API_KEY` is set in your environment or `.env` file
- Check that the key is valid at https://console.groq.com/

**Binary doesn't work on another machine:**
- The binary is built for your specific architecture
- For distribution, users need matching OS and architecture
- System dependencies (portaudio) may still be needed on the target machine

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.