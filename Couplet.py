#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

import sys
import random

from couplet.Utils import Utils
from dueros.Bot import Bot
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1

reload(sys)
sys.setdefaultencoding('utf8')


class Couplet(Bot):
    TITLE = '春节对联'
    ICON_URL = 'http://dbp-resource.gz.bcebos.com/22d37bcb-410f-8bec-b723-069e9190a7be/icon.png?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-12-27T02%3A58%3A13Z%2F-1%2F%2Fcd829a46ebffb8f25529a59cf7e3c598d2f87105d11067e91d6329fd8fa989b6'
    BACKGROUD_URL = 'http://dbp-resource.gz.bcebos.com/22d37bcb-410f-8bec-b723-069e9190a7be/background.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-12-27T02%3A58%3A11Z%2F-1%2F%2F465de55f33380ca1b949093c6a1ccad004e62194303b5e2b2e723b115c60ed6f'

    common_dialog = ['7个字包含中华的对联',
                     '包含中华的对联',
                     '包含中华的7个字的对联',
                     '35个字的对联',
                     '猪年的对联',
                     '猪年的包含财富的春联',
                     ]

    utils = Utils()

    def __init__(self, request_data):
        super(Couplet, self).__init__(request_data)
        self.add_launch_handler(self.launch_request)
        self.add_intent_handler('couplet', self.couplet_intent)
        self.add_intent_handler('next_step', self.next_step_intent)
        self.add_intent_handler('ai.dueros.common.default_intent', self.ai_dueros_common_default_intent_intent)
        self.add_session_ended_handler(self.end_request)

    def couplet_intent(self):
        self.wait_answer()
        zodiac = self.get_slots('zodiac')
        couplet_size = self.get_slots('couplet_size')
        word_size = self.get_slots('word_size')
        couplet_content = self.get_slots('sys.wildcard-slot')
        couplet = self.get_slots('couplet')

        foot = u'你可以对我说:小度小度，' + random.choice(self.common_dialog)
        if couplet:
            couplet_list, find_content = self.utils.get_couplet(zodiac, couplet_content, word_size, couplet_size)

            if couplet_content and not find_content:
                head = u'没有找到包含%s的对联，为您推荐：\n'
            else:
                head = ''

            content, outputSpeech = self.get_ssml_content(couplet_list, head, foot)
        else:
            content = foot
            outputSpeech = content
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content(content)
        template.set_background_image(self.BACKGROUD_URL)
        renderTemplate = RenderTemplate(template)

        return self.getResponse(content, renderTemplate, outputSpeech)

    def next_step_intent(self):
        self.wait_answer()
        couplet_list = self.utils.get_random_couplet()
        foot = u'你可以对我说' + random.choice(self.common_dialog)
        content, outputSpeech = self.get_ssml_content(couplet_list, '', foot)
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content(content)
        template.set_background_image(self.BACKGROUD_URL)
        renderTemplate = RenderTemplate(template)

        return self.getResponse(content, renderTemplate, outputSpeech)

    def ai_dueros_common_default_intent_intent(self):
        self.wait_answer()
        query = self.request.get_query()
        # self.utils.save_user_query(query)
        couplet_list, find_content = self.utils.get_couplet(None, query, None, 3)
        foot = u'你可以对我说: 小度小度' + random.choice(self.common_dialog)
        if couplet_list.__len__() > 0:
            content, outputSpeech = self.get_ssml_content(couplet_list, '', foot)
        else:
            content = foot
            outputSpeech = content
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content(content)
        template.set_background_image(self.BACKGROUD_URL)
        renderTemplate = RenderTemplate(template)
        return self.getResponse(content, renderTemplate, outputSpeech)

    def launch_request(self):
        """
        打开调用名
        """
        self.wait_answer()
        content = '欢迎进入新春对联，您可以这样对我说，猪年的对联'
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content(content)
        template.set_background_image(self.BACKGROUD_URL)
        renderTemplate = RenderTemplate(template)

        return self.getResponse(content, renderTemplate, content)

    def end_request(self):
        """
        清空状态，结束会话
        """
        content = r'您得到了想要的春联了吗？推荐您使用技能动物声音，聆听各种萌萌哒的声音哦'
        self.wait_answer()
        template = BodyTemplate1()
        template.set_title(self.TITLE)
        template.set_plain_text_content("")
        template.set_background_image(self.ICON_URL)
        renderTemplate = RenderTemplate(template)

        return self.getResponse(content, renderTemplate)

    def getResponse(self, content, renderTemplate, outputSpeech=None):
        return {
            'directives': [renderTemplate],
            'reprompt': content,
            'outputSpeech': outputSpeech if outputSpeech else content
        }

    def get_ssml_content(self, couplet_list, head, foot=None):
        if couplet_list.__len__() > 0:
            content = ''
            outputSpeech = ''
            for item in couplet_list:
                content += item['up_part'] + '\n'
                content += item['down_part'] + '\n'
                content += '\n'

                outputSpeech += u'<silence time="1ms"></silence>%s<silence time="500ms"></silence>%s' % (
                    item['up_part'], item['down_part'])

            if foot:
                outputSpeech = u'<speak>%s%s<silence time="3ms"></silence>%s</speak>' % (head, outputSpeech, foot)
            else:
                outputSpeech = u'<speak>%s%s</speak>' % (head, outputSpeech)
        else:
            content = ''
            outputSpeech = ''
        return content, outputSpeech


def handler(event, context):
    bot = Couplet(event)
    result = bot.run()
    return result
