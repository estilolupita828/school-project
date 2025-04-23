import tensorflow as tf
from tensorflow.keras import layers

# Create a simple model
model = tf.keras.Sequential()

# Add two hidden layers with 10 neurons each and activation function ReLU
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(10, activation='relu'))

# Add an output layer with one neuron (representing the final prediction)
model.add(layers.Dense(1))
