import os
import subprocess

files = os.listdir("Videos")

for file in files:
    tutorial_number = file.split("-ytshorts")[0].split("#")[1].replace(".mp4", "").strip()
    file_name = file.split("-ytshorts")[0].split("#")[0].strip().rstrip("-").strip()
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg","-i",f"Videos/{file}",f"audios/{tutorial_number}_{file_name}.mp3"])