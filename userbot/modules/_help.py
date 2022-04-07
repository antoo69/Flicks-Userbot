#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    Recode by Fariz <Github.com/farizjs>
#    From Flicks-Userbot
#    <t.me/TheFlicksUserbot>

import os

from telethon import Button
from userbot import ALIVE_NAME, BOT_USERNAME, CMD_HELP, CMD_HANDLER, CMD_LIST, bot, tgbot
from userbot.utils import flicks_cmd

user = bot.get_me()
DEFAULTUSER = user.first_name
CUSTOM_HELP_EMOJI = "⚡"
main_help_menu = [
    [
        Button.url("Settings ⚙️", f"t.me/{BOT_USERNAME}"),
        Button.inline("Vc Plugin ⚙️", data="flicks_inline"),
    ],
    [
        Button.inline("Help Menu", data="open"),
    ],
    [Button.inline("Close", data="close")],
]


@flicks_cmd(pattern="help ?(.*)")
async def cmd_list(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(f"**✘ Commands available in {args} ✘** \n\n" + str(CMD_HELP[args]) + "\n\n**💕 @TheFlicksUserbot**")
        else:
            await event.edit(f"**Module** `{args}` **Tidak tersedia!**")
    else:
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@FlicksSupport"
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException:
            await event.edit(
                f"** Sepertinya obrolan atau bot ini tidak mendukung inline mode.\nUntuk alternatif gunakan perintah\n👉`{CMD_HANDLER}plugins`**"
            )
