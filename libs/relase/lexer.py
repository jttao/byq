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
        
    def node(self):
        result = self.current_char
        self.advance()
        result += self.current_char
        self.advance()
        return result

    def node_f(self):
        result = self.current_char
        self.advance()
        result += self.current_char
        self.advance()
        result += self.current_char
        self.advance()
        return result

    def node_m(self):
        result = self.current_char
        self.advance()
        result += self.current_char
        self.advance()
        result += self.current_char
        self.advance()
        return result
        
    def node_z(self):
    def node_n(self):

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
            
            if char == '的': 
                self.advance()
                return Token(DE, char)
            
            if char == '节':  
                return Token(NODE, self.node())

            if char == '父':  
                return Token(NODE_F, self.node_f())
                
            if char == '母':  
                return Token(NODE_M, self.node_m())
            
            if char == '子':  
                return Token(NODE_Z, self.node_z())

            if char == '女':  
                return Token(NODE_N, self.node_n())

            if char is not None: 
                self.advance()
                return Token(WORD, char)
            
            self.error()
        
        return Token(EOF, None)
