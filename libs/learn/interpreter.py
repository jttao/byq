#!/usr/bin/python
# -*- coding: utf-8 -*-

from token import *

class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()
    
    def word(self):  
        result = ''
        token = self.current_token
        while token.type==WORD: 
            result += token.value
            self.eat(WORD)
            token = self.current_token 
        return result

    def expr(self):
        """
        expr   : word(是|作)word词
        expr   : word是word关系
        """    
        result = self.word() 
        while self.current_token.type in (SHI, ZUO, CI):
            token = self.current_token
            if token.type == SHI:
                self.eat(SHI)
                result = result +":" + self.word()
            elif token.type == ZUO:
                self.eat(ZUO)
                result = result +":" + self.word()
            elif token.type == CI:
                self.eat(CI)
                result = result + "词" 
        return result