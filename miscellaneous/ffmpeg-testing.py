import subprocess

try:
    result = subprocess.run(["ffmpeg", "-version"], capture_output=True, text=True)
    print("FFmpeg is working ✅")
    print(result.stdout.splitlines()[0])
except FileNotFoundError:
    print("FFmpeg is NOT found in PATH ❌")
