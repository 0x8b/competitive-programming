#!/usr/bin/env python

import re
import fileinput
import numpy as np

num = re.compile(r'\d+')

m = np.zeros((50, 6), dtype=np.int)

for line in fileinput.input():
    a, b = map(int, num.findall(line))

    if 'rect' in line:
        m[:a, :b] = 1
    elif 'column' in line:
        m[a] = np.roll(m[a], b)
    else:
        m[:, a] = np.roll(m[:, a], b)


assert int(np.sum(m)) == 106

print('\n'.join(map(lambda x: ''.join(map(str, x)), m.T)).replace('0', ' ').replace('1', '@'))

'''

 @@  @@@@ @    @@@@ @     @@  @   @@@@@  @@   @@@ 
@  @ @    @    @    @    @  @ @   @@    @  @ @    
@    @@@  @    @@@  @    @  @  @ @ @@@  @    @    
@    @    @    @    @    @  @   @  @    @     @@  
@  @ @    @    @    @    @  @   @  @    @  @    @ 
 @@  @    @@@@ @@@@ @@@@  @@    @  @     @@  @@@  

'''
