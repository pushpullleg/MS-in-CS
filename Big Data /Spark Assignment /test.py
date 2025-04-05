from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

sc = spark.sparkContext # Accessing the SparkContext from the Sparksession
# without spark context we wont be able to use sparks'distributed computing capabliites.

rdd = sc.parallelize([1,2,3,4,5,6,7,8,9,10]) # it  not initialising the Driver 
# it is creating an RDD

print ("first is {}".format(rdd.first()))

even_rdd = rdd.filter(lambda x: x % 2 == 0) ## transformation 

out = even_rdd.collect() ## action

print (out )