"""Hack Prank
Available Commands:
.hack"""

from telethon import events

import asyncio
from uniborg.util import admin_cmd
from telethon.tl.functions.users import GetFullUserRequest



@borg.on(admin_cmd(pattern=r"hack"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 11)

    #input_str = event.pattern_match.group(1)

    #if input_str == "hack":

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(reply_message.from_id))
        firstname = replied_user.user.first_name
        usname = replied_user.user.username
        idd = reply_message.from_id
        if idd== 919209968:
            await event.edit("This is My Master\nI Can't HACK my Master's Account")
        else:
            await event.edit("Hacking..")
            animation_chars = [
        
            "`Connecting To Hacked Private Server...`",
            "`Target Selected.`",
            "`struct group_info *groups_alloc(int gidsetsize){...|  `",
            "`struct group_info *groups_alloc(int gidsetsize){...\  `",
            "`struct group_info *groups_alloc(int gidsetsize){...―  `",
            "`struct group_info *groups_alloc(int gidsetsize){.../  `",
            "`struct group_info *groups_alloc(int gidsetsize){...|  `",
            "`struct group_info *groups_alloc(int gidsetsize){...\  `",
            "`struct group_info *group_info; \n\nint nblocks; \nint i;...―  `",
            "`struct group_info *group_info; \n\nint nblocks; \nint i;.../  `", 
            "`struct group_info *group_info; \n\nint nblocks; \nint i;...|  `",
                "`int i; \nnblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK;...|  `",
                "`nblocks = (gidsetsize + NGROUPS_PER_BLOCK - 1) / NGROUPS_PER_BLOCK; /nnblocks = nblocks ? : 1;...\  `",
                "`nblocks = nblocks ? : 1; /nif (!group_info) /nreturn NULL;...―  `",
                "`if (!group_info) /nreturn NULL; /nfor (i = 0; i < group_info->nblocks; i++).../  `",
                "`for (i = 0; i < group_info->nblocks; i++) \n...|  `",
                "`...\  `",
                "`...―  `",
                "`.../  `",
                "`...|  `",
                "`...\  `",
                "`...―  `",
                "`.../  `",
                "`...|  `",
                "`...\  `",
                "`...―  `",
                "`.../  `",
                "`...|  `",
                "`...\  `",
                "`...―  `",
                "`.../  `",
                "`...|  `",
                "`...\  `",
                "`...―  `",
                "`.../  `",
                "`...|  `",
                "`...\  `",
                "`...―  `",
                "`.../  `",
                "`...|  `",
                "`...\  `",
                "`...―  `",
                "`.../  `",
                
            "`Targeted Account Hacked...\n\nPay 69$ To` @WhySooSerious `To Remove this hack..`"
            ]

            for i in animation_ttl:

                await asyncio.sleep(animation_interval)

                await event.edit(animation_chars[i % 40])
    else:
        await event.edit("No User is Defined\n Can't hack account")
            
