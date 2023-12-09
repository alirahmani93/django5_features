import random
import time

from django.shortcuts import render


# Create your views here.

def check_if(repeat: int = 1000):
    t0 = time.time()
    for i in range(repeat):
        a = random.choices(['x', 'y', 'z'])
        z = 0
        if a == 'x':
            z += 1
        elif a == 'y':
            z += 2
        elif a == 'z':
            z **= z
        else:
            z -= 1
    return time.time() - t0


def check_match(repeat: int = 1000):
    t0 = time.time()
    for i in range(repeat):
        z = 0
        match random.choices(['x', 'y', 'z']):
            case 'x':
                z += 1
            case 'y':
                z += 2
            case 'z':
                z **= z
            case _:
                z -= 1
    return time.time() - t0
