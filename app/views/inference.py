# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/fastCorrect/correctServer/app/views
File Name:     inference.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/05
Software:      Vscode
'''

import re
import time
from sanic import json, text
from sanic.log import logger
from sanic.views import HTTPMethodView


class CorrectInference(HTTPMethodView):
    async def post(self, request):
        app = request.app
        
        # logger.info(app.fast_correct)
        # return text("Good!")

        iter_decode_max = getattr(app.config.MODEL, "iter_decode_max", 0)
        beam_size = getattr(app.config.MODEL, "beam_size", 5)

        start_time = time.time()
        sentence = request.json.get("sentence")
        origin_sentence = sentence
        if not sentence:
            return json({
                "code": 400,
                "process_time": format(time.time() - start_time, ".4f"),
                "msg": "Bad Request: No sentence"
            })
        else:
            re.sub("[a-z][A-Z][0-9]", "", sentence)
            sentence = " ".join(sentence).strip()
            x = app.ctx.fast_correct.binarize(sentence)
            x = app.ctx.fast_correct.generate(x, iter_decode_max=iter_decode_max, beam=beam_size)
            x = app.ctx.fast_correct.decode(x[0][0]["tokens"])

            end_time = time.time()

            # Send into logs
            logger.info(f"Processed in {format(end_time - start_time, '.4f')}s: | {origin_sentence} | -> | {x} |")

            return json({
                "code": 200,
                "process_time": format(end_time - start_time, '.4f'),
                "msg": {
                    "origin": origin_sentence,
                    "corrected": x
                }
            })
