#!/usr/bin/env python2
# -*- encoding=utf-8 -*-
import csv
import sys
import Constants
import os
import pickle

reload(sys)
sys.setdefaultencoding('utf-8')


class Constants(object):
    path = os.path.dirname(Constants.__file__)

    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can't change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError('const name "%s" is not all uppercase' % name)
        self.__dict__[name] = value

    def create_top_scroll_list(self):
        filename = self.path + '/data/topscroll.csv'
        top_scroll_list = list()
        with open(filename, 'rU') as file:
            reader = csv.reader(file)
            for item in reader:
                top_scroll = unicode(item[0])
                top_scroll_list.append(top_scroll)

        pickle_name = self.path + '/data/topscroll.pkl'

        with open(pickle_name, 'w') as file:
            pickle.dump(top_scroll_list, file)
        print(top_scroll_list.__len__())
        return top_scroll_list

    def create_couplet_number_dict(self):
        couplet_number_dict = dict()
        couplet_number_list = list()
        filename = self.path + '/data/couplet_number.csv'
        with open(filename, 'rU') as file:
            reader = csv.reader(file)
            head = next(reader)
            for item in reader:
                (category, down_part, up_part, top_scroll, desc) = (unicode(it) for it in item)
                couplet = {'category': category, 'up_part': up_part, 'down_part': down_part,
                           'top_scroll': top_scroll,
                           'desc': desc}
                couplet_number_list.append(couplet)
        category_list = sorted(set(couplet['category'] for couplet in couplet_number_list))
        print category_list
        for category in category_list:
            num_list = list()
            for couplet in couplet_number_list:
                if couplet['category'] == category:
                    num_list.append(couplet)
            couplet_number_dict.__setitem__(category, num_list)

        pickle_name = self.path + '/data/couplet_number.pkl'

        with open(pickle_name, 'w') as file:
            pickle.dump(couplet_number_dict, file)

        return couplet_number_dict

    def create_couplet_zodiac_dict(self):
        couplet_zodiac_dict = dict()
        couplet_zodiac_list = list()
        filename = self.path + '/data/couplet_zodiac.csv'
        with open(filename, 'rU') as file:
            reader = csv.reader(file)
            next(reader)
            for item in reader:
                (category, down_part, up_part, top_scroll, desc) = (unicode(it) for it in item)
                couplet = {'category': category, 'up_part': up_part, 'down_part': down_part,
                           'top_scroll': top_scroll,
                           'desc': desc}
                couplet_zodiac_list.append(couplet)
        category_list = sorted(set(couplet['category'] for couplet in couplet_zodiac_list))
        print category_list
        for category in category_list:
            num_list = list()
            for couplet in couplet_zodiac_list:
                if couplet['category'] == category:
                    num_list.append(couplet)
            couplet_zodiac_dict.__setitem__(category, num_list)

        pickle_name = self.path + '/data/couplet_zodiac.pkl'

        with open(pickle_name, 'w') as file:
            pickle.dump(couplet_zodiac_dict, file)

        return couplet_zodiac_dict

    '''
    [
        {'category': '4', 
         'down_part': u'',
         'up_part': u'', 
         'top_scroll': u'', 
         'desc': u''}
     ...]
    '''

    def get_couplet_number_dict(self):
        pickle_name = self.path + '/data/couplet_number.pkl'
        with open(pickle_name, 'r') as file:
            couplet_number_dict = pickle.load(file)

        return couplet_number_dict

    def get_couplet_zodiac_dict(self):
        pickle_name = self.path + '/data/couplet_zodiac.pkl'
        with open(pickle_name, 'r') as file:
            couplet_zodiac_dict = pickle.load(file)

        return couplet_zodiac_dict

    def get_couplet_topscroll_list(self):
        pickle_name = self.path + '/data/topscroll.pkl'
        with open(pickle_name, 'r') as file:
            topscroll_list = pickle.load(file)

        return topscroll_list


if __name__ == '__main__':
    contant = Constants()
    assert (contant.create_couplet_number_dict() == contant.get_couplet_number_dict())
    # assert (contant.create_couplet_zodiac_dict() == contant.get_couplet_zodiac_dict())
    # assert (contant.create_top_scroll_list() == contant.get_couplet_topscroll_list())
    pass
