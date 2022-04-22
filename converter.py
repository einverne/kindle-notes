#!/usr/bin/env python
# -*- coding: utf-8 -*-
import abc
import os.path
from abc import ABC
from pathlib import Path


class AbstractConvert(ABC):

    def __init__(self, filepath) -> None:
        self.filename = filepath

    def readfile(self):
        # readfile
        with open(self.filename, mode='r', encoding='UTF-8') as file:
            file_lines = file.readlines()
        # remove '\n' in line end
        for i in range(len(file_lines)):
            file_lines[i] = file_lines[i].rstrip()
        return file_lines

    def writefile(self, path, content):
        if not os.path.exists(path):
            os.makedirs(path)
        path = os.path.join(path, Path(self.filename).stem) + '.md'
        with open(path, 'w', encoding='UTF-8') as f:
            f.writelines(content)

    @abc.abstractmethod
    def convert(self):
        pass
