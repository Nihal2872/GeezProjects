import requests

from geezproject import CMD_HANDLER as cmd
from geezproject import CMD_HELP
from geezproject.utils import edit_or_reply, geez_cmd


@geez_cmd(pattern="lyrics(?:\s|$)([\s\S]*)")
async def _(event):
    query = event.pattern_match.group(1)
    if not query:
        return await edit_or_reply(event, "**Silahkan Masukan Judul Lagu**")
    try:
        xxnx = await edit_or_reply(event, "`Searching Lyrics...`")
        respond = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{respond['data']}"
        await xxnx.edit(result)
    except Exception:
        await xxnx.edit("**Lirik lagu tidak ditemukan.**")


CMD_HELP.update(
    {
        "lyrics": f"**Plugin : **`lyrics`\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}lyrics` <judul lagu>\
        \n  ββΈ : **Dapatkan lirik lagu yang cocok dengan judul lagu.\
    "
    }
)
