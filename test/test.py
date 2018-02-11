#!/usr/bin/python
# -*- coding: utf-8 -*-

import mmseg

def main():
    mmseg.Dictionary.load_dictionaries()
    # 设置中文
    while True:
        try:
            try:
                text = raw_input('say> ')
            except NameError:  # Python3
                text = input('say> ')
        except EOFError:
            break
        if not text:
            continue   
        algor = mmseg.Algorithm(text.decode("GBK"))
        for tok in algor:
            print '%s [%d..%d]' % (tok.text, tok.start, tok.end)

if __name__ == '__main__': 
    main()