from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("SimplePySpark").getOrCreate()
sc = spark.sparkContext

# Sample data
sales_data = [
    ("Laptop", 1000),
    ("Mobile", 500),
    ("Tablet", 300),
    ("Shoes", 120),
    ("Shirt", 50)
]

# Create RDD
rdd = sc.parallelize(sales_data)

# Transform: Filter items with sales > 100
filtered_rdd = rdd.filter(lambda x: x[1] > 100)

# Action: Collect and print the result
result = filtered_rdd.collect()
print("Filtered Items (Sales > 100):", result)

# Stop Spark Session
spark.stop()
