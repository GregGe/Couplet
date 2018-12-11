#!/usr/bin/env python2
# -*- encoding=utf-8 -*-


import sys
from dueros.Bot import Bot
from dueros.directive.Display.RenderTemplate import RenderTemplate
from dueros.directive.Display.template.BodyTemplate1 import BodyTemplate1

reload(sys)
sys.setdefaultencoding('utf8')

class Test(Bot):

    def __init__(self, request_data):
        super(Test, self).__init__(request_data)
        self.add_launch_handler(self.launch_request)
        self.add_intent_handler('inquiry', self.getTaxSlot)

    def launch_request(self):
        """
        打开调用名
        """

        self.wait_answer()
        template = BodyTemplate1()
        template.set_title('查询个税')
        template.set_plain_text_content('欢迎进入查询个税')
        template.set_background_image('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1532350870263&di=c93edb2fb9a3cfe7a632acc46cceba62&imgtype=0&src=http%3A%2F%2Ffile25.mafengwo.net%2FM00%2F0A%2FAC%2FwKgB4lMC26CAWsKoAALb5778DWg60.rbook_comment.w1024.jpeg')
        template.set_token('0c71de96-15d2-4e79-b97e-e52cec25c254')
        renderTemplate = RenderTemplate(template)
        return {
            'directives': [renderTemplate],
            'outputSpeech': r'欢迎进入查询个税，请告诉我你所在的城市是哪里呢'
        }

    def getTaxSlot(self):
        """
        获取槽位及逻辑处理
        """
        num = self.get_slots('sys.number')
        city = self.get_slots('sys.city')
        if num and not city:
            self.nlu.ask('sys.city')
            renderTemplate = self.getTemplate(r'你所在的城市是哪里呢')

            return {
                'directives': [renderTemplate],
                'reprompt': r'你所在的城市是哪里呢',
                'outputSpeech': r'你所在的城市是哪里呢'
            }

        if city and not num:
            self.nlu.ask('sys.number')
            renderTemplate = self.getTemplate(r'你的税前工资是多少呢')

            return {
                'directives': [renderTemplate],
                'reprompt': r'你的税前工资是多少呢',
                'outputSpeech': r'你的税前工资是多少呢'
            }

        taxNum = self.computeType(num, city)
        content = r'你需要缴纳' + str(taxNum)
        renderTemplate = self.getTemplate(content)
        return {
            'directives': [renderTemplate],
            'outputSpeech': content
        }

    def getTemplate(self, content):
        template = BodyTemplate1()
        template.set_title('查询个税')
        template.set_plain_text_content(content)
        template.set_background_image('https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1532350870263&di=c93edb2fb9a3cfe7a632acc46cceba62&imgtype=0&src=http%3A%2F%2Ffile25.mafengwo.net%2FM00%2F0A%2FAC%2FwKgB4lMC26CAWsKoAALb5778DWg60.rbook_comment.w1024.jpeg')
        template.set_token('0c71de96-15d2-4e79-b97e-e52cec25c254')
        renderTemplate = RenderTemplate(template)
        return renderTemplate

    def computeType(self, num, city):
        '''
        调用接口计算个税
        '''
        return 100


def handler(event, context):

    bot = Test(event)
    result = bot.run()
    return result
