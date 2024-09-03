import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

images = []

model = tf.keras.models.load_model('model.keras')
test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    'dataset',
    target_size=(100, 100),
    batch_size=1,
    class_mode='categorical',
    shuffle=False
)

imgs_path = [
    'test_images/test1.png',
    'test_images/test2.png',
    'test_images/test3.png',
    'test_images/test4.png',
    'test_images/test5.png',
    'test_images/test6.png',
    'test_images/test7.png',
    'test_images/test8.png',
    'test_images/test9.png'
]

for img_path in imgs_path:
    img = load_img(img_path, target_size=(100, 100))
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])

    class_indices = test_generator.class_indices
    predicted_class = [k for k, v in class_indices.items() if v == predicted_class_index][0]

    images.append(f"{img_path} -> {predicted_class}")

for image in images:
    print(f"Predicted Image: {image}")