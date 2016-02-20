# List Partiotioner
A small function that takes a list and returns its partition such, that the sum of standard deviations of all parts is minimal.

## Parameters
1. __data__ (_list&lt;float/int&gt;_): data to be partitioned
1. __min_size__ (_int_): Minimum number of elements in a single partition; must
    be at least 2.
1. __max_size__ (_int_): Maximum number of elements in a single partition; must
    be at least min_size or -1 for unlimited.
1. __multiplier__ (_float_): a number that helps determine how many partitions we
    end up with. If less than 0 it means more partitions, if more than
    0 it means we want less (bigger) partitions.

## Example usage:
```python
>> from partitions import make_partiotions
>> data = [1, 1, 1, 5, 6, 111, 122, 999, 1002]
>> make_partiotions(data)
[[1, 1, 1], [5, 6], [111, 122], [999, 1002]]
>> make_partiotions(data, multiplier=1.5)
[[1, 1, 1, 5, 6], [111, 122], [999, 1002]]
>> make_partiotions(data, multiplier=100)
[[1, 1, 1, 5, 6, 111, 122], [999, 1002]]
>> make_partiotions(data, multiplier=1000)
[[1, 1, 1, 5, 6, 111, 122, 999, 1002]]
>> make_partiotions(data, max_size=3, multiplier=1000)
[[1, 1, 1], [5, 6, 111], [122, 999, 1002]]
>> data = [1, 1, 1, 5, 6, 1110, 1220, 999, 1002]
>> make_partiotions(data)
[[1, 1, 1], [5, 6], [1110, 1220], [999, 1002]]
>> make_partiotions(data, 3)
[[1, 1, 1, 5, 6], [1110, 1220, 999, 1002]]
```
