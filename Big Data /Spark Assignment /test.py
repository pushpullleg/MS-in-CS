from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

sc = spark.sparkContext

rdd = sc.parallelize([1,2,3,4,5,6,7,8,9,10]) # initialising the Driver 

print ("first is {}".format(rdd.first()))

even_rdd = rdd.filter(lambda x: x % 2 == 0) ## transformation 

out = even_rdd.collect() ## action

print (out )