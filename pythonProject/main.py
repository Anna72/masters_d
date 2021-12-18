
import pandas as pd
import numpy as np
import random
from geneticalgorithm import geneticalgorithm as ga
import showgraphs
import rezfunction


# n - number of objects in production line
# для каждого обьекта хранятся данные показаттелей его сенсоро
# print("enter n ")
# n = int(input())#number of objects in line
# print("enter estimated working time from, to")
# workingtimex =  int(input())
# workingtimey =  int(input())

n = 10
workingtimex = 81
workingtimey = 100
data_len = np.random.random_integers(workingtimex, workingtimey, n)
print("initial working time lenght : ",  data_len)

x = []
for i in range(n):
  time_of_break = np.random.randint( data_len[i]/2 , (data_len[i] - 1) + 1)
  z1 = np.random.random(time_of_break )/4
  z2 = np.random.random(data_len[i] - time_of_break)*0.75 + 0.25
  z = [*z1, *z2]
  z.sort()
  z[data_len[i] - 1] = 1
  x.append(z)

#print(x)

#showgraphs.show_dist(x,n)

# y = [80, 80,  80, 80, 80 , 80, 80, 80, 80,  80]
# func  = rezfunction.get_rez_func_params(1000,10,10,n,x)
# for i in range(10):
#   print("result " , func(y))
func = rezfunction.get_rez_func_params(1000,10,10,n,x)

import sys
import copy
for i in range(30):
  l = (i*3 + 1)
  y = 10*[l]
  maxfunc = 0
  minfunc = sys.maxsize
  av = 0
  print('parameters y:  ', y)

  for j in range(100):
    yy = copy.deepcopy(y)
    rez_1 = func(yy)
    # print(rez_1)
    maxfunc = max(rez_1, maxfunc)
    minfunc = min(rez_1, minfunc)
    av += rez_1 / 100

  print(av, ' average', '  error  +', (maxfunc / av - 1), '%', '    -', (minfunc / av + 1), '%')