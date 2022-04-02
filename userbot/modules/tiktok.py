from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP, CMD_HANDLER as i
from userbot.events import register


@flicks_cmd(pattern="tiktok(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    d_link = event.pattern_match.group(1)
    if ".com" not in d_link:
        await event.edit("`Mohon Maaf, Saya Membutuhkan Link Video Tiktok Untuk Mendownload Nya`")
    else:
        await event.edit("```Video Sedang Diproses.....```")
    chat = "@TIKTOKDOWNLOADROBOT"
    async with bot.conversation(chat) as conv:
        try:
            msg_start = await conv.send_message("/start")
            r = await conv.get_response()
            msg = await conv.send_message(d_link)
            details = await conv.get_response()
            video = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.edit("**Kesalahan:** **Mohon Buka Blokir** `@TIKTOKDOWNLOADROBOT` **Dan Coba Lagi !**")
            return
        await bot.send_file(event.chat_id, video)
        await event.client.delete_messages(conv.chat_id,
                                           [msg_start.id, r.id, msg.id, details.id, video.id])
        await event.delete()


CMD_HELP.update(
    {
        "tiktok": f"𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `{i}tiktok <Link tiktok>`"
        "\n• : Download Video Tiktok Tanpa Watermark"
    }
)
