# https://medium.com/@the1ju/simple-logistic-regression-using-keras-249e0cc9a970

from keras.callbacks import ModelCheckpoint
from keras.datasets import mnist
from keras.layers import Dense, Activation
from keras.models import Sequential
from keras.optimizers import SGD
from keras.utils import np_utils

# Hyperparameters

batch_size = 128
epochs = 10
lr = 0.1

# Get the data

(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Reshape and normalize the inputs

input_dim = 784 # 28 * 28
X_train = X_train.reshape(60000, input_dim)
X_test = X_test.reshape(10000, input_dim)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Convert class vectors to binary class matrices

classes = 10

Y_train = np_utils.to_categorical(y_train, classes)
Y_test = np_utils.to_categorical(y_test, classes)

# Build the model

model = Sequential()

model.add(Dense(classes, input_dim=input_dim, activation='softmax'))

model.compile(
    optimizer=SGD(lr),
    loss='categorical_crossentropy',
    metrics=['accuracy'])

# Checkpoint callback

checkpoint = ModelCheckpoint('weights.{epoch:02d}-{val_loss:.4f}.hdf5')

# Train the model

model.fit(
    X_train,
    Y_train,
    batch_size=batch_size,
    epochs=epochs,
    verbose=1,
    validation_data=(X_test, Y_test),
    callbacks=[checkpoint])
