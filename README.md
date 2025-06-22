# Voice Input
+ Speech to text transcription using Groq

## Description
This project is a voice input application that uses the [Groq](https://groq.com/) API to transcribe audio files. It uses the [customtkinter](https://github.com/TomSchimansky/CustomTkinter) library for the GUI.

> **Note:** Groq provides a generous **free usage tier** that’s more than enough for typical personal use.  
> No credit card is required to get started.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/arman-ar/voice-input.git
```
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. Set up the [Groq](https://groq.com/) API key in your environment variables:
```bash
# For Linux or macOS
export GROQ_API_KEY="your_api_key_here"
```
4. Run the application:
```bash
python3 main.py # for linux or mac
python main.py # for windows
```

## Usage
The application will start recording audio and transcribe it when you press the space bar. 

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.