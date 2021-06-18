from tensorflow.keras.preprocessing import image

def define_generators(train_path, valid_path, bs=20):
    """
    Function to define training generators
    :param train_path: path to training data (classes = subfolders)
    :param valid_path: path to validation data (classes = subfolders)
    :return: generators for train and validaton data
    """
    train_datagen = image.ImageDataGenerator(rescale=1./255)
    valid_datagen = image.ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        train_path,
        target_size=(150,150),
        batch_size=bs,
        class_mode='categorical'
    )

    valid_generator = valid_datagen.flow_from_directory(
        valid_path,
        target_size=(150,150),
        batch_size=bs,
        class_mode='categorical'
    )
    
    return train_generator, valid_generator