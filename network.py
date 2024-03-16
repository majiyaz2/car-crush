import random
import math
class Layer:
    def __init__(self, inputs_count, outputs_count):
        self.outputs = [0.0 for _ in range(outputs_count)]
        self.weights = [[random.random() * 2 - 1 for _i in range(inputs_count)] for _o in range(outputs_count)]
        self.highest_checkpoint = 0
    
    def feed_forward(self, inputs):
        for output_index, output in enumerate(self.outputs):
            sum = 0
            for weight_index, input in enumerate(inputs):
                sum += input * self.weights[output_index][weight_index]
            self.outputs[output_index] = math.tanh(sum)

class Network:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.layers = []
        for i in range(len(dimensions)-1):
            self.layers.append(Layer(dimensions[i], dimensions[i+1]))
    
    def feed_forward(self, inputs):
        for layer in self.layers:
            layer.feed_forward(inputs)
            inputs = [i for i in layer.outputs]
        return self.layers[-1].outputs
    def serialize(self):
        chromosome = []
        for layer in self.layers:
            for outputs in layer.weights:
                for weight in outputs:
                    chromosome.append()
        return RankableChromosome(self.self.highest_checkpoint, chromosome)
    
    def deserialize(self, chromosome):
        layer_index = 0
        output_index = 0
        input_index = 0
        for gene in chromosome:
            self.layers[layer_index].weights[output_index][input_index] = gene
            input_index += 1
            if input_index > len(self.layers[layer_index].weights[output_index])-1:
                input_index = 0
                output_index += 1
                if output_index > len(self.layers[layer_index].weights) -1:
                    output_index = 0
                    layer_index += 1
    
    
class RankableChromosome:
    def __init__(self, highest_checkpoint, chromosome):
        self.highest_checkpoint = highest_checkpoint
        self.chromosome = chromosome
    
    def __lt__(self, other):
        return self.highest_checkpoint > other.highest_checkpoint