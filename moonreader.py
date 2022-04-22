#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from pathlib import Path

from converter import AbstractConvert


class MoonReader(AbstractConvert):

    def convert(self):
        # readfile
        file_lines = self.readfile()
        # bookname,author style
        content = []
        content.append('# ' + file_lines[5])
        content.append('\n\n---')
        for i in range(3, len(file_lines), 17):
            # highlight
            content.append('\n\n> ' + file_lines[i + 13] + '\n\n')
            if file_lines[i + 12] != '':
                # note
                content.append(file_lines[i + 12] + '\n\n')
            # time
            clipping_time = float(file_lines[i + 10]) / 1000
            clipping_time_transfer = time.strftime("%Y.%m.%d %H:%M:%S", time.localtime(clipping_time))
            content.append('*' + clipping_time_transfer + '*\n\n')
            content.append('---')
        content.append('\n')
        # write file
        self.writefile('docs/moonreader', content)

    def write(self):
        self.convert()


def main(files):
    if Path.is_dir(Path(files)):
        for f in Path(files).glob('*.mrexpt'):
            MoonReader(f).write()
    if Path.is_file(Path(files)):
        if Path(files).suffix == '.mrexpt':
            MoonReader(files).write()


if __name__ == '__main__':
    main('files')
