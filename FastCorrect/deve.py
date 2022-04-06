# -*- coding: utf-8 -*-
'''
Project:       /root/projects/Pythons/fastCorrect/FastCorrect
File Name:     deve.py
Author:        Chaos
Email:         life0531@foxmail.com
Date:          2022/04/05
Software:      Vscode
'''

import re
from FastCorrect.fastcorrect_model import FastCorrectModel


if __name__ == '__main__':
    # set paramters
    model_name_or_path = "FastCorrect/finetune"
    iter_decode_max_iter = 0
    # edit_thre = 0
    # test_epoch = "best"
    checkpoint_file = "checkpoint_best.pt"
    
    data_name_or_path = "FastCorrect/data/bin_data" # <Path-to-AISHELL1-Training-Binary-Data>
    bpe = "sentencepiece"
    sentencepiece_model = "FastCorrect/pretrained_model/FastCorrect_zhwiki_sentencepiece.model"
    
    # init model
    transf_gec = FastCorrectModel.from_pretrained(model_name_or_path, checkpoint_file=checkpoint_file, data_name_or_path=data_name_or_path, bpe=bpe, sentencepiece_model=sentencepiece_model)
    transf_gec.eval()
    
    round = 0
    print("\n\n\n\n\n\n")

    while 1:
        # get input && setup them ready
        # sentence = "说一个人做点好事并不难难的是一辈子做好事"
        print("-"*10 + f"round-{round}" + "-"*10)
        print("Please input a sentence, the script will automatically remove all English or Number in it.")
        sentence = input("Input your sentence: \n")
        re.sub("[a-z][A-Z][0-9]", "", sentence)
        sentence = " ".join(sentence).strip()
        
        # get output
        x = transf_gec.binarize(sentence)
        x = transf_gec.generate(x, iter_decode_max_iter=iter_decode_max_iter)
        y = transf_gec.decode(x[0][0]["tokens"])
        
        print("#"*25)
        print(f"## Input:  {''.join(sentence.split(' '))}")
        print(f"## Output: {y}")
        print("#"*25)
        
        round += 1