"""
    This is a script that automatizes the training process. The training process can be configured by using a yaml file.
"""

from opennng.util.trainer import train_model
from opennng.util.parser import parse_data, parse_model, parse_train, parse_valid, parse_generate_samples
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--model", type=str)

    parser.add_argument("--train_X_path", type=str)
    parser.add_argument("--valid_X_path", type=str)
    parser.add_argument("--train_y_path", type=str)
    parser.add_argument("--valid_y_path", type=str)
    parser.add_argument("--from_noise", type=bool, default=True)

    parser.add_argument("--optimizer", type=str, default="Adam")
    parser.add_argument("--learning_rate", type=float, default=0.0001)
    parser.add_argument("--iterations", type=int, default=10000)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--save_checkpoint_steps", type=int, default=100)
    parser.add_argument("--save_checkpoint_path", type=str, default="trained_models")

    parser.add_argument("--valid_batch_size", type=int, default=32)
    parser.add_argument("--valid_steps", type=int, default=10)

    parser.add_argument("--generate_train_samples", type=bool, default=True)
    parser.add_argument("--num_train_samples", type=int, default=10)

    args = parser.parse_args()

    model, train_step, loss_fcn = parse_model(args)
    X_train, X_valid, y_train, y_valid = parse_data(args)
    optimizer, iterations, batch_size, save_checkpoint_steps, save_checkpoint_path = parse_train(args)
    valid_batch_size, valid_steps = parse_valid(args)
    generate_train_samples, num_train_samples = parse_generate_samples(args)

    train_model(model, train_step, loss_fcn,
                X_train, X_valid, y_train, y_valid,
                optimizer, iterations, batch_size, save_checkpoint_steps, save_checkpoint_path,
                valid_batch_size, valid_steps,
                generate_train_samples, num_train_samples)

