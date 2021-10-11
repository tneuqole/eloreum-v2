import logging

from nacl.signing import VerifyKey

from bot import handle_restart_cmd, handle_start_cmd, handle_status_cmd, handle_stop_cmd
from constants import PUBLIC_KEY, BotCommands, InteractionTypes

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def verify_signature(event):
    raw_body = event.get("rawBody")
    auth_sig = event["params"]["header"].get("x-signature-ed25519")
    auth_ts = event["params"]["header"].get("x-signature-timestamp")

    message = auth_ts.encode() + raw_body.encode()
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    verify_key.verify(message, bytes.fromhex(auth_sig))  # raises an error if unequal


def lambda_handler(event, context):
    logger.info(event)
    # verify the signature
    try:
        verify_signature(event)
    except Exception as err:
        logger.error("unauthorized request", exc_info=True)
        raise Exception(f"[UNAUTHORIZED] Invalid request signature: {err}")

    # check if message is a ping
    if event.get("body-json").get("type") == InteractionTypes.PONG:
        return {"type": InteractionTypes.PONG}

    # handle bot command
    cmd = event.get("body-json").get("data").get("name")
    if cmd == BotCommands.START:
        return handle_start_cmd()
    elif cmd == BotCommands.STOP:
        return handle_stop_cmd()
    elif cmd == BotCommands.RESTART:
        return handle_restart_cmd()
    elif cmd == BotCommands.STATUS:
        return handle_status_cmd()

    logger.info("returning none")
    return None
