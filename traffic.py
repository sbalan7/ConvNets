import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
import matplotlib.pyplot as plt
import numpy as np
import os


def plot_sample():
    imgs = sample_training_images[:5]
    fig, axs = plt.subplots(1, 5, figsize=(6, 1))
    axs = axs.flatten()
    for img, ax in zip(imgs, axs):
        ax.imshow(img)
        ax.axis('off')
    plt.show()

def load_imgs():
    root = 'C:/Users/sbala/Datasets/Traffic_Signs'
    train_dir = os.path.join(root, 'Train')
    test_dir = os.path.join(root, 'Test')

    train_datagen = ImageDataGenerator(rescale=1./255)
    test_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(
            directory=train_dir,
            target_size=(IMG_HEIGHT, IMG_WIDTH),
            shuffle=True,
            batch_size=32)

    return train_generator



IMG_HEIGHT = 28
IMG_WIDTH = 28
EPOCHS = 15

train_gen = load_imgs()
sample_training_images, _ = next(train_gen)
plot_sample()

model = Sequential([
    tf.keras.layers.Conv2D(8, 3, activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(16, 3, activation='relu'),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Conv2D(32, 3, activation='relu'),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(43, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(
    train_gen,
    epochs=EPOCHS,
    steps_per_epoch=39209
)

model.save('traffic_classifier.h5')

