from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("demo") \
    .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow") \
    .getOrCreate()
