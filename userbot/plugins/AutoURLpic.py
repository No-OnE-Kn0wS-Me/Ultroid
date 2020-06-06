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
TELEGRAPH_MEDIA_LINKS = ["https://telegra.ph/file/63775dc739856b33cada7.jpg",
                         "https://telegra.ph/file/4e2c5360ed65596aee60c.jpg",
                         "https://telegra.ph/file/35705dc5b06395d5e0a5b.jpg",
                         "https://telegra.ph/file/a7906c58b99f34925690e.jpg",
                         "https://telegra.ph/file/42c5795a6afed9434f292.jpg",
                         "https://telegra.ph/file/155df2519ac7016088485.jpg"
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
        current_time = datetime.now().strftime("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                    ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡ \n                                                   Time: %H:%M \n                                                   Date: %d.%m.%y \n                                                   ⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
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
            
            await asyncio.sleep(15)
        except:
            return
