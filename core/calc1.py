#!/usr/bin/python
# -*- coding: utf-8 -*-
import mmseg

# Token types 
CHAR       = 'CHAR'
WORD       = 'WORD' 
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

class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "text"
        self.text = text 
        # self.pos is an index into self.text
        self.pos = 0 
        # current token instance
        self.current_token = None  
        self.current_char = self.text[self.pos]  
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
        text = self.text
        
        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        current_char = text[self.pos]

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        
        token = Token(WORD, current_char)
        self.pos += 1
        return token

        self.error()

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> WORD WORD WORD WORD """
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        #
        word = self.current_token
        self.eat(WORD)

        # EOF token

        return word.value

def main():  
    mmseg.Dictionary.load_dictionaries()
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
            print '%s [%d..%d]' % (tok.text, tok.start, tok.end) 
        print('-------------------')   
        interpreter = Interpreter(array)
        result = interpreter.expr() 
        print(result)   
        
if __name__ == '__main__':
    main()
