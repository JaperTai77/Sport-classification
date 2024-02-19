import os
import cv2
import json
import tensorflow as tf

class ClassificationModel:
    model = None
    target = None

    def load_model(self):
        '''path = os.path.join(
            os.getcwd(),
            'sportclass_EN0_model.joblib')
        loaded_model = joblib.load(path)
        model, class_label = loaded_model
        '''
        path = os.path.join(
            os.getcwd(),
            'EfficientNetB0-100-(224 X 224)- 98.40.h5')
        model = tf.keras.models.load_model(path, custom_objects={'F1_score':'F1_score'})
        path = os.path.join(
            os.getcwd(),
            'class_label.json')
        with open(path) as f:
            class_label = json.load(f)
        self.model = model
        self.targets = class_label    

    def load_image(self, image):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)    
    
    def predict(self, image) -> list:
        image_resized = self.load_image(image)
        im = image_resized.copy()       
        if im.ndim == 3:
            im = tf.expand_dims(im, axis = 0)
        elif im.ndim == 4:
            pass

        if tf.test.gpu_device_name() == '' or tf.test.gpu_device_name() == None:
            pred = self.model.predict(im, verbose = 0)
        else:
            with tf.device(tf.test.gpu_device_name()):
                pred = self.model.predict(im, verbose = 0)
        label = [self.targets[str(pred[i].argmax())] for i in range(len(pred))]
        return label

