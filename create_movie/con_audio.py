from moviepy.editor import *
import os, os.path
import shutil

def combine_audio(filepath,writepath,dt_str):
    num_files = 0

    for path in os.listdir(filepath):
        if os.path.isfile(os.path.join(filepath, path)):
            num_files += 1

    audioList = []

    for x in range(num_files):
        audio = AudioFileClip(f"{filepath}/{x}.mp3")
        audioList.append(audio)

    audioClip = concatenate_audioclips(audioList)
    audioClip.write_audiofile(f"{writepath}")

    shutil.rmtree(f"./assets/files_{dt_str}/comments/temp")
    os.mkdir(f"./assets/files_{dt_str}/comments/temp")

