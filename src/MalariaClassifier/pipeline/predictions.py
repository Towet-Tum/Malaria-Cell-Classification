import os
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def makePrediction(self):
        train_ds = os.path.join("artifacts","data_ingestion","dataset","train/")
        train_datagen = ImageDataGenerator(1./255)
        train_gen = train_datagen.flow_from_directory(train_ds, target_size=(224,224), class_mode='categorical', batch_size=32)
        model = load_model(os.path.join("model", "xception_model.h5"))
        img = image.load_img(self.filename, target_size=(224,224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        clas = np.argmax(model.predict(img))
        label_names = train_gen.class_indices
        dict_class = dict(zip(list(range(len(label_names))), label_names))
        name = dict_class[clas]
        print(f"Label name ::: {label_names}")
        print(f"the Dictrionary:::: {dict_class}")
        print(f"The class name ::: {clas}")
        return name
