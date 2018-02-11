#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

def main(): 
    
    while True:
        try:
            try:
                text = raw_input('say> ')
            except NameError:  # Python3
                text = input('say> ')
        except EOFError:
            break
        if not text:
            continue   
        
        #s = u"中国china"
        #text = unicode(text)
        print(len(text)) 
        
        print text[0:2]

        """
        with open('../data/'+text+'.ch', 'r') as f:
            content = f.read().decode("utf")
            print content
            o = json.loads(content)
        """

if __name__ == '__main__':  
    main()