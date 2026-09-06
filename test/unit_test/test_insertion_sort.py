import pytest
from src.insertion_sort import insertion_sort

def test_empty_list():
    assert insertion_sort([]) == []

def test_single_element():
    assert insertion_sort([10]) == [10]

def test_reverse_sorted_list():
    assert insertion_sort([10, 8, 6, 4, 2, 0]) == [0, 2, 4, 6, 8, 10]
