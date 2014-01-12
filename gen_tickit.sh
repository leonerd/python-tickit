#!/bin/sh

echo 'Exporting tickit.h to XML...'
h2xml.py -o _tickit.xml /usr/include/tickit.h 2> /dev/null
echo 'Importing XML into tickit._tickit...'
xml2py.py -o tickit/_tickit.py _tickit.xml -r Tickit.* -r TICKIT_.* -r tickit_.* 2> /dev/null
echo
