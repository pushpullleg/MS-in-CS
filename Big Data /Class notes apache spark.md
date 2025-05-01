Lazy evaluation Analogy 

K means - group 

tupple - immutable 
list - mutable 

RDD is like a blueprint , recipe 

transformations and actions 
only transformation is lazy, lazy untill action




Mar 4 

Creating RD

If you use jupyter notebook , then u need to create own spark constant

Procedural programming
C, Pascal

Object-oriented programming
C++, JAVA

Functional programming
LISP

Transformation program 

traditional computing we bring data to memory 

however in big data, we need not move data, operation guy is moving around , data 

14:40 -> 14:44 nice summarising of what we did

commutavity 

associativyt

must accomodate reduce func

make sure rdd is small enough berfore collect function

15:10 -> 15:14

# Pyspark

Broadcast variables 

send read only variables to the workers 
read only look up tables, consider using broadcasting variables

Accumulator

Transformation and action are the function in the apache spark 

map ()

action triggers all the transformation 

action is a way of driver to get the results back.

flatmap is similar to map , it reduces teh hierarchy 


Two way of creating RDD
- from worker node 

Partition adn no.of workers , 

About slides

Group by function be careful, as it gives more load to the worker

# ApacheSpark

it is similar to panda and apache spark dataframe


-----

Confidence bounds


# Statistical Approaches

## Frequentist vs Bayesian

### Frequentist
- Relies on long-run frequency of events
- Parameters are fixed constants
- Uses Maximum Likelihood Estimation (MLE)
- Confidence intervals
- Hypothesis testing with p-values

### Bayesian
- Uses probability as measure of uncertainty
- Parameters have probability distributions
- Combines prior knowledge with data
- Posterior probability distributions
- Credible intervals for inference

# Point Estimation (Kid-Friendly Explanation)
Imagine you have a huge jar of jellybeans, and you want to guess how many jellybeans are in it.

### How Point Estimation Works:
1. Looking at Part of the Jar
   - You can't count all jellybeans (too many!)
   - So you count jellybeans in one small section
   - Use that to make your best guess for whole jar

2. Example:
   - If 10 jellybeans fit in 1 inch of jar
   - And jar is 5 inches tall
   - Point estimate = 10 × 5 = 50 jellybeans

### In Statistics:
- The jar = population (all data)
- Small section = sample (part we can measure)
- Our guess = point estimate
- We use math instead of counting!

point estimation

data glitches - gata quality - no litches for last 5 years , it means
it is good
data quality continum
data integration 