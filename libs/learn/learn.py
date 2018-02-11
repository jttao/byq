#!/usr/bin/python
# -*- coding: utf-8 -*- 
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from lexer import *
from interpreter import *

def main():    
    while True:
        try:
            try:
                text = raw_input('learn> ')
            except NameError:  # Python3
                text = input('learn> ')
        except EOFError:
            break
        if not text or text.isspace():
            continue 
        
        text  = text.decode("gbk")  
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr() 
        print(result) 
        
if __name__ == '__main__':
    main()
