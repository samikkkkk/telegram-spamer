import asyncio
from typing import List, Tuple

from pyrogram import Client
from pyrogram.errors import AuthKeyUnregistered, UserDeactivated, SessionExpired

from utils.logs import validate_logger as logger


async def validate_single_session(session_name: str, api_id: int, api_hash: str) -> Tuple[bool, str, str]:
    try:
        async with Client(f"sessions/{session_name}", api_id=api_id, api_hash=api_hash) as app:
            user = await app.get_me()

            logger.success(f"[VALID] {session_name} - {user.first_name} {user.last_name} (@{user.username}) | {user.id}")
            await asyncio.sleep(1)
            return True, session_name, ""
    except (AuthKeyUnregistered, UserDeactivated, SessionExpired) as e:

        logger.error(f"[INVALID] {session_name} - {str(e)}")
        return False, session_name, f"Session is invalid: {e}"
    except Exception as e:

        logger.error(f"[VALIDATION ERROR] {session_name} - {str(e)}")
        return False, session_name, f"Error occurred: {e}"

async def validate_session(sessions: List[str], api_id: int, api_hash: str) -> List[str]:
    tasks = [validate_single_session(session, api_id, api_hash) for session in sessions]
    results = await asyncio.gather(*tasks)
    
    valid_sessions = []
    for is_valid, session_name, error_msg in results:
        if is_valid:
            valid_sessions.append(session_name)
        else:
            print(f"Session '{session_name}': {error_msg}")
    
    return valid_sessions