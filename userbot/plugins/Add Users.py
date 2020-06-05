"""Invite the user(s) to the current chat
Syntax: .invite <User(s)>
    © Ultroid"""

from telethon import functions
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern="invite ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    to_add_users = event.pattern_match.group(1)
    if event.is_private:
        await event.edit("`.add` users to a chat, not to a Private Message")
    else:
        logger.info(to_add_users)
        if not event.is_channel and event.is_group:
            # CREDITS :- Lonami Webs OR lonamiwebs.github.io
            #  I am NOT a FUCKING ASSHOLE who Disregards Others Credits ;)
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.messages.AddChatUserRequest(
                        chat_id=event.chat_id,
                        user_id=user_id,
                        fwd_limit=1000000
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Invited Successfully")
        else:
            # https://lonamiwebs.github.io/Telethon/methods/channels/invite_to_channel.html
            for user_id in to_add_users.split(" "):
                try:
                    await borg(functions.channels.InviteToChannelRequest(
                        channel=event.chat_id,
                        users=[user_id]
                    ))
                except Exception as e:
                    await event.reply(str(e))
            await event.edit("Invited Successfully")
