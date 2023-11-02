from telegram import*
from telegram.ext import*
from keys import TOKEN
from random import randint
import os
###################################################################################################################
        
###################################################################################################################
'''
#Handels
When youser uses /'command' the command linked with one of these functions will activate 
'''
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello i'm Cavi's side peice nice to meet you")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("In devellopement...")

async def everyone_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("@nahuh7 @cowbow_lache @NAHOM52 @Alphaboy975 @AlmightyNaeNaeGoblin @Yoniman23 @obanium @lelew_zeG @eyoooel @SMKoutside @Chat_gpt_now @mohkhalidabd @baddboy45")

async def imgday_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(photo="https://images.app.goo.gl/ajfEz3inLi8khkkq7")

'''async def aud_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_audio(audio="Media\Rick Astley.mp3",title="Fortnigga ft.Young Nigga 14" )'''

###################################################################################################################
'''
#Responses
Replies to a designated text
'''
def handle_response(text:str) -> str:
    conv:str = text.lower()
    if "hop on" in conv:
        return "Y'all better hop on the game bitch ass niggas"
    if "easter egg" in conv:
        return "There are special replies if you find the right words"
    return ""

###################################################################################################################
'''
#Message handler
Checks if it's from a Gc or Dm and continiues accordingly
'''
async def handle_message(update:Update, context:ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text:str = update.message.text

    print(f'User({update.message.chat_id}) in {message_type}:"{text}"')
    
    if message_type == "group":
        if "@Imexperimentingmyboys_bot" in text:
            new_text:str = text.replace("@Imexperimentingmyboys_bot", "").strip()
            response:str = handle_response(new_text)
        else:
            return
    else:
        response:str = handle_response(text)

    print('Bot:',response)
    await update.message.reply_text(response)

###################################################################################################################
'''
#Errors
'''

async def errpr(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

###################################################################################################################
'''
#Run bot
'''
if __name__ == '__main__':
    print("Bot is running...")
    app = Application.builder().token(TOKEN).build()
    
    #Commands
    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(CommandHandler('everyone',everyone_command))
    app.add_handler(CommandHandler('img',imgday_command))
    app.add_handler(CommandHandler('aud',aud_command))
    #app.add_handler(CommandHandler('numg',numgame_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT,handle_message))

    #Errors
    app.add_error_handler(error)

    #Updates
    print("Bot is Polling...")
    app.run_polling(poll_interval=1.0)













