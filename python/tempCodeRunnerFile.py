import sys
from rich import print
from time import sleep
import time

lines = [
    ('I wanna da-',0.06),#1
    ('I waana dance in the light',0.05),#2
    ('I wanna ro-',0.07),#3
    ('I wanna rock your body',0.08),#4
    ('I wanna go',0.08),#5
    ('I wanna go for a ride',0.068),#6
    ('Hop in the music and',0.07),#7
    ('Rock your body',0.08),#8
    ('Rock your body',0.069),#9
    ('Come on, come on',0.069),#10
    ('Rock that body',0.05),#11
    ('(Rock your body)',0.03),#12
    ('Rock that body',0.049),#13
    ('Come on, come on',0.035),#14
    ('Rock that body',0.08),#15
    ]

def PrintLyrics():
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
    