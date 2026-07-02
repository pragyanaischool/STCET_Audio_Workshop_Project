"""
=========================================================
AI Video & Audio Studio
media_utils.py (Part 1)
=========================================================
"""

import os
import subprocess
from pathlib import Path
from PIL import Image
from moviepy import VideoFileClip
import yt_dlp


# ----------------------------------------------------------
# Create Folder
# ----------------------------------------------------------

def ensure_directory(folder):
    """Create directory if it does not exist."""
    Path(folder).mkdir(parents=True, exist_ok=True)


# ----------------------------------------------------------
# File Size Formatter
# ----------------------------------------------------------

def format_file_size(size):
    """
    Convert bytes into readable format.
    """

    if size < 1024:
        return f"{size} Bytes"

    elif size < 1024 ** 2:
        return f"{size/1024:.2f} KB"

    elif size < 1024 ** 3:
        return f"{size/(1024**2):.2f} MB"

    else:
        return f"{size/(1024**3):.2f} GB"


# ----------------------------------------------------------
# Video Metadata
# ----------------------------------------------------------

def get_video_info(video_path):
    """
    Read video information using MoviePy.
    """

    try:

        clip = VideoFileClip(video_path)

        width = int(clip.w)
        height = int(clip.h)

        duration = round(clip.duration, 2)
        fps = round(clip.fps, 2)

        audio = "Yes" if clip.audio else "No"

        info = {
            "duration": f"{duration} sec",
            "resolution": f"{width} x {height}",
            "fps": fps,
            "audio": audio,
            "codec": "Unknown"
        }

        clip.close()

        return info

    except Exception as e:

        print(e)
        return None


# ----------------------------------------------------------
# Save Uploaded Video
# ----------------------------------------------------------

def save_uploaded_video(uploaded_file, upload_folder="uploads"):
    """
    Save uploaded Streamlit file.
    """

    ensure_directory(upload_folder)

    save_path = os.path.join(upload_folder, uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.read())

    return save_path


# ----------------------------------------------------------
# Download Video from URL
# ----------------------------------------------------------

def download_video_from_url(
    url,
    output_folder="uploads"
):
    """
    Download video using yt-dlp.
    """

    ensure_directory(output_folder)

    ydl_opts = {
        "outtmpl": os.path.join(
            output_folder,
            "%(title)s.%(ext)s"
        ),
        "format": "best"
    }

    try:

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

            filename = ydl.prepare_filename(info)

            return filename

    except Exception as e:

        print(e)
        return None


# ----------------------------------------------------------
# Thumbnail Generator
# ----------------------------------------------------------

def create_thumbnail(
    video_path,
    output_folder="outputs"
):
    """
    Create thumbnail at 1 second.
    """

    ensure_directory(output_folder)

    try:

        clip = VideoFileClip(video_path)

        frame = clip.get_frame(1)

        image = Image.fromarray(frame)

        output_path = os.path.join(
            output_folder,
            "thumbnail.jpg"
        )

        image.save(output_path)

        clip.close()

        return output_path

    except Exception as e:

        print(e)
        return None


# ----------------------------------------------------------
# Video Exists
# ----------------------------------------------------------

def video_exists(path):

    if path is None:
        return False

    return os.path.exists(path)


# ----------------------------------------------------------
# Delete File
# ----------------------------------------------------------

def delete_file(path):

    try:

        if os.path.exists(path):
            os.remove(path)

    except Exception:
        pass


# ----------------------------------------------------------
# List Videos
# ----------------------------------------------------------

def list_uploaded_videos(folder="uploads"):

    ensure_directory(folder)

    videos = []

    for file in os.listdir(folder):

        if file.lower().endswith(
            (
                ".mp4",
                ".avi",
                ".mov",
                ".mkv",
                ".webm"
            )
        ):

            videos.append(
                os.path.join(folder, file)
            )

    return videos


# ----------------------------------------------------------
# Get Video Name
# ----------------------------------------------------------

def get_filename(path):

    return os.path.basename(path)


# ----------------------------------------------------------
# Get Extension
# ----------------------------------------------------------

def get_extension(path):

    return Path(path).suffix.lower()


# ----------------------------------------------------------
# Is Video
# ----------------------------------------------------------

def is_video(path):

    return get_extension(path) in [
        ".mp4",
        ".avi",
        ".mov",
        ".mkv",
        ".webm"
    ]


# ----------------------------------------------------------
# Run FFmpeg Command
# ----------------------------------------------------------

def run_ffmpeg(command):

    try:

        subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )

        return True

    except Exception as e:

        print(e)

        return False
