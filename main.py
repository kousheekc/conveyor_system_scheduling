from genetic_algorithm import GeneticAlgorithm
from product import Product
import time

if __name__ == '__main__':
    start = time.time()
    counts = {
        1 : Product(48, 35, 49,  8,  0, 1), 
        2 : Product(15,  0, 19, 30,  0, 1),
        3 : Product(50,  0, 20, 34, 18, 0),
        4 : Product(44,  4, 31, 17,  9, 0),
        5 : Product(31,  8, 47, 33, 17, 1),
        6 : Product(39,  0,  0, 25, 50, 1),
        7 : Product(29, 35,  0, 13, 24, 1),
        8 : Product(31,  0, 26,  0, 21, 0),
        9 : Product(21, 31,  0, 35,  5, 1),
        10 : Product(22,19, 37, 42, 30, 0) 
    }
    
    ga = GeneticAlgorithm(counts, 10, 20, 50)
    ga.evolve()