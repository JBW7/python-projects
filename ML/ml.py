import tensorflow as tf
import numpy as np
from tensorflow import keras

# https://colab.research.google.com/github/lmoroney/mlday-tokyo/blob/master/Lab1-Hello-ML-World.ipynb#scrollTo=oxNzL4lS2Gui

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])


model.compile(optimizer='sgd', loss='mean_squared_error')


xs = np.array([0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([4.0, 11.0, 18.0, 25.0, 32.0], dtype=float)

model.fit(xs, ys, epochs= 500)

print(model.predict([10.0]))