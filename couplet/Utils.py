#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

import random
import pickle
import os
import Utils
from Constants import Constants


class Utils:
    path = os.path.dirname(Utils.__file__)
    constants = Constants()

    couplet_number_dict = constants.get_couplet_number_dict()
    couplet_zodiac_dict = constants.get_couplet_zodiac_dict()
    topscroll_list = constants.get_couplet_topscroll_list()

    def get_couplet(self, zodiac, content, word_size=0, num=1):
        find_content = False
        num = self.modify_couplet_size(num)
        couplet_list = []
        if zodiac:
            try:
                zodiac_list = self.couplet_zodiac_dict[zodiac]
                if content:
                    for couplet in zodiac_list:
                        if content in couplet['down_part'] or content in couplet['up_part']:
                            couplet_list.append(couplet)
                        if couplet_list.__len__() >= num:
                            break
            except:
                zodiac_list = self.couplet_zodiac_dict[random.choice(self.couplet_zodiac_dict.keys())]
            if couplet_list.__len__() == 0:
                if num >= zodiac_list.__len__():
                    couplet_list = zodiac_list
                else:
                    couplet_list = random.sample(zodiac_list, num)
            else:
                find_content = True
        elif word_size:
            try:
                number_list = self.couplet_number_dict[word_size]
                if content:
                    for couplet in number_list:
                        if content in couplet['down_part'] or content in couplet['up_part']:
                            couplet_list.append(couplet)

                        if couplet_list.__len__() >= num:
                            break
            except:
                number_list = self.couplet_number_dict[random.choice(self.couplet_number_dict.keys())]
            if couplet_list.__len__() == 0:
                if num >= number_list.__len__():
                    couplet_list = number_list
                else:
                    couplet_list = random.sample(number_list, num)
            else:
                find_content = True
        elif content:
            for number_list in self.couplet_number_dict.values():
                for couplet in number_list:
                    if content in couplet['down_part'] or content in couplet['up_part']:
                        couplet_list.append(couplet)
                    if couplet_list.__len__() >= num:
                        break
            if couplet_list.__len__() > 0:
                find_content = True

        return couplet_list, find_content

    def get_random_couplet(self, num=1):
        couplet_number_value = self.couplet_number_dict[random.choice(self.couplet_number_dict.keys())]
        if num >= couplet_number_value.__len__():
            couplet_list = couplet_number_value
        else:
            couplet_list = random.sample(couplet_number_value, num)

        return couplet_list

    def modify_couplet_size(self, num):
        if num:
            try:
                num = int(num)
                if num > 10:
                    num = 10
            except:
                num = 1
        else:
            num = 1
        return num

    def create_user_query(self):
        pickle_name = self.path + '/data/query.pkl'
        query_list = []
        query_list.append("query")
        with open(pickle_name, 'w') as write_file:
            pickle.dump(query_list, write_file)

    def save_user_query(self, query):
        pickle_name = self.path + '/data/query.pkl'
        with open(pickle_name, 'r') as read_file:
            query_list = pickle.load(read_file)
            if query_list:
                query_list.append(query)
            else:
                query_list = []
                query_list.append(query)
        with open(pickle_name, 'w') as write_file:
            pickle.dump(query_list, write_file)


if __name__ == '__main__':
    utils = Utils()
    utils.create_user_query()
    couplet_list, find_content = utils.get_couplet('神', '中华', '', 55)
    print find_content
    for couplet in couplet_list:
        print('category:%s, up_part:%s, down_part:%s, top_scroll:%s, desc:%s' % (
            couplet['category'], couplet['up_part'], couplet['down_part'], couplet['top_scroll'], couplet['desc']))
    pass
