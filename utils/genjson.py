"""
`utils.genjson` lets you generate JSONs or GeoJSONs for testing purposes.
"""

import json
import random
import uuid
import os

from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, DoubleType

def _create_coords(n: int) -> list[float]:
    arr = []

    for _ in range(n):
        arr.append(random.uniform(-99.0, -99.5))
        arr.append(random.uniform(19.3, 19.5))

    return arr

def basic_mlstr(
        num_points: int
    ) -> dict:
    """
    Generate basic MultiLineString GeoJSON.

    :param num_coordinates: [TODO:description]
    :param type [TODO:type]: [TODO:description]
    :return: [TODO:description]
    """
    c1 = _create_coords(num_points)
    c2 = _create_coords(num_points)

    gjson_str = f'"type": "MultiLineString", "coordinates": [{str(c1)}, {str(c2)}]'
    gjson_str = '{' + gjson_str + '}'

    return json.loads(gjson_str)

def file(
        n: int,
        dir: str = "/tmp"
    ) -> str:
    """
    Generate file with given number of pair points.

    :param n: The number of pair of coordinates to be generated.
    :param dir: The directory where the file will be stored.
        Defaults to '/tmp'.
    :return: The file path where it was generated.
    """
    # Setting GeoJSON info
    gjson_str = '"type": "FeatureCollection","features":'
    features = '"type":"Feature","properties":'
    f_props = '"name":"7","tiempo":"2020-01-01 00:00:00 a 2020-01-01 23:59:59"'
    f_geom = '"type":"LineString","coordinates":'
    coords = ""

    # Generating coordinates
    for i in range(n):
        coords += f'{str(_create_coords(1))}'

        if i < n - 1:
            coords += ','

    # Building string JSON with generated data
    coords = '[' + coords + ']'
    f_geom = '{' + f_geom + coords + '}'
    f_props = '{' + f_props + '}, "geometry":' + f_geom
    features = '[{' + features + f_props + '}]'
    gjson_str = '{' + gjson_str + features + '}'

    # Saving file
    file_name = f"{uuid.uuid4()}_{str(n)}.json"
    file_path = os.path.join(dir, file_name)

    with open(file_path, "w") as file:
        file.write(gjson_str)

    return file_path

def dataframe(
        n: int,
        spark: SparkSession
    ) -> DataFrame:
    """
    Generate 2 GeoJSON trajectories as DataFrame.

    :param n: The number of point pairs that will be created. A trajectory
    consists of pair of points, if `n` is set to `3`, this trajectory will
    have 3 points (x, y), i.e.: 6 elements in total.
    :param spark: A spark session already intialized.
    :return: The GeoJSON generated as a DataFrame.
    """
    coords_type = ArrayType(ArrayType(ArrayType(DoubleType(), True), True), True)
    schema = StructType([
        StructField('coordinates', coords_type, True),
        StructField('type', StringType(), True)
    ])

    trajectories = [_create_coords(n), _create_coords(n)]
    data = [[trajectories], "MultiLineString"]

    return spark.createDataFrame([data], schema=schema)
