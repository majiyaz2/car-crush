import random
import math
class Layer:
    def __init__(self, inputs_count, outputs_count):
        self.outputs = [0.0 for _ in range(outputs_count)]
        self.weights = [[random.random() * 2 - 1 for _i in range(inputs_count)] for _o in range(outputs_count)]
    
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