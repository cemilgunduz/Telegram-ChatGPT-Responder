# This python code is for a telegram bot to respons chat using chatgpt api
# There are no optimizations to the prompts. 
# Using some chat history might return more meaningful responses 
# but i only used the last user message as prompt.

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import openai

# Set up the ChatGPT and TG API endpoints
TG_BOT_KEY = "TOKEN_OF _YOUR_BOT"
OPENAI_KEY = "YOUR_OPENAI_API_KEY"

openai.api_key = OPENAI_KEY

def get_response(prompt):
    # Get the response from davinci-003 
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    #just return the text
    #there are other properties of the response but i just need the text.
    return response["choices"][0]["text"]

def respond(update, context):
    # Get the user's message
    message = update.message.text

    # Generate a response using the ChatGPT API
    response = get_response(message)

    # Send the response to the user
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

if __name__ == '__main__':
    # Create an instance of the Updater class
    updater = Updater(token='{}'.format(TG_BOT_KEY), use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the responder handler to dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, respond))

    # Start polling for updates from Telegram
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT, SIGTERM or SIGABRT
    updater.idle()

