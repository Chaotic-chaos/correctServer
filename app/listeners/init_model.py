# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/fastCorrect/correctServer/app/listeners
File Name:     init_model.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/05
Software:      Vscode
'''

from sanic.log import logger
import os
from FastCorrect.FastCorrect.fastcorrect_model import FastCorrectModel


async def init_model(app, loop):
    logger.info("Starting setup Model...")

    model_path = app.config.MODEL["model_path"]
    data_path = app.config.MODEL["data_path"]
    bpe = getattr(app.config.MODEL, "bpe", "sentencepiece")
    sentencepiece_model = app.config.MODEL["sentencepiece_model"]

    model = FastCorrectModel.from_pretrained(
        model_name_or_path=os.path.split(model_path)[0],
        checkpoint_file=os.path.split(model_path)[-1],
        data_name_or_path=data_path,
        bpe=bpe,
        sentencepiece_model=sentencepiece_model
        )

    model.eval()

    logger.info("Model loaded!")

    app.ctx.fast_correct = model