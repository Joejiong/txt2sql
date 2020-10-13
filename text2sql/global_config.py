#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""global config

Filname: global_config.py
Authors: Wu Jionghao
Date: 2019-11-27 21:05:38
"""

import sys
import os
import traceback
import logging

class GlobalConfig(object):

    """Global Config for the System """

    def __init__(self):
        """init of class """
        super(GlobalConfig, self).__init__()

        self.use_question_feature = False
        self.use_table_feature = False
        self.use_column_feature = False
        self.use_value_feature = False


if __name__ == "__main__":
    """run some simple test cases"""
    pass

