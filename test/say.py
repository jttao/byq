#!/usr/bin/python
# -*- coding: utf-8 -*-
import os 

def main():    
    while True:
        try:
            try:
                text = raw_input('say> ')
            except NameError:  # Python3
                text = input('say> ')
        except EOFError:
            break
        if not text or text.isspace():
            continue 
        
        # 表达式
        lexer = Lexer(text) 
        interpreter = Interpreter(lexer)
        result = interpreter.expr() 

        print(result) 

if __name__ == '__main__':
    main()
