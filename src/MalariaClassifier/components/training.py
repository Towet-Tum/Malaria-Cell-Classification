import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from MalariaClassifier.entity.config_entity import TrainingConfig

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config 

    def train_val_gen(self):
        train_ds = os.path.join(self.config.dataset, "train")
        val_ds = os.path.join(self.config.dataset, "val")
        train_datagen = ImageDataGenerator(rescale=1./255, zoom_range=0.2,
                                           shear_range=0.2, horizontal_flip=True)
        val_datagen = ImageDataGenerator(rescale=1./255)
        train_gen = train_datagen.flow_from_directory(train_ds,
                                                      target_size=(self.config.imgsz,self.config.imgsz),
                                                      class_mode='categorical')
        val_gen = val_datagen.flow_from_directory(val_ds,
                                                      target_size=(self.config.imgsz,self.config.imgsz),
                                                      class_mode='categorical')
        
        return train_gen, val_gen
    
    def train(self):
        base_model = tf.keras.applications.Xception(input_shape=(self.config.imgsz,self.config.imgsz,3),
                                               include_top=self.config.include_top,
                                               weights=self.config.weights)
        base_model.trainable = False
        model = tf.keras.Sequential([
            base_model,
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(2, activation='softmax')
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=self.config.lr),
                      loss = 'categorical_crossentropy',
                      metrics=['accuracy'])
        train_gen, val_gen = self.train_val_gen()
        model.fit(train_gen, epochs=self.config.epochs,
                  validation_data=val_gen,
                  steps_per_epoch=len(train_gen)/self.config.batch_size,
                  validation_steps=len(val_gen)/self.config.batch_size)
        model.save(self.config.model_path)
