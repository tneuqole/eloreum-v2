import os

from dotenv import load_dotenv

load_dotenv()

PUBLIC_KEY = os.environ[
    "PUBLIC_KEY"
]  # found on Discord Application -> General Information page
INSTANCE_ID = os.environ["INSTANCE_ID"]


class BotCommands:
    START = "start"
    STOP = "stop"
    RESTART = "restart"
    STATUS = "status"


class InteractionTypes:
    PONG = 1
    MESSAGE_WITH_SOURCE = 4
