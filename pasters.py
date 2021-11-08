import json
import requests

from html_telegraph_poster import TelegraphPoster

from userbot.Config import Config
from userbot import *

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "content-type": "application/json",
}

async def pasty(message, extension=None):
    siteurl = "https://pasty.lus.pm/api/v1/pastes"
    data = {"content": message}
    try:
        response = requests.post(url=siteurl, data=json.dumps(data), headers=headers)
    except Exception as e:
        return {"error": str(e)}
    if response.ok:
        response = response.json()
        purl = (
            f"https://pasty.lus.pm/{response['id']}.{extension}"
            if extension
            else f"https://pasty.lus.pm/{response['id']}.txt"
        )
        try:
            await bot.send_message(
                Config.kittyBOT_LOGGER,
                f"#PASTE \n\n**Open Paste From** [here]({purl}). \n**Delete that paste by using this token** `{response['deletionToken']}`",
            )
        except Exception as e:
            LOGS.info(str(e))
        return {
            "url": purl,
            "raw": f"https://pasty.lus.pm/{response['id']}/raw",
            "bin": "Pasty",
        }
    return {"error": "Unable to reach pasty.lus.pm"}


async def telegraph_paste(page_title, temxt):
    cl1ent = TelegraphPoster(use_api=True)
    auth = "[ LEGENDARY AF kittyBOT ]"
    cl1ent.create_api_token(auth)
    post_page = cl1ent.post(
        title=page_title,
        author=auth,
        author_url="https://t.me/kittyBot_Support",
        text=temxt,
    )
    return post_page["url"]
