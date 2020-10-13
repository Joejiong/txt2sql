#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""inference process of text2sql task

Filname: text2sql_train.py
Authors: Wu Jionghao
Date: 2020-02-02 10:27:52
"""

import sys
import os
import traceback
import logging
import json
from argparse import ArgumentParser

import numpy as np
from text2sql.framework import register
from text2sql.framework.predictor import Predictor

from text2sql import cli_args
from text2sql.datalib import json_dataset
from text2sql.models.text2sql_model import Text2SQL

if __name__ == "__main__":
    args = cli_args.init_args()
    logging.basicConfig(level=logging.INFO,
        format="%(levelname)s: %(asctime)s %(filename)s"
        " [%(funcName)s:%(lineno)d][%(process)d] %(message)s",
        datefmt="%m-%d %H:%M:%S",
        filename=args.log_file,
        filemode='a')

    try:
        param_dict = cli_args.init_config(args, args.config, args.db_max_len)
        # 忽略 save_predict_file 的 dirname 恰好是个文件的情况
        if 'save_predict_file' in param_dict["predictor"] and \
                not os.path.isdir(os.path.dirname(param_dict["predictor"]['save_predict_file'])):
            os.mkdir(os.path.dirname(param_dict["predictor"]['save_predict_file']))

        register.import_modules()

        dataset = json_dataset.T2SDataSet(param_dict["dataset_reader"])
        model = Text2SQL(param_dict["model"], param_dict["predictor"]["save_predict_file"])
        predictor = Predictor(param_dict["predictor"], dataset, model)
        predictor.do_predict()
    except Exception as e:
        traceback.print_exc()
        if args.log_file is not None:
            logging.critical(traceback.format_exc())
        exit(-1)

