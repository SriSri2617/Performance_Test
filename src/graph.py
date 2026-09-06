import matplotlib.pyplot as plt

# Benchmark results collected from pytest-benchmark output.
# The benchmark prints times in microseconds (us), so we convert
# them to milliseconds (ms) for easier reading in the graph.


# List sizes used in the performance tests
sizes = [100, 200, 300, 400, 500, 1000]

# Mean runtimes from your benchmark output (converted to ms)
# 146.94 us  → 0.146 ms
times_ms = [0.146, 0.557, 1.176, 3.600, 4.446, 15.343]


# Plotting the graph, X-axis: n (list size), Y-axis: t (runtime in ms)

plt.figure(figsize=(8, 5))  # Set graph size
plt.plot(sizes, times_ms, marker='o', linewidth=2)  # Line graph with dots

# Label the axes
plt.xlabel("n (list size)")
plt.ylabel("t (runtime in ms)")

# Title of the graph
plt.title("Insertion Sort Benchmark (pytest-benchmark)")

# Add grid for readability
plt.grid(True)

# Display the graph window
plt.show()
