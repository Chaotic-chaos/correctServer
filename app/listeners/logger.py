# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/fastCorrect/correctServer/app/listeners
File Name:     logger.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/05
Software:      Vscode
'''

'''
Setup the logger, ouput the logs both to file and stdout
'''

from sanic.log import logger
import logging


async def setup_logger(app, loop):
    level_map = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL
    }

    stream_handler = logging.StreamHandler()
    rotating_handler = logging.handlers.RotatingFileHandler(
        filename=app.config.LOG["filename"],
        maxBytes=app.config.LOG["maxBytes"],
        backupCount=app.config.LOG["backupCount"]
    )

    stream_handler.setLevel(level=level_map[app.config.LOG["level"]])
    rotating_handler.setLevel(level=level_map[app.config.LOG["level"]])

    stream_handler.setFormatter(logging.Formatter(app.config.LOG["format"]))
    rotating_handler.setFormatter(logging.Formatter(app.config.LOG["format"]))

    # logger.addHandler(stream_handler)
    logger.addHandler(rotating_handler)
