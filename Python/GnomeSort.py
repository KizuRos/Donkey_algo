#! /usr/bin/python2.7
"""
#=============================================================================#

FILE            : GnomeSort.py 

DESCRIPTION     : Implementation of Elementary Gnome Sorting in Python

COMPLEXITY      : O(n)
NOTES           : 
AUTHOR(s)       : Spyros Lalos (spyroslal@gmail.com)
CREATED         : Nov 16 ##:##:## CEST 2014

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#=============================================================================#
"""
import random

def GnomeSort ( slist ):
    tmp = 0
    i = 0

    while i < len(slist):
        if ( i == 0 or slist[i-1] <= slist[i] ):
            i +=1
        else:
            #swap elements
            slist[i-1], slist[i]  = slist[i], slist[i-1]
            i -= 1

    return slist

# Random generated list
slist = [ random.randint(0, 100) for c in range(10) ]
print GnomeSort (slist)
