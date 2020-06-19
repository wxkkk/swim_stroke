import tensorflow as tf
import time
import os
from process_data import read_h5
import swim_generator
import swim_discriminator
from CNN import constants

h5_path = '../../model/GAN_model/test_generator.h5'
train_data, train_label = read_h5(h5_path)
train_data = train_data.reshape(train_data.shape[0], constants.WINDOW_LENGTH, constants.SENSOR_PARAMETERS, 1).astype('float32')

BUFFER_SIZE = 60000
BATCH_SIZE = 256

# Batch and shuffle the generator_data
train_dataset = tf.data.Dataset.from_tensor_slices(train_data).shuffle(BUFFER_SIZE).batch(BATCH_SIZE)

generator = swim_generator.make_swim_generator()

noise = tf.random.normal([1, 100])
generated_data = generator(noise, training=False)

#

discriminator = swim_discriminator.make_swim_dis()
decision = discriminator(generated_data)
print(decision)

cross_entropy = tf.keras.losses.BinaryCrossentropy(from_logits=True)


def discriminator_loss(real_output, fake_output):
    real_loss = cross_entropy(tf.ones_like(real_output), real_output)
    fake_loss = cross_entropy(tf.zeros_like(fake_output), fake_output)
    total_loss = real_loss + fake_loss
    return total_loss


def generator_loss(fake_output):
    return cross_entropy(tf.ones_like(fake_output), fake_output)


generator_optimizer = tf.keras.optimizers.Adam(1e-4)
discriminator_optimizer = tf.keras.optimizers.Adam(1e-4)

checkpoint_dir = 'training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(generator_optimizer=generator_optimizer,
                                 discriminator_optimizer=discriminator_optimizer,
                                 generator=generator,
                                 discriminator=discriminator)

EPOCHS = 1000
noise_dim = 100
num_examples_to_generate = 30

seed = tf.random.normal([num_examples_to_generate, noise_dim])


@tf.function
def train_step(images):
    noise = tf.random.normal([BATCH_SIZE, noise_dim])

    with tf.GradientTape() as gen_tape, tf.GradientTape() as disc_tape:
        generated_images = generator(noise, training=True)

        real_output = discriminator(images, training=True)
        fake_output = discriminator(generated_images, training=True)

        gen_loss = generator_loss(fake_output)
        disc_loss = discriminator_loss(real_output, fake_output)

    gradients_of_generator = gen_tape.gradient(gen_loss, generator.trainable_variables)
    gradients_of_discriminator = disc_tape.gradient(disc_loss, discriminator.trainable_variables)

    generator_optimizer.apply_gradients(zip(gradients_of_generator, generator.trainable_variables))
    discriminator_optimizer.apply_gradients(zip(gradients_of_discriminator, discriminator.trainable_variables))


def train(dataset, epochs):
    for epoch in range(epochs):
        start = time.time()

        for image_batch in dataset:
            train_step(image_batch)

        # out_generator = generator(seed, training=False)
        # print(out_generator.shape)

        # Save the model every 15 epochs
        if (epoch + 1) % 15 == 0:
            checkpoint.save(file_prefix=checkpoint_prefix)

        print('Time for epoch {} is {} sec'.format(epoch + 1, time.time()-start))

    out_generator = generator(seed, training=False)
    print(out_generator.shape)

    out_path = r'../../../data/generator_data/results_1/result_{}.txt'
    for i in range(len(out_generator)):
        write_file(out_generator[i], out_path.format(i))


def write_file(out_data, path):
    with open(path, 'w', encoding='utf-8') as f:
        rewrite_lines = []
        for _ in range(len(out_data)):
            rewrite_lines.append('%f, %f, %f, %f, %f, %f\n' %
                                 (out_data[_][0], out_data[_][1], out_data[_][2],
                                  out_data[_][3], out_data[_][4], out_data[_][5]))
        f.writelines(rewrite_lines)


train(train_dataset, EPOCHS)
