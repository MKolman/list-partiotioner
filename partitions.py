# Only using numpy to calculate standard deviation
import numpy


def make_partiotions(data):
    # Memoization here to make sure the algorithm is fast by saving
    # already calculated data of the form:
    # memo [i] = what is the best partition of `data[i:]` (from i to the end)
    # Set them to False, so we know we did nothing yet
    memo = [False for _ in data]

    # Return the (score, partition) combo of `data[i:]` with the minimum score,
    # where score is the sum of standard deviations.
    # e.g. such [[x11, x12, x13, ...], [x21, x22, x23, ...], ...] that
    # together they yield `data` but have a minimum
    # sum(i) STD(xi1, xi1, xi3, ...)
    def scoring(i):
        # If we reached the end of the list make sure to end the recursion
        if i >= len(data) - 1:
            return 0, []

        # Check if we already calculated this and if so return it
        if memo[i]:
            return memo[i]
        # Start by assuming every element is in the same partition
        best_score = numpy.std(data[i:])
        best_partition = [i, len(data)]
        # Iterate through all possible sizes of the next partition `data[i:j]`
        for j in range(i+2, len(data)-1):
            # Get the best partition of what's left
            score, part = scoring(j)
            score += numpy.std(data[i:j])
            # Check if this is the new best partition
            if score < best_score:
                best_score = score
                best_partition = [i] + part

        # Save the calculated result and return it
        memo[i] = [best_score, best_partition]
        return memo[i]

    # Calculate the partition and ignore the score
    part = scoring(0)[1]
    # The function scoring only returns indexes of edges, now lets
    # change them into actual tables
    partitioned_data = [data[part[i]:part[i+1]] for i in range(len(part)-1)]
    return partitioned_data

# Set the data
data = [1, 1, 1, 5, 6, 111, 122, 999, 1002]
print(make_partiotions(data))
