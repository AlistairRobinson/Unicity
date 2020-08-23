import signal, sys
import pandas as pd
from unicity.parser import construct_parser
from unicity.clean import clean_data
from unicity.stats import unicity, signal_handler

def main():

    args = construct_parser().parse_args()

    try:
        data = pd.read_csv(args.f, parse_dates=["start time", "end time"], dayfirst=True)
        data = clean_data(data, args.r)
        data.to_csv("data/{}.csv".format(args.r), index=False)
    except ValueError:
        data = pd.read_csv(args.f, parse_dates=["time"], dayfirst=True)

    data = data[(data["time"] >= args.s) & (data["time"] < args.e)]
    if args.v:
        print(data)

    signal.signal(signal.SIGINT, signal_handler)

    s, t = unicity(data, args.u, args.p, args.v)
    print("\nFinal unicity score: {}, {} trials".format(s / t, t), file=sys.stderr)

main()