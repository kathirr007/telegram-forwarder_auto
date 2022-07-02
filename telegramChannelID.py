import sys
import asyncio

from telethon import TelegramClient

# from decouple import config
api_id='14497464'
api_hash='82231becdecd215ff84e7485b4792f13'
channel_link = 'https://t.me/BTCST_Community_EN'

async def channel_id_from_link(client, channel_link):
    return "-100" + str((await client.get_entity(channel_link)).id)

async def main(channel_link):
    async with TelegramClient(
        "test", api_id, api_hash
    ) as client:
        channel_id = await channel_id_from_link(client, channel_link)

    return channel_id

if __name__ == "__main__":
    channel_link = sys.argv[1]
    channel_id = asyncio.run(main(channel_link))
    print(channel_id)
