#!/usr/bin/python
#encoding: utf-8
import codecs
import os
import sys
import xml.dom.minidom
from datetime import datetime, time

SCRIPT_ROOT = os.path.dirname(os.path.abspath(__file__))
YR_XML = SCRIPT_ROOT + '/varsel.xml'
CURRENT_WEATHER = SCRIPT_ROOT + '/current_weather.py'

doc = xml.dom.minidom.parse(YR_XML)
tabular = doc.getElementsByTagName('tabular')
if tabular:
    current = tabular[0].getElementsByTagName('time')[0]
    if current:    
        symbol_tag = current.getElementsByTagName('symbol')[0]
        temp_tag = current.getElementsByTagName('temperature')[0]

        if symbol_tag and temp_tag:
            symbol_num = symbol_tag.getAttribute('number')
            description = symbol_tag.getAttribute('name')
            temperature = temp_tag.getAttribute('value')

            if (len(symbol_num) == 1):
                symbol_num = '0%s' % symbol_num

            cl = time(datetime.now().hour, datetime.now().minute)
            five = time(05, 00)
            eight = time(20, 00)
            symbol = None
            if ((cl > five) and (cl < eight)):
                symbol = '%sd' % symbol_num 
            else:
                symbol = '%sn' % symbol_num 

            w_file = codecs.open(CURRENT_WEATHER, 'w', 'utf-8')
            w_file.write('%s;%s;%s' % (symbol, description, temperature))
            w_file.close()

            sys.exit(0)

w_file = open(CURRENT_WEATHER, 'w')
w_file.write('error')
w_file.close()
sys.exit(0)

