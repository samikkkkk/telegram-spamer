import glob

from utils.logs import parse_logger

async def parse_sessions():
    sessions = []
    for file in glob.glob("sessions/*.session"):
        parse_logger.info(f"Found session file: {file}")

        session_name = file.split("/")[-1].replace(".session", "")
        sessions.append(session_name)
    return sessions