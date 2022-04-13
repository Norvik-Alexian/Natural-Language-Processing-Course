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

## Recurrent Neural Network Theory
Recurrent Neural Network are specifically designed to work with sequence data like time series data. \
We can imagine a sequence just a vector of information where the index location is basically points.

Remember that a normal neuron just takes in some input, and it can be multiple inputs, so it can aggregate them. And then
once it aggregates those inputs, it passes it through some sort of activation function.

A Recurrent Neuron is a little different, it sends the output back to itself so the output goes back into the input of the
same neuron, so we can actually unroll this throughout time.

Cells that are a function of inputs from previous time steps are also known as _**memory cells**_.

RNN are also flexible in their inputs and outputs, for both sequences and single vector values.
* Sequence to Sequence
* Vector to Sequence

An issue RNN face is that after a while the network will begin to "forget" the first inputs, as information is lost at each
step going through the RNN, so the system or Long Short Term Memory(LSTM) cell, was created to help address these
recurrent neural 