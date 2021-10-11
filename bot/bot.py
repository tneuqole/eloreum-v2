import logging

import boto3

from constants import INSTANCE_ID, InteractionTypes

# configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# get ec2 client
ec2 = boto3.client("ec2")


def handle_start_cmd():
    content = ""
    try:
        logger.info("Attempting to start instance.")
        ec2.start_instances(InstanceIds=[INSTANCE_ID])
        content = "Server started."
    except Exception as err:
        logger.error(str(err))
        content = "Error starting server. Try again later."

    return format_response(content)


def handle_stop_cmd():
    content = ""
    try:
        logger.info("Attempting to stop instance.")
        ec2.stop_instances(InstanceIds=[INSTANCE_ID])
        content = "Server stopped."
    except Exception as err:
        logger.error(str(err))
        content = "Error stopping server. Try again later."

    return format_response(content)


def handle_restart_cmd():
    content = ""
    try:
        logger.info("Attempting to restart instance.")
        ec2.reboot_instances(InstanceIds=[INSTANCE_ID])
        content = "Server is restarting."
    except Exception as err:
        logger.error(str(err))
        content = "Error restarting server. Try again later."

    return format_response(content)


def handle_status_cmd():
    content = ""
    try:
        logger.info("Checking instance status.")
        response = ec2.describe_instances(InstanceIds=[INSTANCE_ID])
        status = response["Reservations"][0]["Instances"][0]["State"]["Name"]
        content = f"Server status: {status}"
    except Exception as err:
        logger.error(str(err))
        content = "Error checking status. Try again later."

    return format_response(content)


def format_response(content: str) -> dict:
    return {
        "type": InteractionTypes.MESSAGE_WITH_SOURCE,
        "data": {
            "tts": False,
            "content": content,
            "embeds": [],
            "allowed_mentions": [],
        },
    }
