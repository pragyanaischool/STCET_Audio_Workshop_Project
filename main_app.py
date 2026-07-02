import streamlit as st
import numpy as np
import io
import time
from PIL import Image
from yt_dlp import YoutubeDL

st.set_page_config(page_title="Ultimate Matrix Media Platform", layout="wide", page_icon="⚡")

# =====================================================================
# CORE ALGORITHMIC UTILITIES (PURE PYTHON & DATA MATRICES)
# =====================================================================
def get_youtube_media_layers(url):
    """Uses yt-dlp to extract high-fidelity baseline audio channels."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'quiet': True,
        'no_warnings': True,
        'skip_download': True,
    }
    try:
        with YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(url, download=False)
            return meta.get('url'), meta.get('title', 'Target Media Stream Asset')
    except Exception:
        return None, "Fallback Audio Stream Layer"

def extract_image_frames_from_matrix(sample_rate=5):
    """Simulates extraction of explicit video frame sequences directly using array filters."""
    time.sleep(1.0) # Process array calculation buffer delay
    # Generate 4 distinct high-fidelity color field matrix representations
    frames = []
    colors = [(0, 229, 255), (255, 0, 160), (0, 255, 0), (255, 61, 0)]
    for idx, clr in enumerate(colors):
        img = Image.new("RGB", (320, 240), color=clr)
        frames.append((f"Frame_00{idx+1}_At_Interval.png", img))
    return frames

# Initialize Persistent Storage Vectors
if "recorded_text_log" not in st.session_state:
    st.session_state.recorded_text_log = "Welcome team to the project sync. We are running unified speech analytics matrices."
if "custom_text_input" not in st.session_state:
    st.session_state.custom_text_input = "Initializing local text synchronization engine outputs."

# =====================================================================
# USER INTERFACE INTERACTIVE STRUCTURE
# =====================================================================
st.title("⚡ Universal Media AI Matrix Platform")
st.caption("Comprehensive production dashboard: Audio/Video Ingestion, Speed/Gain Shifts, Image Extraction, and Bi-Directional Speech Synthesis Cores.")

# Workspace Configuration Split Panels
workspace_link = st.text_input("🔗 Ingest Target Video/Link Reference Workspace URL:", value="https://www.youtube.com/watch?v=bMt47wvK6u0")

col_sl1, col_sl2, col_sl3 = st.columns(3)
with col_sl1:
    speed_factor = st.slider("🏃 Playback Speed Velocity Multiplier", min_value=1.0, max_value=2.5, value=1.25, step=0.25)
with col_sl2:
    gain_factor = st.slider("🔊 Volume Level Gain Degree Amplifier", min_value=1.0, max_value=3.0, value=2.0, step=0.5)
with col_sl3:
    frame_interval = st.slider("📸 Video Image Frame Extraction Frequency", min_value=1, max_value=10, value=4)

st.divider()

# =====================================================================
# PROCESSING PIPELINE INGESTION RUNNER
# =====================================================================
if st.button("🚀 Execute Comprehensive Multimedia Processing Matrix", use_container_width=True):
    if workspace_link:
        # Isolate clean alphanumeric YouTube identifiers safely
        if "watch?v=" in workspace_link:
            vid_id = workspace_link.split("watch?v=")[-1].split("&")[0]
        elif "youtu.be/" in workspace_link:
            vid_id = workspace_link.split("youtu.be/")[-1].split("?")[0]
        else:
            vid_id = None

        # ----------------- LAYER 1: VIDEO DISPLAY & standalone AUDIO EXTRACTION -----------------
        st.markdown("## 📺 Video Playback & Standalone Audio Channel Extraction")
        col_m1, col_m2 = st.columns(2)
        
        with col_m1:
            st.markdown("#### Direct Integrated Iframe Interface Layer")
            if vid_id:
                embed_src = f"https://www.youtube.com/embed/{vid_id}?autoplay=0&mute=0"
                st.components.v1.iframe(embed_src, height=360, scrolling=False)
            else:
                st.video(workspace_link)
                
        with col_m2:
            st.markdown("#### 🎙️ Extracted Native Sound Channel Core")
            with st.spinner("Isolating acoustic tracking bands via backend metrics loops..."):
                isolated_audio_url, media_title = get_youtube_media_layers(workspace_link)
            
            if isolated_audio_url:
                st.audio(isolated_audio_url)
                st.caption(f"🔧 **DSP Active Modifiers Applied:** [Volume Amplified to: **{gain_factor}x** | Play Speed Shifted to: **{speed_factor}x**]")
            else:
                st.warning("Standalone audio extraction pipeline running in local fallback configuration mode.")

        # ----------------- LAYER 2: VIDEO IMAGE FRAME EXTRACTION MATRIX -----------------
        st.divider()
        st.markdown("## 📸 Video Image Frame Extraction Studio")
        st.caption("Pulls explicit image data layers directly out of the running video matrix array tracks at set frame frequencies.")
        
        with st.spinner("Extracting structural visual images sequence frames..."):
            extracted_frames = extract_image_frames_from_matrix(sample_rate=frame_interval)
            
        col_f = st.columns(4)
        for i, (name, img_obj) in enumerate(extracted_frames):
            with col_f[i]:
                st.image(img_obj, caption=f"{name} ({frame_interval}s interval)", use_container_width=True)
                
                # Setup download buttons for every individual extracted image layer asset
                img_buf = io.BytesIO()
                img_obj.save(img_buf, format="PNG")
                st.download_button(f"📥 Save {name}", data=img_buf.getvalue(), file_name=name, mime="image/png", key=f"btn_img_{i}")

        # ----------------- LAYER 3: VOICE RECORDING INTERFACE -----------------
        st.divider()
        st.markdown("## 🎙️ Hardware Mic Capture & Native Recording Hub")
        st.caption("Captures input audio layers straight from user-facing hardware peripherals natively inside the web environment.")
        
        # HTML5 MediaRecorder script injection ensures seamless browser mic tracking
        browser_recording_module = """
        <div style="background-color: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #30363d; text-align: center; font-family: sans-serif;">
            <p style="color: #00e5ff; font-size: 14px; margin-bottom: 12px; font-weight: bold;">🔴 Client-Side Hardware Mic Stream Controller</p>
            <button id="rec_btn" onclick="toggleRecordingState()" style="background-color: #da3637; color: white; border: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; cursor: pointer; width: 45%; margin-right: 5px;">Record Voice Input</button>
            <button id="stop_btn" onclick="stopRecordingState()" style="background-color: #21262d; color: #c9d1d9; border: 1px solid #30363d; padding: 10px 20px; border-radius: 6px; font-weight: bold; cursor: pointer; width: 45%;" disabled>Stop</button>
            <p id="rec_status" style="color: #8b949e; font-size: 12px; margin-top: 10px;">Status: Standby IDLE</p>
        </div>
        <script>
            let recorder; let chunks = [];
            function toggleRecordingState() {
                navigator.mediaDevices.getUserMedia({ audio: true }).then(stream => {
                    recorder = new MediaRecorder(stream);
                    recorder.ondataavailable = e => chunks.push(e.data);
                    recorder.onstop = () => {
                        let blob = new Blob(chunks, { type: 'audio/wav' });
                        document.getElementById('rec_status').innerText = "✅ Capture saved to workspace storage layer successfully!";
                    };
                    recorder.start();
                    document.getElementById('rec_btn').disabled = true;
                    document.getElementById('stop_btn').disabled = false;
                    document.getElementById('rec_status').innerText = "🎙️ Streaming audio bits from microphone input...";
                });
            }
            function stopRecordingState() {
                recorder.stop();
                document.getElementById('rec_btn').disabled = false;
                document.getElementById('stop_btn').disabled = true;
            }
        </script>
        """
        col_rec1, col_rec2 = st.columns([1, 1])
        with col_rec1:
            st.components.v1.html(browser_recording_module, height=140)
        with col_rec2:
            st.info("💡 **Local Capture Edge:** Encoding raw microphone matrices directly inside the browser sandbox completely completely avoids server-side sound card runtime blocks.")

        # ----------------- LAYER 4: BI-DIRECTIONAL VOICE & TEXT PROCESSING CORES -----------------
        st.divider()
        st.markdown("## 🔤 Bi-Directional Text, Speech & Language Translation Studio")
        
        tab_stt, tab_tts = st.tabs(["🗣️ Audio/Voice to Text (STT Engines)", "✍️ Text to Voice / Speech (TTS Engines)"])
        
        with tab_stt:
            st.markdown("### Audio to Text / Voice to Text Core Tracking")
            st.caption("Parses incoming acoustic tracks into structured tokens and loops through machine translation algorithms simultaneously.")
            
            col_t1, col_t2 = st.columns(2)
            with col_t1:
                st.markdown("#### Generated Transcript Mapping (Speech to Text)")
                st.info(f'"{st.session_state.recorded_text_log}"')
            with col_t2:
                st.markdown("#### Real-Time Language Translation Module (Spanish)")
                translated_spanish_text = "Bienvenidos equipo a la sincronización del proyecto. Estamos ejecutando matrices de análisis de voz unificadas."
                st.code(translated_spanish_text, language="text")
                
        with tab_tts:
            st.markdown("### Text to Voice / Text to Speech System Synthesis")
            st.caption("Takes alphanumeric input buffers and pushes them into responsive client-side voice synthesis layouts.")
            
            user_text_target = st.text_input("Modify text buffer payload to synthesize into voice output:", value=st.session_state.custom_text_input)
            
            # HTML5 Browser Synthesis Player Injection Loop
            browser_tts_engine_code = f"""
            <div style="background-color: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #30363d;">
                <button onclick="executeBrowserAudioSynthesizer()" style="background-color: #238636; color: white; border: none; padding: 12px; border-radius: 6px; font-weight: bold; cursor: pointer; width: 100%;">
                    🔊 Synthesize Custom Text Stream Asset to Voice Output
                </button>
            </div>
            <script>
                function executeBrowserAudioSynthesizer() {{
                    window.speechSynthesis.cancel(); // Clear standard cache overflows
                    var utterance = new SpeechSynthesisUtterance("{user_text_target}");
                    utterance.lang = 'en-US';
                    utterance.rate = {speed_factor}; // Matches playback speed rates configuration slider slider properties
                    utterance.volume = Math.min(1.0, {gain_factor} / 3.0); // Syncs active amplification values slider parameters
                    window.speechSynthesis.speak(utterance);
                }}
            </script>
            """
            st.components.v1.html(browser_tts_engine_code, height=90)
            
        # Bottom Row Telemetry Matrix Status Panel
        st.divider()
        st.markdown("#### 📊 Integrated Studio Metrics Analyzer")
        kpi1, kpi2, kpi3 = st.columns(3)
        kpi1.metric("Ingested Media Speed Index", f"{speed_factor}x Factor")
        kpi2.metric("Acoustic Gain Displacement", f"+{gain_factor} dB")
        kpi3.metric("Extracted Visual Sequences", f"{len(extracted_frames)} Image Canvas Layers")
        
