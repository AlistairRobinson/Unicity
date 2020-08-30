from itertools import combinations
from math import factorial as fact
import sys
import pandas as pd
import progressbar as pb

success, trials = 0, 0

def unicity(data: pd.DataFrame, id: str, p: int, v: bool):
    """ Returns the unicity of `data` given `p` and an `id` column

    Args:
        data (pd.DataFrame): The data frame to calculate unicity for
        id (str):            The name of the `id` column in `data`
        p (int):             The `p` value to calculate unicity with
        v (bool):            Whether to operate in verbose mode

    Returns:
        (int, int): The number of successful trials and total trials performed
    """
    global success, trials
    success, trials = 0, 0
    pbar = pb.ProgressBar(max_value=len(set(data[id])), redirect_stdout=True, term_width=100)

    # Calculate unicity for each user in the dataset
    for user in pbar(set(data[id])):

        # Find the trajectory associated with the user
        trajectory = data[data[id] == user].drop(id, axis=1).to_dict(orient="records")
        # If the trajectory is shorter than `p`, no subtrajectories can be taken so skip
        if len(trajectory) < p:
            continue
        if v:
            print("Computing unicity for user {} ({} data points, {} permutations)".format(
                user, len(trajectory), fact(len(trajectory)) // fact(p) // fact(len(trajectory) - p)))

        # Calculate unicity for every possible subtrajectory of size `p`
        for subtrajectory in combinations(trajectory, p):
            # Find the set of possible users which could constitute a match
            possible_users = set(data[id])
			# Determine whether the subtrajectory is uniquely characterised
            for observation in subtrajectory:

                # Find the data associated with potential matches
                samples = data[data[id].isin(possible_users)]

                # Find the records which match with this data point in the subtrajectory
                matches = samples[(samples.drop(id, axis=1) == observation).all(axis=1)]

                # Remove users from the possible matches set if they didn't match
                possible_users = possible_users.intersection(set(matches[id]))

                # If only one user remains, skip the rest of the subtrajectory
                if len(possible_users) == 1:
                    break

            # Report a success if the subtrajectory was uniquely characterised
            success += 1 if len(possible_users) == 1 else 0
            trials += 1
            if trials >= 100000 and p >= 5:
                return (success, trials)

    # Return the number of successes and trials (where success/trials is unicity)
    return (success, trials)

def signal_handler(s, frame):
    print("\nFinal unicity score: {}, {} trials".format(success / trials, trials), file=sys.stderr)
    sys.exit(0)