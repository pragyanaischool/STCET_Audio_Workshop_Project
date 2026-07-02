
# app.py
"""Simplified production-ready Streamlit application compatible with media_utils.py.
This file preserves the module layout of the original project while fixing
session-state handling, parameter names, and error handling.
"""

import io
import pandas as pd
import streamlit as st
import media_utils as utils

st.set_page_config(page_title="Universal AI Video Audio Studio",
                   page_icon="⚡",
                   layout="wide")

utils.initialize_platform_directories()

defaults = {
    "uploaded_file_bytes": None,
    "uploaded_file_name": "",
    "processed_transcript_log": utils.generate_text_transcript_export(),
}
for k,v in defaults.items():
    st.session_state.setdefault(k,v)

st.sidebar.title("⚡ AI Media Studio")
page = st.sidebar.radio(
    "Module",
    [
        "Dashboard",
        "Upload",
        "Audio",
        "Speech",
        "Watermark",
        "Frames",
        "Analytics",
        "Downloads",
    ],
)

speed = st.sidebar.slider("Speed",0.5,2.0,1.0,0.25)
gain = st.sidebar.slider("Volume",0.5,3.0,1.0,0.5)

if page=="Dashboard":
    st.title("Universal AI Video Audio Studio")
    st.success("Application initialized successfully.")

elif page=="Upload":
    st.title("Upload Media")
    file=st.file_uploader("Upload",type=["wav","mp3","mp4","avi","mkv","mov"])
    if file:
        st.session_state.uploaded_file_bytes=file.read()
        st.session_state.uploaded_file_name=file.name
        st.success(file.name)
        ext=file.name.lower().split(".")[-1]
        if ext in ("wav","mp3"):
            st.audio(st.session_state.uploaded_file_bytes)
        else:
            st.video(st.session_state.uploaded_file_bytes)

elif page=="Audio":
    st.title("Audio Processing")
    if st.session_state.uploaded_file_bytes is None:
        st.warning("Upload media first.")
    else:
        if st.button("Process Audio"):
            result=utils.process_audio_matrix_dsp(
                uploaded_file_bytes=st.session_state.uploaded_file_bytes,
                speed_factor=speed,
                gain_factor=gain,
            )
            st.success(result["log"])
            st.audio(result["binary_payload"])
            st.download_button(
                "Download WAV",
                result["binary_payload"],
                "processed.wav",
                "audio/wav"
            )

elif page=="Speech":
    st.title("Speech")
    st.text_area(
        "Transcript",
        st.session_state.processed_transcript_log,
        height=200
    )
    st.download_button(
        "Download Transcript",
        st.session_state.processed_transcript_log,
        "transcript.txt"
    )

elif page=="Watermark":
    st.title("Watermark")
    text=st.text_input("Text","CONFIDENTIAL")
    pos=st.selectbox("Position",
        ["Center Center","Top Left","Bottom Right"])
    size=st.slider("Size",12,40,20)
    alpha=st.slider("Opacity",50,255,140)
    if st.button("Generate"):
        img=utils.apply_canvas_text_watermark(
            text,pos,size,alpha
        )
        st.image(img)
        b=io.BytesIO()
        img.save(b,format="PNG")
        st.download_button(
            "Download",
            b.getvalue(),
            "watermark.png",
            "image/png"
        )

elif page=="Frames":
    st.title("Frame Extraction")
    if st.button("Extract"):
        frames=utils.run_matrix_frame_extraction()
        cols=st.columns(4)
        for i,(name,img) in enumerate(frames):
            with cols[i%4]:
                st.image(img,caption=name,use_container_width=True)
        z=utils.compile_extracted_frames_to_zip(frames)
        st.download_button(
            "Download ZIP",
            z,
            "frames.zip",
            "application/zip"
        )

elif page=="Analytics":
    st.title("Analytics")
    info=utils.generate_telemetry_analytics_sheet(
        filename=st.session_state.uploaded_file_name,
        file_size_bytes=len(st.session_state.uploaded_file_bytes)
        if st.session_state.uploaded_file_bytes else None
    )
    st.dataframe(
        pd.DataFrame(info.items(),columns=["Property","Value"]),
        use_container_width=True,
        hide_index=True
    )

elif page=="Downloads":
    st.title("Downloads")
    if st.session_state.uploaded_file_bytes:
        st.download_button(
            "Original File",
            st.session_state.uploaded_file_bytes,
            st.session_state.uploaded_file_name
        )
        st.download_button(
            "Transcript",
            st.session_state.processed_transcript_log,
            "transcript.txt"
        )
    else:
        st.info("Upload a file first.")

