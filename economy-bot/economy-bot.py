from boilerplate.logger import Logger

import modules.configuration as configuration
from classes.bot_database import BotDatabase
from classes.economy_bot import EconomyBot

logger = None
database = None

if configuration.logging_level:
    logger = Logger(level=configuration.logging_level)
else:
    raise Exception("Environment variable ECONOMY_LOGGING_LEVEL not found")

if configuration.database_host and configuration.database_user and configuration.database_password and configuration.database_name and configuration.database_configuration_collection:
    try:
        database = BotDatabase(host=configuration.database_host, user=configuration.database_user,
                               database=configuration.database_name, password=configuration.database_password,
                               configuration_repository=configuration.database_configuration_collection,
                               logger=logger)
    except Exception as ex:
        raise Exception(f"Exception during database startup: {ex}")
else:
    raise Exception("Database environment variables not properly configured, please check documentation")

economy_bot = EconomyBot(database=database, logger=logger)

if configuration.discord_token:
    economy_bot.run(configuration.discord_token)
else:
    raise Exception("Environment variable ECONOMY_DISCORD_TOKEN not found")
