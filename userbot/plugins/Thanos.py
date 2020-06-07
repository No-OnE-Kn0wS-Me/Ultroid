"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""
from telethon import events
import asyncio


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 16)
    input_str = event.pattern_match.group(1)
    if input_str == "thanos":
        await event.edit(input_str)
        animation_chars = [
            "T͆͌ H̽̈́͠ Á͒͝ N͑̚̕ Ò̓͌ S̀̚͠",
            "i͋̿s̔̽̀",
            "C̸̫͇͎̈́̀̔o̵̡͔͚̓͐͝m̴͖̻̺̔͑͘m̴̢͍͓͒͛͠í̸͍͌̿͜n̴̺̦̻͊͐͒g̴͍̝͐̿͆",
            " https://telegra.ph/file/f1ac69a2abeef68c20961.mp4 \nPlug-in by [Wrench](t.me/WhySooSerious)"
        ]
        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 70])
