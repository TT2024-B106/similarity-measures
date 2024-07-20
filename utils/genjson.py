"""
`utils.genjson` lets you generate JSONs or GeoJSONs for testing purposes.
"""

import json
import random

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, FloatType, DoubleType

def test():
    print("Testing genjson...")

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

def dataframe(n: int):
    spark = SparkSession.builder.appName("GeoJSONDataFrame").getOrCreate()
    coords_type = ArrayType(ArrayType(ArrayType(DoubleType(), True), True), True)
    schema = StructType([
        StructField('coordinates', coords_type, True),
        StructField('type', StringType(), True)
    ])

    trajectories = [_create_coords(n), _create_coords(n)]
    data = [[trajectories], "MultiLineString"]

    return spark.createDataFrame([data], schema=schema)
