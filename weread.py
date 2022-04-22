#!/usr/bin/env python
# -*- coding: utf-8 -*-

from converter import AbstractConvert


class Weread(AbstractConvert):

    def convert(self):
        file_lines = self.readfile()

        # book title,author style
        output_content = []
        # first line is the book title
        output_content.append('# ' + file_lines[0] + '\n\n')
        # sencond line is the author
        output_content.append('**' + file_lines[1] + '**\n\n')
        # third line is the count of highlights
        output_content.append('*' + file_lines[2] + '*\n\n---')
        # converter each highlight block to [][]
        block = []
        for i in range(3, len(file_lines)):
            if file_lines[i] == '':
                self.handle_block(block, output_content)
                block.clear()
            else:
                block.append(file_lines[i])
        # write file
        self.writefile('docs/weread/', output_content)

    def handle_block(self, block, output_content):
        for j in range(0, len(block)):
            # chapter title
            if block[j].startswith('◆'):
                output_content.append('---\n\n## ' + block[j][2:] + '\n\n')
            # highlight block
            if block[j].startswith('>>'):
                output_content.append('> ' + block[j][3:] + '\n\n---\n\n')
            elif block[j].startswith('>'):
                output_content.append('> ' + block[j][2:] + '\n\n')
                output_content.append(block[j - 1] + '\n\n---\n\n')
            print(block[j])


def main():
    weread = Weread('weread/非对称风险.txt')
    weread.convert()


if __name__ == '__main__':
    main()
