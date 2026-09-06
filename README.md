This project contains the performance test for 2 different algorithms<br>
         
    - insertion sort<br>
    - merge sort
------------------------

1. Insertion Sort


    Insertion Sort builds a new list by inserting each element into its correct position.
    - Start with an empty result list
    - For each element in the input list:
        Scan the result list until the correct position is found
        Insert the element
    - Continue until all elements are inserted

Unit test

    Unit tests verify that insertion_sort correctly sorts:
        - An empty list
        - A single‑element list
        - A reverse‑sorted list

Performance test

    Performance tests use pytest‑benchmark to measure runtime for increasing list sizes.

        - The list sizes used: 100, 200, 300, 400, 500, 1000

-----------------------

2. Algorithm Merge sort


    Merge Sort works in two phases:

        Divide: Recursively split the list into halves until each part contains one element
        Conquer: Merge the sorted halves back together

    This approach ensures stable and predictable performance.  

Time Complexity

    Worst‑case: O(n log n)
    Average: O(n log n)
    Best‑case: O(n log n)
    Space complexity: O(n)

    Merge Sort is significantly faster than insertion sort for large lists.

Unit test

    Unit tests verify that insertion_sort correctly sorts:
        - An empty list
        - A single‑element list
        - A reverse‑sorted list

Performance test

    Performance tests use pytest‑benchmark to measure runtime for increasing list sizes.

        - The list sizes used: 100, 200, 300, 400, 500, 1000, 1500, 2000,2500