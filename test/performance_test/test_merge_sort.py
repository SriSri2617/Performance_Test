import pytest
from src.merge_sort import merge_sort
from src.list_generation import generate_list

@pytest.mark.performance
@pytest.mark.parametrize("size", [
    100, 200, 300, 400, 500, 1000, 1500, 2000, 2500])
def test_merge_sort_scaling(benchmark, size):
    """
    Performance test for merge_sort using the same list sizes
    as insertion sort, so the runtimes can be compared.
    """
    data = generate_list(size)
    benchmark(merge_sort, data)
