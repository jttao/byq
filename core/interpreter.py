#!/usr/bin/python
# -*- coding: utf-8 -*-

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
