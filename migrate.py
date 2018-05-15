import keras.backend as K
<<<<<<< HEAD

from model import create_model
from vgg16 import vgg16_model


def migrate_model(new_model):
    old_model = vgg16_model(224, 224, 3)
    # print(old_model.summary())
    old_layers = [l for l in old_model.layers]
=======
import numpy as np
from keras.layers import Conv2D

import new_start
from utils import do_compile
from vgg16 import vgg16_model


def migrate_model(img_rows, img_cols, channel=4):
    old_model = vgg16_model(224, 224, 3)
    # print(old_model.summary())
    old_layers = [l for l in old_model.layers]
    new_model = new_start.autoencoder(img_rows, img_cols, 4)
>>>>>>> 66b86b071e4d5e7bc9b3452559133c54ae30d1bf
    new_layers = [l for l in new_model.layers]

    old_conv1_1 = old_model.get_layer('conv1_1')
    old_weights = old_conv1_1.get_weights()[0]
    old_biases = old_conv1_1.get_weights()[1]
<<<<<<< HEAD
    new_weights = old_weights
=======
    new_weights = np.zeros((3, 3, channel, 64), dtype=np.float32)
    new_weights[:, :, 0:3, :] = old_weights
    new_weights[:, :, 3:channel, :] = 0.0
>>>>>>> 66b86b071e4d5e7bc9b3452559133c54ae30d1bf
    new_conv1_1 = new_model.get_layer('conv1_1')
    new_conv1_1.set_weights([new_weights, old_biases])

    for i in range(2, 31):
        old_layer = old_layers[i]
<<<<<<< HEAD
        new_layer = new_layers[i + 1]
=======
        new_layer = new_layers[i]
>>>>>>> 66b86b071e4d5e7bc9b3452559133c54ae30d1bf
        new_layer.set_weights(old_layer.get_weights())

    # flatten = old_model.get_layer('flatten')
    # f_dim = flatten.input_shape
    # print('f_dim: ' + str(f_dim))
    # old_dense1 = old_model.get_layer('dense1')
    # input_shape = old_dense1.input_shape
    # output_dim = old_dense1.get_weights()[1].shape[0]
    # print('output_dim: ' + str(output_dim))
    # W, b = old_dense1.get_weights()
    # shape = (7, 7, 512, output_dim)
    # new_W = W.reshape(shape)
    # new_conv6 = new_model.get_layer('conv6')
    # new_conv6.set_weights([new_W, b])

    del old_model
<<<<<<< HEAD


if __name__ == '__main__':
    model = create_model()
    migrate_model(model)
=======
    do_compile(new_model)
    return new_model


if __name__ == '__main__':
    model = migrate_model(320, 320, 4)
>>>>>>> 66b86b071e4d5e7bc9b3452559133c54ae30d1bf
    print(model.summary())
    model.save_weights('models/model_weights.h5')

    K.clear_session()