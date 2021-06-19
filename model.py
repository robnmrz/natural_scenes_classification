import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras import layers, models

def get_model():
    """
    Function that defines and returns 
    the prepared model with all layers
    :returns: defined model to trian on
    """
    # defining the resnet model with pretrained
    # weights from imagenet dataset
    resnet = ResNet50(
        weights = 'imagenet', 
        include_top = False,
        input_tensor = layers.Input(shape=(150, 150, 3))
    )

    # prevent pretrained weights
    # from getting updated while training
    for layer in resnet.layers:
        layer.trainable = False

    # adding additional layers to ResNet50
    base = resnet.output
    base = layers.MaxPool2D(pool_size=(2,2))(base)
    base = layers.Flatten()(base)
    base = layers.Dense(256, activation=tf.nn.relu)(base)
    base = layers.Dropout(0.5)(base)
    base = layers.Dense(256, activation=tf.nn.relu)(base)
    base = layers.Dropout(0.5)(base)
    # output layer for 6 classes with softmax activation
    base = layers.Dense(6, activation=tf.nn.softmax)(base)

    model = models.Model(inputs=resnet.input, outputs=base)

    return model



    
