# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# recode by @vckyaz
# FROM GeezProjects <https://github.com/vckyou/GeezProjects>
#
# Support @GeezSupport & @GeezProjects

import asyncio
import random
import re

from geezproject import CMD_HANDLER as cmd
from geezproject import CMD_HELP, bot
from geezproject.events import geez_cmd

usernexp = re.compile(r"@(\w{3,32})\[(.+?)\]")
nameexp = re.compile(r"\[([\w\S]+)\]\(tg://user\?id=(\d+)\)\[(.+?)\]")
emoji = "😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🎲 🧩 ♟ 🎯 🎳 🎭💕 💞 💓 💗 💖 ❤️‍🔥 💔 🤎 🤍 🖤 ❤️ 🧡 💛 💚 💙 💜 💘 💝 🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧 🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍨".split(
    " "
)


class FlagContainer:
    is_active = False


@bot.on(geez_cmd(outgoing=True, pattern=r"mention(?: |$)(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.delete()
    query = event.pattern_match.group(1)
    mentions = f"@all {query}"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, 100500):
        mentions += f"[\u2063](tg://user?id={x.id} {query})"
    await bot.send_message(chat, mentions, reply_to=event.message.reply_to_msg_id)


@bot.on(geez_cmd(outgoing=True, pattern=r"emojitag(?: |$)(.*)"))
async def _(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True

        args = event.message.text.split(" ", 1)
        text = args[1] if len(args) > 1 else None
        chat = await event.get_input_chat()
        await event.delete()

        tags = list(
            map(
                lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})",
                await event.client.get_participants(chat),
            ),
        )
        current_pack = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break

            current_pack.append(participant)

            if len(current_pack) == 5:
                tags = list(
                    map(
                        lambda m: f"[{random.choice(emoji)}](tg://user?id={m.id})",
                        current_pack,
                    ),
                )
                current_pack = []

                if text:
                    tags.append(text)

                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(2)
    finally:
        FlagContainer.is_active = False
        
        
      stag = ('𝙝𝙮𝙮𝙮𝙮 ❣️','𝙝𝙚𝙡𝙡𝙤 𝙟𝙞 💞','𝙃𝙚𝙢𝙇𝙤 😈','𝙢𝙪𝙟𝙝𝙨𝙚 𝙗𝙝𝙞 𝙗𝙖𝙖𝙩 𝙠𝙧 𝙡𝙤','𝙝𝙞𝙞 👀','𝙝𝙚𝙡𝙡𝙤 👀','𝙝𝙣𝙟𝙞 👀','𝙠𝙮𝙖 𝙗𝙤𝙡𝙚 🤔','𝙠𝙪𝙘𝙝𝙝 𝙗𝙤𝙡 𝙦 𝙣𝙞 𝙧𝙝𝙚 😒😒','𝙖𝙖𝙟 𝙠𝙖𝙞𝙨𝙚 𝙖𝙖𝙣𝙖 𝙝𝙪𝙖 🤔','𝙢𝙤𝙢 𝙙𝙖𝙙 𝙠𝙖𝙞𝙨𝙚 𝙝 ❤️','𝙠𝙮𝙖 𝙠𝙧 𝙧𝙝𝙚 𝙝𝙤 👀','𝙢𝙚𝙧𝙚 𝙙𝙤𝙨𝙩 𝙝𝙤 𝙣𝙖 😒😒','𝙨𝙪𝙣𝙤 𝙣𝙖 🤞','𝙮𝙖𝙖𝙧 𝙠𝙖𝙡 𝙨𝙝𝙤𝙥𝙥𝙞𝙣𝙜 𝙠𝙧𝙣𝙚 𝙟𝙖𝙖𝙣𝙖 𝙝 💞','𝙠𝙖𝙡 𝙢𝙖𝙧𝙠𝙚𝙩 𝙟𝙖𝙣𝙖 𝙝💞','𝙠𝙝𝙖 𝙡𝙤 𝙗𝙝𝙖𝙬 𝙢𝙩 𝙠𝙧𝙤 𝙗𝙖𝙖𝙩 😒😒','𝙜𝙧𝙤𝙪𝙥 𝙢𝙚 𝙗𝙖𝙖𝙩 𝙦 𝙣𝙞 𝙠𝙧𝙩𝙚 😒😒','𝙗𝙝𝙤𝙩 𝙗𝙝𝙖𝙬 𝙠𝙝𝙖𝙩𝙚 𝙝𝙤 😒😒','𝙠𝙝𝙖 𝙝𝙤 𝙮𝙖𝙖𝙧𝙖 ❤️💫','𝙢𝙞𝙨𝙨 𝙮𝙤𝙪 𝙙𝙤𝙨𝙩🥺🥀 ','𝙤𝙣 𝙖𝙖 𝙟𝙖𝙤 𝙮𝙖𝙖𝙡𝙖 🤗','𝙗𝙖𝙖𝙩 𝙠𝙧 𝙡𝙤 𝙣𝙖 𝙮𝙖𝙖𝙧𝙖 ❤️👀 ','𝙨𝙤 𝙜𝙮𝙚 𝙠𝙮𝙖 🤔🤔 ','𝙪𝙩𝙝 𝙗𝙝𝙞 𝙟𝙖𝙖𝙤 😶 ','𝙠𝙝𝙖 𝙧𝙚𝙝 𝙜𝙮𝙚 🧐 ','𝙠𝙖𝙞𝙨𝙚 𝙝𝙤 𝙮𝙖𝙖𝙧𝙖 🤗','𝙠𝙝𝙖𝙣𝙖 𝙝𝙪𝙖? 😚 ','𝙫𝙘 𝙖𝙖 𝙟𝙖𝙤 🥳🥳 ','𝙠𝙝𝙖 𝙝𝙤 𝙟𝙖𝙗 𝙨𝙚 🧐 ','𝙖𝙖𝙟 𝙖𝙖 𝙗𝙝𝙞 𝙟𝙖𝙖𝙤𝙜𝙚 🧐🧐 ','𝙠𝙞𝙩𝙩𝙖 𝙗𝙝𝙖𝙬 𝙠𝙝𝙖𝙩𝙚 𝙝𝙤 😒😒','𝙠𝙖𝙞𝙨𝙚 𝙝𝙤 𝙢𝙚𝙧𝙚 𝙮𝙖𝙖𝙧𝙖 ❣️','𝙘𝙝𝙖𝙩𝙩𝙞𝙣𝙜 𝙠𝙧 𝙡𝙤 🥺🥺❤️🥀✨️','𝙈𝙪𝙟𝙝𝙚 𝙗𝙝𝙪𝙡 𝙜𝙮𝙚 🥺🥀✨','𝙨𝙪𝙣𝙤 𝙣 😔❤️🌸','𝙘𝙝𝙖𝙩𝙩𝙞𝙣𝙜 𝙗𝙝𝙞 𝙠𝙧 𝙡𝙤 𝙩𝙝𝙤𝙙𝙖 😩🥀❤️','𝙜𝙝𝙖𝙧 𝙥𝙚 𝙨𝙗 𝙠𝙖𝙞𝙨𝙚 𝙝 😌❤️🥀','𝙠𝙮𝙖 𝙘𝙝𝙖𝙡 𝙧𝙝𝙖 𝙝 𝙖𝙖𝙟 𝙠𝙖𝙡 😌❤️🥀','𝘼𝙪𝙧 𝙨𝙗 𝙠𝙝𝙖𝙧𝙞𝙮𝙖𝙩 🤞','𝙗𝙝𝙤𝙩 𝙮𝙖𝙖𝙙 𝙖𝙖 𝙧𝙝𝙞 𝙝 💔🥀','𝙮𝙖𝙖𝙙 𝙣𝙞 𝙖𝙖𝙩𝙞 𝙢𝙚𝙧𝙞 𝙠𝙗𝙝𝙞 💔💔','𝙠𝙮 𝙠𝙧 𝙧𝙝𝙚 𝙝𝙤 👀','𝙜𝙝𝙪𝙢𝙣𝙚 𝙘𝙝𝙖𝙡𝙤𝙜𝙚 👀','𝙖𝙪𝙧 𝙗𝙖𝙣𝙙𝙞 𝙠𝙖𝙞𝙨𝙞 𝙝 👀','𝙠𝙖𝙡 𝙠𝙝𝙞 𝙜𝙮𝙚 𝙩𝙝𝙚 🤔','𝙤𝙣𝙡𝙞𝙣𝙚 𝙝𝙤 𝙠𝙮𝙖 👀','𝙠𝙞𝙩𝙣𝙖 𝙘𝙝𝙪𝙥 𝙧𝙝𝙩𝙚 𝙝𝙤 𝙮𝙖𝙖𝙧 😒','𝙙𝙚𝙠𝙝𝙖 𝙝𝙖𝙯𝙖𝙧𝙤𝙣 𝙙𝙖𝙛𝙖 𝙖𝙖𝙥𝙠𝙤 ❤️👀','𝙠𝙖𝙡 𝙖𝙖𝙥𝙠𝙤 𝙙𝙚𝙠𝙝𝙚 𝙩𝙝𝙚 👀','𝙖𝙖𝙥𝙠𝙤 𝙜𝙖𝙖𝙣𝙖 𝙜𝙖𝙖𝙣𝙚 𝙖𝙖𝙩𝙖 𝙝 👀','𝙩𝙧𝙪𝙩𝙝 𝙤𝙧 𝙙𝙖𝙧𝙚 𝙠𝙝𝙚𝙡𝙤𝙜𝙚 🤞🤞','𝙠𝙖𝙡 𝙢𝙖𝙯𝙖 𝙖𝙖𝙮𝙖 𝙩𝙝𝙖 𝙣𝙖 🥳🥳','𝙘𝙝𝙖𝙡𝙤 𝙥𝙖𝙧𝙩𝙮 𝙠𝙧𝙩𝙚 𝙝 🥳🥳','𝙢𝙖𝙯𝙖 𝙖𝙖𝙮𝙖 😍','𝙠𝙮𝙖 𝙝𝙪𝙖 😳','𝙘𝙝𝙤𝙘𝙤𝙡𝙖𝙩𝙚 𝙠𝙝𝙖𝙣𝙖 𝙝 🤓👉🍫','𝙠𝙮𝙖 𝙝𝙪𝙖 🙁','𝙖𝙖𝙟 𝙢𝙖𝙞 𝙨𝙖𝙙 𝙝𝙪 🥺🥺','𝙢𝙪𝙟𝙝𝙚 𝙢𝙖𝙣𝙖𝙤 😒😒','𝙗𝙝𝙤𝙩 𝙩𝙚𝙯 𝙝𝙤 𝙧𝙞𝙮𝙖𝙝 😏😏','𝙖𝙖𝙟 𝙢𝙖𝙞𝙣𝙚 𝙗𝙖𝙣𝙙𝙖𝙧 𝙙𝙚𝙠𝙝𝙖 😌👉🐒','𝙠𝙮𝙖 𝙮𝙧𝙧𝙧 🤢','𝙨𝙗 𝙨𝙝𝙖𝙣𝙩 𝙝𝙤 𝙟𝙖𝙖𝙤 🤫','𝙖𝙖𝙥 𝙧𝙚𝙡𝙖𝙩𝙞𝙤𝙣𝙨𝙝𝙞𝙥 𝙢𝙚 𝙝𝙤? 👀','𝙨𝙞𝙣𝙜𝙡𝙚 𝙝𝙤 𝙝𝙖 𝙢𝙞𝙣𝙜𝙡𝙚 👀','𝙔𝙝𝙖 𝘼𝙖 𝙅𝙖𝙖𝙤 @FRIENDSSOME 👀 ','𝗔𝗮𝗷 𝗽𝗿𝗲𝘀𝗵𝗮𝗻 𝗾 𝗵𝗼...? 😒','𝗺𝘂𝗺𝗺𝘆 𝗻𝗲 𝗱𝗮𝗻𝘁𝗮 🥲','𝗸𝗵𝘂𝘀𝗵 𝗿𝗵𝗮 𝗸𝗿𝗼✌️🙂','𝗴𝗹𝘁 𝗻𝗶 𝗯𝗼𝗹𝗻𝗮 𝗰𝗵𝗮𝗵𝗶𝘆𝗲🙊','𝗺𝘂𝗷𝗵𝗲 𝗱𝗲𝗸𝗵𝗼 😒❤️👀','𝗮𝗮𝗷 𝗸𝗮 𝗱𝗶𝗻 𝗸𝗮𝗶𝘀𝗮 𝗿𝗵𝗮 ☺️','𝗔𝗮𝗼 𝗣𝗮𝗿𝘁𝘆 𝗞𝗿𝘁𝗲 𝗵 🥂🥂','𝗮𝗮𝗽 𝗮𝗱𝗺𝗶𝗻 𝗵𝗼 𝗸𝘆𝗮 👀','𝗸𝘆𝗮 𝗸𝗲𝗵𝘁𝗲 𝗵𝗼 😎😎',) 
        
    @bot.on(geez_cmd(outgoing=True, pattern=r"stag(?: |$)(.*)"))
async def _(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True

        args = event.message.text.split(" ", 1)
        text = args[1] if len(args) > 1 else None
        chat = await event.get_input_chat()
        await event.delete()

        tags = list(
            map(
                lambda m: f"[{m.first_name}](tg://user?id={m.id}) {random.choice(stag)}",
                await event.client.get_participants(chat),
            ),
        )
        current_pack = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break

            current_pack.append(participant)

            if len(current_pack) == 1:
                tags = list(
                    map(
                        lambda m: f"[{m.first_name}](tg://user?id={m.id}) {random.choice(stag)}",
                        current_pack,
                    ),
                )
                current_pack = []

                if text:
                    tags.append(text)

                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(5)
    finally:
        FlagContainer.is_active = False
        
 

@bot.on(geez_cmd(outgoing=True, pattern=r"all(?: |$)(.*)"))
async def _(event):
    if event.fwd_from or FlagContainer.is_active:
        return
    try:
        FlagContainer.is_active = True

        args = event.message.text.split(" ", 1)
        text = args[1] if len(args) > 1 else None
        chat = await event.get_input_chat()
        await event.delete()

        tags = list(
            map(
                lambda m: f"[{m.first_name}](tg://user?id={m.id})",
                await event.client.get_participants(chat),
            ),
        )
        jumlah = []
        async for participant in event.client.iter_participants(chat):
            if not FlagContainer.is_active:
                break

            jumlah.append(participant)

            if len(jumlah) == 1:
                tags = list(
                    map(
                        lambda m: f"[{m.first_name}](tg://user?id={m.id})",
                        jumlah,
                    ),
                )
                jumlah = []

                if text:
                    tags.append(text)

                await event.client.send_message(event.chat_id, " ".join(tags))
                await asyncio.sleep(5)
    finally:
        FlagContainer.is_active = False


CMD_HELP.update(
    {
        "tag": f"**Plugin : **`tag`\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}mention`\
        \n  ↳ : **Untuk Menmention semua anggota yang ada di group tanpa menyebut namanya.\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}all` <text>\
        \n  ↳ : **Untuk Mengetag semua anggota Maksimal 3.000 orang yg akan ditag di grup untuk mengurangi flood wait telegram.\
        \n\n  𝘾𝙤𝙢𝙢𝙖𝙣𝙙 :** `{cmd}emojitag` <text>\
        \n  ↳ : **Untuk Mengetag semua anggota di grup dengan random emoji berbeda.\
        \n\n  •  **NOTE :** Untuk Memberhentikan Tag ketik `.restart`\
    "
    }
)
