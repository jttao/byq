#!/usr/bin/python
# -*- coding: utf-8 -*-

# Token types  主语、谓语、宾语（定语、状语、补语） 
ZHU        = 'ZHU'
WEI        = 'WEI'
BIN        = 'BIN'
DING       = 'DING'
ZHUANG     = 'ZHUANG'
BU         = 'BU' 
BA         = 'BA'
BEI        = 'BEI'
SHI        = '是'
ZUO        = '作'
CI         = '词'
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