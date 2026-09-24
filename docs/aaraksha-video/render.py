import os
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip
import subprocess

base_dir = r"c:\Users\aryan\Desktop\Aaraksha\docs\aaraksha-video"
assets_dir = os.path.join(base_dir, "assets")

# Collect available cartoons and UIs
cartoon_images = [os.path.join(assets_dir, f"cartoon_{i}.png") for i in range(10)]
ui_images = [os.path.join(assets_dir, f"ui_{i}.png") for i in range(12)]

# Ensure they exist (fallback to the last available if missing)
def get_safe(arr, idx):
    if len(arr) == 0: return None
    if idx < len(arr) and os.path.exists(arr[idx]): return arr[idx]
    return arr[-1] if os.path.exists(arr[-1]) else None

# Narrative sequence mappings: (Background Image, Overlay UI Image)
# This creates a highly dynamic 22-scene sequence over 106 seconds! (~4.8 seconds per cut)
sequence = [
    (get_safe(cartoon_images, 0), None),                      # Hook
    (get_safe(cartoon_images, 0), get_safe(ui_images, 0)),    # Welcome UI
    (get_safe(cartoon_images, 1), get_safe(ui_images, 1)),    # Map + AI Chat
    (get_safe(cartoon_images, 1), get_safe(ui_images, 2)),    # Map + Budget
    (get_safe(cartoon_images, 2), get_safe(ui_images, 3)),    # Homestay + Ticket
    (get_safe(cartoon_images, 3), get_safe(ui_images, 4)),    # Train + Itinerary
    (get_safe(cartoon_images, 3), get_safe(ui_images, 5)),    # Train + TSI Weather
    (get_safe(cartoon_images, 4), get_safe(ui_images, 6)),    # Guardian + Share Link
    (get_safe(cartoon_images, 4), get_safe(ui_images, 7)),    # Guardian + Battery view
    (get_safe(cartoon_images, 5), None),                      # Storm!
    (get_safe(cartoon_images, 5), get_safe(ui_images, 8)),    # Storm + Zero Signal
    (get_safe(cartoon_images, 6), get_safe(ui_images, 9)),    # Crisis + DMS active
    (get_safe(cartoon_images, 7), None),                      # Command Center
    (get_safe(cartoon_images, 7), get_safe(ui_images, 10)),   # Command Center + Case File
    (get_safe(cartoon_images, 8), None),                      # Rescuer
    (get_safe(cartoon_images, 8), get_safe(ui_images, 11)),   # Rescuer + Dispatch
    (get_safe(cartoon_images, 9), get_safe(ui_images, 11)),   # Handoff + Verification
    (get_safe(cartoon_images, 9), None)                       # Final Payoff
]

# Total duration = 106.0
duration_per_clip = 106.0 / len(sequence)

print("Rendering advanced PiP video with Cinematic Storyboard...")
clips = []

for idx, (bg_path, ui_path) in enumerate(sequence):
    if not bg_path: continue
    
    try:
        # Create Background
        bg_clip = ImageClip(bg_path).set_duration(duration_per_clip)
        w, h = bg_clip.size
        # Crop or resize to 1920x1080 without stretching
        if w/h > 1920/1080:
            bg_clip = bg_clip.resize(height=1080)
            bg_clip = bg_clip.crop(x_center=bg_clip.w/2, width=1920)
        else:
            bg_clip = bg_clip.resize(width=1920)
            bg_clip = bg_clip.crop(y_center=bg_clip.h/2, height=1080)
            
        bg_clip = bg_clip.set_position("center").on_color(size=(1920,1080), color=(0,0,0))
        
        # Crossfade background transition
        if idx > 0:
            bg_clip = bg_clip.crossfadein(0.5)

        if ui_path and os.path.exists(ui_path):
            # Create UI Overlay
            ui_clip = ImageClip(ui_path).set_duration(duration_per_clip)
            # Scale mobile UI to fit nicely (e.g. height 900)
            ui_clip = ui_clip.resize(height=900)
            # Position it on the right side with a little margin
            ui_clip = ui_clip.set_position(("right", "center")).margin(right=100, opacity=0)
            
            # Composite them
            comp_clip = CompositeVideoClip([bg_clip, ui_clip], size=(1920, 1080))
            clips.append(comp_clip)
        else:
            clips.append(bg_clip)

    except Exception as e:
        print(f"Error processing {bg_path}: {e}")

final_video = concatenate_videoclips(clips, method="compose")

# Add Audio
audio_path = os.path.join(base_dir, "voiceover.wav")
audio = AudioFileClip(audio_path)
final_video = final_video.set_audio(audio)

out_mp4 = os.path.join(base_dir, "Aaraksha_Full_Ecosystem_Video_temp.mp4")
final_video.write_videofile(out_mp4, fps=24, codec="libx264", audio_codec="aac")

print("Video rendered. Running FFmpeg to add styled SRT...")
final_mp4 = os.path.join(base_dir, "Aaraksha_Full_Ecosystem_Video.mp4")

# FFmpeg with Force Style for black background box to make subtitles readable
style = "BorderStyle=3,Outline=1,Shadow=0,MarginV=40,FontSize=20,BackColour=&H80000000"
subprocess.run([
    "ffmpeg", "-y", "-i", out_mp4, 
    "-vf", f"subtitles=captions.srt:force_style='{style}'", 
    final_mp4
], cwd=base_dir)

print("DONE!")
