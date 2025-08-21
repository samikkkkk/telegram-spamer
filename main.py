import os
import asyncio

from dotenv import load_dotenv

from pyrogram import Client

from utils.parser import parse_sessions
from utils.validate import validate_session

load_dotenv()

async def main():

    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')

    if not api_id or not api_hash:
        raise ValueError("API_ID and API_HASH must be set in the environment variables.")
    
    sessions = await parse_sessions()
    print(sessions) # debug

    if not sessions:
        print("No sessions found.")
        return
    
    valid_sessions = await validate_session(sessions, api_id, api_hash)

    for session_name in valid_sessions:
            async with Client(f"sessions/{session_name}", api_id=api_id, api_hash=api_hash) as app:
                user = await app.get_me()


                

asyncio.run(main())
