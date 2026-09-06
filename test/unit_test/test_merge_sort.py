import pytest
from src.merge_sort import merge_sort

def test_empty_list():
    assert merge_sort([]) == []

def test_single_element():
    assert merge_sort([20]) == [20]

def test_reverse_sorted_list():
    assert merge_sort([10, 9, 8, 7, 6]) == [6, 7, 8, 9, 10]
