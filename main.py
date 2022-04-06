# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/fastCorrect/correctServer
File Name:     main.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/05
Software:      Vscode
'''

from app import create_app


if __name__ == '__main__':
    app = create_app("./config.yaml")

    app.run(host="0.0.0.0", port=8000, debug=app.config.get("DEBUG", False), workers=app.config.get("WORKERS", 1))