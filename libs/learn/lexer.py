#!/usr/bin/python
# -*- coding: utf-8 -*-

from token import *

class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "(A):(ABC),(A):[{X:[XX,XX]},{}"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Invalid character')

    def advance(self):
        """Advance the `pos` pointer and set the `current_char` variable.""" 
        self.pos += 1
        if self.pos > len(self.text) - 1:
            self.current_char = None  # Indicates end of input
        else: 
            self.current_char = self.text[self.pos]
        
    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
        
    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer) 
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:
            
            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            char = self.current_char.decode("utf")
            
            if char == '是': 
                self.advance()
                return Token(SHI, char)
            
            if char == '作': 
                self.advance()
                return Token(ZUO, char)
                        
            if char == '词': 
                self.advance()
                return Token(CI, char)
            
            if char is not None: 
                self.advance()
                return Token(WORD, char)
            
            self.error()
        
        return Token(EOF, None)
