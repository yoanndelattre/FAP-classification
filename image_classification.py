import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def classification(train_dir, image_height, image_width, name_model_file, new_name_model_file):
    # Load the existing model in .h5 format
    model = load_model(name_model_file)

    # Define training parameters
    batch_size = 64
    epochs = 50

    # Preprocess the images
    train_datagen = ImageDataGenerator(rescale=1.0/255)

    # Load the training images
    train_generator = train_datagen.flow_from_directory(
            train_dir,
            target_size=(image_height, image_width),
            batch_size=batch_size,
            class_mode='categorical')

    # Compile the model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(
        train_generator,
        epochs=epochs
    )

    # Save the trained model
    model.save(new_name_model_file)