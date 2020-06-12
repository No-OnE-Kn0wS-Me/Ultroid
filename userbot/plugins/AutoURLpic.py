"""
Srt Automatic Profile Pic.....
Command: `.cpp`
:::::Credits::::::
1) Coded By: @WhySooSerious
2) Ported By: @Tb0N3 (Legend)
3) End Game Help By: @spechide
4) Custom / Modified Plugin for some magical effects by this Legendary Guy @PhycoNinja13b 
#curse: who ever edits this credit section will goto hell
⚠️DISCLAIMER⚠️
USING THIS PLUGIN CAN RESULT IN ACCOUNT BAN + CAS BAN + SPAM BAN + ACCOUNT SUSPENSION . IF THIS CAUSES ANY ISSUES< DON'T REPORT US.
WE WILL LAUGH AT YOU !!! xD
"""
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions
from uniborg.util import admin_cmd
import asyncio
import shutil 
import random, re


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

#Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/653fc27e3682bbf162909.jpg", #1
                         "https://telegra.ph/file/5ba3a1f382eb93e63fed4.jpg", #2
                         "https://telegra.ph/file/1325963e250c3fb7743a9.jpg", #3
                         "https://telegra.ph/file/1e204aae5fd8590170b41.jpg", #4
                         "https://telegra.ph/file/74980d69dbdca158707b2.jpg", #5
                         "https://telegra.ph/file/6e4129870762cd4dbbe02.jpg", #6
                         "https://telegra.ph/file/35705dc5b06395d5e0a5b.jpg", #7
                         "https://telegra.ph/file/a7906c58b99f34925690e.jpg", #8
                         "https://telegra.ph/file/42c5795a6afed9434f292.jpg", #9
                         "https://telegra.ph/file/d56f78f16b6dbb4d63761.jpg", #10
                         "https://telegra.ph/file/c562a89f51f200cd2d73d.jpg", #11
                         "https://telegra.ph/file/38cb0ae7a597f90cdfb6f.jpg", #12
                         "https://telegra.ph/file/5db152b6816ed38eeaa54.jpg", #13
                         "https://telegra.ph/file/8798ba20268c4d565c768.jpg", #14
                         "https://telegra.ph/file/155df2519ac7016088485.jpg", #15
                         "https://telegra.ph/file/32a1d3d57fc6e55a27a30.jpg",
                         "https://telegra.ph/file/fbcc1e15a9108624469e8.jpg",
                         "https://telegra.ph/file/0adfdf07fc605401a46ba.jpg",
                         "https://telegra.ph/file/f8f20b977921f70579699.jpg",
                         "https://telegra.ph/file/e53442f8088999bdcc9dd.jpg",
                         "https://telegra.ph/file/82b25c6d61a7cba911cea.jpg",
                         "https://telegra.ph/file/2a90be83bda957faae677.jpg",
                         "https://telegra.ph/file/29d5fc794c1ec04f70270.jpg",
                         "https://telegra.ph/file/39acabb5adda99239de57.jpg",
                         "https://telegra.ph/file/4757698842d88a76d578b.jpg", #10
                         "https://telegra.ph/file/77030271092dc88c3c6b3.jpg",
                         "https://telegra.ph/file/d7a29822dd81da67c3f06.jpg",
                         "https://telegra.ph/file/56d0bc1d268ba4b820fee.jpg",
                         "https://telegra.ph/file/b7a19715884228c1a07c4.jpg",
                         "https://telegra.ph/file/6bba4a75f40876003ae8a.jpg",
                         "https://telegra.ph/file/f07359a81ca8c783f9883.jpg",
                         "https://telegra.ph/file/b5120d0c4bf8f76f220fd.jpg",
                         "https://telegra.ph/file/1f1cff83afd6fc7321350.jpg",
                         "https://telegra.ph/file/f1b040c4c1bebf6e72e76.jpg".
                         "https://telegra.ph/file/783d45f0a273bfc3a782f.jpg"
                        ]
@borg.on(admin_cmd(pattern="cpp ?(.*)"))

async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./WRENCH/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            place_holder = None
    
    
        shutil.copy(downloaded_file_name, photo)
        im = Image.open(photo)
        current_time = datetime.now().strftime("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                    ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \n                                                             Time: %H:%M \n                                                          Date: %d.%m.%y \n                                                   ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 36)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(functions.photos.UploadProfilePhotoRequest(  # pylint:disable=E0602
                file
            ))
            os.remove(photo)
            
            await asyncio.sleep(60)
        except:
            return
