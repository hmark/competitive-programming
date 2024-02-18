import sys
import math
from collections import deque


def task(n, c, a):
    # print(n, c, a)

    deck = {
        'C': [],
        'D': [],
        'H': [],
        'S': [],
    }

    for aa in a:
        deck[aa[1]].append(int(aa[0]))

    odds = 0

    if c != 'C' and len(deck['C']) % 2 == 1:
        odds += 1
    if c != 'D' and len(deck['D']) % 2 == 1:
        odds += 1
    if c != 'H' and len(deck['H']) % 2 == 1:
        odds += 1
    if c != 'S' and len(deck['S']) % 2 == 1:
        odds += 1

    if len(deck[c]) < odds:
        print('IMPOSSIBLE')
        return

    deck['C'].sort()
    deck['D'].sort()
    deck['H'].sort()
    deck['S'].sort()

    pairs = []
    odds = []

    if c != 'C':
        if len(deck['C']) % 2 == 1:
            odds.append(str(deck['C'][-1]) + 'C')
            deck['C'] = deck['C'][:-1]
        while len(deck['C']) >= 2:
            pairs.append([str(deck['C'][0]) + 'C', str(deck['C'][1]) + 'C'])
            deck['C'] = deck['C'][2:]

    if c != 'D':
        if len(deck['D']) % 2 == 1:
            odds.append(str(deck['D'][-1]) + 'D')
            deck['D'] = deck['D'][:-1]
        while len(deck['D']) >= 2:
            pairs.append([str(deck['D'][0]) + 'D', str(deck['D'][1]) + 'D'])
            deck['D'] = deck['D'][2:]

    if c != 'H':
        if len(deck['H']) % 2 == 1:
            odds.append(str(deck['H'][-1]) + 'H')
            deck['H'] = deck['H'][:-1]
        while len(deck['H']) >= 2:
            pairs.append([str(deck['H'][0]) + 'H', str(deck['H'][1]) + 'H'])
            deck['H'] = deck['H'][2:]

    if c != 'S':
        if len(deck['S']) % 2 == 1:
            odds.append(str(deck['S'][-1]) + 'S')
            deck['S'] = deck['S'][:-1]
        while len(deck['S']) >= 2:
            pairs.append([str(deck['S'][0]) + 'S', str(deck['S'][1]) + 'S'])
            deck['S'] = deck['S'][2:]

    for odd in odds:
        trumpcard = deck[c][0]
        pairs.append([odd, str(trumpcard) + c])
        deck[c] = deck[c][1:]

    while len(deck[c]) >= 2:
        pairs.append([str(deck[c][0]) + c, str(deck[c][1]) + c])
        deck[c] = deck[c][2:]

    for pair in pairs:
        print(pair[0], pair[1])


t = int(input())
for _ in range(t):
    n = int(input())
    c = input()
    a = list(input().split())
    task(n, c, a)
