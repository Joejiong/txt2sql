#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""wrapper of paddle executor

Filname: executor.py
Authors: Wu Jionghao
Date: 2019-12-20 20:08:38
"""

import sys
import os
import traceback
import logging

from paddle import fluid

class Executor(object):

    """Simple Executor. """

    def __init__(self, place='cpu'):
        """init of class """
        super(Executor, self).__init__()

        if place == 'cpu':
            self.exe = fluid.Executor(fluid.CPUPlace())
        else:
            raise ValueError('currently only support cpu place')
        self.exe.run(fluid.default_startup_program())

    def run(self, *args, **kwargs):
        """wrapper of Executor.run()

        Args:
            *args (TYPE): NULL
            **kwargs (TYPE): NULL

        Returns: TODO

        Raises: NULL

        """
        return self.exe.run(fluid.default_main_program(), *args, **kwargs)


if __name__ == "__main__":
    """run some simple test cases"""
    pass

