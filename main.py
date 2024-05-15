
from network import Network
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

from canvas import Canvas
from racetrack import Track
from network import Network
from network import Layer
from evolution import Evolution
from storage import Storage
import os


class Position(BaseModel):
    x: int
    y: int

class Radar(BaseModel):
    length: int
    position: Position
    hasCollided: bool

class RadarList(BaseModel):
    radars: List[Radar]

class LayerModel(BaseModel, Layer):
    outputs: List[float]
    weights: List[List[float]]
    highest_checkpoint : int

    class Config:
        arbitrary_types_allowed=True

class NetworkModel(BaseModel, Network):
    dimensions: List[int]
    hasReachedGoal: bool
    smallestEdgeDistance: int
    layers: List[LayerModel]
    inputs: List[int]

    class Config:
        arbitrary_types_allowed=True



app = FastAPI()




@app.post("/predict")
def get_results(radars: RadarList, network: NetworkModel):
    
    return network.feed_forward([radar.length for radar in radars.radars])


@app.get("/train")
def train_brain():
    network = Network((5,4,2))

    population_count = 2
    max_generation_iterations = 10
    keep_count = 4
    
    evolution = Evolution(population_count, keep_count)
    storage = Storage("brain.json")
    best_chromosomes = storage.load()

    network.deserialize(best_chromosomes[0])
    print(best_chromosomes[0])

    simulation_round = 1
    while simulation_round <= max_generation_iterations:
        print(f"=== Round: {simulation_round} ===")
        simulation_round +=1

        print(f"-- Average checkpoint reached: { (network.highest_checkpoint):.2f}.")
        print(f"-- Cars reached goal: { (network.has_reached_goal)} of population {population_count}")
        print(f"-- Average edge distance: { (network.smallest_edge_distance ) :.2f}")

        serialized = [network.serialize(), network.serialize()]
        offspring = evolution.execute(serialized)
        storage.save(offspring[:keep_count])

        network.deserialize(offspring[0])
    
        
    return network

# @app.get("/train")
# def train_brain():
    
#     network_dimensions = 5,4,2
#     population_count = 40
#     max_generation_iterations = 10
#     keep_count = 4

   
#     evolution = Evolution(population_count, keep_count)
#     storage = Storage("brain.json")
#     best_chromosomes = storage.load()
    
#     network.deserialize(best_chromosomes[0])

#     simulation_round = 1

#     while simulation_round <= max_generation_iterations:
#         print(f"=== Round: {simulation_round} ===")
#         simulation_round +=1
        
#         print(f"-- Average checkpoint reached: { (network.highest_checkpoint):.2f}.")
#         print(f"-- Cars reached goal: { (network.has_reached_goal)} of population {population_count}")
#         print(f"-- Average edge distance: { (network.smallest_edge_distance ) :.2f}")

#         serialized = network.serialize()
#         offspring = evolution.execute(serialized)
#         storage.save(offspring[:keep_count])
#         networks = []
#         for chromosome in offspring:
#             network = Network(network_dimensions)
#             network.deserialize(chromosome)
#         network = network
#     return NetworkModel(network.dimensions, network.has_reached_goal, network.smallest_edge_distance, network.layers)