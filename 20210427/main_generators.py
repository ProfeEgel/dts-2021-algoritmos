
import random
from sorting_animator import animate_sorting_algorithm
from sorting_algorithms import *

n = 250
max = 100
data = [random.randint(0,max) for i in range(n)]
# animate_sorting_algorithm(data, n, max, bubble_sort_generator(data))
# animate_sorting_algorithm(data, n, max, selection_sort_generator(data))
animate_sorting_algorithm(data, n, max, insertion_sort_generator(data))
