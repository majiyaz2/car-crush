import random
from network import Network
from evolution import Evolution
from storage import Storage


class Tester():

    def __init__(self):
        self.network_dimensions = 5,4,2
        self.population_count = 6
        self.max_generation_iterations = 10
        self.keep_count = 6

        self.networks = [Network(self.network_dimensions) for _ in range(self.population_count)]
        self.storage = Storage("brain.json")
        self.best_chromosomes = self.storage.load()
        self.simulation_round = 1
        

        

    def test(self):

        for c, n in zip(self.best_chromosomes, self.networks):
            n.deserialize(c)

        while self.simulation_round <= self.max_generation_iterations:
            print(f"=== Round: {self.simulation_round} ===")
            # self.simulate_generation()
            self.simulation_round +=1

            print(f"-- Average checkpoint reached: {sum (n.highest_checkpoint for n in self.networks) / len(self.networks):.2f}.")
            print(f"-- Cars reached goal: {sum (n.has_reached_goal for n in self.networks)} of population {self.population_count}")
            print(f"-- Average edge distance: {sum (n.smallest_edge_distance for n in self.networks[:self.keep_count]) / self.keep_count:.2f}")

   
      
            
  
            

    def simulate_generation(self):
        for network in self.networks:
            network.highest_checkpoint = random.randint(0, 10)
            network.smallest_edge_distance = random.uniform(-1.0, 1.0)
            network.has_reached_goal = random.choice([True, False])
        

