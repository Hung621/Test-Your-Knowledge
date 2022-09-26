import timeit

c1 = """
import math
t = math.sqrt(5)"""
c2 = """5**0.5"""
c3 = """pow(5,0.5)"""

execution_time1 = timeit.timeit(stmt = c1, number =1)
print(execution_time1, "seconds" )
execution_time2 = timeit.timeit(stmt = c2, number =1)
print(execution_time2, "seconds" )
execution_time3 = timeit.timeit(stmt = c3, number =1)
print(execution_time3, "seconds" )
