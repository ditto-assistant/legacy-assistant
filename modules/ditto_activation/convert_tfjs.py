import tensorflow as tf
# import tensorflowjs as tfjs

print('\n[Converting Keras model to TFJS...]\n')

model = tf.keras.models.load_model('models/HeyDittoNet-v2')
model.save('models/HeyDittoNet-v2.h5')
# tfjs.converters.save_keras_model(model, 'models/HeyDittoNet-v2.json')

print('\n[Done! Saved to "models/HeyDittoNet-v2.h5"]\n')
