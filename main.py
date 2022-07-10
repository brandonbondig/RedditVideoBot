from reddit.redditAPI import getPost
from TTS.TikTokTSS import TikTok
from get_screenshot.take_screenshot import PWscreenshort
from create_movie.createMovie import combine_audio_video
from create_movie.con_audio import combine_audio
from datetime import datetime
from chopper.chopper import chopString
import os
import shutil

if __name__ == "__main__":

    subreddit = "AskReddit"
    post_num = 9
    amount_comments = 5

    # Datetime used to create a unique id for the final render.
    now = datetime.now()
    dt_str = now.strftime("%d-%m-%Y_%H-%M-%S")

    # Getting post info
    title, post, url, commentsDict, is_nsfw = getPost(subreddit, post_num, amount_comments)

    # Creating initial dir's for 'create_movie' to access.
    while True:
        try:
            os.mkdir(f"./assets")
            os.mkdir(f"./assets/files_{dt_str}/")
            os.mkdir(f"./assets/files_{dt_str}/comments")
            os.mkdir(f"./assets/files_{dt_str}/comments/temp")
            break
        except FileExistsError:
            shutil.rmtree("./assets")
            continue

    for i, selector in enumerate(commentsDict):

        # If the length of the comment is over 300, it will chops it down, because
        # the TikTok TTS API only allows string < 300.
        if len(commentsDict[selector]) > 300:
            chopper = chopString(commentsDict[selector])

            for index, value in enumerate(chopper):
                TikTok().run(
                    value, f"./assets/files_{dt_str}/comments/temp/{index}.mp3"
                )
            combine_audio(
                f"./assets/files_{dt_str}/comments/temp/",
                f"./assets/files_{dt_str}/comments/{i}_comment_{dt_str}.mp3",
                dt_str,
            )
        else:
            TikTok().run(
                commentsDict[selector],
                f"./assets/files_{dt_str}/comments/{i}_comment_{dt_str}.mp3",
            )

        PWscreenshort.takeScreenShot(url, dt_str, i, "#" + selector, is_nsfw)

    PWscreenshort.takeScreenShot(url, dt_str, "title", is_nsfw=is_nsfw)
    TikTok().run(title, f"./assets/files_{dt_str}/title_{dt_str}.mp3")

    combine_audio_video(dt_str, f"./assets/files_{dt_str}/comments")

    shutil.rmtree(f"./assets")

