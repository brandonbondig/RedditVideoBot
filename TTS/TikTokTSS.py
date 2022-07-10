import base64
import os
import random
import requests
from requests.adapters import HTTPAdapter, Retry
from sanitize.voice import sanitize_text

# from profanity_filter import ProfanityFilter
# pf = ProfanityFilter()
# Code by @JasonLovesDoggo
# https://twitter.com/scanlime/status/1512598559769702406

nonhuman = [  # DISNEY VOICES
    "en_us_ghostface",  # Ghost Face
    "en_us_chewbacca",  # Chewbacca
    "en_us_c3po",  # C3PO
    "en_us_stitch",  # Stitch
    "en_us_stormtrooper",  # Stormtrooper
    "en_us_rocket",  # Rocket
    # ENGLISH VOICES
]
human = [
    "en_au_001",  # English AU - Female
    "en_au_002",  # English AU - Male
    "en_uk_001",  # English UK - Male 1
    "en_uk_003",  # English UK - Male 2
    "en_us_001",  # English US - Female (Int. 1)
    "en_us_002",  # English US - Female (Int. 2)
    "en_us_006",  # English US - Male 1
    "en_us_007",  # English US - Male 2
    "en_us_009",  # English US - Male 3
    "en_us_010",
]
voices = nonhuman + human

noneng = [
    "fr_001",  # French - Male 1
    "fr_002",  # French - Male 2
    "de_001",  # German - Female
    "de_002",  # German - Male
    "es_002",  # Spanish - Male
    # AMERICA VOICES
    "es_mx_002",  # Spanish MX - Male
    "br_001",  # Portuguese BR - Female 1
    "br_003",  # Portuguese BR - Female 2
    "br_004",  # Portuguese BR - Female 3
    "br_005",  # Portuguese BR - Male
    # ASIA VOICES
    "id_001",  # Indonesian - Female
    "jp_001",  # Japanese - Female 1
    "jp_003",  # Japanese - Female 2
    "jp_005",  # Japanese - Female 3
    "jp_006",  # Japanese - Male
    "kr_002",  # Korean - Male 1
    "kr_003",  # Korean - Female
    "kr_004",  # Korean - Male 2
]


# good_voices = {'good': ['en_us_002', 'en_us_006'],
#               'ok': ['en_au_002', 'en_uk_001']}  # less en_us_stormtrooper more less en_us_rocket en_us_ghostface


class TikTok:
    def __init__(self):
        self.URI_BASE = "https://api16-normal-useast5.us.tiktokv.com/media/api/text/speech/invoke/?text_speaker="

    def run(self, text, filepath):
        text_concatinate = []
        text = sanitize_text(text)
        
        r = requests.post(f"{self.URI_BASE}{'en_au_002'}&req_text={text}&speaker_map_type=0")
        
        # print(r.text)
        vstr = [r.json()["data"]["v_str"]][0]
        b64d = base64.b64decode(vstr)

        with open(filepath, "wb") as out:
            out.write(b64d)