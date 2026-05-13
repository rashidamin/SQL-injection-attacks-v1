
import tensorflow as tf
from tensorflow.keras import layers, models

def build_cnn(vocab_size=5000, max_len=200):
    model = models.Sequential([
        layers.Embedding(vocab_size, 128, input_length=max_len),
        layers.Conv1D(64, 3, activation='relu'),
        layers.MaxPooling1D(2),
        layers.Conv1D(128, 3, activation='relu'),
        layers.GlobalMaxPooling1D(),
        layers.Dense(64, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
    return model
