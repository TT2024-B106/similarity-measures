"""
`utils.plotfn` plots functions to know their complexity. Currently, it plots
time complexities mainly that can be helpful to compare different distance
calculations functions.
"""

import timeit
import matplotlib.pyplot as plt
import pyspark.sql.functions as F

from matplotlib.axes import Axes
from pyspark.sql.session import SparkSession
from pyspark.sql.dataframe import DataFrame
from typing import Callable, Any

def time_complexity3(
        function: Callable,
        populate_fn: Callable,
        plot_title: str,
        max_input_size_step = 1000,
        max_input_size = 1000
    ) -> None:
    """
    Plot the time complexity of a given function with 3 maximum input sizes
    that will be the upper limit of a range of inputs that will start from 2
    and will give 3 subplots.

    This function is designed for plotting the time complexity of a function
    that calculates the distance between 2 trajectories.

    :param function Callable: The function that calculates the distance
    between 2 trajectories.
    :param populate_fn Callable: The function that generates trajectories.
    :param plot_title str: The plot title that will be displayed in the 3
    subplots along with the maximum input size.
    :param max_input_size_step int: The maximum input step that will increase
    each subplot, i.e.: If this is set to `1000`, the second subplot will
    increase `+1000` and the third subplot will increase to `+2000`.
    :param max_input_size int: The maximum input size that
    `max_input_size_step` will take as base.
    """
    sizes = [max_input_size + (max_input_size_step * i) for i in range(3)]

    _, axs = plt.subplots(1, 3, figsize=(15, 5))

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

        ax: Axes = axs[i]
        ax.plot(times)
        ax.set_title(f"{plot_title} (input size: {max_size})")
        ax.set_xlabel("Input size")
        ax.set_ylabel("Time")

    plt.tight_layout()
    plt.show()

def time_complexity3_spark(
        function,
        populate_fn,
        spark: SparkSession,
        plot_title: str,
        max_input_size = 1000,
        max_input_step = 1000,
    ) -> None:
    sizes = [max_input_size + (max_input_step * i) for i in range(3)]

    _, axs = plt.subplots(1, 3, figsize=(15, 5))

    for i, max_size in enumerate(sizes):
        times = []

        for size in range(1, max_size + 1):
            gdf: DataFrame = populate_fn(size, spark)

            start = timeit.default_timer()
            gdf = gdf.withColumn('distance', function(F.col('coordinates')))
            end = timeit.default_timer() - start

            times.append(end)

        ax: Axes = axs[i]
        ax.plot(times)
        ax.set_title(f"{plot_title} (input size: {max_size})")
        ax.set_xlabel("Input size")
        ax.set_ylabel("Time")

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

