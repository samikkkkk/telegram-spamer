from loguru import logger

logger.add(
    "logs/validate/{time}.log",
    rotation="1 day",
    format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}",
    filter=lambda record: record["extra"].get("name") == "validate"
)

logger.add(
    "logs/parsing/{time}.log",
    rotation="1 day",
    format="{time:YYYY-MM-DD HH:mm:ss} {level} {message}",
    filter=lambda record: record["extra"].get("name") == "parse"
)

parse_logger = logger.bind(name="parse")
validate_logger = logger.bind(name="validate")
