import pytest
from src.insertion_sort import insertion_sort
from src.list_generation import generate_list

@pytest.mark.performance
def test_insertion_sort(benchmark):
    data = generate_list(2000)
    benchmark(insertion_sort, data)


@pytest.mark.performance
@pytest.mark.parametrize("size", [100, 200, 300, 400, 500, 1000])
def test_insertion_sort_scaling(benchmark, size):
    data = generate_list(size)
    benchmark(insertion_sort, data)


@pytest.mark.performance
@pytest.mark.parametrize("size", [100, 200, 300, 400, 500, 1000, 2000, 3000])
def test_insertion_sort_scaling(benchmark, size):
    data = generate_list(size)
    benchmark(insertion_sort, data)