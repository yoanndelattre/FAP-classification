import tensorflow as tf

# Définition des paramètres d'entraînement
image_height = 1024
image_width = 1024

# Création du modèle CNN
model = tf.keras.models.Sequential([
    tf.keras.applications.MobileNetV2(
        input_shape=(image_height, image_width, 3),  # Taille d'entrée du modèle
        include_top=False,          # Ne pas inclure la couche fully connected à la sortie
        weights='imagenet'          # Utiliser les poids pré-entraînés sur ImageNet
    ),
    tf.keras.layers.GlobalAveragePooling2D(),  # Réduction de dimension
    tf.keras.layers.Dense(128, activation='relu'),  # Couche fully connected
    tf.keras.layers.Dense(2, activation='softmax')  # Couche de sortie avec 2 classes (personne, non personne)
])

# Compilation du modèle
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Sauvegarde du modèle
model.save('fap_model.h5')