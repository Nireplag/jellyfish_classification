# download data

import os
import zipfile
import tensorflow as tf

tf.random.set_seed(42)

path = os.path.join(os.getcwd(), 'dataset.zip')

# unzip and delete zip file
with zipfile.ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall(os.getcwd())

dt_path = os.path.join(os.getcwd(), 'dataset')
train_path = os.path.join(dt_path, 'Train')
test_path = os.path.join(dt_path, 'test')
valid_path = os.path.join(dt_path, 'valid')

# define ImageDataGenerators

train_gen = tf.keras.preprocessing.image.ImageDataGenerator(
    horizontal_flip=True,
    vertical_flip=True,
    rescale=1/255.
)

train_ds = train_gen.flow_from_directory(
    train_path,
    target_size=(179, 179),
    batch_size=32
)

test_gen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1/255.
    )

test_ds = test_gen.flow_from_directory(
    test_path,
    target_size=(179, 179),
    batch_size=32
)

eval_gen = tf.keras.preprocessing.image.ImageDataGenerator(
    rescale=1/255.
    )

eval_ds = test_gen.flow_from_directory(
    valid_path,
    target_size=(179, 179),
    batch_size=32
)

# download base model
base_model = tf.keras.applications.VGG16(
                      input_shape = (179, 179, 3),
                      include_top = False,
                      weights = "imagenet")

base_model.trainable = False

# create function with model creation and training

def model3(lr, epoch):

  flat = tf.keras.layers.Flatten()(base_model.output)
  output = tf.keras.layers.Dense(6, activation="softmax")(flat)

  model = tf.keras.Model(base_model.input, output)

  model.compile(optimizer = tf.keras.optimizers.Adam(learning_rate=lr),
                loss = "categorical_crossentropy",
                metrics = ["accuracy"])

  model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath='/tmp/checkpoint',
    save_weights_only=True,
    monitor='val_accuracy',
    mode='max',
    save_best_only=True)

  model.fit(
    train_ds,
    epochs=epoch,
    validation_data=test_ds,
    callbacks=[model_checkpoint_callback],
    verbose = 0)

  model.load_weights('/tmp/checkpoint')
  metric = model.evaluate(test_ds, verbose = 0)
  print(lr, epoch, metric)

  return model

# train model

model = model3(0.001, 5)
print(model.evaluate(test_ds, verbose = 0))

# save model as .h5

model.save('jellyfish.h5')

# save model as tf-serving
tf.saved_model.save(model, 'jellyfish-classification')
