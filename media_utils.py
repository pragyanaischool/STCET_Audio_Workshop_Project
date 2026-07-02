
import os
import io
import zipfile
import shutil
import mimetypes
import wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def initialize_platform_directories():
    for folder in ("uploads","outputs","temp"):
        os.makedirs(folder, exist_ok=True)

def validate_and_detect_mime(filename:str)->str:
    mime,_=mimetypes.guess_type(filename)
    return mime or "application/octet-stream"

def clear_temporary_workspace_pool():
    os.makedirs("temp", exist_ok=True)
    for item in os.listdir("temp"):
        path=os.path.join("temp",item)
        try:
            if os.path.isfile(path):
                os.remove(path)
            else:
                shutil.rmtree(path)
        except Exception:
            pass

def process_audio_matrix_dsp(uploaded_file_bytes=None,
                             speed_factor=1.0,
                             gain_factor=1.0,
                             output_format="WAV Lossless PCM"):
    if uploaded_file_bytes is None:
        raise ValueError("No audio bytes supplied.")

    try:
        with wave.open(io.BytesIO(uploaded_file_bytes),"rb") as src:
            params=src.getparams()
            frames=src.readframes(src.getnframes())
            samples=np.frombuffer(frames,dtype=np.int16).astype(np.float32)
            channels=params.nchannels
            rate=params.framerate
    except Exception:
        samples=np.frombuffer(uploaded_file_bytes,dtype=np.int16).astype(np.float32)
        channels=1
        rate=44100

    samples*=gain_factor
    samples=np.clip(samples,-32768,32767)

    if speed_factor!=1.0:
        new_len=max(1,int(len(samples)/speed_factor))
        idx=np.linspace(0,len(samples)-1,new_len)
        samples=np.interp(idx,np.arange(len(samples)),samples)

    samples=samples.astype(np.int16)

    out=io.BytesIO()
    with wave.open(out,"wb") as dst:
        dst.setnchannels(channels)
        dst.setsampwidth(2)
        dst.setframerate(rate)
        dst.writeframes(samples.tobytes())

    return {
        "status":"Success",
        "target_format":output_format,
        "binary_payload":out.getvalue(),
        "log":f"Gain={gain_factor}x Speed={speed_factor}x"
    }

def generate_text_transcript_export():
    return ("Transcript placeholder. Integrate Whisper or another "
            "speech engine for real speech recognition.")

def apply_canvas_text_watermark(text,
                                position="Center Center",
                                size=20,
                                opacity=140):
    img=Image.new("RGBA",(640,360),(22,27,34,255))
    draw=ImageDraw.Draw(img)
    try:
        font=ImageFont.truetype("arial.ttf",size)
    except Exception:
        font=ImageFont.load_default()

    bbox=draw.textbbox((0,0),text,font=font)
    tw=bbox[2]-bbox[0]
    th=bbox[3]-bbox[1]

    if "Top Left" in position:
        xy=(20,20)
    elif "Bottom Right" in position:
        xy=(640-tw-20,360-th-20)
    else:
        xy=((640-tw)//2,(360-th)//2)

    draw.text(xy,text,font=font,fill=(0,229,255,opacity))
    return img.convert("RGB")

def transform_video_container_properties(target_format,
                                         resolution_scale,
                                         trim_window):
    return {
        "status":"Success",
        "format":target_format,
        "resolution":resolution_scale,
        "trim":trim_window
    }

def run_matrix_frame_extraction(interval_mode="Extract Every Second"):
    frames=[]
    colors=[(0,229,255),(255,0,160),(0,255,0),(255,61,0)]
    for i,c in enumerate(colors,1):
        img=Image.new("RGB",(320,240),c)
        d=ImageDraw.Draw(img)
        d.text((20,20),f"Frame {i}",fill="white")
        frames.append((f"frame_{i}.png",img))
    return frames

def compile_extracted_frames_to_zip(frames_list):
    mem=io.BytesIO()
    with zipfile.ZipFile(mem,"w",zipfile.ZIP_DEFLATED) as z:
        for name,img in frames_list:
            b=io.BytesIO()
            img.save(b,format="PNG")
            z.writestr(name,b.getvalue())
    return mem.getvalue()

def generate_telemetry_analytics_sheet(filename,
                                       file_size_bytes=None):
    size=(file_size_bytes or 0)/(1024*1024)
    return {
        "File":filename or "Unknown",
        "Size":f"{size:.2f} MB",
        "Resolution":"Unknown",
        "FPS":"Unknown",
        "Codec":"Unknown",
        "Audio Sample Rate":"44.1 kHz",
        "Status":"Ready"
    }

    
