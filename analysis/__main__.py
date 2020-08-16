import pandas as pd
from matplotlib import pyplot as plt

def main():
    data = pd.read_csv("results/2014-06-01.csv")
    print(data)
    plt.figure()
    a = plt.axes()
    a.set_xlabel("Data points revealed")
    a.set_ylabel("Unicity")
    a.set_title("Unicity against p")
    for res in set(data["resolution"]):
        d = data[data["resolution"] == res]
        plt.plot(d["p"], d["unicity"])
    plt.show()

main()