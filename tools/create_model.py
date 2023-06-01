import tensorflow as tf

# Training parameters definition
image_height = 512
image_width = 512

# Create the CNN model
model = tf.keras.models.Sequential([
    tf.keras.applications.MobileNetV2(
        input_shape=(image_height, image_width, 3),  # Input size of the model
        include_top=False,          # Exclude the fully connected layer at the output
        weights='imagenet'          # Use pre-trained weights from ImageNet
    ),
    tf.keras.layers.GlobalAveragePooling2D(),  # Dimension reduction
    tf.keras.layers.Dense(128, activation='relu'),  # Fully connected layer
    tf.keras.layers.Dense(2, activation='softmax')  # Output layer with 2 classes (person, non-person)
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Save the model
model.save('fap_model.h5')