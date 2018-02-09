#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import mmseg

# Token types  主语、谓语、宾语（定语、状语、补语） 
ZHU        = 'ZHU'
WEI        = 'WEI'
BIN        = 'BIN'
DING       = 'DING'
ZHUANG     = 'ZHUANG'
BU         = 'BU'
SHI        = 'SHI'
BA         = 'BA'
BEI        = 'BEI'
EOF        = 'EOF'

class Token(object):
    def __init__(self, type, value):
        # token type: CHAR,WORD
        self.type = type
        # token value:  or None
        self.value = value   

    def __str__(self):
        """String representation of the class instance. 
        Examples: 
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()

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
    
    def factor(self):
        """factor : INTEGER | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == INTEGER:
            self.eat(INTEGER)
            return token.value
        elif token.type == LPAREN:
            self.eat(LPAREN)
            result = self.expr()
            self.eat(RPAREN)
            return result

    def phrase(self):
        """phrase : factor ((MUL | DIV) factor)*"""
        result = self.factor()

        while self.current_token.type in (MUL, DIV):
            token = self.current_token
            if token.type == MUL:
                self.eat(MUL)
                result = result * self.factor()
            elif token.type == DIV:
                self.eat(DIV)
                result = result / self.factor()

        return result

    def expr(self):
        """Arithmetic expression parser / interpreter.
        主谓宾、定状补，主干枝叶分清楚。
        定语必居主宾前，谓前为状谓后补。
        状语有时位主前，逗号分开心有数。
        符号：
        =主语=|谓语|{宾语}(定语)[状语]<补语> 
        say> 主语、谓语、宾语（定语、状语、补语）  
        1.=主语=|谓语|
        2.=主语=|谓语|{宾语}
        
        expr   : phrase (=主语=|谓语|{宾语}(定语)[状语]<补语>)*
        phrase : word ((MUL | DIV) word)*
        word   : char | word 
        """ 

        result = self.phrase()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.phrase()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.phrase()
        
        return result

def main():   
    #path_words = os.path.join(os.path.dirname(__file__), 'data', 'words.dic')
    #path_chars = os.path.join(os.path.dirname(__file__), 'data', 'chars.dic') 
    #mmseg.Dictionary.load_words(path_words)
    #mmseg.Dictionary.load_chars(path_chars)
    #mmseg.Dictionary.load_dictionaries()
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

        algor = mmseg.Algorithm(text.decode("GBK"))
        array = [] 
        for tok in algor:
            array.append(tok.text)
            #print '%s [%d..%d]' % (tok.text, tok.start, tok.end) 
        print('-------------------')  
        
        lexer = Lexer(array)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)
        
if __name__ == '__main__':
    main()
