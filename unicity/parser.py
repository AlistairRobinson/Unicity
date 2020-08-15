import argparse

def construct_parser() -> argparse.PARSER:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", help="operate experiment in verbose mode", action='store_true')
    parser.add_argument("-p", help="the number of data points exposed to calculate unicity")
    parser.add_argument("-f", help="the .csv file to read data from")
    parser.add_argument("-u", help="the user id column of the data")
    parser.add_argument("-d", help="the date to start observations from")
    parser.add_argument("-e", help="the date to end observations from")
    return parser