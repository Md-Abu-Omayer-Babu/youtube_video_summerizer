import yt_dlp
import whisper
import google.generativeai as genai
from config import your_api_key
import os
import warnings


# Configure Gemini API
genai.configure(api_key=your_api_key)

def get_youtube_transcript(video_url):
    """Extract transcript from YouTube if available."""
    ydl_opts = {"skip_download": True, "write_auto_sub": True, "sub_lang": "en", "quiet": True}
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        subtitles = info.get("subtitles", {})

        if "en" in subtitles:
            transcript_url = subtitles["en"][0]["url"]
            return transcript_url
        else:
            return None

def download_audio(video_url):
    """Download YouTube video audio if transcript is unavailable."""
    print("Downloading audio...")
    filename = "video_audio"  # Prevents double .mp3 issue
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": filename,  # No .mp3 to prevent double extension issue
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192"
            }
        ],
        "noplaylist": True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    final_filename = filename + ".mp3"
    
    if os.path.exists(final_filename):
        print(f"Audio downloaded successfully as {final_filename}")
        return final_filename
    else:
        raise FileNotFoundError("Audio download failed!")

def transcribe_audio(audio_file):
    """Transcribe audio using Whisper."""
    print("Transcribing audio...")
    # model = whisper.load_model("base")
    
    warnings.filterwarnings("ignore", category=UserWarning)  # Suppress FP16 warning
    model = whisper.load_model("base")
    
    result = model.transcribe(audio_file)
    return result["text"]

def summarize_with_gemini(transcript):
    """Summarize transcript using Gemini API."""
    model = genai.GenerativeModel("gemini-pro")
    prompt = f"Summarize the following YouTube video transcript:\n\n{transcript}"
    response = model.generate_content(prompt)
    return response.text

def main():
    video_url = input("Enter YouTube video URL: ")

    # Step 1: Try to get transcript
    transcript = get_youtube_transcript(video_url)
    
    if transcript:
        print("Transcript found, summarizing...")
    else:
        print("No transcript found. Downloading and transcribing audio...")
        audio_file = download_audio(video_url)
        transcript = transcribe_audio(audio_file)
    
    # Save transcript
    with open("transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript)

    # Step 2: Summarize transcript
    summary = summarize_with_gemini(transcript)

    # Save summary
    with open("summary.txt", "w", encoding="utf-8") as f:
        f.write(summary)

    print("Summary saved to summary.txt")

if __name__ == "__main__":
    main()
