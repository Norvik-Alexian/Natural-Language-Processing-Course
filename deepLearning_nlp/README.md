# Deep Learning for NLP

## Introduction to Neural Network
1. Input Layer:
   * Real values from the data
2. Hidden Layers:
   * Layers in between input and output
   * 3 or more layers is "deep network"
3. Output Layer:
   * Final Estimate of the output

As we go forward through more layers, the level of abstraction increases.

## Activation Function
Activation Function apply a nonlinear transformation and decide whether a neuron should be activated or not. \
Without Activation Functions we only get linear transformation after each other so the whole network is basically just a 
stacked linear regression model that is not able to learn complex patterns and this is exactly why activation functions
come into play, so after each layer we want to apply an activation function, this applies a non-linear transformation and 
helps our network to solve complex tasks.