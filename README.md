# YouTube Video Summarizer

This project extracts and summarizes YouTube video transcripts using **yt-dlp**, **Whisper**, and **Google Gemini AI**.

## Features

- Extracts subtitles from YouTube videos (if available).
- Downloads audio and transcribes it using OpenAI's Whisper if subtitles are unavailable.
- Summarizes the transcript using Google's Gemini AI.
- Saves both the transcript and summary to text files.

## Installation

### Prerequisites

- Python 3.8+
- FFmpeg installed (required for `yt-dlp`)
- Whisper model dependencies

### Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/Md-Abu-Omayer-Babu/youtube_video_summerizer.git
   cd youtube_video_summerizer
   ```

2. Create a virtual environment (optional but recommended):

   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

4. Configure API key:

   - Create a `config.py` file and add your **Gemini API key**:
     ```python
     your_api_key = "YOUR_GEMINI_API_KEY"
     ```

## Usage

Run the script and enter a YouTube video URL:

```sh
python main.py
```

- If a transcript is available, it will be used for summarization.
- If no transcript is found, the script downloads and transcribes the video audio.
- The summarized content is saved in `summary.txt`.

## Requirements

Ensure the following Python libraries are installed:

- `yt-dlp` – To download YouTube videos and subtitles.
- `openai-whisper` – For transcribing audio into text.
- `google-generativeai` – To generate summaries.
- `ffmpeg` – Required for `yt-dlp` to process media files.

Install all dependencies using:

```sh
pip install -r requirements.txt
```

## Dependencies

- `yt-dlp` – Downloads YouTube audio and subtitles.
- `whisper` – Converts audio into text.
- `google-generativeai` – Generates the summary.

## License

This project is open-source under the MIT License.

## Author

Developed by [Md Abu Omayer Babu](https://github.com/Md-Abu-Omayer-Babu).

---

⭐ Star this repo if you found it useful!

