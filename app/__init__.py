# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/fastCorrect/correctServer/app
File Name:     __init__.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/05
Software:      Vscode
'''

import sanic
from sanic.log import logger

from app.utils import read_config
from app.views.inference import CorrectInference
from app.listeners.logger import setup_logger
from app.listeners.init_model import init_model



def create_app(config_path="config.yaml"):
    # Create an App
    app = sanic.Sanic(__name__)

    # Read configurations
    config = read_config(config_path)

    app.config.update(config)

    # add listeners
    app.register_listener(setup_logger, "before_server_start")
    app.register_listener(init_model, "before_server_start")

    # add routers
    app.add_route(CorrectInference.as_view(), "/correct")

    return app
