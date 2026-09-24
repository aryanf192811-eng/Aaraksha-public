import os
import json
import urllib.request
import glob
import subprocess

base_dir = r"c:\Users\aryan\Desktop\Aaraksha\docs\aaraksha-video"
assets_dir = os.path.join(base_dir, "assets")
os.makedirs(assets_dir, exist_ok=True)

brain_dir = r"C:\Users\aryan\.gemini\antigravity-ide\brain\24ef30fb-387a-42e5-ba76-540a6f9ea5f9"
system_gen = os.path.join(brain_dir, ".system_generated", "steps")

ui_files = []
cartoon_files = []

# Scrape all step outputs and sort them by step number so they are chronologically ordered
step_dirs = glob.glob(os.path.join(system_gen, "*"))
step_dirs = [d for d in step_dirs if os.path.basename(d).isdigit()]
step_dirs.sort(key=lambda x: int(os.path.basename(x)))

for step_dir in step_dirs:
    out_file = os.path.join(step_dir, "output.txt")
    if os.path.exists(out_file):
        try:
            with open(out_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                
                # Check for outputComponents
                for comp in data.get('outputComponents', []):
                    if 'design' in comp and 'screens' in comp['design'] and len(comp['design']['screens']) > 0:
                        screen = comp['design']['screens'][0]
                        if 'screenshot' in screen and 'downloadUrl' in screen['screenshot']:
                            url = screen['screenshot']['downloadUrl']
                            w = int(screen.get('width', 0))
                            h = int(screen.get('height', 0))
                            prompt = screen.get('prompt', '').lower()
                            
                            is_cartoon = "cinematic storytelling" in prompt or w == 1200
                            file_prefix = "cartoon" if is_cartoon else "ui"
                            file_idx = len(cartoon_files) if is_cartoon else len(ui_files)
                            
                            # check mimeType from htmlCode (sometimes used for image type)
                            is_svg = False
                            if 'htmlCode' in screen and screen['htmlCode'].get('mimeType') == 'image/svg+xml':
                                is_svg = True
                            
                            ext = ".svg" if is_svg else ".png"
                            out_path = os.path.join(assets_dir, f"{file_prefix}_{file_idx}{ext}")
                            
                            print(f"Downloading {out_path} from {url[:50]}...")
                            urllib.request.urlretrieve(url, out_path)
                            
                            if is_svg:
                                png_path = out_path.replace('.svg', '.png')
                                try:
                                    import cairosvg
                                    cairosvg.svg2png(url=out_path, write_to=png_path)
                                    out_path = png_path
                                except ImportError:
                                    pass
                            
                            if is_cartoon:
                                cartoon_files.append(out_path)
                            else:
                                ui_files.append(out_path)
        except Exception as e:
            pass

print(f"Downloaded {len(cartoon_files)} cartoons and {len(ui_files)} UIs.")
