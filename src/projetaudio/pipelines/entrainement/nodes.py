"""
This is a boilerplate pipeline 'entrainement'
generated using Kedro 0.18.10
"""
import mlflow
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, regularizers



def template_model(input_shape, units=128, activation='relu', l2_value=0.01, dropout_rate=None, learning_rate=1e-3):
    
    # Définition de la couche d'entrée
    inputs = layers.Input(shape=input_shape)
    
    # Définition des couches de convolution
    x = layers.Conv1D(filters=32, kernel_size=3, activation=activation)(inputs)
    x = layers.MaxPooling1D(pool_size=2)(x)
    x = layers.ZeroPadding1D(padding=1)(x)
    x = layers.Conv1D(filters=64, kernel_size=3, activation=activation)(x)
    x = layers.ZeroPadding1D(padding=1)(x)
    
    # Ajouter une couche de padding
    x = layers.MaxPooling1D(pool_size=2)(x)

    # Aplatir les données
    x = layers.Flatten()(x)
    
    # Définition des couches entièrement connectées
    x = layers.Dense(units, activation='relu', kernel_regularizer=regularizers.l2(l2_value))(x)
    if dropout_rate is not None:
        x = layers.Dropout(dropout_rate)(x)
    x = layers.Dense(input_shape[0], activation='softmax')(x)
    # Création du modèle
    model = tf.keras.Model(inputs=inputs, outputs=x)
    model.compile(loss='categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate), metrics=[tf.keras.metrics.CategoricalAccuracy()])

    return model

def create_model(x_train, y_train, x_test, y_test):
    mlflow.autolog()

    x_train = x_train.astype(int)

    model = template_model((x_train.shape[1], 1))

    model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

    model.save("custom_model.keras")

    mlflow.end_run(mlflow.entities.RunStatus.FAILED)

    return model



