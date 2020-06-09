import datetime
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="getlink ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    if not event.reply_to_msg_id:
       await event.edit("```Reply To Any File!```")
       return
    reply_message = await event.get_reply_message() 
    if not reply_message.text:
       await event.edit("```Reply To A File!```")
       return
    chat = "@highspeedlinksbot"
    sender = reply_message.sender
    if reply_message.sender.bot:
       await event.edit("```Reply To Any Link!```")
       return
    await event.edit("```Generating Link.. Please wait!!```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1071746481))
              await event.client.forward_messages(chat, reply_message)
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Please unblock Files to LinkBot```")
              return
          if response.text.startswith("I"):
             await event.edit("```Disable Your Forward Privacy Settings!```")
          else: 
             return
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
