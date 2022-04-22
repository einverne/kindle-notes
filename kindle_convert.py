#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re

from converter import AbstractConvert

BOUNDARY = u"==========\n"  # 分隔符
intab = " \/::*?\"<>|"
outtab = "------？-《》-"  # 用于替换特殊字符


# 替换不能用作文件名的字符
def change_char(s):
    s = s.strip()
    return s.translate(str.maketrans(intab, outtab))


def normalize_book_name(origin_name):
    return change_char(origin_name)[0:80]


def make_file_name(s):
    s = s.strip()
    s = s.replace("！", '')
    s = s.replace("?", '')
    s = s.replace('!', '')
    s = s.replace(';', '-')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace('[', '')
    s = s.replace(']', '')
    s = s.replace('（', '')
    s = s.replace('）', '')
    s = re.sub("([\(\[（]).*?([\)\]）])", "\g<1>\g<2>", s)
    return s[0:40]


# 获取标注位置
def get_addr(s):
    g = s.split(" | ")[0]
    return g.strip()


# 获取添加时间
def get_time(s):
    g = s.split(" | ")[1]
    return g.split("\n\n")[0]


# 获取标注内容
def get_mark(s):
    g = s.split(" | ")[1]
    try:
        return g.split("\n\n")[1]
    except IndexError:
        # print("list index out of range due to empty content")
        return "empty content"


class Kindle(AbstractConvert):

    def convert(self):
        # 结果为每一条单独的笔记，包含书名，时间，位置和内容
        f = open(self.filename, "r", encoding='utf-8')

        # 读取标注文件全部内容
        content = f.read()
        # 替换书名前的空格
        content = content.replace(u'\ufeff', u'')
        clips = content.split(BOUNDARY)

        # 获取列表的个数
        print("列表个数：", clips.__len__())
        total = clips.__len__()

        # 获取书名存储为列表books，获取除书名外的内容为sentence
        book_to_sentence_set = dict()  # map book_name -> list
        for i in range(0, total):
            book = clips[i].split("\n-")
            if len(book) < 2:
                continue
            normalized_name = normalize_book_name(book[0])
            book_sentence_set_exist = book_to_sentence_set.get(normalized_name)
            if not book_sentence_set_exist:
                book_to_sentence_set[normalized_name] = list()
                book_to_sentence_set[normalized_name].append(book[1])
            else:
                if book[1] not in book_sentence_set_exist:
                    book_sentence_set_exist.append(book[1])
        print('各本书笔记数：')
        for book in book_to_sentence_set:
            print(f'{book} 笔记数：{book_to_sentence_set.get(book).__len__()}')

        print('书籍总数：', len(book_to_sentence_set))

        if not os.path.exists('docs/kindle'):
            os.makedirs('docs/kindle')

        # 向文件添加标注内容
        for book_name in book_to_sentence_set:
            file_path = make_file_name(book_name)
            f = open('docs/kindle/' + file_path + '.md', 'w', encoding='utf-8')
            f.writelines('# ' + book_name + '\n\n---\n\n')
            sentence_set = book_to_sentence_set.get(book_name)
            for sentence in sentence_set:
                s1 = get_addr(sentence)
                s2 = get_time(sentence)
                s3 = get_mark(sentence)
                if s3 != '\n':
                    f.writelines('> ' + s3 + '\n')
                    f.writelines(s1 + ' ' + s2 + '\n\n---\n\n')
            f.close()


def main():
    kd = Kindle('source.txt')
    kd.convert()


if __name__ == '__main__':
    main()
