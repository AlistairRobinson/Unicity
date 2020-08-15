import pandas as pd
from unicity.parser import construct_parser
from unicity.clean import clean_data
from unicity.stats import unicity

def main():

    args = construct_parser().parse_args()
    args.f = args.f if args.f else "data/clean.csv"
    args.u = args.u if args.u else "user id"
    args.s = args.s if args.s else "2014-06-01"
    args.e = args.e if args.e else "2014-06-02"
    args.p = int(args.p) if args.p else 1

    try:
        data = pd.read_csv(args.f, parse_dates=["start time", "end time"], dayfirst=True)
        data = clean_data(data)
    except ValueError:
        data = pd.read_csv(args.f, parse_dates=["time"], dayfirst=True)

    data = data[(data["time"] >= args.s) & (data["time"] < args.e)]
    print(data)

    s, t = unicity(data, args.u, args.p)
    print("\nFinal unicity score: {}, {} trials".format(s / t, t))

main()