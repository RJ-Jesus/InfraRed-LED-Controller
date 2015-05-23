#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from math import pi, sin


frequency = {'c4':  261.63, 'd4':  293.66, 'e4':  329.63, 'f4':  349.23, 'g4':  392.00, 'a4':  440.00, 'b4':  493.88, 'c5':  523.25}
frame_rate = 44100
amplitude = 32767


def sinusoid(note):
    data = []
    if note in frequency:
        freq = frequency[note]
    else:
        freq = 0
    for i in range(round(frame_rate/freq)):
        result = amplitude * sin(2*pi*freq*i/frame_rate)
        data.append((result, result))
    return data


def save_list(samples_list, note):
    f = open(note + ".txt", 'w')
    f.write(repr(samples_list))
    f.close()

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        notes = sys.argv[1:]
        for note in notes:
            data = sinusoid(note)
            save_list(data, note)
    else:
        print(sys.argv[0] + "|Expecting notes (plus their octaves) as argument.")