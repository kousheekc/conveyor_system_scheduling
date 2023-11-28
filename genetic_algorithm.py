from order_manager import OrderManager
from flexsim_connector import FlexsimConnector
import numpy as np
import random

class GeneticAlgorithm:
    def __init__(self, count: dict, population_size: int , generations: int, crossover_percent: int) -> None:
        self.count = count
        self.population_size = population_size
        self.generations = generations
        self.crossover_percent = crossover_percent

        self.order_manager = OrderManager(self.count)
        self.flexsim_connector = FlexsimConnector("Projet_auto.fsm")

        self.best = {
            "cur_time": float('inf'),
            "pre_time": float('inf'),
            "cur_schedule": [],
            "pre_schedule": []
        }

        self.second_best = {
            "cur_time": float('inf'),
            "pre_time": float('inf'),
            "cur_schedule": [],
            "pre_schedule": []
        }

        self.global_best = {
            "time": float('inf'),
            "schedule": []
        }

    def update_bests(self, time, schedule):
        if time < self.best["cur_time"]:
            self.second_best["cur_time"] = self.best["cur_time"]
            self.second_best["cur_schedule"] = self.best["cur_schedule"]
            self.best["cur_time"] = time
            self.best["cur_schedule"] = schedule
        elif time < self.second_best["cur_time"] and time != self.best["cur_time"]:
            self.second_best["cur_time"] = time
            self.second_best["cur_schedule"] = schedule

        if time < self.global_best["time"]:
            self.global_best["time"] = time
            self.global_best["schedule"] = schedule

    def crossover(self):
        random_index = random.randint(0, len(self.best["pre_schedule"]) - 1)
        new_schedule = self.best["pre_schedule"][:random_index] + self.second_best["pre_schedule"][random_index:]
        return new_schedule


    def evolve(self):
        for i in range(self.generations):
            print(f"Generation {i}")
            self.best["cur_time"] = float('inf')
            self.best["cur_schedule"] = []
            self.second_best["cur_time"] = float('inf')
            self.second_best["cur_schedule"] = []

            for j in range(self.population_size):
                print(f"Gene {j}")
                if (i == 0):
                    self.order_manager.generate_random_schedule()
                    self.order_manager.write2excel("arrival_schedule.xlsx")
                else:
                    if (j < self.crossover_percent/100 * self.population_size):
                        new_schedule = self.crossover()
                        self.order_manager.set_schedule(new_schedule)
                    else:
                        self.order_manager.generate_random_schedule()
                        self.order_manager.write2excel("arrival_schedule.xlsx")

                schedule = self.order_manager.get_schedule()
                time = self.flexsim_connector.simulate()
                self.update_bests(time, schedule)

            self.best["pre_time"] = self.best["cur_time"]
            self.best["pre_schedule"] = self.best["cur_schedule"]
            self.second_best["pre_time"] = self.second_best["cur_time"]
            self.second_best["pre_schedule"] = self.second_best["cur_schedule"]
            print(self.best["pre_time"], self.second_best["pre_time"])
            np.save('best_schedule.npy', np.array(self.global_best["schedule"]))


                    