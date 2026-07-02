import os
import tempfile
from pathlib import Path

import streamlit as st
from PIL import Image

from media_utils import (
    get_video_info,
    download_video_from_url,
)

# ----------------------------------------------------
# Streamlit Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Video & Audio Studio",
    page_icon="🎬",
    layout="wide"
)

# ----------------------------------------------------
# Create Working Directories
# ----------------------------------------------------

UPLOAD_DIR = Path("uploads")
OUTPUT_DIR = Path("outputs")
TEMP_DIR = Path("temp")

UPLOAD_DIR.mkdir(exist_ok=True)
OUTPUT_DIR.mkdir(exist_ok=True)
TEMP_DIR.mkdir(exist_ok=True)

# ----------------------------------------------------
# Title
# ----------------------------------------------------

st.title("🎬 AI Video & Audio Studio")
st.caption("Python + Streamlit + Pillow + MoviePy + Whisper")

# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Select Module",
    [
        "🏠 Home",
        "📂 Upload Video",
        "🌐 Video URL",
        "🎵 Audio",
        "🎞 Video Tools",
        "🖼 Frames",
        "📊 Analytics",
        "ℹ About",
    ],
)

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "video_path" not in st.session_state:
    st.session_state.video_path = None

if "video_name" not in st.session_state:
    st.session_state.video_name = ""

# ----------------------------------------------------
# HOME
# ----------------------------------------------------

if menu == "🏠 Home":

    st.header("Welcome")

    st.markdown("""
This application allows you to:

- Upload Videos
- Download Videos from URL
- Play Videos
- Extract Audio
- Convert Video Formats
- Convert Audio Formats
- Speech-to-Text
- Extract Frames
- Add Watermarks
- Download Results
""")

# ----------------------------------------------------
# Upload Video
# ----------------------------------------------------

elif menu == "📂 Upload Video":

    st.header("Upload Video")

    uploaded_file = st.file_uploader(
        "Choose a Video",
        type=["mp4", "avi", "mov", "mkv", "webm"]
    )

    if uploaded_file:

        save_path = UPLOAD_DIR / uploaded_file.name

        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())

        st.session_state.video_path = str(save_path)
        st.session_state.video_name = uploaded_file.name

        st.success("Video uploaded successfully.")

        st.subheader("Video Preview")
        st.video(str(save_path))

        st.subheader("Basic Information")

        file_size = save_path.stat().st_size / (1024 * 1024)

        col1, col2, col3 = st.columns(3)

        col1.metric("File Name", uploaded_file.name)
        col2.metric("Size (MB)", f"{file_size:.2f}")
        col3.metric("Format", save_path.suffix.upper())

        info = get_video_info(str(save_path))

        if info:

            st.markdown("### Detailed Information")

            c1, c2, c3 = st.columns(3)

            c1.metric("Duration", info.get("duration"))
            c2.metric("Resolution", info.get("resolution"))
            c3.metric("FPS", info.get("fps"))

            c4, c5 = st.columns(2)

            c4.metric("Audio", info.get("audio"))
            c5.metric("Codec", info.get("codec"))

# ----------------------------------------------------
# Download Video from URL
# ----------------------------------------------------

elif menu == "🌐 Video URL":

    st.header("Download Video from URL")

    url = st.text_input("Paste Video URL")

    if st.button("Download Video"):

        if url.strip() == "":
            st.warning("Please enter a URL.")

        else:

            with st.spinner("Downloading..."):

                output_file = download_video_from_url(
                    url=url,
                    output_folder=str(UPLOAD_DIR)
                )

            if output_file:

                st.success("Video downloaded successfully.")

                st.session_state.video_path = output_file
                st.session_state.video_name = os.path.basename(output_file)

                st.video(output_file)

                info = get_video_info(output_file)

                if info:

                    st.json(info)

            else:

                st.error("Unable to download video.")

# ----------------------------------------------------
# Placeholder Pages
# ----------------------------------------------------

elif menu == "🎵 Audio":
    st.info("Audio tools will be implemented in Part 2.")

elif menu == "🎞 Video Tools":
    st.info("Video tools will be implemented in Part 3.")

elif menu == "🖼 Frames":
    st.info("Frame extraction will be implemented in Part 4.")

elif menu == "📊 Analytics":
    st.info("Analytics dashboard will be implemented in Part 5.")

elif menu == "ℹ About":

    st.header("About")

    st.write(
        """
AI Video & Audio Studio

Built using:

- Streamlit
- Pillow
- MoviePy
- Faster-Whisper
- FFmpeg
- yt-dlp
"""
    )
        
