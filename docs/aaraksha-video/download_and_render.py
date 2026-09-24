import os
import json
import urllib.request
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip, vfx, CompositeVideoClip
import glob
import subprocess

# Directories
base_dir = r"c:\Users\aryan\Desktop\Aaraksha\docs\aaraksha-video"
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)

# Step JSONs containing the Stitch outputs
step_dirs = [213, 214, 215, 231, 232, 233, 236, 237, 238]
brain_dir = r"C:\Users\aryan\.gemini\antigravity-ide\brain\24ef30fb-387a-42e5-ba76-540a6f9ea5f9"
system_gen = os.path.join(brain_dir, ".system_generated", "steps")

ui_images = []
print("Downloading Stitch UIs...")
for i, step in enumerate(step_dirs):
    output_file = os.path.join(system_gen, str(step), "output.txt")
    if os.path.exists(output_file):
        with open(output_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            url = None
            for comp in data.get('outputComponents', []):
                if 'design' in comp and 'screens' in comp['design'] and len(comp['design']['screens']) > 0:
                    if 'screenshot' in comp['design']['screens'][0] and 'downloadUrl' in comp['design']['screens'][0]['screenshot']:
                        url = comp['design']['screens'][0]['screenshot']['downloadUrl']
                        break
            
            if url:
                out_path = os.path.join(assets_dir, f"ui_{i}.jpg")
                urllib.request.urlretrieve(url, out_path)
                ui_images.append(out_path)
                print(f"Downloaded {out_path}")
            else:
                print(f"Warning: Could not find downloadUrl in {output_file}")

# Add Gemini images
gemini_images = sorted(glob.glob(os.path.join(brain_dir, "scene_*.jpg")))

# Order the assets to match the narrative (106s, ~20 assets = ~5s each)
# Story:
# Hook: Handloom (gemini), AI Planner (ui_0)
# Tourism: Homestay (gemini), Dest UI (ui_1)
# Guardian: Parents/Tracker (ui_2)
# DMS: Storm (gemini), DMS (ui_3)
# Crisis: Offline SOS (gemini), Fallback (ui_4)
# Govt: Govt map (ui_5)
# Rescue: Rescuer (gemini), Rescuer UI (ui_6), Handoff (ui_7)
# Passport: Digital ID (ui_8), Payoff (gemini)

sequence = [
    gemini_images[0], # handloom
    ui_images[0],     # ai planner
    gemini_images[2], # homestay
    ui_images[1],     # dest ui
    ui_images[2],     # guardian
    gemini_images[3], # storm
    ui_images[3],     # dms
    gemini_images[4], # offline sos
    ui_images[4],     # fallback
    ui_images[5],     # govt map
    gemini_images[5], # rescuer
    ui_images[6],     # rescuer app
    ui_images[7],     # handoff
    ui_images[8],     # passport
    gemini_images[6]  # payoff
]

print("Rendering video...")
clips = []
# Duration per image to fill 106 seconds (106 / 15 = ~7 seconds per clip)
# Wait, user said 3-5s per screen. To fill 106s with 15 clips, it's ~7s per clip.
# I will interleave duplicate or reversed pans to increase the cut rate.
extended_sequence = sequence + sequence[::-1][:10]
duration_per_clip = 106.0 / len(extended_sequence)

for idx, img_path in enumerate(extended_sequence):
    clip = ImageClip(img_path).set_duration(duration_per_clip)
    
    # Simple zoom effect using resize
    # To avoid moviepy crash on resize function with time, we do a simple crossfade sequence
    # and standard zoom out by creating a CompositeVideoClip
    w, h = clip.size
    # crop to 16:9 roughly if it's tall
    if h > w:
        clip = clip.crop(y1=0, y2=int(w*1.77)).resize(height=1080)
    else:
        clip = clip.resize(height=1080)
    
    # center
    clip = clip.set_position("center").on_color(size=(1920,1080), color=(0,0,0))
    
    # subtle fadein
    if idx > 0:
        clip = clip.crossfadein(0.5)
        
    clips.append(clip)

final_video = concatenate_videoclips(clips, method="compose")

# Add Audio
audio_path = os.path.join(base_dir, "voiceover.wav")
audio = AudioFileClip(audio_path)
final_video = final_video.set_audio(audio)

out_mp4 = os.path.join(base_dir, "Aaraksha_Full_Ecosystem_Video_temp.mp4")
final_video.write_videofile(out_mp4, fps=24, codec="libx264", audio_codec="aac")

print("Video rendered. Running FFmpeg to add SRT...")
# generate SRT (dummy fast generation based on text)
srt_content = """1
00:00:00,000 --> 00:00:08,000
I always dreamed of exploring the deepest valleys of Northeast India. But planning was overwhelming.

2
00:00:08,500 --> 00:00:15,000
Until Aaraksha. It didn't just give me a map—it built a complete, intelligent ecosystem around me.

3
00:00:15,500 --> 00:00:23,000
Its AI assistant crafted my itinerary in seconds, tailored to my budget. It guided me straight to Tenzing's homestay—a government-verified local stay.

4
00:00:23,500 --> 00:00:32,000
Even before I arrived, Aaraksha’s Travel Safety Index analyzed live weather and terrain, scoring my route.

5
00:00:32,500 --> 00:00:41,000
And the best part? I didn't have to worry my parents. Before I left, I sent them a simple link. No app installs, no logins.

6
00:00:41,500 --> 00:00:51,000
Through the Guardian Portal, my family could see my live location, battery life, and itinerary in real-time.

7
00:00:51,500 --> 00:01:02,000
But the mountains are unpredictable. Knowing I was entering a zero-connectivity zone, I activated Aaraksha's Dead Man's Switch.

8
00:01:02,500 --> 00:01:10,000
A silent timer, watching over me when no one else could. When the storm hit and my signal died completely, I wasn't alone.

9
00:01:10,500 --> 00:01:21,000
Aaraksha’s offline SMS fallback triggered instantly. No internet required. Miles away, my emergency hit a unified network.

10
00:01:21,500 --> 00:01:32,000
In the Government Command Center, dispatchers saw my exact coordinates mapped onto a live 3D elevation terrain, instantly identifying the safest approach.

11
00:01:32,500 --> 00:01:42,000
They dispatched a verified citizen volunteer through the Rescuer App. Using live road routing, he reached me safely.

12
00:01:42,500 --> 00:01:53,000
But the case wasn't closed until he verified my 6-digit cryptographic handoff code—ensuring accountability.

13
00:01:53,500 --> 00:02:03,000
Every step of my journey—every check-in, the SOS, the rescue—was permanently secured into a tamper-evident integrity hash.

14
00:02:03,500 --> 00:02:08,000
A verifiable Digital Journey Passport. Aaraksha is more than an app.

15
00:02:08,500 --> 00:02:15,000
It is a connected ecosystem. Plan intelligently. Travel confidently. Respond decisively. Aaraksha.
"""

srt_path = os.path.join(base_dir, "captions.srt")
with open(srt_path, "w", encoding="utf-8") as f:
    f.write(srt_content)

final_mp4 = os.path.join(base_dir, "Aaraksha_Full_Ecosystem_Video.mp4")
subprocess.run([
    "ffmpeg", "-y", "-i", out_mp4, 
    "-vf", f"subtitles={srt_path.replace(chr(92), '/')}", 
    final_mp4
])

print("DONE!")
