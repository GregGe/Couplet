#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

import Constants
import random


class Utils:
    '''
    @:return animal = {{'name': 'name', 'desc': 'desc', 'img': 'img', 'sound': 'sound'}}
    '''

    @staticmethod
    def getAnimal(name):
        return Constants.ANIMALS.get(name)

    @staticmethod
    def getNextAnimal(name):
        if not name:
            name = u'35种经典动物合集'
            index = Constants.ANIMALS.keys().index(name)
        else:
            index = Constants.ANIMALS.keys().index(name)
            index = (index + 1) % Constants.ANIMALS.keys().__len__()
        return Constants.ANIMALS.get(Constants.ANIMALS.keys().__getitem__(index))

    @staticmethod
    def getRandomAnimal():
        # index = random.randint(0, Constants.ANIMALS.keys().__len__() - 1)
        # return Constants.ANIMALS.get(Constants.ANIMALS.keys().__getitem__(index))
        return random.choice(Constants.ANIMALS.values())

    @staticmethod
    def getRandomAnimalList(len=3):
        return random.sample(Constants.ANIMALS.values(), len)

    @staticmethod
    def getName(animal):
        return animal['name']

    @staticmethod
    def getDescribtion(animal):
        return animal['desc']

    @staticmethod
    def getImageUrl(animal):
        return animal['img']

    @staticmethod
    def getSoundUrl(animal):
        return animal['sound']


if __name__ == '__main__':
    animal = Utils.getAnimal(u'猫')
    print(animal['name'])
    for i in range(1, Constants.ANIMALS.keys().__len__()):
        animal = Utils.getNextAnimal(animal['name'])
        print(animal['name'])

    # for i in range(1, Constants.ANIMALS.keys().__len__()):
    #     animal = Utils.getRandomAnimal()
    #     #print(animal['name'])
    #
    # for i in range(1, 10):
    #     animals = Utils.getRandomAnimalList()
    #     print(i)
    #     for a in animals:
    #         print(a['name'])

    pass
