from moviepy.editor import *
import os, os.path
import random

def combine_audio_video(dt_str, comment_dir):
    num_files = 0

    for path in os.listdir(comment_dir):
        if os.path.isfile(os.path.join(comment_dir, path)):
            num_files += 1

    title_audio = AudioFileClip(f"./assets/files_{dt_str}/title_{dt_str}.mp3")
    title_screenshot = (
        ImageClip(f"./assets/files_{dt_str}/title_post_{dt_str}.png")
        .set_duration(title_audio.duration)
        .fx(vfx.resize, width=(1080) * 0.9)
        .set_position(("center", "center"))
    )

    audioList = [title_audio]
    imageList = [title_screenshot]

    for x in range(num_files):
        audio = AudioFileClip(
            f"./assets/files_{dt_str}/comments/{x}_comment_{dt_str}.mp3"
        )
        audioList.append(audio)
        image = (
            ImageClip(f"./assets/files_{dt_str}/{x}_post_{dt_str}.png")
            .set_duration(audioList[-1].duration)
            .fx(vfx.resize, width=(1080) * 0.9)
            .set_position(("center", "center"))
        )
        imageList.append(image)

    videoClip = concatenate_videoclips(imageList).set_position(("center", "center"))
    audioClip = concatenate_audioclips(audioList)

    videoClip.set_audio(audioClip)
    minecraft_clip = VideoFileClip("./minecraft_video/bbswitzer.mp4")

    start_clp = random.randint(20,1800)

    minecraft_clip = minecraft_clip.subclip((start_clp), (start_clp+videoClip.duration)).set_position(
        ("center", "center")
    )
    minecraft_clip = minecraft_clip.resize(height=1920)

    composite = CompositeVideoClip([minecraft_clip, videoClip], (1080, 1920))
    composite.audio = audioClip
    composite.duration = audioClip.duration

    composite.write_videofile(
        f"./rendered_videos/render_{dt_str}.mp4", threads=4, fps=30
    )


