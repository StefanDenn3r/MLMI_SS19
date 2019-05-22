import json
import os
from collections import OrderedDict
from datetime import datetime
from pathlib import Path


def ensure_dir(dirname):
    dirname = Path(dirname)
    if not dirname.is_dir():
        dirname.mkdir(parents=True, exist_ok=False)


def read_json(fname):
    with fname.open('rt') as handle:
        return json.load(handle, object_hook=OrderedDict)


def write_json(content, fname):
    with fname.open('wt') as handle:
        json.dump(content, handle, indent=4, sort_keys=False)


def retrieve_sub_folder_paths(root):
    dir_paths = []
    for subdir in os.listdir(root):
        for subsubdir in os.listdir(os.path.join(root, subdir)):
            dir_paths.append(os.path.join(root, subdir, subsubdir))
    return dir_paths


def apply_loss(criterion, output, target):
    batch_size = output.size(1)
    num_joints = output.size(0)
    heatmaps_pred = output.reshape((batch_size, num_joints, -1)).split(1, 1)
    heatmaps_gt = target.reshape((batch_size, 1, -1))
    loss = 0
    for idx in range(num_joints):
        heatmap_pred = heatmaps_pred[idx].squeeze()
        heatmap_gt = heatmaps_gt
        loss += criterion(heatmap_pred, heatmap_gt)
    return loss / num_joints


class Timer:
    def __init__(self):
        self.cache = datetime.now()

    def check(self):
        now = datetime.now()
        duration = now - self.cache
        self.cache = now
        return duration.total_seconds()

    def reset(self):
        self.cache = datetime.now()
