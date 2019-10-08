import datetime
import os

from glideinmonitor.lib.config import config


# TODO: use python std logging

def log(error_level, message):
    if config["Log_Level"] == "NONE":
        return

    if config["Log_Level"] == "ERROR":
        if error_level != "ERROR":
            return

    if config["Log_Level"] == "WARNING":
        if error_level == "INFO":
            return

    # Write to error log
    log_location_dir = os.path.join(config['Log_Dir'], 'indexer')
    if not os.path.exists(log_location_dir):
        os.makedirs(log_location_dir)
    log_location = os.path.join(log_location_dir, datetime.datetime.now().strftime("%Y-%m-%d") + ".txt")
    with open(log_location, "a") as log_file:
        log_file.write(error_level + " - " + str(int(datetime.datetime.now().timestamp())) + " - " + message + "\n")
