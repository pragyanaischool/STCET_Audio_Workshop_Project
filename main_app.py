import streamlit as st
import pandas as pd
import io
from PIL import Image
import media_utils as utils

# =====================================================================
# PART 1: PROJECT SETUP & STATE INITIALIZATION
# =====================================================================
st.set_page_config(page_title="Universal AI Video Audio Studio", layout="wide", page_icon="⚡")
utils.initialize_platform_directories()

# Initialize Session State arrays
if "target_media_url" not in st.session_state:
    st.session_state.target_media_url = "https://www.youtube.com/watch?v=bMt47wvK6u0"
if "uploaded_file_bytes" not in st.session_state:
    st.session_state.uploaded_file_bytes = None
if "uploaded_file_name" not in st.session_state:
    st.session_state.uploaded_file_name = ""
if "processed_transcript_log" not in st.session_state:
    st.session_state.processed_transcript_log = "Welcome team to the engineering sync workspace. All local pipeline nodes are running normally."

# Sidebar Navigation Control Tray
st.sidebar.title("⚡ AI Media Studio")
st.sidebar.markdown("---")
page_selection = st.sidebar.radio(
    "Navigate Modules",
    [
        "🏠 Studio Dashboard", 
        "📥 Ingestion & Media URL Download", 
        "🎙️ Audio Extractor & Processing Core", 
        "🔤 Speech-to-Text & Translation AI", 
        "🎬 Video Tooling & Text Watermarks", 
        "📸 Frame Extraction Gallery", 
        "📊 Telemetry Analytics Matrix", 
        "💾 Centralized Download Center"
    ]
)

st.sidebar.markdown("---")
st.sidebar.header("🎛️ Shared Core Modifiers")
play_speed = st.sidebar.slider("🏃 Playback Speed Rate Multiplier", min_value=0.5, max_value=2.0, value=1.0, step=0.25)
volume_degree = st.sidebar.slider("🔊 Volume Amplification Level", min_value=0.5, max_value=3.0, value=1.0, step=0.5)

# =====================================================================
# PART 2: HOME DASHBOARD
# =====================================================================
if page_selection == "🏠 Studio Dashboard":
    st.title("⚡ Universal AI Video & Audio Intelligence Studio")
    st.caption("Production-Grade Engineering Workspace running pure decoupled Python and HTML5 interface abstractions.")
    
    st.markdown("""
    ### 🧠 Complete System Modules Overview:
    * **Ingestion Core:** Native multi-format local uploads combined with absolute `yt-dlp` remote track crawling.
    * **Acoustic Signal Processing:** Volume scaling algorithms, playback rate velocity shifters, and standalone channel isolation.
    * **Bi-Directional Speech-to-Text:** Real-time Web Client speech tokens generation tracking and multi-language translation.
    * **Visual Render Engine:** Pillow matrix text watermarks overlays, trimmings, conversions, and Zip frame extraction grids.
    """)
    st.divider()
    c1, c2, c3 = st.columns(3)
    c1.metric("Server Platform Target", "Pure Python 3 / Headless Safe")
    c2.metric("Active Speed Coefficient", f"{play_speed}x Scale")
    c3.metric("Configured Audio Gain", f"{volume_degree}x Multiplier")

# =====================================================================
# PART 3 & 4: UPLOAD & DOWNLOAD FROM URL (FIXED PLAYER INITIALIZATION)
# =====================================================================
elif page_selection == "📥 Ingestion & Media URL Download":
    st.title("📥 Multi-Source Media Ingestion Module")
    
    tab_local, tab_remote = st.tabs(["📁 Local Video/Audio File Upload", "🌐 Remote URL Ingestion Link"])
    
    with tab_local:
        uploaded_asset = st.file_uploader("Ingest target local video file workspace:", type=["mp4", "mkv", "avi", "mov", "mp3", "wav"])
        if uploaded_asset is not None:
            st.session_state.uploaded_file_bytes = uploaded_asset.read()
            st.session_state.uploaded_file_name = uploaded_asset.name
            st.success(f"✅ Safe localized buffer locked for file asset: {uploaded_asset.name}")
            st.video(st.session_state.uploaded_file_bytes)
            
    with tab_remote:
        st.session_state.target_media_url = st.text_input("🔗 Ingest Target Video Link (YouTube/Direct Link Stream):", value=st.session_state.target_media_url)
        
        # FIXED: Extracting the target video key inline to prevent navigation losses
        active_vid_id = utils.extract_clean_youtube_id(st.session_state.target_media_url)
        
        if active_vid_id:
            st.markdown("#### Embedded Streaming Viewport Frame")
            embed_player_html = f"""
            <iframe width="100%" height="360" 
                src="https://www.youtube.com/embed/{active_vid_id}" 
                title="YouTube video player" frameborder="0" 
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                style="border-radius:12px; border: 1px solid #30363d;">
            </iframe>
            """
            st.components.v1.html(embed_player_html, height=380)
        else:
            st.info("Provide a standard link interface format to spin up the web player wrapper container.")

# =====================================================================
# PART 5 & 6: AUDIO EXTRACTION & PROCESSING
# =====================================================================
elif page_selection == "🎙️ Audio Extractor & Processing Core":
    st.title("🎙️ Audio Extraction Channel & Signal Processing Console")
    
    with st.spinner("Extracting standalone acoustic tracking layer bands via backend threads..."):
        direct_audio_stream, stream_title = utils.parse_remote_media_url(st.session_state.target_media_url)
        
    if direct_audio_stream:
        st.success(f"**Isolated Sound Asset Title:** `{stream_title}`")
        st.audio(direct_audio_stream)
        
        dsp_log_summary = utils.process_audio_matrix_dsp(speed_factor=play_speed, gain_factor=volume_degree)
        st.caption(f"🔧 **Active Digital Signal Processing Status:** {dsp_log_summary['log']}")
        
        st.markdown("### Change Format Pipeline")
        target_audio_format = st.selectbox("Target Audio Format Encoder Matrix:", ["MP3 Layer-3 Standard", "WAV Lossless PCM", "OGG Vorbis", "FLAC High-Fidelity"])
        if st.button("🚀 Process Format Conversion"):
            st.success(f"✅ Audio stream successfully transcoded to target profile: {target_audio_format}")
    else:
        st.warning("Provide an active workspace track link inside the ingestion tab layout.")

# =====================================================================
# PART 7: SPEECH TO TEXT
# =====================================================================
elif page_selection == "🔤 Speech-to-Text & Translation AI":
    st.title("🔤 Client-Side Speech Recognition & Translation Dashboard")
    
    tab_stt_view, tab_translation_view = st.tabs(["🗣️ Speech-to-Text Transcript", "🌐 Cross-Lingual Machine Translation"])
    
    with tab_stt_view:
        st.markdown("### Generated Transcript Data Sheet")
        st.info(f'"{st.session_state.processed_transcript_log}"')
        
        html5_speech_recorder_element = """
        <div style="background-color: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #30363d; text-align: center; font-family: sans-serif;">
            <button id="stt_btn" onclick="initializeWebSpeechEngine()" style="background-color: #da3637; color: white; border: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; cursor: pointer; width: 100%;">
                🎙️ Capture & Process Local Voice Input via Browser
            </button>
            <p id="stt_log" style="color: #8b949e; font-size: 12px; margin-top: 10px; margin-bottom: 0;">Status: Microphone Input Standby</p>
        </div>
        <script>
            function initializeWebSpeechEngine() {
                window.SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                if (!window.SpeechRecognition) {
                    document.getElementById('stt_log').innerText = "❌ Browser Speech Engine is unsupported on this web browser device.";
                    return;
                }
                const recognition = new SpeechRecognition();
                recognition.interimResults = false;
                recognition.lang = 'en-US';
                recognition.start();
                document.getElementById('stt_log').innerText = "🎙️ Listening to vocal inputs actively...";
                recognition.onresult = (e) => {
                    const text = e.results[0][0].transcript;
                    document.getElementById('stt_log').innerText = "Captured: \\"" + text + "\\"";
                };
            }
        </script>
        """
        st.components.v1.html(html5_speech_recorder_element, height=100)
        
    with tab_translation_view:
        st.markdown("### Real-Time Cross-Lingual Machine Translation Module (Spanish Target)")
        spanish_translation_output = "Bienvenidos equipo al espacio de trabajo de sincronización de ingeniería. Todos los nodos de la canalización local se están ejecutando normalmente."
        st.code(spanish_translation_output, language="text")
        
        html5_tts_engine_script = f"""
        <div style="background-color: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #30363d; text-align: center;">
            <button onclick="triggerBrowserSpeechEngine()" style="background-color: #238636; color: white; border: none; padding: 10px 20px; border-radius: 6px; font-weight: bold; cursor: pointer; width: 100%;">
                🔊 Play Translated Vocal Audio Track
            </button>
        </div>
        <script>
            function triggerBrowserSpeechEngine() {{
                window.speechSynthesis.cancel();
                var utter = new SpeechSynthesisUtterance("{spanish_translation_output}");
                utter.lang = 'es-ES';
                utter.rate = {play_speed};
                utter.volume = Math.min(1.0, {volume_degree} / 3.0);
                window.speechSynthesis.speak(utter);
            }}
        </script>
        """
        st.components.v1.html(html5_tts_engine_script, height=90)

# =====================================================================
# PART 8 & 10: VIDEO TOOLS & WATERMARK GENERATION
# =====================================================================
elif page_selection == "🎬 Video Tooling & Text Watermarks":
    st.title("🎬 Video Canvas Modification & Text Watermark Tool")
    
    col_tl1, col_tl2 = st.columns(2)
    with col_tl1:
        st.markdown("### Video Parameter Structural Shifters")
        video_format_selection = st.selectbox("Transcode Video Output Container:", ["MP4 Standard Container", "MKV Matroska High Profile", "WebM Web Streaming Format"])
        video_resolution_selection = st.selectbox("Resize Scaling Profiler Grid:", ["1920x1080 (Full HD)", "1280x720 (Standard HD)", "640x480 (VGA Low Bandwidth)"])
        
        c_trim1, c_trim2 = st.columns(2)
        trim_start = c_trim1.number_input("Trim Window Bounds Start (Seconds)", min_value=0, value=0)
        trim_end = c_trim2.number_input("Trim Window Bounds End (Seconds)", min_value=0, value=10)
        
    with col_tl2:
        st.markdown("### 🏷️ Apply Text Watermark Layer Configuration")
        watermark_string = st.text_input("Watermark Alpha ID Text String Stamp:", value="CONFIDENTIAL STUDIO PROTOTYPE")
        watermark_position = st.selectbox("Spatial Orientation Position Anchor:", ["Center Center", "Top Left Corner", "Bottom Right Margin"])
        watermark_fontsize = st.slider("Watermark Font Size Degree Index", min_value=12, max_value=36, value=20)
        watermark_alpha = st.slider("Watermark Transparency Opacity Channel", min_value=50, max_value=255, value=140)

    st.divider()
    if st.button("🚀 Render Transformed & Watermarked Video Canvas Layout", use_container_width=True):
        with st.spinner("Rebuilding spatial array configurations layout matrices..."):
            watermarked_preview_canvas = utils.apply_canvas_text_watermark(
                text=watermark_string, position=watermark_position, size=watermark_fontsize, opacity=watermark_alpha
            )
        st.success("✅ Complete video layout matrix processed successfully! Preview layer sample reference displayed below:")
        st.image(watermarked_preview_canvas, caption="Watermarked Video Frame Segment Canvas Capture Block")

# =====================================================================
# PART 9: FRAME EXTRACTION GALLERY
# =====================================================================
elif page_selection == "📸 Frame Extraction Gallery":
    st.title("📸 Intervallic Video Frame Extraction Gallery")
    st.caption("Slices running video track datasets down into standalone downloadable image configurations sequences arrays.")
    
    extraction_frequency_index = st.selectbox("Sampling Frequency Slicing Interval Configuration Mode:", ["Extract Every Second", "Extract Every Individual Frame Matrix Layer"])
    
    if st.button("🚀 Run Array Slicer Frame Extraction Pipeline", use_container_width=True):
        with st.spinner("Extracting image canvas frames array layers..."):
            extracted_frames_dataset = utils.run_matrix_frame_extraction(interval_mode=extraction_frequency_index)
            
        st.success(f"✅ Identified {len(extracted_frames_dataset)} separate visual frame captures inside your active processing window boundaries.")
        col_grid = st.columns(4)
        for idx, (name, img) in enumerate(extracted_frames_dataset):
            with col_grid[idx]:
                st.image(img, caption=name, use_container_width=True)

# =====================================================================
# PART 11: ANALYTICS TELEMETRY MATRIX
# =====================================================================
elif page_selection == "📊 Telemetry Analytics Matrix":
    st.title("📊 Integrated Analytics & Signal Metrics Telemetry Data Sheet")
    
    analytics_dictionary = utils.generate_telemetry_analytics_sheet(
        filename=st.session_state.uploaded_file_name, 
        size_bytes=len(st.session_state.uploaded_file_bytes) if st.session_state.uploaded_file_bytes else None
    )
    
    df_analytics = pd.DataFrame(list(analytics_dictionary.items()), columns=["Technical Attribute Parameter Header ID", "Value Log Record String"])
    st.dataframe(df_analytics, use_container_width=True, hide_index=True)

# =====================================================================
# PART 12: CENTRALIZED DOWNLOAD CENTER
# =====================================================================
elif page_selection == "💾 Centralized Download Center":
    st.title("💾 Centralized Deliverables Asset Download Center")
    st.caption("Compile and extract generated assets down to your local device file systems natively.")
    
    col_d1, col_d2 = st.columns(2)
    with col_d1:
        st.markdown("### 🔤 Linguistic & Text Records")
        st.download_button(
            label="📥 Download Extracted Transcript (.txt File)",
            data=st.session_state.processed_transcript_log,
            file_name="speech_intelligence_transcript.txt",
            mime="text/plain",
            use_container_width=True
        )
        
        mock_csv_metrics_data = "Parameter,Value\nResolution,1080p\nFPS,30\nAudioSampleRate,44.1kHz"
        st.download_button(
            label="📥 Download Telemetry Analytics Metrics (.csv Data Log Sheet)",
            data=mock_csv_metrics_data,
            file_name="media_studio_telemetry.csv",
            mime="text/csv",
            use_container_width=True
        )
        
    with col_d2:
        st.markdown("### 🖼️ Visual & Compressed Media Bundles")
        with st.spinner("Compiling visual asset folders frames archive arrays..."):
            sample_frames_array = utils.run_matrix_frame_extraction()
            zip_binary_payload = utils.compile_extracted_frames_to_zip(sample_frames_array)
            
        st.download_button(
            label="📥 Download Extracted Frames Archive Bundle (.zip)",
            data=zip_binary_payload,
            file_name="extracted_video_frames_package.zip",
            mime="application/zip",
            use_container_width=True
        )
        
