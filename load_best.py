import numpy as np
from order_manager import OrderManager
from product import Product
from flexsim_connector import FlexsimConnector

best_schedule = np.load('best_schedule.npy')

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

connector = FlexsimConnector("Projet.fsm")
manager = OrderManager(counts)
manager.set_schedule(best_schedule)
manager.write2excel("arrival_schedule.xlsx")
connector.simulate(True)
