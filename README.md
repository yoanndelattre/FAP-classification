# FAP-classification
## FAP-classification retrieving training images from various online sources. These training images will train the FAP recognition data model.
<br>

## __Performance test__

### *Description of the test configuration*  
CPU : 6 cors / 12 threads  
RAM : 16GO  
DISK : 20GO of SSD  
OS : Ubuntu 22.04 LTS

### *Description of the data samples*
Subject : Dog  
Number of images : 100  
Resolution : 512x512 pixels

### *Parameters for creating the CNN model*
```
tf.keras.applications.MobileNetV2(
    input_shape=(image_height, image_width, 3),  # Input size of the model
    include_top=False,          # Exclude the fully connected layer at the output
    weights='imagenet'          # Use pre-trained weights from ImageNet
),
tf.keras.layers.GlobalAveragePooling2D(),  # Dimension reduction
tf.keras.layers.Dense(128, activation='relu'),  # Fully connected layer
tf.keras.layers.Dense(2, activation='softmax')  # Output layer with 2 classes (person, non-person)
```

### *Model compilation parameters*
```
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

### *Model training parameters*
```
batch_size = 32
epochs = 50
```

### Duration of execution
The execution time of the image download and model training tasks is 32mins 14secs.
The execution time of the server (from its start to its shutdown) is 35mins.

### Price of the execution
*The price includes the hourly cost of server rental for CPU, RAM, storage type and storage space.*  
The hourly cost is **0.11 $US**.  
The cost of performing the task is approximately **0.059 $US**.  
The total cost (from server startup to shutdown) is approximately **0.064 $US**.