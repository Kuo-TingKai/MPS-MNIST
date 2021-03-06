import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preprocessing.FashionMNISTpreprocessing import FashionMNISTDatasource
from trmps import *

# Model parameters
d_feature = 2
d_output = 10
input_size = 784
lin_reg_learning_rate = 10**(-4)
lin_reg_iterations = 10000

# Data parameters
permuted = False
shuffled = False
shrink = False
if shrink:
    input_size = 196

special_node_loc = None

# Optimizer parameters
batch_size = 20000
max_size = 65
min_singular_value = 0.00
reg = 0.01
armijo_coeff = 10**(-4)
armijo_iterations = 25
updates_per_step = 10

rate_of_change = 5 * 10 ** (-4)
lr_reg = 0.0

logging_enabled = False
verbosity = -0

cutoff = 100
n_step = 6
weights = None

data_source = FashionMNISTDatasource(shrink=shrink, permuted=permuted, shuffled=shuffled)

# Create network from scratch
# network = sqMPS(d_feature, d_output, input_size, special_node_loc)
# network.prepare(data_source=data_source, learning_rate=lin_reg_learning_rate,
#                 iterations=lin_reg_iterations)

# Load network from saved configuration
network = MPS.from_file()

# Training
optimizer_parameters = MPSOptimizerParameters(cutoff=cutoff, reg=reg, lr_reg=lr_reg,
                                              verbosity=verbosity, armijo_iterations=armijo_iterations,
                                              updates_per_step=updates_per_step)
training_parameters = MPSTrainingParameters(rate_of_change=rate_of_change, initial_weights=weights,
                                            _logging_enabled=logging_enabled)
optimizer = SingleSiteMPSOptimizer(network, max_size, optimizer_parameters)
optimizer.train(data_source, batch_size, n_step,
                training_parameters)

# Testing
# network.test(data_source.test_data[0], data_source.test_data[1])
