from pyrogram import Client, filters
from pyrogram import *
import time
import os
import datetime




#############################################################[]
#############################################################[]
PYRO_CODE = os.environ.get("PYROC")                         #[]
ID = os.environ.get("IDV")                                  #[]
idtr = [int(ID)]                                            #[]
#############################################################[]  
#############################################################[]
asta = Client("asta", session_string = PYRO_CODE )          #[]
#############################################################[]
#############################################################[]






@asta.on_message(filters.text,group=7)
async def copy_text(clover, message):
    mci = message.chat.id
    m = message.text
    date = time.ctime()
    current_time = time.strftime("%H:%M:%S", time.localtime())
    date = datetime.datetime.now().strftime("%B")
    if message.from_user.id in idtr :
     if m=="فحص" or m == "asta" or m== "/test":
       ASTAID = "https://t.me/astapy"
       men = f"[𝖳𝗁𝖾 𝖡𝖾𝗌𝗍 𝖣𝖾𝗏 - (888)]({ASTAID})"
       await message.edit_text(f"{men}\nشغال والحمدالله 🏝️\n- 𝖳𝗁𝖾 𝖳𝗂𝗆𝖾 :  {current_time}\n- 𝖳𝗁𝖾 𝖣𝖺𝗍𝖾:  {date}",disable_web_page_preview=True)

dis1 = []

@asta.on_message(filters.text,group=1)
async def copy_text(clover, message):
    mci = message.chat.id
    m = message.text
    if message.from_user.id in idtr :
     if m=="تعطيل الارقام" or m=="تعطيل الرقم":
       if mci in dis1:
          await message.edit_text( f"**- الارقام معطلة من قبل**")
       if not mci in dis1:
          dis1.append(mci)
          await message.edit_text( f"**- تم تعطيل الارقام**")

     if m=="تفعيل الارقام" or m=="تفعيل الرقم":
       if not mci in dis1:
         await message.edit_text( f"**- الارقام مفعلة من قبل**")
       if mci in dis1:
         dis1.remove(mci)  
         await message.edit_text( f"**- تم تفعيل الارقام**")

     if "الرقم ↢"  in message.text:
         if not mci in dis3:
          sentence = message.text
          start_index = sentence.find("(")
          end_index = sentence.find(")")
          if start_index != -1 and end_index != -1:
           copied_text = sentence[start_index + 1:end_index]
           await message.edit_text( f"{copied_text}")
           time.sleep(3)
           await message.edit_text( f"ارقام")



dis2 = []

@asta.on_message(filters.text,group=2)
async def copy_text(clover, message):
    mci = message.chat.id
    m = message.text
    if message.from_user.id in idtr :
     if m=="تعطيل الكلمات" or m=="تعطيل الكلمة":
       if mci in dis2:
          await message.edit_text( f"**- الكلمات معطلة من قبل**")
       if not mci in dis2:
          dis2.append(mci)
          await message.edit_text( f"**- تم تعطيل الكلمات**")

     if m=="تفعيل الكلمات" or m=="تفعيل الكلمة":
       if not mci in dis2:
         await message.edit_text( f"**- الكلمات مفعلة من قبل**")
       if mci in dis2:
         dis2.remove(mci)  
         await message.edit_text( f"**- تم تفعيل الكلمات**")
     if "الكلمة ↢"  in message.text:
      if not mci in dis2:
       sentence = message.text
       start_index = sentence.find("(")
       end_index = sentence.find(")")
       if start_index != -1 and end_index != -1:
        copied_text = sentence[start_index + 1:end_index]
        await message.edit_text( f"{copied_text}")
        time.sleep(3)
        await message.edit_text( f"كلمات")




dis3 = []

@asta.on_message(filters.text,group=3)
async def copy_text(clover, message):
    mci = message.chat.id
    m = message.text
    if message.from_user.id in idtr  :
     if m=="تعطيل التفكيك" or m=="تعطيل تفكيك":
       if mci in dis3:
          await message.edit_text( f"**- التفكيك معطل من قبل**")
       if not mci in dis3:
          dis3.append(mci)
          await message.edit_text( f"**- تم تعطيل التفكيك**")

     if m=="تفعيل التفكيك" or m=="تفعيل تفكيك":
       if not mci in dis3:
         await message.edit_text( f"**- التفكيك مفعل من قبل**")
       if mci in dis3:
         dis3.remove(mci)  
         await message.edit_text( f"**- تم تفعيل التفكيك**")
     if "فكك ↢"  in message.text:
      if not mci in dis3:
       sentence = message.text
       start_index = sentence.find("(")
       end_index = sentence.find(")")
       if start_index != -1 and end_index != -1:
        copied_text = sentence[start_index + 1:end_index]
        spaced_text = " ".join(copied_text)
        await message.edit_text( f"{spaced_text}")
        time.sleep(3)
        await message.edit_text( f"تفكيك")


        

dis4 = []
@asta.on_message(filters.text,group=4)
async def copy_text(clover, message):
    mci = message.chat.id
    m = message.text
    if message.from_user.id in idtr :
     if m=="تعطيل التركيب" or m=="تعطيل تركيب":
       if mci in dis4:
          await message.edit_text( f"**- التركيب معطل من قبل**")
       if not mci in dis4:
          dis4.append(mci)
          await message.edit_text( f"**- تم تعطيل التركيب**")

     if m=="تفعيل التركيب" or m=="تفعيل تركيب":
       if not mci in dis4:
         await message.edit_text( f"**- التركيب مفعل من قبل**")
       if mci in dis4:
         dis4.remove(mci)  
         await message.edit_text( f"**- تم تفعيل التركيب**")
     if "ركب ↢"  in message.text:
       if not mci in dis4:
        sentence = message.text
        start_index = sentence.find("(")
        end_index = sentence.find(")")
        if start_index != -1 and end_index != -1:
         copied_text = sentence[start_index + 1:end_index]
         no_spaces_text = copied_text.replace(" ", "")
         await message.edit_text( f"{no_spaces_text}")
         time.sleep(3)
         await message.edit_text( f"تركيب")





print("User Bot Is Runing 🏝️🥇 ")
asta.run()