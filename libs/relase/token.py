#!/usr/bin/python
# -*- coding: utf-8 -*-

# Token types  

NODE       = 'NODE'
NODE_F     = 'NODE_F'
NODE_M     = 'NODE_M' 
NODE_Z     = 'NODE_Z'
NODE_N     = 'NODE_N' 
SHI        = 'SHI'
DE         = 'DE'
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