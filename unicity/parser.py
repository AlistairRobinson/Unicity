import argparse

def construct_parser() -> argparse.PARSER:
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", help="operate experiment in verbose mode",
        default=False, action='store_true')
    parser.add_argument("-p", help="the number of data points exposed to calculate unicity",
        default=1, type=int)
    parser.add_argument("-f", help="the .csv file to read data from",
        default="data/telecom_data.csv")
    parser.add_argument("-u", help="the user id column of the data",
        default="user id")
    parser.add_argument("-s", help="the date to start observations from",
        default="2014-06-01")
    parser.add_argument("-e", help="the date to end observations from",
        default="2014-06-02")
    parser.add_argument("-r", help="the temporal resolution to use (default '60min')",
        default="60min")
    return parser