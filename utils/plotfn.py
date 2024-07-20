"""
`utils.plotfn` plots functions to know their complexity. Currently, it plots
time complexities mainly that can be helpful to compare different distance
calculations functions.
"""

import timeit
import matplotlib.pyplot as plt

from pyspark.sql.session import SparkSession
from pyspark.sql.dataframe import DataFrame

# from collections.abc import Callable
# from typing_extensions import ParamSpec
#
# _P = ParamSpec('_P')
# _R = TypeVar('_R')
# _T = TypeVar('_T')

def time_complexity3(
        # function: Callable[_P, _R],
        function,
        # populate_fn: Callable[_P, _R],
        populate_fn,
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

        axs[i].plot(times)
        axs[i].set_title(f"{plot_title} (input size: {max_size})")
        axs[i].set_xlabel("Input size")
        axs[i].set_ylabel("Time")

    plt.tight_layout()
    plt.show()

def time_complexity3_spark(
        # function,
        populate_fn,
        spark: SparkSession,
        plot_title: str,
        max_input_size = 1000,
        max_input_step = 1000
    ) -> None:
    sizes = [max_input_size + (max_input_step * i) for i in range(3)]
    _, axs = plt.subplots(1, 3, figsize=(15, 5))

    for i, max_size in enumerate(sizes):
        times = []

        for size in range(1, max_size + 1):
            geojson = populate_fn(size)
            df: DataFrame = spark.createDataFrame(geojson['coordinates'])
            print(df)

            # TODO: Measure time complexity of distance function
            start = timeit.default_timer()
            # TODO:
            end = timeit.default_timer() - start

            times.append(end)

        axs[i].plot(times)
        axs[i].set_title(f"{plot_title} (input size: {max_size})")
        axs[i].set_xlabel("Input size")
        axs[i].set_ylabel("Time")

    plt.tight_layout()
    plt.show()
