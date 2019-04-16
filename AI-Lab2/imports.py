from queue import PriorityQueue
from copy import deepcopy
from math import sqrt,sin
from itertools import groupby
from datetime import datetime
import random
import matplotlib.pyplot as plt
import numpy as np

IND_SIZE = 2
POP_SIZE = 100
RANDSEED = True
VMIN = [-1.5,-3]
VMAX = [-3.0,4.0]
SIM_CH = 25
PARENT_PROB = 0.75
MUTATE_PROB = 0.5
NO_ITER = 100 #10k
TEST_ITER = 40
TEST_RUNS = 30
TEST_POP = 40