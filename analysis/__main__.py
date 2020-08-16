import pandas as pd

def main():
    data = pd.read_csv("results/2014-06-01.csv")
    print(data)

main()