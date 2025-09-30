import sys
from rich import print
from time import sleep
import time

lines = [      #'lines' is an array
    ('I wanna da-',0.06, 0.3), #1
    ('I waana dance in the light',0.05, 0.6), #2
    ('I wanna ro-',0.07, 0.3), #3
    ('I wanna rock your body',0.08, 0.8), #4
    ('I wanna go',0.08, 0.3), #5
    ('I wanna go for a ride',0.068, 0.8), #6
    ('Hop in the music and',0.07, 0.35), #7
    ('Rock your body',0.08, 0.6), #8
    ('Rock your body',0.069, 0.6), #9
    ('Come on, come on',0.069, 0.5), #10
    ('Rock that body',0.05, 0.5), #11
    ('(Rock your body)',0.03, 0.5), #12
    ('Rock that body',0.049, 0.4), #13
    ('Come on, come on',0.035, 0.4), #14
    ('Rock that body',0.08, 0.5) #15
]

def PrintLyrics():                                 #delays the display of chars
    for text, char_delay, line_delay in lines:
        for char in text:
            print(char, end='',flush=True)
            if char in [' ',"-",',','(',')']:
                time.sleep(char_delay + 0.02)
            else:
                time.sleep(char_delay)
        print()
        time.sleep(line_delay)

if __name__ == "__main__":
    PrintLyrics()
