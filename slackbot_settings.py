# -*- coding: utf-8 -*-
import os

API_TOKEN = os.environ["SLACK_API_TOKEN"]

PLUGINS = [
    'slackbot.plugins',
    'plugins',
]

default_reply = "pi" 
