"""
`utils.plotfn` plots functions to know their complexity. Currently, it plots
time complexities mainly that can be helpful to compare different distance
calculations functions.
"""

import timeit
import matplotlib.pyplot as plt

# from collections.abc import Callable
# from typing_extensions import ParamSpec
#
# _P = ParamSpec('_P')
# _R = TypeVar('_R')
# _T = TypeVar('_T')

def time_complexity3(
        # function: Callable[_P, _R],
        function: any,
        # populate_fn: Callable[_P, _R],
        populate_fn: any,
        plot_title: str,
        max_input_size_step: int | None = None,
        max_input_size_2: int | None = None,
        max_input_size_3: int | None = None,
        max_input_size = 1000
    ) -> None:
    """
    Plot the time complexity of a given function with 3 maximum input sizes
    that will be the upper limit of a range of inputs that will start from 2
    and will give 3 subplots.

    This function is designed for plotting the time complexity of a function
    that calculates the distance between 2 trajectories.

    :param function [TODO:type]: [TODO:description]
    :param max_input_size [TODO:type]: [TODO:description]
    :return: [TODO:description]
    """
    if max_input_size_step is None:
        sizes = [max_input_size + (1000 * i) for i in range(3)]
    else:
        sizes = [max_input_size + (max_input_size_step * i) for i in range(3)]

    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    for i, max_size in enumerate(sizes):
        times = []

        for size in range(1, max_size+1):
            t1 = populate_fn(size)
            t2 = populate_fn(size)

            # Where measuring time complexity actaually happens
            start = timeit.default_timer()
            function(t1, t2)
            end = timeit.default_timer() - start

            times.append(end)

        axs[i].plot(times)
        axs[i].set_title(f"{plot_title} (input size: {max_size})")
        axs[i].set_xlabel("Input size")
        axs[i].set_ylabel("Time")

    plt.tight_layout()
    plt.show()

def time_complexity(
        function: Callable,
        *args: Any,
        **kwargs: Any
    ) -> None:
    """
    Plot the time complexity of a given function.

    :param function [Callable]: The function to analyze.
    """
    max_input_size = kwargs.get('max_input_size', 1000)
    min_input_size = kwargs.get('min_input_size', 1)
    xlabel = kwargs.get('xlabel', "Input size")
    ylabel = kwargs.get('ylabel', "Execution time (s)")

    times = []
    min_max_range = range(min_input_size, max_input_size + 1)

    for i in min_max_range:
        time = function(i, *args)
        times.append(time)

    if 'convert_seconds' in kwargs:
        times = [t / kwargs['convert_seconds'] for t in times]

    plt.plot(min_max_range, times)

    if 'title' in kwargs:
        plt.title(kwargs['title'])

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.show()
def plot_time_vs_step_size(file_path, upper_bound, step_size):
    """Plots the time it takes to load n coordinates from a JSON file for increasing values of n.

    Args:
        file_path (str): The path to the JSON file.
        upper_bound (int): The maximum number of coordinates to load.
        step_size (int): The increment between each measurement.
    """

    n_values = range(step_size, upper_bound + 1, step_size)
    times = []

    for n in n_values:
        _, elapsed_time = load_n_coordinates_from_json_file(file_path, n)
        times.append(elapsed_time)

    plt.plot(n_values, times)
    plt.xlabel("Number of Coordinates (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Time Loading " + str(upper_bound) + " Coordinates")
    plt.grid(True)
    plt.show()
    
def test():
    print("Testing")
