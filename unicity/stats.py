from itertools import combinations
from math import factorial as fact
import sys
import pandas as pd
import progressbar as pb

success, trials = 0, 0

def unicity(data: pd.DataFrame, id: str, p: int, v: bool):
    global success, trials
    success, trials = 0, 0
    pbar = pb.ProgressBar(max_value=len(set(data[id])), redirect_stdout=True, term_width=100)
    for user in pbar(set(data[id])):
        trajectory = data[data[id] == user].drop(id, axis=1).to_dict(orient="records")
        if len(trajectory) < p:
            continue
        if v:
            print("Computing unicity for user {} ({} data points, {} permutations)".format(
                user, len(trajectory), fact(len(trajectory)) // fact(p) // fact(len(trajectory) - p)))
        for subset_trajectory in combinations(trajectory, p):
            possible_users = set(data[id])
            for observation in subset_trajectory:
                samples = data[data[id].isin(possible_users)]
                matches = samples[(samples.drop(id, axis=1) == observation).all(axis=1)]
                possible_users = possible_users.intersection(set(matches[id]))
                if len(possible_users) == 1:
                    break
            success += 1 if len(possible_users) == 1 else 0
            trials += 1
            if trials >= 100000 and p >= 5:
                return (success, trials)
    return (success, trials)

def signal_handler(s, frame):
    print("\nFinal unicity score: {}, {} trials".format(success / trials, trials), file=sys.stderr)
    sys.exit(0)