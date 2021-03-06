#!python3
from common_junk import *
from configparser import SafeConfigParser
import ebay_scraper
import gh_scraper
import reddit_scraper
import logging
import json
import discord_bot
import time
import re 

# Master script that executes searches, then, based on configuraiton, reports the information to various outlets like Discord (soon to include SMS vis twilio)/.

# configure logging
logger = logging.getLogger(__name__)

def write_temp(data):
    with open('notifications.txt', 'w') as temp_file:
        json_obj = []
        for item in data:
           json_obj.append(item)
        temp_file.write(json.dumps(json_obj))

def add_to_list(existing_list, new_list):
    for item in new_list:
        if item not in existing_list:
            existing_list.append(item)
    return existing_list

def main():
    while True:
        data_block = []
        if True:
            reddit_data = reddit_scraper.main()
            data_block = add_to_list(data_block, reddit_data)
        if True:
            ebay_data = ebay_scraper.main()
            data_block = add_to_list(data_block, ebay_data)
        #if True:
        #    gh_data = gh_scraper.main()
        #    data_block = add_to_list(data_block, gh_data)
        write_temp(data_block) 
        if len(data_block):
            discord_bot.main()
        time.sleep(30)
        data_block = []
        write_temp(data_block)
if __name__ == "__main__":
    main()
