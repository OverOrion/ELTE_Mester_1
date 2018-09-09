# -*- coding: utf-8 -*-

def main():
    from sys import stdin, stdout

    standardinput = list(map(int, stdin.readline().split()))
    hourslist = ['one',
                 'two',
                 'three',
                 'four',
                 'five',
                 'six',
                 'seven',
                 'eight',
                 'nine',
                 'ten',
                 'eleven',
                 'twelve']
    hours = int(standardinput[0])
    minutes = int(standardinput[1])

    if minutes in range(15, 46):
        if minutes == 15:
            stdout.write('a quarter past ')
        elif minutes == 30:
            stdout.write('half past ')
        elif minutes == 45:
            stdout.write('a quarter to ')
            hours = hours + 1
    if hours in range(1, 13, 1):
        stdout.write(hourslist[hours - 1])
        if minutes != 0:
            stdout.write(' a.m.')
        elif minutes == 0:
            stdout.write(" o'clock a.m.")
    elif hours in range(12, 25, 1):
        stdout.write(hourslist[(hours - 13)])
        if minutes != 0:
            stdout.write(' p.m.')
        elif minutes == 0:
            stdout.write(" o'clock p.m.")


main()

