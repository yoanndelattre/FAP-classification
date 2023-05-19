import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Définition des paramètres d'entraînement
batch_size = 64
epochs = 50
image_height = 1024
image_width = 1024

# Chemin vers les données d'entraînement
train_data_dir = 'download'

# Création du générateur d'images d'entraînement
train_datagen = ImageDataGenerator(rescale=1./255)  # Rescale les valeurs des pixels entre 0 et 1

train_generator = train_datagen.flow_from_directory(
    train_data_dir,
    target_size=(image_height, image_width),
    batch_size=batch_size,
    class_mode='binary'  # Classe binaire : 0 pour les têtes sans personne, 1 pour les têtes avec une personne
)

# Création du modèle CNN
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(image_height, image_width, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')  # Couche de sortie avec une seule unité pour la classification binaire
])

# Compilation du modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entraînement du modèle
model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=epochs
)

# Sauvegarde du modèle entraîné
model.save('fap_model.h5')