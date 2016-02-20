# Only using numpy to calculate standard deviation
import numpy


def make_partitions(data, min_size=2, max_size=-1, multiplier=0):
    """Partitions data into multiple bins.
    Args:
        data (list<float/int>): data to be partitioned
        min_size (int): Minimum number of elements in a single partition; must
            be at least 2
        max_size (int): Maximum number of elements in a single partition; must
            be at least min_size or -1 for unlimited
        multiplier (float): a number that helps determine how many partitions we
            end up with. If less than 0 it means more partitions, if more than
            0 it means we want less partitions
    Returns:
        list<list<float/int>>: partitioned data
    """
    # Set max_size to maximum if left to -1
    if max_size < 0:
        max_size = len(data)
    # Assertions to check input parameters
    assert 2 <= min_size <= len(data), \
        "min_size must be at least 2 but not bigger than all of data"
    assert min_size <= max_size, "max_size must be at least min_size"
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
        if i == len(data):
            return 0, [i]
        # Check if we already calculated this and if so return it
        if memo[i]:
            return memo[i]
        # Start with infinite score and empty partition
        best_score = float("inf")
        best_partition = []
        # Iterate through all possible sizes of the next partition `data[i:j]`
        # for j in range(i+min_size, min(len(data)+1, i+max_size+1)):
        for j in range(min(len(data), i+max_size), i+min_size-1, -1):
            # Get the best partition of what's left
            score, part = scoring(j)
            score += numpy.std(data[i:j])
            score += multiplier * len(part)
            # Check if this is the new best partition
            if score < best_score:
                best_score = score
                best_partition = [i] + part

        # Save the calculated result and return it
        memo[i] = [best_score, best_partition]
        return memo[i]

    # Calculate the partition and check the score
    score, part = scoring(0)
    assert score != float("inf"), "I could't make the partitions. :("

    # ~~ Uncomment this line if you only want indeces of edges ~~
    # return part
    # The function scoring only returns indexes of edges, now lets
    # change them into actual tables
    partitioned_data = [data[part[i]:part[i+1]] for i in range(len(part)-1)]
    partitioned_data = [data[i:j] for i, j in zip(part, part[1:])]
    return partitioned_data

if __name__ == "__main__":
    # Set the data
    data = [1, 1, 1, 5, 6, 111, 122, 999, 1002]
    print("default ".ljust(30, "-"), make_partitions(data))
    print("default with mult. 1.5 ".ljust(30, "-"),
          make_partitions(data, multiplier=1.5))
    print("default with mult. 100 ".ljust(30, "-"),
          make_partitions(data, multiplier=100))
    print("default with mult. 1000 ".ljust(30, "-"),
          make_partitions(data, multiplier=1000))
    print("max_size=3 with mult. 1000 ".ljust(30, "-"),
          make_partitions(data, max_size=3, multiplier=1000))
    print("====================")
    data = [1, 1, 1, 5, 6, 1110, 1220, 999, 1002]
    print("default ".ljust(30, "-"), make_partitions(data))
    print("min_size=3 ".ljust(30, "-"), make_partitions(data, 3))
