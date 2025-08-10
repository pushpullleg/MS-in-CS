from pyspark.sql import SparkSession

# Initialize Spark Session
spark = SparkSession.builder.appName("SimplePySpark").getOrCreate()
sc = spark.sparkContext


wordsList = ['cat', 'elephant', 'rat', 'rat', 'cat']
wordsRDD = sc.parallelize(wordsList, 4)
# Print out the type of wordsRDD
print(type(wordsRDD))
#<class 'pyspark.rdd.RDD'>

# TODO: Replace <FILL IN> with appropriate code
def makePlural(word):
# """Adds an 's' to `word`.
# Note:
# This is a simple function that only adds an 's'. No attempt is made to follow proper
# pluralization rules.
# Args:
# word (str): A string.
# Returns:
# str: A string with 's' added to it.
# """

 return word+'s'
print( makePlural('cat'))

# TODO: Replace <FILL IN> with appropriate code
pluralRDD = wordsRDD.map(makePlural)
print( pluralRDD.collect() )
#['cats', 'elephants', 'rats', 'rats', 'cats']

pluralLambdaRDD = wordsRDD.map(lambda x:x+'s')
print(pluralLambdaRDD.collect())
#'cats', 'elephants', 'rats', 'rats', 'cats']

# TODO: Replace <FILL IN> with appropriate code

pluralLengths = pluralRDD.map(lambda x:len(x))
length=pluralLengths.collect()

print (length)

#[4, 9, 4, 4, 4]

wordPairs = wordsRDD.map(lambda x:(x,1))
print ('debug start')
print (wordPairs.collect())

#[('cat', 1), ('elephant', 1), ('rat', 1), ('rat', 1), ('cat', 1)]

wordsGrouped = wordPairs.groupByKey()
for key, value in wordsGrouped.collect():
    print('{0}: {1}'.format(key, list(value)))
# rat: [1, 1]
# elephant: [1]
# cat: [1, 1]
print (sorted(wordsGrouped.mapValues(lambda x: list(x)).collect()))
#[('cat', [1, 1]), ('elephant', [1]), ('rat', [1, 1])]


def foo(bar):
   print (bar)
   print (len (bar))
   return 'k'
   

wordCountsGrouped = wordsGrouped.map(lambda x : (x[0], sum( x[1])))
print (wordCountsGrouped.collect())
#[('rat', 2), ('elephant', 1), ('cat', 2)]

wordCounts = wordPairs.reduceByKey(lambda x,y:x+y)
#print (wordCounts.collect())
#[('rat', 2), ('elephant', 1), ('cat', 2)]

wordCountsCollected = (wordsRDD.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).collect())
print (wordCountsCollected)
#[('rat', 2), ('elephant', 1), ('cat', 2)]
print(sorted(wordCountsCollected))
#[('cat', 2), ('elephant', 1), ('rat', 2)]


uniqueWords = wordsRDD.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y).count()
print (uniqueWords)


from operator import add
totalCount = (wordCounts.map(lambda x:x[1]).reduce(add))
average = totalCount/float(uniqueWords)
print (totalCount)
#5
print (round(average, 2))
#1.67

def wordCount(wordListRDD):
# """Creates a pair RDD with word counts from an RDD of words.
# Args:
# wordListRDD (RDD of str): An RDD consisting of words.
# Returns:
# RDD of (str, int): An RDD consisting of (word, count) tuples.
# """
    return (wordListRDD.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y))



print (wordCount(wordsRDD).collect())

#[(‘rat', 2), ('elephant', 1), ('cat', 2)]

# TODO: Replace <FILL IN> with appropriate code

import re
def removePunctuation(text):
# """Removes punctuation, changes to lower case, and strips leading and trailing spaces.
# Note:
# Only spaces, letters, and numbers should be retained. Other characters should be
# eliminated (e.g. it's becomes its). Leading and trailing spaces should be removed after
# punctuation is removed.
# Args:
# text (str): A string.
# Returns:
# str: The cleaned up string.
# """

    step1 = re.sub(r'[^\w\s]','',text)
    step2 = re.sub(r'_','',step1)
    lowercase=step2.lower()
    strip=lowercase.strip()
    return strip 

print (removePunctuation('Hi, you!'))
#hi you
print (removePunctuation(' No under_score!'))
#no underscore
print (removePunctuation(' * Remove punctuation then spaces * '))
                         
#remove punctuation then spaces

fileName = "shakespeare.txt"
shakespeareRDD = (sc
.textFile(fileName, 8)
.map(removePunctuation))
print ('\n'.join(shakespeareRDD
.zipWithIndex() # to (line, lineNum)
.map(lambda x: '{0}: {1}'.format(x[1], x[0])) # to 'lineNum: line'
.take(15)))

# TODO: Replace <FILL IN> with appropriate code
shakespeareWordsRDD = shakespeareRDD.flatMap(lambda x:x.split(" ") )
shakespeareWordCount = shakespeareWordsRDD.count()
print (shakespeareWordsRDD.top(5))
#[u'zwaggerd', u'zounds', u'zounds', u'zounds', u'zounds']
print (shakespeareWordCount)
#946354

# TODO: Replace <FILL IN> with appropriate code
shakeWordsRDD = shakespeareWordsRDD.filter(lambda x:x.strip()!="")
shakeWordCount = shakeWordsRDD.count()
print (shakeWordCount)
#901109

# TODO: Replace <FILL IN> with appropriate code

top15WordsAndCounts = wordCount(shakeWordsRDD).takeOrdered(15,lambda x:-x[1])

print ('\n'.join(map(lambda w: '{0}: {1}'.format(w[0],w[1]), top15WordsAndCounts)))

# the: 27645
# and: 26733
# i: 20683
# to: 19198
# of: 18180
# a: 14613
# you: 13650
# my: 12480
# that: 11122
# in: 10967
# is: 9598
# not: 8725
# for: 8245
# with: 7996
# me: 7768