import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def classification(train_dir, image_height, image_width, name_model_file):
    # Chargez le modèle existant en format .h5
    model = load_model(name_model_file)

    # Définir les paramètres d'entraînement
    batch_size = 64
    epochs = 50

    # Pré-traiter les images
    train_datagen = ImageDataGenerator(rescale=1./255)

    # Charger les images d'entraînement
    train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=(image_height, image_width),
            batch_size=batch_size,
            class_mode='binary')

    # Compiler le modèle
    model.compile(loss='binary_crossentropy',
                optimizer=tf.keras.optimizers.RMSprop(lr=1e-4),
                metrics=['acc'])

    # Entraîner le modèle
    history = model.fit(
        train_generator,
        steps_per_epoch=train_generator.samples/train_generator.batch_size ,
        epochs=epochs)

    # Enregistrer le modèle entraîné
    model.save(name_model_file)