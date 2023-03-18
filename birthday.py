#!/usr/bin/env python3

# File: birthdays.py

"""
Odds of at least two people in a group of n people
sharing a birthday.
We'll assume 365 days in a year.
The probablility of 2 people sharing a b'day is
1 - the probablity that 2 people do not share a b'day.
"""

# If only one in the group: 365/365 (= 1) is the probability of a
# shared b'day.
# if two people: the probablity of the second person NOT sharing a
# b'day with the first would be 365/365 * 364/365
# since the second person would have to have one of the remaining
# 364 days.

# So we get the series:
# (365 - n)/365 * (365-(n+1))/365 * ... (365-(N-1))/365
# Where the value of n ranges from 0 to N-1, the number of people
# available to share a b'day with the first person in the room.

# Having calculated the probability of people _not_ sharing a
# b'day, we subtract that probablity from 1, to get the
# probability that two people do share a birthday.

# Probability in a group of n people
# that 2 or more have the same birthday
# expressed "pythonically" is as follows:

import sys


def get_prob(n_people):
    ret = 1
    for n in range(n_people):
        ret *= (365-n)/365
    return 1 - ret

while True:
    as_str = input(
        "How many (1..365) ('Q' to quit) in the room? ")
    if ((not as_str) 
    or (as_str and as_str[0] in 'qQ')):
        break
    n_people = int(as_str)
    print(f'{get_prob(n_people):.3}')

