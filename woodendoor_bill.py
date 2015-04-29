#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime

COMING_TIME = datetime.time(12, 15)


def count_time(coming_time):
    leaving_time = datetime.datetime.time(datetime.datetime.now())
    spent_hours = leaving_time.hour - COMING_TIME.hour
    spent_minutes = leaving_time.minute - COMING_TIME.minute
    spent_time = {
        'hours': spent_hours if spent_hours >= 0 else 24+spent_hours,
        'minutes': spent_minutes
    }
    return spent_time


def count_cost(spent_time):
    if spent_time['hours'] >= 2:
        cost = 240 + (spent_time['hours'] - 2) * 60 + spent_time['minutes']
    else:
        cost = spent_time['hours'] * 60 * 2 + spent_time['minutes'] * 2
    return cost


def print_report(spent_time, cost):
    print ("You had spent at WoodenDoor:\n\t{0} hour(s),"
           "\n\t{1} minute(s).\n\nYou owe {2} rubles.").format(
            spent_time['hours'], spent_time['minutes'], cost)


def main():
    spent_time = count_time(COMING_TIME)
    cost = count_cost(spent_time)
    print_report(spent_time, cost)

if __name__ == "__main__":
    main()
