import numpy as np
import calc.mathops as mo
import util.rdate as rd
import ml.gbm as gbm
import sys
import os
import json


def resource_path(res_):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, res_)
    return os.path.join(res_)


def print_timestamp():
    print rd.get_timestamp()


def print_ndarray():
    if len(sys.argv) != 2:
        print "Wrong number of arguments"
    else:
        cnt = int(sys.argv[1])
        print mo.get_randn(n=cnt)


def serialize_sklearn_model():
    num_points = 100
    scale = 0.5
    X = np.linspace(-2, 2, num_points)
    y = np.sin(2 * np.pi * X) + scale * np.random.normal(num_points)
    X = X.reshape(-1, 1)
    y = y.reshape(num_points, )
    gbm.gbm_regressor(X, y)


def read_package_data():
    cfg_path = resource_path("resources/main.json")
    with open(cfg_path) as cf:
        dct = json.load(cf)

    print dct


if __name__ == "__main__":
    print_timestamp()
    print_ndarray()
    serialize_sklearn_model()
    read_package_data()

