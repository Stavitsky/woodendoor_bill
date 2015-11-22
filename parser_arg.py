import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--coming_times_hour", type=int,
                    required=True,
                    help="there you must write hour when you came to cafe")
parser.add_argument("-m", "--coming_times_min", type=int,
                    required=True,
                    help="there you must write minutes when you came to cafe")
args = parser.parse_args()
COMING_TIME_HOUR = args.coming_times_hour
COMING_TIME_MIN = args.coming_times_min
