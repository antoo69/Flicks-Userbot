# thanks full for © TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
#
# Ported by @vckyaz
#
# FROM GeezProjects <https://github.com/vckyou/GeezProjects>
#
# Support @GeezSupport & @GeezProjects
# 

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register
from userbot.utils import edit_delete, edit_or_reply, flicks_cmd


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@flicks_cmd(pattern="startvc$")
async def start_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(startvc(c.chat_id))
        await edit_or_reply(c, "`Voice Chat Started...`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@flicks_cmd(pattern="stopvc$")
async def stop_voice(c):
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await edit_delete(c, f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await edit_or_reply(c, "`Voice Chat Stopped...`")
    except Exception as ex:
        await edit_delete(c, f"**ERROR:** `{ex}`")


@flicks_cmd(pattern="vcinvite")
async def _(c):
    xxnx = await edit_or_reply(c, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    xflicks = list(user_list(users, 6))
    for p in xflicks:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await xxnx.edit(f"`{z}` **Orang Berhasil diundang ke VCG**")


@flicks_cmd(pattern="vctitle(?: |$)(.*)")
async def change_title(e):
    title = e.pattern_match.group(1)
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await edit_delete(e, "**Silahkan Masukan Title Obrolan Suara Grup**")

    if not admin and not creator:
        await edit_delete(e, f"**Maaf {ALIVE_NAME} Bukan Admin 👮**")
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await edit_or_reply(e, f"**Berhasil Mengubah Judul VCG Menjadi** `{title}`")
    except Exception as ex:
        await edit_delete(e, f"**ERROR:** `{ex}`")


CMD_HELP.update(
    {
        "vctools": f"**Plugin : **`vctools`\
        \n\n  Command :** `{cmd}startvc`\
        \n  • : **Untuk Memulai voice chat group\
        \n\n  Command :** `{cmd}stopvc`\
        \n  • : **Untuk Memberhentikan voice chat group\
        \n\n  Command :** `{cmd}vctitle` <title vcg>\
        \n  • : **Untuk Mengubah title/judul voice chat group\
        \n\n  Command :** `{cmd}vcinvite`\
        \n  • : **Mengundang Member group ke voice chat group\
        \n\n  Command :** `{cmd}joinvc`\
        \n  • : Untuk Join VC Group\
        \n\n  Command :** `{cmd}leavevc`\
        \n  • : Untuk Turun Dari VC Group\
    "
    }
)
