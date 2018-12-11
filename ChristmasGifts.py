# !/usr/bin/env python2
# -*- encoding=utf-8 -*-

import sys

from dueros.Bot import Bot
from dueros.directive.AudioPlayer.Stop import Stop
from dueros.directive.Display.Hint import Hint
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1
from dueros.directive.Display.template.BodyTemplate3 import BodyTemplate3
from gifts.Utils import Utils

reload(sys)
sys.setdefaultencoding('utf8')


class ChristmasGifts(Bot):
    TITLE = '动物声音'
    WELCOM_TIPS = '欢迎进入动物声音的世界'
    ICON_URL = 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/icon.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-30T02%3A40%3A14Z%2F-1%2F%2F573d10b151236982db06300eb1764f47368870dd555cd350bf859bdfc644bbe3'

    test = "http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/3_bear-%E7%86%8A.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A10%3A40Z%2F-1%2F%2Fec6487fb69ad9d93cdcbf02f95483a74cbb9d6ca29e8ad1038b9b5dea8f52440"

    def __init__(self, request_data):
        super(AnimalSounds, self).__init__(request_data)
        self.add_launch_handler(self.launch_request)
        self.add_intent_handler('play_animal_sounds', self.handleAnimalSlots)
        self.add_intent_handler('change_another_sounds', self.handleNextAnimalSounds)
        self.add_intent_handler('random_play_sounds', self.handleRandomAnimalSounds)
        self.add_session_ended_handler(self.end_request)

    def launch_request(self):
        """
        打开调用名
        """

        self.wait_answer()
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content(self.WELCOM_TIPS)
        template.set_background_image(self.ICON_URL)
        renderTemplate = RenderTemplate(template)

        hints = self.getHints()
        outputSpeech = r'你可以对我说播放猫的叫声？'

        return self.getResponse(outputSpeech, renderTemplate, hints, outputSpeech)

    def end_request(self):
        """
        清空状态，结束会话
        """
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content(self.WELCOM_TIPS)
        template.set_background_image(self.ICON_URL)
        renderTemplate = RenderTemplate(template)

        outputSpeech = r'期待下次与您见面，再见！'

        stop = Stop()

        return {
            'directives': [stop],
            'outputSpeech': outputSpeech
        }

    def handleAnimalSlots(self):
        name = self.get_slots('animal')
        if name:
            animal = Utils.getAnimal(name)
            if animal:
                self.set_session_attribute('name', animal['name'], None)
                return self.getAnimalResponse(animal)
            else:
                return self.askWhichAnimal()

        else:
            return self.askWhichAnimal()

    def handleNextAnimalSounds(self):
        name = self.get_session_attribute('name', None)
        animal = Utils.getNextAnimal(name)
        return self.getAnimalResponse(animal)

    def handleRandomAnimalSounds(self):
        animal = Utils.getRandomAnimal()
        return self.getAnimalResponse(animal)

    def askWhichAnimal(self):
        self.nlu.ask('animal')

        content = r'请问您想听什么动物的声音呢？'
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content(content)
        template.set_background_image(self.ICON_URL)
        renderTemplate = RenderTemplate(template)

        return self.getResponse(content, renderTemplate, self.getHints())

    def getAnimalResponse(self, animal):
        self.set_expect_speech(True)
        self.wait_answer()
        #self.nlu.ask('animal')

        name = Utils.getName(animal)
        content = Utils.getDescribtion(animal)
        imgUrl = Utils.getImageUrl(animal)
        soundUrl = Utils.getSoundUrl(animal)

        self.set_session_attribute('name', name, None)

        template = BodyTemplate3()
        template.set_title(name)
        template.set_plain_content(content)
        template.set_image(imgUrl)
        template.set_background_image(imgUrl)

        renderTemplate = RenderTemplate(template)

        outputSpeech = '<speak>%s<audio src="%s"></audio>请问您还想听什么动物的声音呢？</speak>' % (name, soundUrl)
        reprompt = '请问您还想听什么动物的声音呢？'
        return {
            'directives': [renderTemplate],
            'reprompt': reprompt,
            'outputSpeech': outputSpeech
        }

    def getHints(self, hasPrefix=False):
        animals = Utils.getRandomAnimalList()
        tips = list()
        for animal in animals:
            tip = "播放%s的叫声" % Utils.getName(animal)
            if hasPrefix:
                tip = "小度小度," + tip
            tips.append(tip)
        hint = Hint(tips)
        return hint

    def getResponse(self, content, renderTemplate, hint=None, outputSpeech=None):
        directives = list()
        directives.append(renderTemplate)
        if hint:
            directives.append(hint)

        return {
            'directives': directives,
            'reprompt': content,
            'outputSpeech': outputSpeech if outputSpeech else content
        }


def handler(event, context):
    bot = ChristmasGifts(event)
    result = bot.run()
    return result
