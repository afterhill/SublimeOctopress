# -*- coding: utf-8 -*-
import os.path


class Pinyin(object):

    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Mandarin.dat')

    def __init__(self):
        self.dict = {}
        for line in open(self.data_path):
            k, v = line.split('\t')
            self.dict[k] = v

    def get_pinyin(self, chars=u'', splitter='-'):
        result = []
        non_hanzi_builder = ''
        non_hanzi_flag = 0
        i = 0
        for char in chars:
            i = i + 1
            try:
                key = "%X" % ord(char)
                if self.dict[key]:
                    if non_hanzi_flag == 1:
                        result.append(non_hanzi_builder)
                        non_hanzi_flag = 0
                        non_hanzi_builder = ''
                result.append(self.dict[key].split(" ")[0].strip()[:-1]
                    .lower())

            except:
                non_hanzi_builder = non_hanzi_builder + char
                non_hanzi_flag = 1
                if char == ' ':
                    if non_hanzi_builder[:-1] != '':
                        result.append(non_hanzi_builder[:-1])
                    non_hanzi_flag = 0
                    non_hanzi_builder = ''
                elif i == chars.__len__():
                    result.append(non_hanzi_builder)
                    non_hanzi_flag = 0
                    non_hanzi_builder = ''

        return splitter.join(result)
