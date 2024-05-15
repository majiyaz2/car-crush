
from network import Network
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel
from network import Network
from network import Layer
from training import Trainer
from test_drive import Tester




class Position(BaseModel):
    x: int
    y: int

class Radar(BaseModel):
    length: int
    position: Position
    hasCollided: bool


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

class RadarList(BaseModel):
    radars: List[Radar]

class NetworkList(BaseModel):
    networks: List[NetworkModel]


app = FastAPI()




@app.post("/predict")
def get_results(radars: RadarList, network: NetworkModel):
    return network.feed_forward([radar.length for radar in radars.radars])

@app.get("/train")
def train_brain():
    trainer = Trainer()
    trainer.train()
    return trainer.networks

@app.get("/test")
def train_brain():
    tester = Tester()
    tester.test()
    return tester.networks