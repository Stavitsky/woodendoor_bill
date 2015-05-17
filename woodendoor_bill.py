#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import parser_arg


def full_coming_time(hours, minutes):
    coming_time = datetime.time(hours, minutes)
    return coming_time


def count_time(coming_time):
    leaving_time = datetime.datetime.now().time()
    spent_hours = leaving_time.hour - coming_time.hour
    spent_minutes = leaving_time.minute - coming_time.minute
    if spent_hours < 0:
        spent_hours += 24
    if spent_minutes < 0:
        spent_minutes += 60
        spent_hours -= 1
    spent_time = {
        'hours': spent_hours,
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
    print("You had spent at WoodenDoor:\n\t{0} hour(s),"
          "\n\t{1} minute(s).\n\nYou owe {2} rubles.").format(
        spent_time['hours'], spent_time['minutes'], cost)


def main():
    COMING_TIME = full_coming_time(
        parser_arg.COMING_TIME_HOUR,
        parser_arg.COMING_TIME_MIN)
    spent_time = count_time(COMING_TIME)
    cost = count_cost(spent_time)
    print_report(spent_time, cost)

if __name__ == "__main__":
    main()
