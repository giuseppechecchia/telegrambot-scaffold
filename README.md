# Create a Telegram Bot

To create a bot on Telegram, follow these steps:

- Open Telegram and search for the bot named BotFather.
- Start a chat with BotFather and use the command `/newbot` to create a new bot.
- Choose a name for your bot.
- Choose a username for your bot that ends with "bot".
- After completing these steps, BotFather will provide you with an Access Token. This token is essential for interacting with your bot via the API.

## Obtain a Test Payment Token

- Contact @BotFather using the command `/mybots`.
- Select the bot for which you want to enable payments.
- Go to the 'payment' section and follow the instructions to obtain a payment token.
- Note: The Test Payment Token allows you to simulate transactions.

For more details: [Telegram Payments Documentation](https://core.telegram.org/bots/payments)

## How to Run the Bot?

- Ensure Python 3 is installed on your device.
- Install the necessary libraries (listed in the `requirements.txt` file).
- Take the data provided by @BotFather and insert it into the `main.py` file.

Library Documentation: [PyTBA Documentation](https://pytba.readthedocs.io/en/latest/)  
Telegram Documentation: [Telegram Bot API](https://core.telegram.org/bots/api)
