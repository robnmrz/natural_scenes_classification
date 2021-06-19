import os
import config

from dataset import define_generators
from model import get_model

from tensorflow.keras import callbacks

def train(epochs):
    train_generator, valid_generator = define_generators(
    config.TRAIN_PATH, config.VALID_PATH
    )
    
    # retrive ResNet50 model with custom head
    model = get_model()

    model.compile(
        loss='categorical_crossentropy', 
        optimizer='adam', 
        metrics=['AUC']
    )

    # define callbacks for training
    earlystopping = callbacks.EarlyStopping(
        monitor='val_loss', verbose=1, 
        patience=20
    )
    checkpoint = callbacks.ModelCheckpoint(
        os.path.join(config.MODEL_PATH, 'classifier_scenes_resnet.hdf5'), 
        monitor='val_loss', 
        verbose=1, 
        save_best_only=True
    )

    model.fit(
        train_generator, 
        steps_per_epoch=train_generator.n // 20,
        epochs=epochs, 
        validation_data=valid_generator, 
        validation_steps= valid_generator.n // 20,
        callbacks=[checkpoint, earlystopping]
    )

if __name__ == '__main__':
    train(epochs=10)
