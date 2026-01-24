#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Additional functions
"""

def seat_indices_indicator(seats):
    O = ()
    X = ()
    A = ()
    H = ()
    D = ()
    excepts = False
    for i in range(len(seats)):
        match seats[i]:
            case "O":
                O += (i,)
            case "X":
                X += (i,)
            case "|":
                A += (i,)
            case "H":
                H += (i,)
            case "D":
                D += (i,)
            case _:
                excepts = True
    return (O, X, A, H, D, excepts)

def seat_indices_indicator_with_heroes(seats):
    O = ()
    X = ()
    A = ()
    H = ()
    D = ()
    excepts = False
    for i in range(len(seats)):
        match seats[i]:
            case "O":
                O += (i,)
            case "X":
                X += (i,)
            case "|":
                A += (i,)
            case "H":
                H += (i,)
            case "D":
                D += (i,)
            case "T":
                ""
            case "S":
                ""
            case "N":
                ""
            case "B":
                ""
            case "A":
                ""
            case "C":
                ""
            case "L":
                ""
            case _:
                excepts = True
    return (O, X, A, H, D, excepts)

def split_func(s, by="|"):
    sep_t = ()
    while by in s:
        sep_t += (s[:s.find(by)],)
        s = s[s.find(by)+1:]
    sep_t += (s,)
    return sep_t
        

def indicate_class(seats):
    row_sep = split_func(seats)
    flight_class = None
    if len(row_sep) == 3:
        if len(row_sep[0])==1 and len(row_sep[1])==2 and len(row_sep[2])==1:
            flight_class = "First"
        elif len(row_sep[0])==2 and len(row_sep[1])==2 and len(row_sep[2])==2:
            flight_class = "Business"
        elif len(row_sep[0])==3 and len(row_sep[1])==4 and len(row_sep[2])==3:
            flight_class = "Economy"
    return flight_class

def indices_of_pref_seats(fl_class):
    match fl_class:
        case "First":
            return ((0, 5), (), (0, 2, 3, 5))
        case "Business":
            return ((0, 7), (), (1, 3, 4, 6))
        case "Economy":
            return ((0 ,11), (1, 5, 6, 10), (2, 4, 7, 9))
        case _:
            return None
        
def find_intersection(t1, t2):
    intersection = ()
    for x in t1:
        for y in t2:
            if x == y:
                intersection += (x,)
    return intersection


def replace_with_index(s, i, add):
    return s[:i]+add+s[i+1:]