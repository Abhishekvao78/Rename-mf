import logging
from telegram.ext import Updater, CommandHandler

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Telegram bot token (replace with your own token)
TOKEN = 'your_token_here'

# Create the updater and dispatcher
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

# Define the rename command handler
def rename(update, context):
    # Get the message from the user
    old_name = context.args[0]
    new_name = context.args[1]

    # Perform the renaming logic (replace with your own logic)
    renamed_name = old_name.replace(' ', '_')

    # Send the renamed name back to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'Renamed "{old_name}" to "{renamed_name}"')

# Register the command handler
rename_handler = CommandHandler('rename', rename)
dispatcher.add_handler(rename_handler)

# Start the bot
updater.start_polling()

