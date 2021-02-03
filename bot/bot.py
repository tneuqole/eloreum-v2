from discord.ext import commands
import boto3
import logging
import os
from dotenv import load_dotenv

# get env vars
load_dotenv()
bot_token = os.environ['BOT_TOKEN']
instance_id = os.environ['INSTANCE_ID']

# constants
prefix = '!'
start_cmd = prefix + 'start'
stop_cmd = prefix + 'stop'
status_cmd = prefix + 'status'
help_cmd = prefix + 'help'

# configure logger
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# get discord client
bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

# get ec2 client
ec2 = boto3.client('ec2')

@bot.event
async def on_ready():
    logger.info('Logged in as:')
    logger.info(bot.user.name)
    logger.info(bot.user.id)
    logger.info('------')

@bot.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Invalid command. Type !help for more info.')
    return
  raise error

@bot.command()
async def start(ctx, args=None):
  try:
    logger.info('Attempting to start instance.')
    ec2.start_instances(InstanceIds=[instance_id])
    await ctx.send('Server started.')
  except Exception as err:
    logger.error(str(err))
    await ctx.send('Error starting server. Try again later.')

@bot.command()
async def stop(ctx, args=None):
  try:
    logger.info('Attempting to stop instance.')
    ec2.stop_instances(InstanceIds=[instance_id])
    await ctx.send('Server stopped.')
  except Exception as err:
    logger.error(str(err))
    await ctx.send('Error stopping server. Try again later.')

@bot.command()
async def restart(ctx, args=None):
  try:
    logger.info('Attempting to restart instance.')
    ec2.reboot_instances(InstanceIds=[instance_id])
    await ctx.send('Server is restarting.')
  except Exception as err:
    logger.error(str(err))
    await ctx.send('Error restarting server. Try again later.')

@bot.command()
async def status(ctx, args=None):
  try:
    status = None
    logger.info('Checking instance status.')
    response = ec2.describe_instances(InstanceIds=[instance_id])
    status = response['Reservations'][0]['Instances'][0]['State']['Name']
    await ctx.send(f'Server status: {status}') 

  except Exception as err:
    logger.error(str(err))
    await ctx.send('Error checking status. Try again later.')

@bot.command()
async def help(ctx, args=None):
  await ctx.send('```start\t Start the server.\nstop\t  Stop the server.\nstatus\tCheck the server status.\nhelp\t  Show this message.```')



bot.run(bot_token)