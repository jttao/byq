#!/usr/bin/python
# -*- coding: utf-8 -*-
import Token form Token

class Lexer(object):
    def __init__(self, text):
        # client string input, e.g. "4 + 2 * 3 - 6 / 2"
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

    def is_chinese(self,uchar): 
        """判断一个unicode是否是汉字""" 
        if uchar >= u'/u4e00' and uchar<=u'/u9fa5': 
            return True 
        else: 
            return False

    def word(self):
        """Return a (multidigit) integer consumed from the input."""
        result = ''
        while self.current_char is not None and self.is_chinese(self.current_char):
            result += self.current_char
            self.advance()
        return result
        
    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        while self.current_char is not None:

            if self.current_char.isspace():
                self.skip_whitespace()
                continue
            
            if self.is_chinese(self.current_char):
                return Token(WORD, self.word())
            
            if self.current_char == '是':
                self.advance()
                return Token(SHI, '是')
            
            self.error()

        return Token(EOF, None)
