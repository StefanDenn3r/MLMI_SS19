CONFIG = {
    "name": "XRay",
    "n_gpu": 1,
    "arch": {
        "type": "ConvolutionalPoseMachines",
        "args": {
            "x_channels": 5,
            "stage_channels": 5,
            "num_stages": 1,
            "num_classes": 23,
            "depthwise_separable_convolution": True,
            "dilation": 1,
            "squeeze_excitation": True
        }
    },
    "data_loader": {
        "type": "XRayDataLoader",
        "args": {
            "data_dir": "data/XRay/Patient_0",
            "batch_size": 1,
            "shuffle": False,
            "validation_split": 0.5,
            "num_workers": 0,
            "custom_args": {
                'isTraining': True,
                'sigma': 80,
                'sigma_reduction_factor': 0.95,
                'minimum_sigma_image_ratio': 0.02,
                'fraction_of_dataset': 0.05,
            }
        }
    },
    "optimizer": {
        "type": "Adam",
        "args": {
            "lr": 0.001,
            "weight_decay": 0,
            "amsgrad": True
        }
    },
    "loss": "smooth_l1_loss",
    "metrics": [
        "percentage_correct_keypoints",
        "keypoint_distance_loss",
        "mse_loss"
    ],
    "lr_scheduler": {
        "type": "StepLR",
        "args": {
            "step_size": 50,
            "gamma": 0.1
        }
    },
    "trainer": {
        "epochs": 10,
        "save_dir": "saved/",
        "save_period": 1,
        "verbosity": 2,
        "monitor": "min val_loss",
        "early_stop": 20,
        "tensorboardX": True
    },
    'threshold': 0.4,
    'prediction_blur': 1
}
