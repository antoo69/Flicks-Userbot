# From Geez-Userbot
# Fix by Fariz <github.com/farizjs>
"""
Plugin : tempmail

Perintah : `{i}tempmail`
Penggunaan : dapatkan email gratis dari tempmail
"""
from telethon import events
from userbot import CMD_HELP, CMD_HANDLER, bot
from userbot.utils import flicks_cmd
from telethon.errors.rpcerrorlist import YouBlockedUserError
import asyncio


@flicks_cmd(pattern="tempmail(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    flicks = await event.edit("Sedang Memprosess...")
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            flicksuserbot = ((response).reply_markup.rows[2].buttons[0].url)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await flicks.edit("`Mohon Maaf, Silahkan Buka` @TempMailBot `Lalu Tekan Start dan Coba Lagi.`")
            return
        await event.edit(f"**FLICKS TEMPMAIL** ~ `{response.message.message}`\n\n[KLIK DISINI UNTUK VERIFIKASI]({flicksuserbot})")


CMD_HELP.update({"tempmail": f"{__doc__.format(i=CMD_HANDLER)}"})
