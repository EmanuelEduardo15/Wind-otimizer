import tensorflow as tf
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Dense, Flatten

def build_model(input_shape=(256, 256, 1)):
    inputs = Input(shape=input_shape)
    x = Conv2D(32, (3,3), activation='relu')(inputs)
    x = MaxPooling2D((2,2))(x)
    x = Conv2D(64, (3,3), activation='relu')(x)
    x = Flatten()(x)
    outputs = Dense(1, activation='sigmoid')(x)
    return tf.keras.Model(inputs, outputs)

def train_model(dataset_path, epochs=10):
    model = build_model()
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    train_data = tf.keras.utils.image_dataset_from_directory(
        dataset_path, 
        image_size=(256,256), 
        batch_size=32
    )
    model.fit(train_data, epochs=epochs)
    model.save("medfractal_model.h5")
