#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

import sys

from dueros.Bot import Bot
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1
from dueros.directive.Display.template.BodyTemplate3 import BodyTemplate3
from dueros.directive.AudioPlayer.Play import Play
from dueros.directive.AudioPlayer.PlayBehaviorEnum import PlayBehaviorEnum
from dueros.directive.AudioPlayer.StreamFormatEnum import StreamFormatEnum
from dueros.directive.AudioPlayer.PlayerInfo import PlayerInfo
from dueros.directive.AudioPlayer.Control.PlayPauseButton import PlayPauseButton
from dueros.directive.AudioPlayer.Control.PreviousButton import PreviousButton
from dueros.directive.AudioPlayer.Control.NextButton import NextButton
from Utils import Utils

reload(sys)
sys.setdefaultencoding('utf8')


class AnimalSounds(Bot):
    TITLE = '动物声音'
    WELCOM_TIPS = '欢迎聆听动物声音'
    ICON_URL = 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/icon.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-30T02%3A40%3A14Z%2F-1%2F%2F573d10b151236982db06300eb1764f47368870dd555cd350bf859bdfc644bbe3'

    def __init__(self, request_data):
        super(AnimalSounds, self).__init__(request_data)
        self.add_launch_handler(self.launch_request)
        self.add_intent_handler('play_animal_sounds', self.handleAnimalSlots)
        self.add_intent_handler('change_another_sounds', self.handleNextAnimalSounds)
        self.add_intent_handler('random_play_sounds', self.handleRandomAnimalSounds)
        self.add_event_listener('AudioPlayer.PlaybackFinished', self.palybackSound)
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

        outputSpeech = r'欢迎聆听动物声音，请告诉我您想听什么动物的叫声呢？'

        return self.getResponse(outputSpeech, renderTemplate, outputSpeech)

    def end_request(self):
        """
        清空状态，结束会话
        """

        self.wait_answer()
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content(self.WELCOM_TIPS)
        template.set_background_image(self.ICON_URL)
        renderTemplate = RenderTemplate(template)

        outputSpeech = r'期待下次与您见面，再见！'

        return self.getResponse(outputSpeech, renderTemplate, outputSpeech)

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

        return self.getResponse(content, renderTemplate)

    def palybackSound(self):
        self.nlu.ask('animal')

        content = r'请问您还想听什么动物的声音呢？'
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content(content)
        template.set_background_image(self.ICON_URL)
        renderTemplate = RenderTemplate(template)

        return self.getResponse(content, renderTemplate)

    def getAnimalResponse(self, animal):
        name = Utils.getName(animal)
        content = Utils.getDescribtion(animal)
        imgUrl = Utils.getImageUrl(animal)
        soundUrl = Utils.getSoundUrl(animal)

        self.set_session_attribute('name', name, None)

        play = Play(soundUrl, PlayBehaviorEnum.REPLACE_ALL)

        playerInfo = PlayerInfo()

        playpause = PlayPauseButton()
        previous = PreviousButton()
        next = NextButton()

        previous.set_selected(True)

        controls = [previous, playpause, next]
        playerInfo.set_controls(controls)
        playerInfo.set_title(name)
        playerInfo.set_title_subtext1(content)
        playerInfo.set_art(imgUrl)
        play.set_player_info(playerInfo)

        template = BodyTemplate3()
        template.set_title(name)
        template.set_plain_content(content)
        template.set_image(Utils.getImageUrl(animal))
        template.set_background_image(Utils.getImageUrl(animal))

        renderTemplate = RenderTemplate(template)
        outputSpeech = name

        return {
            'directives': [play],
            'reprompt': content,
            'outputSpeech': outputSpeech
        }

    def getResponse(self, content, renderTemplate, outputSpeech=None):
        return {
            'directives': [renderTemplate],
            'reprompt': content,
            'outputSpeech': outputSpeech if outputSpeech else content
        }


def handler(event, context):
    bot = AnimalSounds(event)
    result = bot.run()
    return result
