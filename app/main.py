import discord
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TextClassificationPipeline,
)
from config import Config
from logger import get_logger

DISCORD_TOKEN = Config.discord_token
client = discord.Client()
logger = get_logger("discord-bot")

tokenizer = AutoTokenizer.from_pretrained(
    "/app/app/xlm-roberta-base-language-detection", local_files_only=True
)
model = AutoModelForSequenceClassification.from_pretrained(
    "/app/app/xlm-roberta-base-language-detection/", local_files_only=True
)
pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer)


@client.event
async def on_message(message):
    msg = message.content

    logger.info(msg)

    # if msg is sent by bot itself then ignore
    if message.author == client.user:
        return

    # don't use model to too short messages
    if len(msg) <= Config.min_post_char_length:
        return

    # show message if language not on the language list
    prediction = pipeline(msg)[0]
    if not prediction["label"] in Config.accepted_languages:
        logger.info(prediction)
        await message.channel.send(Config.message)


if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
    logger.info("Running")
