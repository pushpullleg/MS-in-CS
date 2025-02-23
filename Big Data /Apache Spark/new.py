from pyspark.sql import SparkSession

try:
    print("Initializing Spark session...")
    # Initialize a Spark session
    spark = SparkSession.builder.appName("SparkInstallationCheck").getOrCreate()
    print("Spark session initialized successfully.")

    # Create a simple DataFrame
    print("Creating DataFrame...")
    data = [("John", 28), ("Anna", 23), ("Peter", 35)]
    columns = ["Name", "Age"]
    df = spark.createDataFrame(data, columns)
    print("DataFrame created successfully.")

    # Show the DataFrame
    print("Showing DataFrame...")
    df.show()

    # Perform a basic operation
    print("Printing schema...")
    df.printSchema()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Stop the Spark session
    print("Stopping Spark session...")
    spark.stop()
    print("Spark session stopped.")
