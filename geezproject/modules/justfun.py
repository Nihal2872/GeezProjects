# Based Plugins
# Ported For Lord-geezproject By liualvinas/Alvin
# If You Kang It Don't Delete / Warning!! Jangan Hapus Ini!!!
from geezproject import CMD_HANDLER as cmd
from geezproject import CMD_HELP, bot
from geezproject.events import geez_cmd


@bot.on(geez_cmd(outgoing=True, pattern=r"xogame(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()


# Alvin Gans


@bot.on(geez_cmd(outgoing=True, pattern=r"wp(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    wwwspr = event.pattern_match.group(1)
    botusername = "@whisperBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, wwwspr)
    await tap[0].click(event.chat_id)
    await event.delete()


# Alvin Gans


@bot.on(geez_cmd(outgoing=True, pattern=r"mod(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    modr = event.pattern_match.group(1)
    botusername = "@PremiumAppBot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, modr)
    await tap[0].click(event.chat_id)
    await event.delete()


# Ported For Lord-geezproject By liualvinas/Alvin


CMD_HELP.update(
    {
        "justfun": f"**Plugin : **`justfun`\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}xogame`\
        \n  ββΈ : **Game xogame bot\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}mod <nama app>`\
        \n  ββΈ : **Dapatkan applikasi mod\
    "
    }
)


CMD_HELP.update(
    {
        "secretchat": f"**Plugin : **`secretchat`\
        \n\n  πΎπ€π’π’ππ£π :** `{cmd}wp <teks> <username/ID>`\
        \n  ββΈ : **Memberikan pesan rahasia haya orang yang di tag yang bisa melihat\
    "
    }
)
