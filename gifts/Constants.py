#!/usr/bin/env python2
# -*- encoding=utf-8 -*-

# description:
# author:jack
# create_time: 2018/4/15

"""
    desc:pass
"""
import csv


class _Constants(object):
    ANIMALS = {u'\u6bcd\u9e21': {
        'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/40_hen%E6%AF%8D%E9%B8%A1.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A49Z%2F-1%2F%2Fadbe18a3bb12453af64037c9982cfd610b7b1a30f577d8ffcbf98f372a469aa6',
        'name': u'\u6bcd\u9e21',
        'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/41_geese%E9%B9%85.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2Fc241827652926a5ffcc0678feeb2b33915af169a85cfee6b3b49bf1cf9105dc9',
        'desc': u'\u6bcd\u9e21\uff0c\u4e00\u79cd\u5bb6\u79bd\uff0c\u5934\u5c0f\uff0c\u773c\u692d\u5706\uff0c\u5634\u5c16\u4e14\u786c\uff0c\u6bdb\u591a\u800c\u5bc6\u53c8\u957f\uff0c\u6545\u53c8\u540d\u5706\u6bdb\u6bcd\u9e21\uff0c\u5f00\u98df\u8fdf\uff0c\u91c7\u98df\u6162'},
        u'\u6885\u82b1\u9e7f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/60_SikaDeer%E6%A2%85%E8%8A%B1%E9%B9%BF.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A12Z%2F-1%2F%2Fb391636425cb1a7c8b1144637e6e4a23d4163f558d2c0b8d8a2399a61b10a0e2',
            'name': u'\u6885\u82b1\u9e7f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/60_SikaDeer%E6%A2%85%E8%8A%B1%E9%B9%BF.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A16Z%2F-1%2F%2F3e10beac87acf17bbb616c0d681c1d32b47c05be1e64f2cbaeaa19ce9e059440',
            'desc': u'\u9e7f\u7684\u4e00\u79cd\uff0c\u590f\u5b63\u6bdb\u6817\u7ea2\u8272\uff0c\u80cc\u90e8\u6709\u767d\u6591\uff0c\u51ac\u5b63\u6bdb\u53d8\u6210\u68d5\u9ec4\u8272\uff0c\u767d\u6591\u53d8\u5f97\u4e0d\u660e\u663e\u3002\u56db\u80a2\u7ec6\u800c\u5f3a\u58ee\uff0c\u5584\u8dd1\u3002\u96c4\u9e7f\u6709\u89d2\uff0c\u521d\u751f\u7684\u89d2\u53eb\u9e7f\u8338\uff0c\u53ef\u5165\u836f\u3002'},
        u'\u706b\u70c8\u9e1f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/98_Flamingo%E7%81%AB%E7%83%88%E9%B8%9F.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A29Z%2F-1%2F%2F0173d711465ec33f02a332f5590a3cf85718e82e3a99c3022382e3672986895f',
            'name': u'\u706b\u70c8\u9e1f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/98_Flamingo%E7%81%AB%E7%83%88%E9%B8%9F.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2F48a8275a968e64416abe5d99620565d9354854e39a1818b19ff991c5544d84c4',
            'desc': u'\u9e1f\uff0c\u5916\u5f62\u50cf\u9e64\uff0c\u5634\u5f2f\u66f2\uff0c\u9888\u90e8\u5f88\u957f\uff0c\u7fbd\u6bdb\u767d\u8272\u5fae\u7ea2\uff0c\u8dbe\u95f4\u6709\u8e7c\u3002\u5403\u9c7c\u3001\u86e4\u870a\u3001\u6606\u866b\u548c\u6c34\u8349\u7b49\u3002\u591a\u751f\u6d3b\u5728\u5730\u4e2d\u6d77\u6cbf\u5cb8\u3002'},
        u'\u7ef5\u7f8a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/31_sheep%E7%BB%B5%E7%BE%8A.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A44Z%2F-1%2F%2F9f1d64ad73986056e3bcaeeff0f7d72198b4502d1d389b6b9ce798ffd86bf495',
            'name': u'\u7ef5\u7f8a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/31_sheep%E7%BB%B5%E7%BE%8A.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A56Z%2F-1%2F%2F6c221d897cc704dcdd919a542e8493e3e6048245a81fc0a47dc23f7c0a70dd3b',
            'desc': u'\u7f8a\u7684\u4e00\u79cd\uff0c\u516c\u7f8a\u591a\u6709\u87ba\u65cb\u72b6\u5927\u89d2\uff0c\u6bcd\u7f8a\u89d2\u7ec6\u5c0f\u6216\u65e0\u89d2\uff0c\u53e3\u543b\u957f\uff0c\u56db\u80a2\u77ed\uff0c\u8dbe\u6709\u8e44\uff0c\u5c3e\u80a5\u5927\uff0c\u6bdb\u767d\u8272\uff0c\u957f\u800c\u5377\u66f2\u3002\u6027\u6e29\u987a\u3002\u53d8\u79cd\u5f88\u591a\uff0c\u6709\u7070\u9ed1\u7b49\u989c\u8272\u3002\u6bdb\u662f\u7eba\u7ec7\u54c1\u7684\u91cd\u8981\u539f\u6599\uff0c\u76ae\u53ef\u5236\u9769\u3002'},
        u'\u72ee\u5b50': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/23_lion%E7%8B%AE%E5%AD%90.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A38Z%2F-1%2F%2Fed142fc28cc2b181150a0770063222e83f5faac847bfb10bcf5bb4ccc3e798c7',
            'name': u'\u72ee\u5b50',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/23_lion%E7%8B%AE%E5%AD%90.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A56Z%2F-1%2F%2Fa48bc6291f7daa577600c7409e288c1e5c93f7636c9423f99a2bd0a82c5503ad',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u8eab\u4f53\u957f\u7ea63\u7c73\uff0c\u56db\u80a2\u5f3a\u58ee\uff0c\u6709\u94a9\u722a\uff0c\u638c\u90e8\u6709\u8089\u5757\uff0c\u5c3e\u5df4\u7ec6\u957f\uff0c\u672b\u7aef\u6709\u4e00\u4e1b\u6bdb\uff0c\u96c4\u72ee\u7684\u9888\u90e8\u6709\u957f\u9b23\uff0c\u5168\u8eab\u6bdb\u68d5\u9ec4\u8272\u3002\u751f\u6d3b\u5728\u975e\u6d32\u548c\u4e9a\u6d32\u897f\u90e8\u3002\u6355\u98df\u7f9a\u7f8a\u3001\u6591\u9a6c\u7b49\u52a8\u7269\uff0c\u543c\u58f0\u5f88\u5927\uff0c\u6709\u201c\u517d\u738b\u201d\u4e4b\u79f0\u3002'},
        u'\u8725\u8734': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/66_lizard%E8%9C%A5%E8%9C%B4.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A15Z%2F-1%2F%2F966ce0fe39bf8625e6dfef3e99f1c1c8f136b38f4eb5044c795a1fa6c1300c98',
            'name': u'\u8725\u8734',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/66_lizard%E8%9C%A5%E8%9C%B4.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A17Z%2F-1%2F%2F0698acb25bb7e69680456f9f6a518ee487fccc52e71a2e850e036fd3acad4f24',
            'desc': u'\u722c\u884c\u52a8\u7269\uff0c\u8eab\u4f53\u8868\u9762\u6709\u7ec6\u5c0f\u9cde\u7247\uff0c\u591a\u6570\u6709\u56db\u80a2\uff0c\u5c3e\u5df4\u7ec6\u957f\uff0c\u4e3a\u8ff7\u60d1\u654c\u5bb3\uff0c\u53ef\u81ea\u884c\u65ad\u6389\u3002\u96c4\u7684\u80cc\u9762\u9752\u7eff\u8272\uff0c\u6709\u9ed1\u8272\u76f4\u7eb9\u6570\u6761\uff0c\u96cc\u7684\u80cc\u9762\u6de1\u8910\u8272\uff0c\u4e24\u4fa7\u5404\u6709\u9ed1\u8272\u76f4\u7eb9\u4e00\u6761\uff0c\u8179\u9762\u90fd\u5448\u6de1\u9ec4\u8272\u3002\u751f\u6d3b\u5728\u8349\u4e1b\u4e2d\uff0c\u6355\u98df\u6606\u866b\u548c\u5176\u4ed6\u5c0f\u52a8\u7269\u3002\u4e5f\u53eb\u56db\u811a\u86c7\u3002'},
        u'\u6591\u9a6c': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/37_zebra%E6%96%91%E9%A9%AC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A48Z%2F-1%2F%2Fba065734dbe59b8d4b27f7aa8665f08933bfb400006407c9dadd4abe86c5cf74',
            'name': u'\u6591\u9a6c',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/37_zebra%E6%96%91%E9%A9%AC.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2Fd434107912073199dd3ee9bfc6246e8d624b07723414ab4f9af82e875d3c69dc',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5f62\u72b6\u50cf\u9a6c\uff0c\u5168\u8eab\u7684\u6bdb\u6de1\u9ec4\u8272\u548c\u9ed1\u8272\u6761\u7eb9\u76f8\u95f4\uff0c\u542c\u89c9\u7075\u654f\u3002\u4ea7\u5728\u975e\u6d32\uff0c\u662f\u73cd\u8d35\u7684\u89c2\u8d4f\u52a8\u7269\u3002'},
        u'\u5c0f\u6d63\u718a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/84_littleraccoon%E5%B0%8F%E6%B5%A3%E7%86%8A.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A23Z%2F-1%2F%2F7a4dfb1fa8f4cadd921e06c7c12822573de237aca3c19ce511be0d5865c8ce1a',
            'name': u'\u5c0f\u6d63\u718a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/84_littleraccoon%E5%B0%8F%E6%B5%A3%E7%86%8A.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A19Z%2F-1%2F%2F04134f20966737e2a77f3c10430eeed39bfce144f6a9d54c2cf5fd6f005472ad',
            'desc': u'\u56e0\u5176\u98df\u524d\u8981\u5c06\u98df\u7269\u5728\u6c34\u4e2d\u6d17\u6fef\uff0c\u6545\u540d\u6d63\u718a\u3002\u773c\u775b\u5468\u56f4\u4e3a\u9ed1\u8272\uff0c\u5c3e\u67095-6\u4e2a\u9ed1\u8272\u73af\u7eb9\uff0c\u4f53\u957f65\u81f375\u5398\u7c73\uff0c\u5c3e\u957f\u7ea625\u5398\u7c73\uff0c\u76ae\u6bdb\u7684\u5927\u90e8\u5206\u4e3a\u7070\u8272\uff0c\u4e5f\u6709\u90e8\u5206\u4e3a\u68d5\u8272\u548c\u9ed1\u8272\u3002\u4e5f\u6709\u7f55\u89c1\u7684\u767d\u5316\u79cd\u3002'},
        u'\u8774\u8776': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/114_Butterfly-%E8%9D%B4%E8%9D%B6.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A11Z%2F-1%2F%2F7d52e0daed12777af8f573b84ab39d203330f30a3fc7600c57ddf4d6ae04919a',
            'name': u'\u8774\u8776',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/114_Butterfly-%E8%9D%B4%E8%9D%B6.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2Fd18c1df40f5f7aac647c38f955909876b38226ab6d35f9eed8fa7f91c1c05e8b',
            'desc': u'\u6606\u866b\uff0c\u7fc5\u8180\u9614\u5927\uff0c\u989c\u8272\u7f8e\u4e3d\uff0c\u9759\u6b62\u65f6\u56db\u7fc5\u7ad6\u7acb\u5728\u80cc\u90e8\uff0c\u8179\u90e8\u7626\u957f\u3002 \u5438\u82b1\u871c\u3002\u79cd\u7c7b\u5f88\u591a\uff0c\u6709\u7684\u5e7c\u866b\u5403\u519c\u4f5c\u7269\uff0c\u662f\u5bb3\u866b\uff0c\u6709\u7684\u5e7c\u866b\u5403\u869c\u866b\uff0c\u662f\u76ca\u866b\u3002\u7b80\u79f0\u8776\u3002'},
        u'\u6d77\u9f9f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/85_turtle%E6%B5%B7%E9%BE%9F.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A23Z%2F-1%2F%2Fdc63d27a97544770bdbd7efbf8e3f4c3dff2f60d0a54c4f711518c0a2664005c',
            'name': u'\u6d77\u9f9f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/85_turtle%E6%B5%B7%E9%BE%9F.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A19Z%2F-1%2F%2F5f3590c45cd6a9f3b57e073531d8495dfb58776ad6c7e0f030ea81af516e61ae',
            'desc': u'\u722c\u884c\u52a8\u7269\u3002\u5916\u5f62\u548c\u666e\u901a\u9f9f\u76f8\u4f3c\uff0c\u4f53\u5927\uff0c\u4e0a\u988c\u5e73\u51fa\uff0c\u4e0b\u988c\u7565\u5411\u4e0a\u94a9\u66f2\uff0c\u989a\u7f18\u6709\u952f\u9f7f\u72b6\u7f3a\u523b\u3002\u80cc\u7532\u6a44\u6984\u8272\u6216\u68d5\u8910\u8272\uff0c\u8179\u7532\u9ec4\u8272\u3002\u56db\u80a2\u5448\u9ccd\u72b6\u3002\u4ee5\u9c7c\u3001\u867e\u53ca\u6d77\u85fb\u4e3a\u98df\u3002\u5e7f\u5e03\u4e8e\u5927\u897f\u6d0b\u3001\u592a\u5e73\u6d0b\u548c\u5370\u5ea6\u6d0b\u8fd1\u6d77\u4e0a\u5c42\u3002'},
        u'\u6731\u9e6d': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/21_ibis%E6%9C%B1%E9%B9%AD.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A37Z%2F-1%2F%2Ffaeaf9e0cb2858bb39d76ca9555ca871304851e2f1e917ffab517a293681b339',
            'name': u'\u6731\u9e6d',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/21_ibis%E6%9C%B1%E9%B9%AD.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A55Z%2F-1%2F%2F4d6438822f6e88fc1fbbfc7ce4b5d8869d100f6117642a4b2eae9ebf9f96c6cd',
            'desc': u'\u53c8\u79f0\u6731_\u3002 \u6d89\u79bd\u7c7b\uff0c\u4f53\u5f62\u5982\u9e64\uff0c\u800c\u7fbd\u8272\u6de1\u7ea2\uff0c\u5634\u4e0e\u811a\u4ea6\u5448\u6de1\u7ea2\u8272\u3002'},
        u'\u5b54\u96c0': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/27_peacock%E5%AD%94%E9%9B%80.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A41Z%2F-1%2F%2F81bee4b8dc9f7503275390beba12d91fbb89c64475dad9ee44b86bc65eb6fbec',
            'name': u'\u5b54\u96c0',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/27_peacock%E5%AD%94%E9%9B%80.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A56Z%2F-1%2F%2F87e7d1c196fad23edd76ef1d4b8b534fc43c56c30986d89fcf866d7845a72370',
            'desc': u'\u9e1f\uff0c\u5934\u4e0a\u6709\u7fbd\u51a0\uff0c\u96c4\u7684\u5c3e\u5df4\u7684\u7fbd\u6bdb\u5f88\u957f\uff0c\u989c\u8272\u7eda\u4e3d\uff0c\u5c55\u5f00\u65f6\u50cf\u6247\u5b50\u3002 \u5e38\u89c1\u7684\u6709\u7eff\u5b54\u96c0\u548c\u767d\u5b54\u96c0\u4e24\u79cd\u3002\u6210\u7fa4\u5c45\u4f4f\u5728\u70ed\u5e26\u68ee\u6797\u4e2d\u6216\u6cb3\u5cb8\u8fb9\uff0c\u5403\u8c37\u7c7b\u548c\u679c\u5b9e\u7b49\u3002\u591a\u9972\u517b\u6765\u4f9b\u89c2\u8d4f\u3002'},
        u'\u7eba\u7ec7\u5a18': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/118_katydid-%E7%BA%BA%E7%BB%87%E5%A8%98.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A13Z%2F-1%2F%2F65036e6cd3ed22400d09b80cf06c97ed6e3bf5d98d160235428cf3150cbfdf17',
            'name': u'\u7eba\u7ec7\u5a18',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/118_katydid-%E7%BA%BA%E7%BB%87%E5%A8%98.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2F7171adce32d40a97cf18017bfb2a049ad6c8b694de78ddc45f5a839e48aa12c0',
            'desc': u'\u8eab\u4f53\u7eff\u8272\u6216\u9ec4\u8910\u8272\uff0c\u5934\u5c0f\uff0c\u89e6\u89d2\u7ec6\u957f\uff0c\u5403\u98df\u74dc\u7c7b\u82b1\u6735\u3001\u74dc\u7a70\u7b49\u3002\u96c4\u866b\u524d\u7fc5\u90e8\u6709\u53d1\u58f0\u5668\u5b98\uff0c\u9e23\u58f0\u201c\u8f67\u7ec7\u3001\u8f67\u7ec7\u201d\uff0c\u4f3c\u7eba\u8f66\u7eba\u7eb1\u4e4b\u58f0\u3002'},
        u'\u9e35\u9e1f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/110_ostrich%E9%B8%B5%E9%B8%9F.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A09Z%2F-1%2F%2Ffbb9bcce5dcc16d5103d9beab1aa6c7103b04a934e2215e3e955fdea9891253c',
            'name': u'\u9e35\u9e1f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/110_ostrich%E9%B8%B5%E9%B8%9F.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2Fa59355cf8056625cc6df7c858f5ec06b4ce501c64a52808eb4a710e8e7ab08be',
            'desc': u'\u9e1f\uff0c\u662f\u73b0\u4ee3\u9e1f\u7c7b\u4e2d\u4f53\u5f62\u6700\u5927\u7684\uff0c\u9ad8\u53ef\u8fbe3\u7c73\uff0c\u9888\u957f\uff0c\u5934\u5c0f\uff0c\u5634\u6241\u5e73\uff0c\u7ffc\u77ed\u5c0f\uff0c\u4e0d\u80fd\u98de\uff0c\u817f\u957f\uff0c\u811a\u6709\u529b\uff0c\u5584\u8d70\u3002\u96cc\u9e1f\u7070\u8910\u8272\uff0c\u96c4\u9e1f\u7684\u7ffc\u548c\u5c3e\u90e8\u6709\u767d\u8272\u7fbd\u6bdb\u3002\u751f\u6d3b\u5728\u975e\u6d32\u7684\u8349\u539f\u548c\u6c99\u6f20\u5730\u5e26\u3002'},
        u'\u86c7': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/32_snake%E8%9B%87.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A45Z%2F-1%2F%2F94183305414369c8b398dba3f62e696b87ba0799645df1f9445a0654b1b1e637',
            'name': u'\u86c7',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/32_snake%E8%9B%87.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2Fb5486bf34ffada808b9486c4b6120f63f725f54b13897a7a6f1ff14a3ae40571',
            'desc': u'\u722c\u884c\u52a8\u7269\uff0c\u8eab\u4f53\u5706\u800c\u7ec6\u957f\uff0c\u6709\u9cde\uff0c\u6ca1\u6709\u56db\u80a2\u3002\u79cd\u7c7b\u5f88\u591a\uff0c\u6709\u7684\u6709\u6bd2\u3002\u5403\u9752\u86d9\u7b49\u5c0f\u52a8\u7269\uff0c\u5927\u86c7\u4e5f\u80fd\u541e\u98df\u5927\u7684\u517d\u7c7b\u3002'},
        u'\u9ec4\u8702': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/35_wasp%E9%BB%84%E8%9C%82.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A47Z%2F-1%2F%2F0c614a43b6408620c77432350a252c7736063fd2d811711708f243a385d597c3',
            'name': u'\u9ec4\u8702',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/35_wasp%E9%BB%84%E8%9C%82.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2F12f853b8d31afec603edb9b810c362f5552c5bcadaddcae677bb6a4de1e83463',
            'desc': u'\u8bb8\u591a\u6709\u7fc5\u7684\u819c\u7fc5\u76ee\u6606\u866b\u7684\u4e00\u79cd\uff0c\u901a\u5e38\u6709\u4e00\u4e2a\u7ec6\u957f\u3001\u5149\u6ed1\u7684\u8eab\u4f53\uff0c\u9760\u4e00\u4e2a\u7ec6\u67c4\u4e0e\u8179\u90e8\u76f8\u8fde\uff0c\u6709\u53d1\u80b2\u5b8c\u6574\u7684\u7fc5\uff0c\u56bc\u5438\u5f0f\u53e3\u5668\uff0c'},
        u'\u5929\u725b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/119_longhornbeetle-%E5%A4%A9%E7%89%9B.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A14Z%2F-1%2F%2Fd0685ca3660c73d62244c2b71e1a50381e6482e4fd49f8dcfd71d0c7d02dd77b',
            'name': u'\u5929\u725b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/119_longhornbeetle-%E5%A4%A9%E7%89%9B.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2F0f8b046ce6187c3c28d1786657010b1c9084d56394efc25a41602dbca5f8dc98',
            'desc': u'\u6606\u866b\u3002\u79cd\u7c7b\u5f88\u591a\u3002\u6210\u866b\u5927\u5c0f\u3001\u5f62\u72b6\u3001\u989c\u8272\u56e0\u79cd\u7c7b\u800c\u5f02\uff0c\u4e00\u822c\u4e3a\u957f\u692d\u5706\u5f62\uff0c\u89e6\u89d2\u8f83\u8eab\u4f53\u957f\u3002\u5e7c\u866b\u9ec4\u767d\u8272\uff0c\u6241\u957f\u5706\u7b52\u5f62\u3002\u86c0\u98df\u6811\u6728\u679d\u5e72\uff0c\u6545\u53c8\u540d\u952f\u6811\u90ce\u3002\u4e3a\u68ee\u6797\u3001\u6851\u6811\u548c\u679c\u6811\u7684\u91cd\u8981\u5bb3\u866b\u3002\u5e38\u89c1\u7684\u5982\u661f\u5929\u725b\u3001\u6851\u5929\u725b\u7b49\u3002'},
        u'\u58c1\u864e': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/47_walllizard%E5%A3%81%E8%99%8E.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A54Z%2F-1%2F%2F596898939373868bc30364d4072c0224146c2dc4301bda5bc5377cfa8633be2d',
            'name': u'\u58c1\u864e',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/47_walllizard%E5%A3%81%E8%99%8E.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A58Z%2F-1%2F%2Fb0662085329f9c221229e6ce2d9ee3082910c6abd4efc9fd56cc5babb341ff29',
            'desc': u'\u722c\u884c\u52a8\u7269\uff0c\u8eab\u4f53\u6241\u5e73\uff0c\u56db\u80a2\u77ed\uff0c\u8dbe\u7aef\u6269\u5c55\uff0c\u6709\u9ecf\u9644\u80fd\u529b\uff0c\u80fd\u5728\u58c1\u4e0a\u722c\u884c\u3002 \u5403\u868a\u3001\u8747\u3001\u86fe\u7b49\u5c0f\u6606\u866b\uff0c\u5bf9\u4eba\u7c7b\u6709\u76ca\u3002\u4e5f\u53eb\u874e\u864e\u3002\u65e7\u79f0\u5b88\u5bab\u3002'},
        u'\u7caa\u91d1\u9f9f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/115_dorbeetle-%E7%B2%AA%E9%87%91%E9%BE%9F.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A11Z%2F-1%2F%2F7ef72d22e20d35c235ebd0f722b788d893cd2abd9916760d3aa5416b7318f752',
            'name': u'\u7caa\u91d1\u9f9f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/115_dorbeetle-%E7%B2%AA%E9%87%91%E9%BE%9F.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2F5a1c43b55e39ba2a40b7bbdf51464a6d4b78326adf3819393aa81086d563026f',
            'desc': u'\u4fd7\u79f0\u5c4e\u58f3\u90ce\uff0c\u5927\u591a\u90fd\u5177\u6709\u7caa\u98df\u6027\uff0c\u53ef\u4ee5\u5c06\u7caa\u4fbf\u6eda\u52a8\u6210\u7403\u72b6\uff0c\u63a8\u884c\u5411\u524d\u3002\u5176\u4e3b\u8981\u4ee5\u52a8\u7269\u7caa\u4fbf\u4e3a\u98df\u3002'},
        u'\u72d7': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/9_dog%E7%8B%97.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A16Z%2F-1%2F%2Fca7151762f4370d6d6a4a97b1506826f5ce7bb4d59cdd0947a35d1c54617da6e',
            'name': u'\u72d7',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/9_dog%E7%8B%97.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A54Z%2F-1%2F%2F9a99b32213fbb66b337d4a5af6a6ed961d4c2c3cfbe3d368227ef78b938ce29c',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u79cd\u7c7b\u5f88\u591a\uff0c\u55c5\u89c9\u548c\u542c\u89c9\u90fd\u5f88\u7075\u654f\uff0c\u820c\u957f\u800c\u8584\uff0c\u53ef\u6563\u70ed\uff0c\u6bdb\u6709\u9ec4\u3001\u767d\u3001\u9ed1\u7b49\u989c\u8272\u3002'},
        u'\u7f8a\u9a7c': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/63_alpaca%E7%BE%8A%E9%A9%BC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A13Z%2F-1%2F%2Fea5fd51eb0a20b527e654f82888c108b13bc9b6fb03412b708ea2239939ca5a2',
            'name': u'\u7f8a\u9a7c',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/63_alpaca%E7%BE%8A%E9%A9%BC.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A17Z%2F-1%2F%2Fdb4e5b8905e415f051664f09c0a4408ea8c6a4758414384135fcf9385571b2ea',
            'desc': u'\u7f8a\u9a7c\u4e3a\u5076\u8e44\u76ee\u3001\u9a86\u9a7c\u79d1\u7684\u52a8\u7269\uff0c\u4f53\u91cd55-65\u5343\u514b\uff0c\u5934\u4f53\u957f\u5ea61200-2250\u6beb\u7c73\u3002\u5916\u5f62\u6709\u70b9\u50cf\u7ef5\u7f8a\uff0c\u4e00\u822c\u6816\u606f\u4e8e\u6d77\u62d44000\u7c73\u7684\u9ad8\u539f\u3002'},
        u'\u82cd\u8747': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/12_fly%E8%8B%8D%E8%9D%87.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A22Z%2F-1%2F%2Fb47b5d9c6b1a6c6be682519d179b9cf70ef6bae011aecf1a03f77121ff9eecbd',
            'name': u'\u82cd\u8747',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/12_fly%E8%8B%8D%E8%9D%87.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A54Z%2F-1%2F%2F88db975e0b8064c8c40ec73d951baabafd5b123a948cdb83bdac4f61d4df6b91',
            'desc': u'\u6606\u866b\u3002 \u79cd\u7c7b\u5f88\u591a\uff0c\u901a\u5e38\u6307\u5bb6\u8747\u3002\u5934\u90e8\u6709\u4e00\u5bf9\u590d\u773c\u3002\u5e7c\u866b\u53eb\u86c6\u3002\u6210\u866b\u80fd\u4f20\u64ad\u970d\u4e71\u3001\u4f24\u5bd2\u3001\u75e2\u75be\u7b49\u591a\u79cd\u75be\u75c5\u3002'},
        u'\u9ec4\u9f20\u72fc': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/73_Weasel%E9%BB%84%E9%BC%A0%E7%8B%BC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A18Z%2F-1%2F%2F17ff3417d05649bd2507d4e88ab4d2391d15d3c36846605f05ad7f8febab576b',
            'name': u'\u9ec4\u9f20\u72fc',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/73_Weasel%E9%BB%84%E9%BC%A0%E7%8B%BC.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2F22d0251005ff89b30df561bb40289d6cc015137372547b4fec816ce797f765c3',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u8eab\u4f53\u7ec6\u957f\uff0c\u56db\u80a2\u77ed\uff0c\u5c3e\u84ec\u677e\uff0c\u80cc\u90e8\u68d5\u7070\u8272\u3002\u663c\u4f0f\u591c\u51fa\uff0c\u4e3b\u8981\u6355\u98df\u9f20\u7c7b\uff0c\u6709\u65f6\u4e5f\u5403\u5bb6\u79bd\u3002\u5c3e\u6bdb\u53ef\u5236\u6bdb\u7b14\u3002'},
        u'\u516b\u54e5': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/106_starling%E5%85%AB%E5%93%A5.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A07Z%2F-1%2F%2F853227e70fe418acc7e7fb70e3aac3fc782df5cad2f6fb2bf7bc6840e9a6dda9',
            'name': u'\u516b\u54e5',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/106_starling%E5%85%AB%E5%93%A5.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A47Z%2F-1%2F%2F22352bb79b917f4a74a8686a1758f3f1ddb1b8f54a70638e574debdc00b635b8',
            'desc': u'\u4e5f\u53eb\u9e32\u9e46\u3002\u9e1f\u7c7b\u3002\u7fbd\u6bdb\u9ed1\u800c\u6709\u5149\u6cfd\uff0c\u5599\u548c\u8db3\u9ec4\u8272\u3002\u7ffc\u4e0a\u6709\u767d\u6591\uff0c\u98de\u65f6\u663e\u9732\uff0c\u5448\u516b\u5b57\u5f62\uff0c\u6545\u540d\u3002\u96c4\u9e1f\u5584\u9e23\uff0c\u7ecf\u8bad\u7ec3\u80fd\u53d1\u51fa\u7c7b\u4f3c\u4eba\u8bf4\u8bdd\u7684\u58f0\u97f3\u3002'},
        u'\u516c\u9e21': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/30_rooster%E5%85%AC%E9%B8%A1.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A46Z%2F-1%2F%2Fd2b5aa719ad711b11e56d861ec7a885a364c51c8ba2e68236e2332db6b28a83c',
            'name': u'\u516c\u9e21',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/30_rooster%E5%85%AC%E9%B8%A1.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A56Z%2F-1%2F%2F7db7793004e40cccaa921719437894f606d99da3e8de6086922363cae8df1d57',
            'desc': u'\u516c\u9e21\uff0c\u5bb6\u79bd\uff0c\u54c1\u79cd\u5f88\u591a\uff0c\u7fc5\u8180\u77ed\uff0c\u4e0d\u80fd\u9ad8\u98de\uff1b\u557c\u80fd\u62a5\u6653\u3002\u516c\u9e21\u662f\u6cd5\u56fd\u7684\u56fd\u9e1f \uff0c\u539f\u56e0\u662f\u7531\u4e8e\u5b83\u90a3\u82f1\u52c7\u3001\u987d\u5f3a\u3001\u597d\u6597\u7684\u6027\u683c\u3002'},
        u'\u9a86\u9a7c': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/52_camel%E9%AA%86%E9%A9%BC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A08Z%2F-1%2F%2F8ac09f65a203c60a543e7e5fd76e33b6408b5bdee93b51f0479e6cb5ef89a01d',
            'name': u'\u9a86\u9a7c',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/52_camel%E9%AA%86%E9%A9%BC.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A15Z%2F-1%2F%2F2770ebd1bc6ef33517bf24c92cbdece0e8813363a75c7482fa8de7fa87f899a4',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u53cd\u520d\u7c7b\uff0c\u8eab\u4f53\u9ad8\u5927\uff0c\u5934\u5c0f\u9888\u957f\uff0c\u80cc\u4e0a\u6709\u9a7c\u5cf0\uff0c\u8e44\u6241\u5e73\uff0c\u8e44\u5e95\u6709\u8089\u8d28\u7684\u57ab\uff0c\u9002\u4e8e\u5728\u6c99\u6f20\u4e2d\u884c\u8d70\u3002\u6709\u53cc\u91cd\u773c\u7751\uff0c\u4e0d\u6015\u98ce\u6c99\u3002\u6709\u9ad8\u5ea6\u8010\u9965\u6e34\u7684\u80fd\u529b\u3002\u55c5\u89c9\u7075\u654f\uff0c\u80fd\u55c5\u51fa\u8fdc\u5904\u7684\u6c34\u6e90\uff0c\u53c8\u80fd\u9884\u611f\u5927\u98ce\u7684\u5230\u6765\u3002\u4f9b\u9a91\u4e58\u6216\u8fd0\u8d27\uff0c\u662f\u6c99\u6f20\u5730\u533a\u4e3b\u8981\u7684\u529b\u755c\u3002'},
        u'\u9a6c': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/20_house%E9%A9%AC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A35Z%2F-1%2F%2F7f38dc0bb2db6651e7a88cfbe23b8976f7ad5b7467d4a9cd377e8b6ac6fcaa47',
            'name': u'\u9a6c',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/20_house%E9%A9%AC.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A55Z%2F-1%2F%2F5e867b5d97915f57624818004c469c9ef242138c0f1b13d48768e3adde2d2f81',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5934\u5c0f\uff0c\u9762\u90e8\u957f\uff0c\u8033\u58f3\u76f4\u7acb\uff0c\u9888\u90e8\u6709\u9b23\uff0c\u56db\u80a2\u5f3a\u5065\uff0c\u6bcf\u80a2\u5404\u6709\u4e00\u8e44\uff0c\u5584\u8dd1\uff0c\u5c3e\u751f\u6709\u957f\u6bdb\u3002\u662f\u91cd\u8981\u7684\u529b\u755c\u4e4b\u4e00\uff0c\u53ef\u4f9b\u62c9\u8f66\u3001\u8015\u5730\u3001\u4e58\u9a91\u7b49\u7528\u3002\u76ae\u53ef\u5236\u9769\u3002'},
        u'\u9e70': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/67_Eagle%E9%B9%B0.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A15Z%2F-1%2F%2F3b23b3dae148dc61fa302dfbab2be7ff80dd1fe983cdd0ca76c896717760a99f',
            'name': u'\u9e70',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/67_Eagle%E9%B9%B0.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A17Z%2F-1%2F%2F07e00b7b1f7af6e3a5af2c5ed2ccc10baa6d7071084bd7b02eb41fb7c9347fb9',
            'desc': u'\u9e1f\uff0c\u4e0a\u5634\u5448\u94a9\u5f62\uff0c\u9888\u77ed\uff0c\u811a\u90e8\u6709\u957f\u6bdb\uff0c\u8db3\u8dbe\u6709\u957f\u800c\u9510\u5229\u7684\u722a\u3002\u662f\u731b\u79bd\uff0c\u6355\u98df\u5c0f\u517d\u53ca\u5176\u4ed6\u9e1f\u7c7b\u3002\u79cd\u7c7b\u5f88\u591a\uff0c\u5982\u82cd\u9e70\u3001\u96c0\u9e70\u3001\u8001\u9e70\u7b49\u3002'},
        u'\u9a74': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/42_donkey%E9%A9%B4.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A54Z%2F-1%2F%2F3478709a07d34a52152c5b2c48f853cae76771194a7ceaa0a9a343df14c872ff',
            'name': u'\u9a74',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/42_donkey%E9%A9%B4.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A58Z%2F-1%2F%2F11c66dfd517ac960e8c81b10612919f9efe3a22a67269e78b3a60af5391a9ccf',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u9a74\u7684\u5f62\u8c61\u4f3c\u9a6c\uff0c\u591a\u4e3a\u7070\u8910\u8272\uff0c\u4e0d\u5a01\u6b66\u96c4\u58ee\uff0c\u5b83\u7684\u5934\u5927\u8033\u957f\uff0c\u80f8\u90e8\u7a0d\u7a84\uff0c\u56db\u80a2\u7626\u5f31\uff0c\u8eaf\u5e72\u8f83\u77ed\uff0c\u56e0\u800c\u4f53\u9ad8\u548c\u8eab\u957f\u5927\u4f53\u76f8\u7b49\uff0c\u5448\u6b63\u65b9\u578b\u3002'},
        u'\u5927\u96c1': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/99_wildgoose%E5%A4%A7%E9%9B%81.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A29Z%2F-1%2F%2Fa993742b8af52d1de39c58138c793ae7eeb4615bedff3f7333bcd9634f6967f1',
            'name': u'\u5927\u96c1',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/99_wildgoose%E5%A4%A7%E9%9B%81.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2Fd771dbb17e64698cfbf615c462479cb992b47f0f77f986b3b9c1d9d9a0d3019c',
            'desc': u'\u9e1f\uff0c\u5634\u6241\u5e73\uff0c\u817f\u77ed\uff0c\u8dbe\u95f4\u6709\u8e7c\uff0c\u7fbd\u6bdb\u7d2b\u8910\u8272\uff0c\u8179\u90e8\u767d\u8272\uff0c\u6709\u9ed1\u8272\u6761\u72b6\u6a2a\u7eb9\u3002\u7fa4\u5c45\u5728\u6c34\u8fb9\uff0c\u5403\u690d\u7269\u79cd\u5b50\uff0c\u4e5f\u5403\u9c7c\u548c\u6606\u866b\u3002\u98de\u65f6\u4e00\u822c\u6392\u5217\u6210\u884c\uff0c\u662f\u4e00\u79cd\u51ac\u5019\u9e1f\u3002'},
        u'\u5929\u9e45': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/34_swan%E5%A4%A9%E9%B9%85.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A46Z%2F-1%2F%2Fd458cf654ada79148c5d431aa0f1687db96bdd3952dbf856d4ac0bd8c2ae6d3d',
            'name': u'\u5929\u9e45',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/34_swan%E5%A4%A9%E9%B9%85.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2F3143d7050710a2dde626e4a55e1e2ff8c41cfb18370d046dda545ac055fae935',
            'desc': u'\u9e1f\uff0c\u5916\u5f62\u50cf\u9e45\u800c\u8f83\u5927\uff0c\u5168\u8eab\u767d\u8272\uff0c\u811a\u548c\u5c3e\u90fd\u77ed\uff0c\u811a\u9ed1\u8272\uff0c\u6709\u8e7c\u3002\u751f\u6d3b\u5728\u6e56\u8fb9\u6216\u6cbc\u6cfd\u5730\u5e26\uff0c\u5584\u98de\uff0c\u5403\u690d\u7269\u3001\u6606\u866b\u7b49\u3002\u79cd\u7c7b\u8f83\u591a\uff0c\u5982\u5927\u5929\u9e45\u3001\u5c0f\u5929\u9e45\u3001\u75a3\u9f3b\u5929\u9e45\u3002\u4e5f\u53eb\u9e44\u3002'},
        u'\u8003\u62c9': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/82_koala%E8%80%83%E6%8B%89.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A22Z%2F-1%2F%2Fd2376592c308a9a64ae27ff52844e6c0fbf4b6334f96c81fc311056a28c54fef',
            'name': u'\u8003\u62c9',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/82_koala%E8%80%83%E6%8B%89.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A19Z%2F-1%2F%2F6f2930d3df80af79cea4fb2d7f0c763545f3b9666546d11b6273043141db8706',
            'desc': u'\u53c8\u79f0\u6811\u888b\u718a\uff0c\u4f53\u6001\u61a8\u539a\uff0c\u957f\u76f8\u9177\u4f3c\u5c0f\u718a\uff0c\u6709\u4e00\u8eab\u53c8\u539a\u53c8\u8f6f\u7684\u6d53\u5bc6\u7070\u8910\u8272\u77ed\u6bdb\uff0c\u80f8\u90e8\u3001\u8179\u90e8\u3001\u56db\u80a2\u5185\u4fa7\u548c\u5185\u8033\u76ae\u6bdb\u5448\u7070\u767d\u8272\u3002'},
        u'\u732b\u5934\u9e70': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/102_owl%E7%8C%AB%E5%A4%B4%E9%B9%B0.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A06Z%2F-1%2F%2Ff617c525adc0a4449ee6fc259d14c5daa6bed049157799012a9f5390408d0d98',
            'name': u'\u732b\u5934\u9e70',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/102_owl%E7%8C%AB%E5%A4%B4%E9%B9%B0.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A47Z%2F-1%2F%2F82ddb6f9dd60a520a0206b2e29e9bb9ebc3e83fd70d8ff2c28f03ed18fcb4856',
            'desc': u'\u9e1f\uff0c\u8eab\u4f53\u6de1\u8910\u8272\uff0c\u591a\u9ed1\u6591\uff0c\u5934\u90e8\u6709\u89d2\u72b6\u7684\u7fbd\u6bdb\uff0c\u773c\u775b\u5927\u800c\u5706\uff0c\u663c\u4f0f\u591c\u51fa\uff0c\u5403\u9f20\u3001\u9ebb\u96c0\u7b49\uff0c\u5bf9\u4eba\u7c7b\u6709\u76ca\u3002\u5e38\u5728\u6df1\u591c\u53d1\u51fa\u51c4\u5389\u7684\u53eb\u58f0\uff0c\u8ff7\u4fe1\u7684\u4eba\u8ba4\u4e3a\u662f\u4e00\u79cd\u4e0d\u5409\u7965\u7684\u9e1f\u3002\u6709\u7684\u5730\u533a\u53eb\u591c\u732b\u5b50\u3002'},
        u'\u72d0\u72f8': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/59_Fox%E7%8B%90%E7%8B%B8.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A12Z%2F-1%2F%2F7cc78f90b78bbb83c93ab32a0aef6bd013ce4f5784cf11050d862b5afb6d25c6',
            'name': u'\u72d0\u72f8',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/59_Fox%E7%8B%90%E7%8B%B8.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A16Z%2F-1%2F%2F4ca7016e0d15bae8fe3811be0edd2d32274dc2337f1ff8b49acca3dce5aa1918',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5916\u5f62\u7565\u50cf\u72fc\uff0c\u9762\u90e8\u8f83\u957f\uff0c\u8033\u6735\u4e09\u89d2\u5f62\uff0c\u5c3e\u5df4\u957f\uff0c\u6bdb\u901a\u5e38\u8d64\u9ec4\u8272\u3002\u6027\u72e1\u733e\u591a\u7591\uff0c\u663c\u4f0f\u591c\u51fa\uff0c\u5403\u91ce\u9f20\u3001\u9e1f\u7c7b\u3001\u5bb6\u79bd\u7b49\u3002\u5e38\u89c1\u7684\u6709\u8d64\u72d0\u548c\u6c99\u72d0\u3002'},
        u'\u718a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/3_bear-%E7%86%8A.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A28%3A59Z%2F-1%2F%2Fb204b8654cd23948e6b70fe839e60671983adb55e260b3c2a4d5f27129f1194c',
            'name': u'\u718a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/3_bear-%E7%86%8A.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A54Z%2F-1%2F%2Fa303028784b0d33e2b4394822e07dfbc775f49d96f9084523cf3a8e234a05fc3',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5934\u5927\uff0c\u5c3e\u5df4\u77ed\uff0c\u56db\u80a2\u77ed\u800c\u7c97\uff0c\u811a\u638c\u5927\uff0c\u8dbe\u7aef\u6709\u5e26\u94a9\u7684\u722a\uff0c\u80fd\u722c\u6811\u3002\u4e3b\u8981\u5403\u52a8\u7269\u6027\u98df\u7269\uff0c\u4e5f\u5403\u6c34\u679c\u3001\u575a\u679c\u7b49\u3002\u79cd\u7c7b\u5f88\u591a\uff0c\u5982\u68d5\u718a\u3001\u9a6c\u6765\u718a\u3001\u9ed1\u718a\u3002\u6709\u7684\u5730\u533a\u53eb\u718a\u778e\u5b50'},
        u'\u8001\u864e': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/50_tiger%E8%80%81%E8%99%8E.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A56Z%2F-1%2F%2F1aea1eb6db21a88cd2c442222d235cd29f41761852796e1992df24188eceefa1',
            'name': u'\u8001\u864e',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/50_tiger%E8%80%81%E8%99%8E.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A58Z%2F-1%2F%2F0c3d320f1ed1ce2f3062732916c1cf479a72e5470769207b4b4ee6b73c711653',
            'desc': u'\u864e\u662f\u79cd\u9ad8\u5ea6\u8fdb\u5316\u7684\u730e\u98df\u52a8\u7269\uff0c\u5e9e\u5927\u7684\u4f53\u578b\u4e0e\u6709\u529b\u808c\u8089\uff0c\u767d\u8272\u5230\u6a58\u7ea2\u8272\u7684\u6bdb\u76ae\u4e0a\u6709\u9ed1\u8272\u5782\u76f4\u7684\u6761\u7eb9\u3002'},
        u'\u8748\u8748': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/78_grasshopper%E8%9D%88%E8%9D%88.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A21Z%2F-1%2F%2F14702a36c52dcae58c28bf0e5ef13826736ff0e37b49871eb06c3951332cb365',
            'name': u'\u8748\u8748',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/78_grasshopper%E8%9D%88%E8%9D%88.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2F39216bd894ff5607401ed54df89e5134b689e3f732466ba7d4a5c328717d1b63',
            'desc': u'\u6606\u866b\u3002\u87bd\u65af\u7684\u4e00\u79cd\u3002\u7fc5\u77ed\uff0c\u8179\u5927\u3002\u96c4\u7684\u524d\u7fc5\u57fa\u90e8\u53ef\u6469\u64e6\u53d1\u58f0\u3002\u5403\u690d\u7269\u7684\u5ae9\u53f6\u548c\u82b1\uff0c\u5371\u5bb3\u519c\u4f5c\u7269\u3002'},
        u'\u9e8b\u9e7f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/64_elk%E9%BA%8B%E9%B9%BF.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A14Z%2F-1%2F%2F5c62e42fdd00d6ab1551dc7158294c232726685dcfad78ff1686c844ff4da84c',
            'name': u'\u9e8b\u9e7f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/64_elk%E9%BA%8B%E9%B9%BF.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A16Z%2F-1%2F%2F81cdbd439f0ec3533e5466b1c11d337652082538ba16f7ba9eacc4084977bf8e',
            'desc': u'\u4e5f\u53eb\u56db\u4e0d\u50cf\u3002\u54fa\u4e73\u52a8\u7269\u3002\u8fc7\u53bb\u8ba4\u4e3a\u5b83\u89d2\u4f3c\u9e7f\uff0c\u5934\u4f3c\u9a6c\uff0c\u4f53\u4f3c\u9a74\uff0c\u8e44\u4f3c\u725b\uff0c\u4f46\u53c8\u4e0d\u5168\u50cf\u4ee5\u4e0a\u56db\u79cd\u52a8\u7269\u4e2d\u7684\u4e00\u79cd\uff0c\u6545\u540d\u3002\u6bdb\u6de1\u8910\u8272\uff0c\u6027\u6e29\u9a6f\uff0c\u98df\u690d\u7269\u3002\u662f\u4e2d\u56fd\u7279\u6709\u73cd\u7a00\u52a8\u7269\u3002\u7531\u4e8e\u5386\u4ee3\u65e0\u8282\u5236\u5730\u730e\u6355\uff0c\u73b0\u5df2\u65e0\u91ce\u751f\u79cd\u3002'},
        u'\u957f\u9888\u9e7f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/14_giraffe%E9%95%BF%E9%A2%88%E9%B9%BF.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A25Z%2F-1%2F%2F94ac19ec71b1f1332aae169127793539948d1be55c80c87af891b22f443c987a',
            'name': u'\u957f\u9888\u9e7f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/14_giraffe%E9%95%BF%E9%A2%88%E9%B9%BF.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A55Z%2F-1%2F%2F2a596117aab90ab5edd48a0fe8a2db5ed4dfc4e0852cb9bc7b264730aa4316ee',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u9888\u5f88\u957f\uff0c\u96c4\u6027\u4f53\u9ad8\u7ea66\u7c73\uff0c\u662f\u9646\u5730\u4e0a\u6700\u9ad8\u7684\u52a8\u7269\u3002\u96cc\u96c4\u90fd\u6709\u4e00\u5bf9\u5c0f\u89d2\u3002\u773c\u5927\u800c\u7a81\u51fa\uff0c\u4f4d\u4e8e\u5934\u9876\u4e0a\u3002\u5168\u8eab\u6709\u68d5\u9ec4\u8272\u7f51\u72b6\u6591\u7eb9\u3002\u5954\u8dd1\u5f88\u5feb\u3002\u98df\u690d\u7269\u53f6\u3002\u4ea7\u4e8e\u975e\u6d32\u3002'},
        u'\u6d77\u8c61': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/91_walrus%E6%B5%B7%E8%B1%A1.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A26Z%2F-1%2F%2F04cd42bb22a4aaa0b3be80f7ece8096e1608e14f148448fad9e141516241cf3b',
            'name': u'\u6d77\u8c61',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/91_walrus%E6%B5%B7%E8%B1%A1.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2F27ec987ded7733a871ce3a989d3893bd91d92f047a63481ea86fab0d57bdf64d',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u8eab\u4f53\u7c97\u58ee\uff0c\u957f\u53ef\u8fbe3\u7c73\u591a\uff0c\u5934\u5706\uff0c\u773c\u5c0f\uff0c\u5634\u77ed\u800c\u9614\uff0c\u4e0a\u988c\u6709\u4e24\u4e2a\u7279\u522b\u957f\u7684\u7259\uff0c\u56db\u80a2\u5448\u9ccd\u72b6\u3002\u751f\u6d3b\u5728\u6d77\u6d0b\u4e2d\uff0c\u4e5f\u80fd\u5728\u9646\u5730\u4e0a\u884c\u52a8\uff0c\u5403\u8d1d\u7c7b\u7b49\u3002'},
        u'\u5544\u6728\u9e1f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/36_woodpecker%E5%95%84%E6%9C%A8%E9%B8%9F.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A47Z%2F-1%2F%2Fd786401df51acc8ca54c80d3e3a304f74fac61e174a1a90f43302b3f5e82ff28',
            'name': u'\u5544\u6728\u9e1f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/36_woodpecker%E5%95%84%E6%9C%A8%E9%B8%9F.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2F6ebb6af2f6f740b7f94343fb7d1e6c2f55007cab87b61ce5f5a96329cd07452d',
            'desc': u'\u9e1f\uff0c\u811a\u77ed\uff0c\u8dbe\u7aef\u6709\u9510\u5229\u7684\u722a\uff0c\u5584\u4e8e\u6500\u7f18\u6811\u6728\uff0c\u5634\u5c16\u800c\u76f4\uff0c\u80fd\u5544\u5f00\u6728\u5934\uff0c\u7528\u7ec6\u957f\u800c\u5c16\u7aef\u6709\u94a9\u7684\u820c\u5934\u6355\u98df\u6811\u6d1e\u91cc\u7684\u866b\uff0c\u5c3e\u7fbd\u7c97\u786c\uff0c\u5544\u6728\u65f6\u652f\u6491\u8eab\u4f53\u3002\u662f\u76ca\u9e1f\u3002'},
        u'\u87d1\u8782': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/113_cockroach-%E8%9F%91%E8%9E%82.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A11Z%2F-1%2F%2F155daa7729cf08c3a9cdfb8786e9377d9589fb0211cd52723838b2f6692f69d4',
            'name': u'\u87d1\u8782',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/113_cockroach-%E8%9F%91%E8%9E%82.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2F0ad0dde6f3cedd7945095a30e28c664e126f6f5968ed0554866d5454f77c243c',
            'desc': u'\u6606\u866b\uff0c\u8eab\u4f53\u6241\u5e73\uff0c\u9ed1\u8910\u8272\uff0c\u80fd\u53d1\u51fa\u81ed\u5473\u3002\u5e38\u54ac\u574f\u8863\u7269\uff0c\u6c61\u67d3\u98df\u7269\uff0c\u5e76\u80fd\u4f20\u67d3\u4f24\u5bd2\u3001\u970d\u4e71\u7b49\u75be\u75c5\uff0c\u662f\u5bb3\u866b\u3002\u79cd\u7c7b\u5f88\u591a\u3002\u4e5f\u53eb\u871a\u880a\u3002'},
        u'\u9cb8': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/86_whale%E9%B2%B8.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A24Z%2F-1%2F%2F6174508a9b2536513b6aa72ff30d68f7acb44b1d40f0e3c53aff6f0cf8a35e98',
            'name': u'\u9cb8',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/86_whale%E9%B2%B8.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A19Z%2F-1%2F%2F5e9736c2d462d742447b6dd29a236f0579aab213e64229fe5f1e5b3a53633de1',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u79cd\u7c7b\u5f88\u591a\uff0c\u751f\u6d3b\u5728\u6d77\u6d0b\u4e2d\uff0c\u80ce\u751f\uff0c\u5916\u5f62\u50cf\u9c7c\uff0c\u4f53\u957f\u53ef\u8fbe30\u591a\u7c73\uff0c\u662f\u73b0\u5728\u4e16\u754c\u4e0a\u6700\u5927\u7684\u4e00\u7c7b\u52a8\u7269\uff0c\u5934\u5927\uff0c\u773c\u5c0f\uff0c\u6ca1\u6709\u8033\u58f3\uff0c\u524d\u80a2\u5f62\u6210\u9ccd\uff0c\u540e\u80a2\u5b8c\u5168\u9000\u5316\uff0c\u5c3e\u5df4\u53d8\u6210\u5c3e\u9ccd\uff0c\u9f3b\u5b54\u5728\u5934\u7684\u4e0a\u90e8\uff0c\u7528\u80ba\u547c\u5438\u3002\u4fd7\u79f0\u9cb8\u9c7c\u3002'},
        u'\u5976\u725b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/8_cow%E5%A5%B6%E7%89%9B.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A14Z%2F-1%2F%2F65bdec2c5011621b83555e4752841010baf6d733f6e9c1a28fc7ebb880a0340a',
            'name': u'\u5976\u725b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/8_cow%E5%A5%B6%E7%89%9B.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A54Z%2F-1%2F%2Ffaf5dc7e6707ab713d57e98590751ca87420c3a7fa722006ea591fe25483a59e',
            'desc': u'\u5976\u725b\u662f\u4e73\u7528\u54c1\u79cd\u7684\u9ec4\u725b\uff0c\u7ecf\u8fc7\u9ad8\u5ea6\u9009\u80b2\u7e41\u6b96\u7684\u4f18\u826f\u54c1\u79cd\uff0c\u6211\u56fd\u7684\u5976\u725b\u4e3b\u8981\u4ee5\u9ed1\u767d\u82b1\u5976\u725b\u4e3a\u4e3b\u3002'},
        u'\u96ea\u8c82': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/92_ferret%E9%9B%AA%E8%B2%82.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A26Z%2F-1%2F%2F47a9cdd612c4f23b7d8b6a91b336eeffc389c0ec576abdc0a6ca8611efe04a3c',
            'name': u'\u96ea\u8c82',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/92_ferret%E9%9B%AA%E8%B2%82.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2Fd932dbf74007fc1817d97bd66211d09198e32a953eafc33de472f3afa5d91cb8',
            'desc': u'\u4e00\u79cd\u7279\u522b\u51f6\u6076\u7684\u8c82\uff0c\u662f\u5f88\u6709\u4ef7\u503c\u7684\u6355\u9f20\u8005\uff0c\u4e0e\u91ce\u751f\u7684\u6b27\u6d32\u9e21\u8c82\u975e\u5e38\u76f8\u4f3c\uff0c\u636e\u8bf4\u662f\u7531\u5bb6\u517b\u7684\u96ea\u8c82\u4e0e\u91ce\u751f\u7684\u9e21\u8c82\u6742\u4ea4\u4ea7\u751f\u7684\u3002'},
        u'\u91ce\u732a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/71_boar%E9%87%8E%E7%8C%AA.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A17Z%2F-1%2F%2F54fa297feeba6c9a14417d150d4185ac3936b10ffbde8f71a7e97633fcb044bb',
            'name': u'\u91ce\u732a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/71_boar%E9%87%8E%E7%8C%AA.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2F39d365aa830580a69446a6b29cf9b57059872a65ee7da0dcf6e36d3ed30adf95',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u4f53\u957f\u7ea61.2\u7c73\u3002\u4f53\u9762\u758f\u751f\u521a\u6bdb\uff0c\u9ed1\u8910\u8272\u3002\u72ac\u9f7f\u6781\u53d1\u8fbe\uff0c\u96c4\u7684\u6210\u5de8\u7259\u72b6\u3002\u543b\u90e8\u6bd4\u5bb6\u732a\u957f\u3002\u6027\u51f6\u66b4\u3002\u901a\u5e38\u591c\u51fa\u6398\u98df\u519c\u4f5c\u7269\u3002\u4e2d\u56fd\u5404\u5730\u5747\u4ea7\u3002'},
        u'\u53e9\u5934\u866b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/116_clickbeetle-%E5%8F%A9%E5%A4%B4%E8%99%AB.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A13Z%2F-1%2F%2F8d3c6d79daa2981dfecccafa87b977b1a68fe19d5ba55c9a1a8a892ed964191a',
            'name': u'\u53e9\u5934\u866b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/116_clickbeetle-%E5%8F%A9%E5%A4%B4%E8%99%AB.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2Fc7619b3d533450e490f834ca9bdf2aab7ed83949f6e90f84d79ec4afcdaf8f95',
            'desc': u'\u4f53\u7ec6\u957f\u800c\u7565\u6241\u5e73\uff0c\u957f\u7ea618\u6beb\u7c73\uff0c\u6d53\u6817\u8272\uff0c\u6709\u5149\u6cfd\uff0c\u5bc6\u88ab\u91d1\u9ec4\u8272\u77ed\u6bdb\u3002\u5934\u90e8\u6241\u5e73\uff0c\u5934\u9876\u6709\u4e09\u89d2\u51f9\u6d3c\uff0c\u5177\u590d\u773c\u4e00\u5bf9\u3002'},
        u'\u8749': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/74_cicada%E8%9D%89.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A19Z%2F-1%2F%2F2b4964bdad3ea93e76286776b7aef0ef05767b79cc4f5c8169fbd713444cb4ff',
            'name': u'\u8749',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/74_cicada%E8%9D%89.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2F2771ac6c459c9d1355044ed0f5864cd8420ba05f3ee824b6a14b9f49824f9e66',
            'desc': u'\u6606\u866b\uff0c\u79cd\u7c7b\u5f88\u591a\uff0c\u96c4\u7684\u8179\u90e8\u6709\u53d1\u97f3\u5668\uff0c\u80fd\u8fde\u7eed\u4e0d\u65ad\u53d1\u51fa\u5c16\u9510\u7684\u58f0\u97f3\u3002\u5e7c\u866b\u751f\u6d3b\u5728\u571f\u91cc\uff0c\u5438\u98df\u690d\u7269\u6839\u7684\u6c41\u6db2\u3002\u6210\u866b\u523a\u5438\u690d\u7269\u7684\u6c41\u3002'},
        u'\u9cc4\u9f9f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/55_crocodile%E9%B3%84%E9%B1%BC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A09Z%2F-1%2F%2F39ac5caa4074dea90be72b53a0b5ecab1e183168a0e3fdea0a7cd4cbdc407ab8',
            'name': u'\u9cc4\u9f9f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/55_crocodile%E9%B3%84%E9%B1%BC.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A16Z%2F-1%2F%2Fcb341767bcc3e002be454a570d8e0b0fc13f79f0c8744c3f515553328051d37a',
            'desc': u'\u9cc4\u9f9f\uff0c\u662f\u73b0\u5b58\u6700\u53e4\u8001\u7684\u722c\u884c\u52a8\u7269\uff0c\u4e16\u754c\u6700\u5927\u7684\u6de1\u6c34\u9f9f\u4e4b\u4e00\u3001\u6709\u6de1\u6c34\u52a8\u7269\u738b\u8005\u4e4b\u79f0\uff0c\u5206\u4e3a\u4e24\u5927\u79cd\u7c7b\uff0c\u4fd7\u79f0\u5927\u9cc4\u4e0e\u5c0f\u9cc4\u3002'},
        u'\u5927\u8c61': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/11_elephant%E5%A4%A7%E8%B1%A1.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A18Z%2F-1%2F%2F5c4b669f4b74e1ee3a50a3bb9676a3bd5e2535ce3a93c81863f911c2f13ce7ca',
            'name': u'\u5927\u8c61',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/11_elephant%E5%A4%A7%E8%B1%A1.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A54Z%2F-1%2F%2F79970cc177ed4c33e3986ae432ed08a13491da46154c4687228a3f6fff766916',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u662f\u9646\u5730\u4e0a\u73b0\u5b58\u6700\u5927\u7684\u52a8\u7269\uff0c\u8033\u6735\u5927\uff0c\u9f3b\u5b50\u957f\u5706\u7b52\u5f62\uff0c\u80fd\u8737\u66f2\uff0c\u591a\u6709\u4e00\u5bf9\u957f\u5927\u7684\u95e8\u7259\u4f38\u51fa\u53e3\u5916\uff0c\u5168\u8eab\u7684\u6bdb\u5f88\u7a00\u758f\uff0c\u76ae\u5f88\u539a\uff0c\u5403\u5ae9\u53f6\u548c\u91ce\u83dc\u7b49'},
        u'\u79c3\u9e6b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/68_vultures%E7%A7%83%E9%B9%AB.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A16Z%2F-1%2F%2F3c8146d9d66aed0cab871c920b8b8db64d5bfc1d262ea47ccd0b68187eecb186',
            'name': u'\u79c3\u9e6b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/68_vultures%E7%A7%83%E9%B9%AB.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A17Z%2F-1%2F%2F0143d35141b74c3aab5eae2ad77590afdc297c1e27a76e816d9d63395ca32812',
            'desc': u'\u9e1f\u7c7b\u3002\u5927\u578b\u731b\u79bd\u3002\u4f53\u957f\u7ea61.2\u7c73\u3002\u4f53\u7fbd\u4e3b\u8981\u5448\u9ed1\u8910\u8272\u3002\u5934\u88ab\u7ed2\u7fbd\uff0c\u9888\u540e\u6709\u90e8\u5206\u88f8\u79c3\uff0c\u6545\u540d\u3002\u6816\u606f\u9ad8\u5c71\uff0c\u55dc\u98df\u9e1f\u3001\u517d\u7b49\u7684\u5c38\u4f53\u3002\u7ec8\u5e74\u7559\u5c45\u4e2d\u56fd\u897f\u90e8\u5c71\u5730\u3002'},
        u'\u9ed1\u7329\u7329': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/7_chimpanzee%E9%BB%91%E7%8C%A9%E7%8C%A9.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A12Z%2F-1%2F%2Fd605ef7c453e3d5e0fcb404c11d785884fc6747d6f3fb7f2044b8f2a122a78dd',
            'name': u'\u9ed1\u7329\u7329',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/7_chimpanzee%E9%BB%91%E7%8C%A9%E7%8C%A9.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A53Z%2F-1%2F%2F854d75625789e3df1ba1b18700cc3e51e414c64e19c79b657ae970f02b6e9703',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u76f4\u7acb\u65f6\u9ad8\u53ef\u8fbe1.5\u7c73\uff0c\u6bdb\u9ed1\u8272\u3002\u5934\u8f83\u5706\uff0c\u9762\u90e8\u7070\u8910\u8272\uff0c\u65e0\u6bdb\u3002\u7709\u9aa8\u9ad8\u3002\u751f\u6d3b\u5728\u975e\u6d32\u68ee\u6797\u4e2d\uff0c\u7fa4\u5c45\u6811\u4e0a\uff0c\u6709\u7b51\u5de2\u4e60\u6027\uff0c\u98df\u91ce\u679c\u3001\u5c0f\u9e1f\u548c\u6606\u866b\u3002'},
        u'\u9b23\u72d7': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/56_Hyena%E9%AC%A3%E7%8B%97.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A10Z%2F-1%2F%2F7593ff04bbd356c441ccd380633b3027f5f0691a6446b46d020baca4c5d199eb',
            'name': u'\u9b23\u72d7',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/56_Hyena%E9%AC%A3%E7%8B%97.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A16Z%2F-1%2F%2F37eddf7bf4bd4c540b85fb57da86e42226f6994f9ba0de8739f4abd30995020b',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5916\u5f62\u7565\u50cf\u72d7\uff0c\u9888\u540e\u6709\u957f\u9b23\u6bdb\uff0c\u5934\u6bd4\u72d7\u7684\u5934\u77ed\u800c\u5706\uff0c\u989d\u90e8\u5bbd\uff0c\u5c3e\u5df4\u77ed\uff0c\u524d\u817f\u957f\uff0c\u540e\u817f\u77ed\uff0c\u6bdb\u68d5\u9ec4\u8272\u6216\u68d5\u8910\u8272\uff0c\u6709\u8bb8\u591a\u4e0d\u89c4\u5219\u7684\u9ed1\u8910\u8272\u6591\u70b9\u3002\u591a\u751f\u6d3b\u5728\u70ed\u5e26\u6216\u4e9a\u70ed\u5e26\u5730\u533a\uff0c\u5403\u517d\u7c7b\u5c38\u4f53\u8150\u70c2\u7684\u8089\u3002'},
        u'\u732b\u9f2c': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/24_meerkat%E7%8C%AB%E9%BC%AC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A39Z%2F-1%2F%2F85fa79438ceb9703097ca8df1bd9e775194f2f284a44e17adc508be55e7897d6',
            'name': u'\u732b\u9f2c',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/24_meerkat%E7%8C%AB%E9%BC%AC.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A56Z%2F-1%2F%2F5c764754f2cc68348698888ee6c4c0ef242eae022e9ad4c36e2b3c67d76c18aa',
            'desc': u'\u72d0_\uff0c\u5934\u5c3e\u957f42-60\u5398\u7c73\uff0c\u662f\u4e00\u79cd\u5c0f\u578b\u7684\u54fa\u4e73\u52a8\u7269\u3002\u4f53\u5f62\u7c97\u7b28\u3002\u56db\u80a2\u77ed\uff0c\u540e\u8db3\u4ec5\u51774\u8dbe\uff0c\u8dbe\u95f4\u6709\u8e7c\uff1b\u5c3e\u957f\u800c\u5706\uff0c\u7ea6\u4e3a\u4f53\u957f\u76842/3\uff0c\u4e0a\u88ab\u5c0f\u9cde\u7247\u53ca\u7a00\u758f\u7684\u6bdb\u3002\u80cc\u90e8\u6bdb\u8272\u9ed1\u8910\uff0c\u6742\u4ee5\u9ec4\u8272\u6bdb\u5c16\uff0c\u7ed2\u6bdb\u4e3a\u6df1\u5496\u5561\u8272\uff1b\u5c3e\u4e24\u8272\uff0c\u4e0a\u9762\u68d5\u9ed1\u8272\uff0c\u5c3e\u57fa\u90e8\u548c\u4e0b\u90e8\u4e3a\u6de1\u9ec4\u8272\u3002'},
        u'\u4e39\u9876\u9e64': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/103_RedCrownedCrane%E4%B8%B9%E9%A1%B6%E9%B9%A4.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A08Z%2F-1%2F%2F9bb6764d99a9f6ea742170614846b0f31e7ea278c6c0cd211d30092f28d92925',
            'name': u'\u4e39\u9876\u9e64',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/103_RedCrownedCrane%E4%B8%B9%E9%A1%B6%E9%B9%A4.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A47Z%2F-1%2F%2Feaaf54702da5bdf143a6469228f1504e466de201922319ba1eb114fb1114a3a8',
            'desc': u'\u4e5f\u53eb\u4ed9\u9e64\u3001\u767d \u9e64\u3002\u9e1f\u7c7b\u3002\u4f53\u957f\u57281.2\u7c73\u4ee5\u4e0a\u3002\u4f53\u7fbd\u4e3b\u8981\u4e3a\u767d\u8272\uff0c\u5589\u3001\u988a\u3001\u9888\u90e8\u6697\u8910\u8272\u3002\u5c3e\u77ed\uff0c\u5599\u3001\u9888\u548c\u8dd7_\u8f83\u957f\u3002\u5934\u9876 \u76ae\u80a4\u88f8\u9732\uff0c\u5448\u6731\u7ea2\u8272\u3002\u98de\u7fbd\u9ed1\u8272\u3002\u9e23\u58f0\u54cd\u4eae\uff0c\u98de\u7fd4\u529b\u5f3a\u3002\u4e3b\u4ea7\u4e8e\u4e2d\u56fd\u9ed1\u9f99\u6c5f\u7b49\u5730\u3002\u662f\u4e2d\u56fd\u56fd\u5bb6\u91cd\u70b9\u4fdd\u62a4 \u52a8\u7269\u3002'},
        u'\u6c34\u736d': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/87_otter%E6%B0%B4%E7%8D%AD.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A24Z%2F-1%2F%2Fa5d907cd54108c47c0917ce0cc2c6d856655f474dbadb18c36a0cf93742077ac',
            'name': u'\u6c34\u736d',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/87_otter%E6%B0%B4%E7%8D%AD.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A19Z%2F-1%2F%2F1f339be6dd31ab27ae3d7c2913c50f369f99c8bac825c54979653f4fd99d2c29',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u4f53\u957f\u7ea670\u5398\u7c73\u3002\u5934\u6241\uff0c\u8033\u5c0f\uff0c\u811a\u77ed\uff0c\u8dbe\u95f4\u6709\u8e7c\u3002\u6bdb\u77ed\u800c\u8f6f\u5bc6\uff0c\u80cc\u9762\u6df1\u8910\u8272\uff0c\u6709\u5149\u6cfd\u3002\u6816\u606f\u4e8e\u6c34\u8fb9\uff0c\u5584\u6e38\u6cf3\u3002\u901a\u5e38\u591c\u95f4\u6d3b\u52a8\u3002\u5206\u5e03\u4e8e\u4e2d\u56fd\u5357\u5317\u5404\u5730\u3002'},
        u'\u9e33\u9e2f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/88_Mandarinduck%E9%B8%B3%E9%B8%AF.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A24Z%2F-1%2F%2F0eef74d229afa34c7f4175c3ca9a032d54a79d46e00f9aece8b357b13c9022bd',
            'name': u'\u9e33\u9e2f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/88_Mandarinduck%E9%B8%B3%E9%B8%AF.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2Ffda39f60dac23bcf6eab7faa1dc4be6b5e370dac589281820b5d7b2b03f50f92',
            'desc': u'\u9e1f\uff0c\u5916\u5f62\u50cf\u91ce\u9e2d\u800c\u8f83\u5c0f\uff0c\u5634\u6241\uff0c\u9888\u957f\uff0c\u8dbe\u95f4\u6709\u8e7c\uff0c\u5584\u4e8e\u6e38\u6cf3\uff0c\u7fc5\u8180\u957f\uff0c\u80fd\u98de\u3002\u96c4\u9e1f\u6709\u5f69\u8272\u7fbd\u6bdb\uff0c\u5934\u540e\u6709\u94dc\u8d64\u3001\u7d2b\u3001\u7eff\u7b49\u8272\u7684\u957f\u51a0\u6bdb\uff0c\u5634\u7ea2\u8272\u3002\u96cc\u9e1f\u7fbd\u6bdb\u82cd\u8910\u8272\uff0c\u5634\u7070\u9ed1\u8272\uff0c\u96cc\u96c4\u591a\u6210\u5bf9\u751f\u6d3b\u5728\u6c34\u8fb9\u3002'},
        u'\u753b\u7709': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/107_thrush%E7%94%BB%E7%9C%89.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A08Z%2F-1%2F%2F6e283979381111beadc02f16163bdd268bf57c9c3daa3aa0ef6b00d999751082',
            'name': u'\u753b\u7709',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/107_thrush%E7%94%BB%E7%9C%89.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2F4806ae06accafa45daa05720d91ed085338ad8b803983ac7bf38e944f9953f8e',
            'desc': u'\u9e1f\u7c7b\u3002 \u80cc\u7fbd\u7eff\u8910\u8272\uff0c\u4e0b\u4f53\u9ec4\u8910\u8272\uff0c\u773c\u5708\u767d\u8272\uff0c\u5411\u540e\u5ef6\u4f38\u50cf\u5a25\u7709\u3002\u9e23\u58f0\u5a49\u8f6c\uff0c\u96c4\u9e1f\u597d\u6597\u3002\u5e38\u751f\u6d3b\u5728\u6811\u6797\u4e2d\uff0c\u4ee5\u6606\u866b\u548c\u690d\u7269\u79cd\u5b50\u4e3a\u98df\u3002\u53ef\u4f9b\u89c2\u8d4f\u3002'},
        u'\u72fc': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/53_wolf%E7%8B%BC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A08Z%2F-1%2F%2F1f34cd12e73bdd2fd27b04c6fd5c1048830651b4c81d988b3f411a2df4518e77',
            'name': u'\u72fc',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/53_wolf%E7%8B%BC.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A15Z%2F-1%2F%2Fa16e3ddf175e7ea10c0c28e170c1aa426273fe73cb67e02051d8f1f6b250290d',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5916\u5f62\u50cf\u72d7\uff0c\u9762\u90e8\u957f\uff0c\u8033\u6735\u76f4\u7acb\uff0c\u6bdb\u9ec4\u8272\u6216\u7070\u8910\u8272\uff0c\u5c3e\u5df4\u5411\u4e0b\u5782\u3002\u663c\u4f0f\u591c\u51fa\uff0c\u51ac\u5929\u5e38\u805a\u96c6\u6210\u7fa4\uff0c\u6027\u51f6\u66b4\uff0c\u5403\u91ce\u751f\u52a8\u7269\u548c\u5bb6\u755c\u7b49\uff0c\u6709\u65f6\u4e5f\u4f24\u5bb3\u4eba\u3002'},
        u'\u5927\u7329\u7329': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/16_gorilla%E5%A4%A7%E7%8C%A9%E7%8C%A9.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A29Z%2F-1%2F%2F301967da7562bf970dacbe0db9822763bb624ad4f850ffebc97a18e8ee6e98c7',
            'name': u'\u5927\u7329\u7329',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/16_gorilla%E5%A4%A7%E7%8C%A9%E7%8C%A9.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A55Z%2F-1%2F%2F59be15ecbeff31674fc94b7e13ddf4827903da51ee7a5c1afe5e8f9471bae204',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u7c7b\u4eba \u733f\u7684\u4e00\u79cd\u3002\u4f53\u8eaf\u58ee\u5927\uff0c\u96c4\u6027\u9ad8\u7ea61.65\u7c73\uff0c\u96cc\u6027\u9ad8\u7ea61.40\u7c73\u3002\u524d\u80a2\u6bd4\u540e\u80a2\u957f\uff0c\u4e24\u81c2\u5c55\u5f00\u53ef\u8fbe2.72\u7c73\u3002\u6bdb\u9ed1 \u8910\u8272\uff0c\u7565\u53d1\u7070\u3002\u6027\u51f6\u66b4\u3002'},
        u'\u523a\u732c': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/18_hedgehog%E5%88%BA%E7%8C%AC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A32Z%2F-1%2F%2Fdb194cb8211914b9a0f9e783d4dd64d961d3ef2ec43a30b4dc5e0d5d9279e06f',
            'name': u'\u523a\u732c',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/18_hedgehog%E5%88%BA%E7%8C%AC.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A55Z%2F-1%2F%2F507884e9186f34fc1b2922715855007c8fb704377077d2c2d28c97b804277e93',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u4f53\u80a5\u77ed\uff0c\u957f\u7ea625\u5398\u7c73\u3002\u56db\u80a2\u77ed\uff0c\u722a\u5f2f\u800c\u9510\u5229\u3002\u773c\u548c\u8033\u90fd\u5c0f\u3002\u6bdb\u77ed\uff0c\u6709\u77ed\u800c\u5bc6\u7684\u523a\uff0c\u9047\u654c\u5bb3\u65f6\u80fd\u8737\u66f2\u6210\u7403\uff0c\u4ee5\u523a\u4fdd\u62a4\u8eab\u4f53\u3002\u591c\u95f4\u6d3b\u52a8\uff0c\u4e3b\u98df\u6606\u866b\u548c\u8815\u866b\u3002\u5bf9\u519c\u4e1a\u6709\u76ca\u3002'},
        u'\u7329\u7329': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/26_orangutan%E7%8C%A9%E7%8C%A9.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A41Z%2F-1%2F%2Faca5b7a11f91f20a2af183e962ac381a432239ffb56597b9c9b92f8f9d944724',
            'name': u'\u7329\u7329',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/26_orangutan%E7%8C%A9%E7%8C%A9.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A56Z%2F-1%2F%2F69450a15d210017e071977f5d445e04152af51e2cede6558da712c7c8ea1a5c4',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u6bd4\u7334\u5b50\u5927\uff0c\u5934\u5c16\uff0c\u543b\u90e8\u7a81\u51fa\uff0c\u4e24\u81c2\u957f\uff0c\u5168\u8eab\u6709\u8d64\u8910\u8272\u957f\u6bdb\uff0c\u6ca1\u6709\u81c0\u75a3\u3002\u751f\u6d3b\u5728\u82cf\u95e8\u7b54\u814a\u548c\u52a0\u91cc\u66fc\u4e39\u7684\u68ee\u6797\u4e2d\uff0c\u5403\u91ce\u679c\u7b49\u3002'},
        u'\u9ed1\u8723': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/112_bessbeetle-%E9%BB%91%E8%9C%A3.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A10Z%2F-1%2F%2Fe0cf5447ca6196edbbec203ffe244aafbd605e410d313b4b37b0b22fda2322d3',
            'name': u'\u9ed1\u8723',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/112_bessbeetle-%E9%BB%91%E8%9C%A3.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2F470ad3a3bc1ec883ecbd4af6d8c28783ffc01c466adb238146153de12bc96500',
            'desc': u'\u4ee5\u4f53\u578b\u5927\u4e3a\u7279\u5f81\uff0c\u9798\u7fc5\u9ed1\u8272\uff0c\u6709\u5149\u6cfd\uff0c\u6545\u53c8\u79f0\u6f06\u76ae\u7532\u866b\u3002\u4f53\u6241\u5e73\uff0c\u5934\u524d\u65b9\u6709\u89d2\u72b6\u7a81\u3002'},
        u'\u9e2d\u5b50': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/10_duck%E9%B8%AD%E5%AD%90.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A17Z%2F-1%2F%2F599c8f1bb88cb253d7abb07b0afc974e5ee7a7dbfef54962d9a38f8f45a1193e',
            'name': u'\u9e2d\u5b50',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/10_duck%E9%B8%AD%E5%AD%90.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A54Z%2F-1%2F%2Fca313e28d3c85e55faa4edea55b97413421bc2aeca467640588a1dfea6bf3f3a',
            'desc': u'\u9e1f\uff0c\u5634\u6241\u817f\u77ed\uff0c\u8dbe\u95f4\u6709\u8e7c\uff0c\u5584\u6e38\u6cf3\uff0c\u6709\u5bb6\u9e2d\u3001\u91ce\u9e2d\u4e24\u79cd\u3002\u6bdb\u53ef\u7528\u6765\u7d6e\u88ab\u5b50\u3001\u7fbd\u7ed2\u670d\u6216\u586b\u5145\u6795\u5934\u3002\u901a\u5e38\u6307\u5bb6\u9e2d\u3002\u901a\u79f0\u9e2d\u5b50'},
        u'\u72ec\u89d2\u4ed9': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/111_Uang-%E7%8B%AC%E8%A7%92%E4%BB%99.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A10Z%2F-1%2F%2Fb5f665439514a1521bf077596a97ed799e02e3c8f5a67d35a0184bc3c2fa9ab5',
            'name': u'\u72ec\u89d2\u4ed9',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/111_Uang-%E7%8B%AC%E8%A7%92%E4%BB%99.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2F0d33d7c6456d4023157df9373f852acc4c021fdd8b1ead23191666aae486d80a',
            'desc': u'\u53c8\u540d\u53cc\u53c9\u7280\u91d1\u9f9f\uff0c\u662f\u4e00\u79cd\u91d1\u9f9f\u5b50\u79d1\u3001\u53c9\u7280\u91d1\u9f9f\u5c5e\u6606\u866b\uff0c\u56e0\u96c4\u6027\u6709\u53d1\u8fbe\u7684\u5934\u89d2\u800c\u5f97\u540d\u3002\u5206\u5e03\u4e8e\u4e2d\u56fd\u4e1c\u90e8\uff0c\u65e5\u672c\uff0c\u6cf0\u56fd\u7b49\u5730\uff0c\u751f\u6d3b\u5728\u68ee\u6797\u4e2d\u3002'},
        u'\u5a03\u5a03\u9c7c': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/83_giantsalamander%E5%A8%83%E5%A8%83%E9%B1%BC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A22Z%2F-1%2F%2F7415a9ad23febff8250c0cfa1539b19141bcc3e0de54da23b78f7343196aa085',
            'name': u'\u5a03\u5a03\u9c7c',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/83_giantsalamander%E5%A8%83%E5%A8%83%E9%B1%BC.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A19Z%2F-1%2F%2Faadafffb6fc91baa0be1d5d5c87ff3e815b295cd63982725848e070fb5b8bd03',
            'desc': u'\u53c8\u79f0\u5927\u9cb5\u3002\u4e24\u6816\u52a8\u7269\u3002\u957f60\u201470\u5398\u7c73\u3002\u80cc\u9762\u68d5\u8910\u8272\uff0c\u6709 \u5927\u9ed1\u6591\uff0c\u8179\u9762\u8272\u6de1\u3002\u5934\u5bbd\u800c\u6241\uff0c\u53e3\u5927\u3002\u8eaf\u5e72\u7c97\u58ee\u800c\u6241\uff0c\u5c3e\u4fa7\u6241\uff0c\u56db\u80a2\u751a\u77ed\u3002\u53eb\u58f0\u4f3c\u5c0f\u5b69\u557c\u54ed\u3002\u6816\u606f\u4e8e\u5c71 \u8c37\u6eaa\u6c34\u4e2d\u3002\u662f\u4e2d\u56fd\u7279\u6709\u73cd\u7a00\u52a8\u7269\u3002'},
        u'\u9e3d\u5b50': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/45_pigeon%E9%B8%BD%E5%AD%90.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A53Z%2F-1%2F%2Fc98d75c36614c18ac4f281c5b1d302ec26ef15ad378d2cffaff278dca8668148',
            'name': u'\u9e3d\u5b50',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/45_pigeon%E9%B8%BD%E5%AD%90.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A58Z%2F-1%2F%2Fb1ab1f08362cd748596c5a2e406ecc90a9a8f120bdfa29dddb805efe0dc186dd',
            'desc': u'\u9e1f\uff0c\u7fc5\u8180\u5927\uff0c\u5584\u4e8e\u98de\u884c\uff0c\u54c1\u79cd\u5f88\u591a\uff0c\u7fbd\u6bdb\u6709\u767d\u8272\u3001\u7070\u8272\u3001\u9171\u7d2b\u8272\u7b49\uff0c\u4ee5\u8c37\u7c7b\u690d\u7269\u7684\u79cd\u5b50\u4e3a\u98df\u7269\uff0c\u6709\u7684\u53ef\u4ee5\u7528\u6765\u4f20\u9012\u4e66\u4fe1\u3002 \u5e38\u7528\u4f5c\u548c\u5e73\u7684\u8c61\u5f81\u3002'},
        u'\u8757\u866b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/75_locust%E8%9D%97%E8%99%AB.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A19Z%2F-1%2F%2Fecc64687bf2ac5e775288c3b5d6f097f73a1feb953a3fe0e548700547856cb80',
            'name': u'\u8757\u866b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/75_locust%E8%9D%97%E8%99%AB.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2F0be78cd90318c798df20f2d2ae46fab7fa82a86abcb550eeed2cf042977bf698',
            'desc': u'\u6606\u866b\uff0c\u53e3\u5668\u575a\u786c\uff0c\u524d\u7fc5\u72ed\u7a84\u800c\u575a\u97e7\uff0c\u540e\u7fc5\u5bbd\u5927\u800c\u67d4\u8f6f\uff0c\u540e\u80a2\u5f88\u53d1\u8fbe\uff0c\u5584\u4e8e\u8df3\u8dc3\uff0c\u591a\u6570\u5584\u4e8e\u98de\u884c\u3002\u4e3b\u8981\u5371\u5bb3\u79be\u672c\u79d1\u690d\u7269\uff0c\u662f\u519c\u4e1a\u5bb3\u866b\u3002\u79cd\u7c7b\u5f88\u591a\u3002\u6709\u7684\u5730\u533a\u53eb\u8682\u86b1\u3002'},
        u'\u868a\u5b50': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/77_mosquito%E8%9A%8A%E5%AD%90.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A19Z%2F-1%2F%2F6bfe52ceee73065f406b3e1144a30f743802c34009e6df8949a5d82a97ace6a4',
            'name': u'\u868a\u5b50',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/77_mosquito%E8%9A%8A%E5%AD%90.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2F00b246c6188c3ff0ebd4435a33aa3023b6ffb4da2123e8405c2fe09f466577d7',
            'desc': u'\u6606\u866b\uff0c\u6210\u866b\u8eab\u4f53\u7ec6\u957f\uff0c\u80f8\u90e8\u6709\u4e00\u5bf9\u7fc5\u8180\u548c\u4e09\u5bf9\u7ec6\u957f\u7684\u811a\uff0c\u5e7c\u866b\uff08\u5b51\u5b53\uff09\u548c\u86f9\u90fd\u751f\u957f\u5728\u6c34\u4e2d\u3002\u96c4\u868a\u5438\u690d\u7269\u7684\u6c41\u6db2\u3002\u96cc\u868a\u5438\u4eba\u755c\u7684\u8840\u6db2\uff0c\u80fd\u4f20\u64ad\u759f\u75be\u3001\u4e1d\u866b\u75c5\u3001\u6d41\u884c\u6027\u4e59\u578b\u8111\u708e\u7b49\u75c5\u3002\u6700\u5e38\u89c1\u7684\u6709\u6309\u868a\u3001\u5e93\u868a\u548c\u4f0a\u868a\u4e09\u7c7b\u3002'},
        u'\u6cb3\u9a6c': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/19_hippo%E6%B2%B3%E9%A9%AC.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A34Z%2F-1%2F%2F42061ef39c6634436fd42efdb6dea51e1cdea0f73d5f3f0006fe989099bb88c1',
            'name': u'\u6cb3\u9a6c',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/19_hippo%E6%B2%B3%E9%A9%AC.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A55Z%2F-1%2F%2Fd23d7acbedec72feb4872567bc2aee1189d765ae98b2f585b73537f19dc60783',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u4f53\u80a5\u91cd\u3002\u957f3\u20144\u7c73\uff0c\u91cd\u8fbe3\u20144\u5428\u3002\u76ae\u80a4\u88f8\u9732\uff0c\u9ed1\u8910\u8272\u3002\u5934\u5927\uff0c\u5634\u9614\uff0c\u8033\u5c0f\uff0c\u5c3e\u77ed\u3002\u5927\u90e8\u5206\u65f6\u95f4\u751f\u6d3b\u5728\u6c34\u4e2d\uff0c\u98df\u8349\u7c7b\u548c\u6c34\u751f\u690d\u7269\u3002\u5206\u5e03\u4e8e\u975e\u6d32\u7684\u6cb3\u6d41\u548c\u6e56\u6cbc\u5730\u5e26\u3002'},
        u'\u873b\u8713': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/117_dragonfly-%E8%9C%BB%E8%9C%93.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A12Z%2F-1%2F%2F4c4a84b62960a02bac581039c960aa7267f9af3b68faf6e35ebd6a4b5ab87958',
            'name': u'\u873b\u8713',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/117_dragonfly-%E8%9C%BB%E8%9C%93.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2Feb7f6743a412d350138f2a4b94a5e10968b5beebb593f6702fc99ba17c176274',
            'desc': u'\u6606\u866b\uff0c\u8eab\u4f53\u7ec6\u957f\uff0c\u80f8\u90e8\u7684\u80cc\u9762\u6709\u4e24\u5bf9\u819c\u72b6\u7684\u7fc5\uff0c\u751f\u6d3b\u5728\u6c34\u8fb9\uff0c\u6355\u98df\u868a\u5b50\u7b49\u5c0f\u98de\u866b\uff0c\u80fd\u9ad8\u98de\u3002\u96cc\u7684\u7528\u5c3e\u70b9\u6c34\u800c\u4ea7\u5375\u4e8e\u6c34\u4e2d\u3002\u5e7c\u866b\u53eb\u6c34\u867f\uff0c\u751f\u6d3b\u5728\u6c34\u4e2d\u3002\u662f\u76ca\u866b\u3002\u6709\u7684\u5730\u533a\u53eb\u8682\u8782\u3002'},
        u'\u9f39\u9f20': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/25_mole%E9%BC%B9%E9%BC%A0.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A40Z%2F-1%2F%2F17cf9cd10c84fb273e15e4d00768cbe5d7fb5aa58d05c7a1e4093b89e23cf93f',
            'name': u'\u9f39\u9f20',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/25_mole%E9%BC%B9%E9%BC%A0.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A56Z%2F-1%2F%2F6a029a7094e5819a30f59127e789139f5a1f13dc8a0b0c6fdb73fb934b1ee2e5',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u4f53\u5f62\u50cf\u8001\u9f20\uff0c\u5634\u5c16\uff0c\u751f\u6d3b\u5728\u7530\u95f4\uff0c\u6316\u6398\u6d1e\u9053\u3002\u98df\u6606\u866b\u7b49\u5c0f\u52a8\u7269\uff0c\u4e5f\u4f24\u5bb3\u4f5c\u7269\uff0c\u5bf9\u519c\u4e1a\u6709\u5bb3\u3002'},
        u'\u718a\u732b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/72_panda%E7%86%8A%E7%8C%AB.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A18Z%2F-1%2F%2F28ef5a4a820ee577e60fe68b0e2189534115f7e71c6ca69749a72021e2a3590a',
            'name': u'\u718a\u732b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/72_panda%E7%86%8A%E7%8C%AB.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2Fe43c425561b02d6c5f97a4639485f2c6bd24e770760bc98d839334788d048f76',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u4f53\u80a5\u80d6\uff0c\u5c3e\u77ed\uff0c\u4f3c\u718a\u800c\u7565\u5c0f\uff0c\u4e24\u8033\u3001\u773c\u5468\u3001\u80a9\u90e8\u548c\u56db\u80a2\u9ed1\u8272\uff0c\u5176\u4f59\u90e8\u5206\u767d\u8272\u3002\u98df\u7af9\u53f6\u3001\u7af9\u7b0b\u7b49\u3002\u751f\u6d3b\u5728\u897f\u5357\u9ad8\u5c71\u5730\u533a\u3002\u662f\u4e2d\u56fd\u56fd\u5bb6\u91cd\u70b9\u4fdd\u62a4\u52a8\u7269\u3002'},
        u'\u5c0f\u9e21': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/39_chicks%E5%B0%8F%E9%B8%A1.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A49Z%2F-1%2F%2Fe9804416e1a8fbd8dc4b6c9ed63338c0ce0faaf36c173e38379708fbc29c3727',
            'name': u'\u5c0f\u9e21',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/39_chicks%E5%B0%8F%E9%B8%A1.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2F555941a3f2ff3049cdb6bc64e5ab5827d292ca67f4c6dcb84b8ab969665668aa',
            'desc': u'\u5c0f\u9e21\u5c31\u662f\u9e21\u7684\u5e7c\u5d3d\uff0c\u4ece\u9e21\u86cb\u4e2d\u5b75\u5316\u3002\u5c0f\u9e21\u5403\u9972\u6599\u53ca\u9752\u83dc\u3001\u5c0f\u866b\u3001\u788e\u7c73\u6210\u957f\u3002'},
        u'\u54cd\u5c3e\u86c7': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/58_rattlesnake%E5%93%8D%E5%B0%BE%E8%9B%87.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A12Z%2F-1%2F%2Ff148d63809bbac88943d9da0edd319eaa32a39e3277db4f75452592d46698b10',
            'name': u'\u54cd\u5c3e\u86c7',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/58_rattlesnake%E5%93%8D%E5%B0%BE%E8%9B%87.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A16Z%2F-1%2F%2F4c434806ebc789c79325a50def2659038489050c67de06956efe588d20d308ee',
            'desc': u'\u722c\u884c\u52a8\u7269\u3002 \u6bd2\u86c7\u7684\u4e00\u79cd\u3002\u957f\u7ea62\u7c73\u3002\u4f53\u5448\u7eff\u9ec4\u8272\uff0c\u5177\u83f1\u5f62\u9ed1\u8910\u8272\u6591\u3002\u5c3e\u7aef\u6709\u89d2\u8d28\u73af\uff0c\u5267\u52a8\u65f6\u80fd\u53d1\u58f0\uff0c\u6545\u540d\u3002\u5206\u5e03\u4e8e\u5317\u7f8e\u6d32\u3002'},
        u'\u871c\u8702': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/76_bee%E8%9C%9C%E8%9C%82.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A19Z%2F-1%2F%2F7d1f1b8c9aa344d59d0a91c330e20a146c99c3dbf48becd76d0fcd6c023d1172',
            'name': u'\u871c\u8702',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/76_bee%E8%9C%9C%E8%9C%82.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2Fd5d14c161c874c6de06ad741d81f32052909bf93ba955b08b2448d41cf2a32e3',
            'desc': u'\u6606\u866b\uff0c\u4f53\u8868\u6709\u5f88\u5bc6\u7684\u7ed2\u6bdb\uff0c\u524d\u7fc5\u6bd4\u540e\u7fc5\u5927\uff0c\u96c4\u8702\u89e6\u89d2\u8f83\u957f\uff0c\u6bcd\u8702\u548c\u5de5\u8702\u6709\u6bd2\u523a\uff0c\u80fd\u8707\u4eba\u3002\u6210\u7fa4\u5c45\u4f4f\u3002\u5de5\u8702\u80fd\u91c7\u82b1\u7c89\u917f\u871c\uff0c\u5e2e\u52a9\u67d0\u4e9b\u690d\u7269\u4f20\u7c89\u3002\u8702\u871c\u3001\u8702\u8721\u3001\u8702\u738b\u6d46\u6709\u5f88\u9ad8\u7684\u7ecf\u6d4e\u4ef7\u503c\u3002'},
        u'\u675c\u9e43': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/100_cuckoo%E6%9D%9C%E9%B9%83.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A29Z%2F-1%2F%2F16f28d345078402c5362e096f1322ad9c2db6492db5409efdf1fac9534144a9c',
            'name': u'\u675c\u9e43',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/100_cuckoo%E6%9D%9C%E9%B9%83.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2F4f06b8576e486821615e06d720859cfff3d88610109a95252dcd96c04f4134f1',
            'desc': u'\u9e1f\uff0c\u8eab\u4f53\u9ed1\u7070\u8272\uff0c\u5c3e\u5df4\u6709\u767d\u8272\u6591\u70b9\uff0c\u8179\u90e8\u6709\u9ed1\u8272\u6a2a\u7eb9\u3002 \u521d\u590f\u65f6\u5e38\u663c\u591c\u4e0d\u505c\u5730\u53eb\u3002\u5403\u6bdb\u866b\uff0c\u662f\u76ca\u9e1f\u3002\u591a\u6570\u628a\u5375\u4ea7\u5728\u522b\u7684\u9e1f\u5de2\u4e2d\u3002\u4e5f\u53eb\u675c\u5b87\u3001\u5e03\u8c37\u6216\u5b50\u89c4\u3002'},
        u'\u87cb\u87c0': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/79_cricket%E8%9F%8B%E8%9F%80.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A21Z%2F-1%2F%2F144e440dd6766cdc5e214a0269341178bb6d05fb1a7bf468f8fb77e2ac5bd469',
            'name': u'\u87cb\u87c0',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/79_cricket%E8%9F%8B%E8%9F%80.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2F1ace6fc1d73aef287bfe38a020e192300fbd53618cd821b08971c6529f11a42f',
            'desc': u'\u6606\u866b\uff0c\u8eab\u4f53\u9ed1\u8910\u8272\uff0c\u89e6\u89d2\u5f88\u957f\uff0c\u540e\u817f\u7c97\u5927\uff0c\u5584\u4e8e\u8df3\u8dc3\u3002 \u5c3e\u90e8\u6709\u5c3e\u987b\u4e00\u5bf9\u3002\u96c4\u7684\u597d\u6597\uff0c\u4e24\u7fc5\u6469\u64e6\u80fd\u53d1\u58f0\u3002\u751f\u6d3b\u5728\u9634\u6e7f\u7684\u5730\u65b9\uff0c\u5403\u690d\u7269\u7684\u6839\u3001\u830e\u548c\u79cd\u5b50\uff0c\u5bf9\u519c\u4e1a\u6709\u5bb3\u3002\u4e5f\u53eb\u4fc3\u7ec7\uff0c\u6709\u7684\u5730\u533a\u53eb\u86d0\u86d0\u513f\u3002'},
        u'\u6d77\u96c0': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/29_puffin%E6%B5%B7%E9%9B%80.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A43Z%2F-1%2F%2F8f24921860474f65fe3d699a45afd4d3349095464b32a395d95b8d86a3ce41f1',
            'name': u'\u6d77\u96c0',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/29_puffin%E6%B5%B7%E9%9B%80.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2Faf313f8846a5cdf5f2ce802113d1feba5627d88cdcc0ef83dbd53f6da0efe580',
            'desc': u'\u6d77\u96c0\u662f\u9e1f\u7eb2\u9e25\u5f62\u76ee\u6d77\u96c0\u79d1\u9e1f\u7c7b\u7684\u901a\u79f0\uff0c\u662f\u5178\u578b\u7684\u6d77\u9e1f\uff0c\u4f53\u7fbd\u9ed1\u767d\u8272\u3002\u4e2d\u56fd\u67093\u79cd\uff1a\u6241\u5634\u6d77\u96c0\uff0c\u89d2\u5634\u6d77\u96c0\uff0c\u6591\u6d77\u96c0\u3002'},
        u'\u98df\u8681\u517d': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/69_anteater%E9%A3%9F%E8%9A%81%E5%85%BD.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A17Z%2F-1%2F%2F739378ae85b5d04a9c26c06d25a78fcbec38efe4d271a088b7f12e869efbd9c9',
            'name': u'\u98df\u8681\u517d',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/69_anteater%E9%A3%9F%E8%9A%81%E5%85%BD.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A17Z%2F-1%2F%2Fb91340c6e5bec9b0036ed0d0a968062d74badd7b579ec2bdb849dd40b965faf6',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u4f53\u957f\u7ea61.3\u7c73\u3002\u5c3e\u90e8\u5bc6\u751f\u957f\u6bdb\u3002\u5934\u7ec6\u957f\u3002\u773c\u548c\u8033\u6781\u5c0f\u3002\u543b\u6210\u7ba1\u72b6\u3002\u65e0\u9f7f\uff0c\u820c\u7ec6\u957f\uff0c\u80fd\u4f38\u7f29\uff0c\u501f\u4ee5\u8210\u98df\u8681\u7c7b\u53ca\u5176\u4ed6\u6606\u866b\u3002\u4f53\u7070\u8272\uff0c\u80cc\u9762\u4e24\u4fa7\u6709\u5bbd\u9614\u7684\u7eb5\u7eb9\uff0c\u7eb9\u7684\u8fb9\u7f18\u767d\u8272\u3002\u5206\u5e03\u4e8e\u4e2d\u7f8e\u548c\u5357\u7f8e\u6d32\u7684\u70ed\u5e26\u5730\u533a\u3002'},
        u'\u71d5\u5b50': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/109_swallow%E7%87%95%E5%AD%90.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A08Z%2F-1%2F%2Fecf8215f89d8096f770423be4428172e9284293479def90d9f64ada807751714',
            'name': u'\u71d5\u5b50',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/109_swallow%E7%87%95%E5%AD%90.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2Ff5a9f40e9bbb88cfaee7c36737a31773cd993fff76f141103a90d6ad8b3cd0ab',
            'desc': u'\u71d5\u7684\u4e00\u79cd\uff0c\u8eab\u4f53\u5c0f\uff0c\u80cc\u90e8\u7fbd\u6bdb\u9ed1\u8272\uff0c\u6709\u5149\u6cfd\uff0c\u8179\u90e8\u767d\u8272\uff0c\u9888\u90e8\u6709\u6df1\u7d2b\u8272\u5706\u6591\uff0c\u591a\u5728\u5c4b\u6a90\u4e0b\u7b51\u7a9d\u3002\u901a\u79f0\u71d5\u5b50\u3002'},
        u'\u87fe\u870d': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/46_toad%E8%9F%BE%E8%9C%8D.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A55Z%2F-1%2F%2F7293ad3e1a77bfd3465d8182b5c6ed281748b75d6d193c0cdf3d571ac564c826',
            'name': u'\u87fe\u870d',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/46_toad%E8%9F%BE%E8%9C%8D.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A58Z%2F-1%2F%2F6340dc964676283f8449ac1a262bafc3b2d869952298494b2bc7d89b71ec8fb4',
            'desc': u'\u4e24\u6816\u52a8\u7269\uff0c\u8eab\u4f53\u8868\u9762\u6709\u8bb8\u591a\u7599\u7629\uff0c\u5185\u6709\u6bd2\u817a\uff0c\u80fd\u5206\u6ccc\u9ecf\u6db2\uff0c\u5403\u6606\u866b\u3001\u8717\u725b\u7b49\u5c0f\u52a8\u7269\uff0c\u5bf9\u519c\u4e1a\u6709\u76ca\u3002\u901a\u79f0\u765e\u86e4\u87c6\u6216\u75a5\u86e4\u87c6\u3002'},
        u'\u773c\u955c\u86c7': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/57_cobra%E7%9C%BC%E9%95%9C%E8%9B%87.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A11Z%2F-1%2F%2Ffc4fcae303b90b35e806ec4ad010304b651f488fc839f52ff9f9db7c92596271',
            'name': u'\u773c\u955c\u86c7',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/57_cobra%E7%9C%BC%E9%95%9C%E8%9B%87.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A16Z%2F-1%2F%2F2fda470df85c17809612b99c3c0274adddcc17995fc41fcaa86834702c0c87d0',
            'desc': u'\u722c\u884c\u52a8\u7269\u3002\u6bd2\u86c7\u7684\u4e00\u79cd\u3002\u9888\u90e8\u5f88\u7c97\uff0c\u4e0a\u9762\u6709\u4e00\u5bf9\u767d\u8fb9\u9ed1\u5fc3\u7684\u73af\u72b6\u6591\u7eb9\uff0c\u50cf\u4e00\u526f\u773c\u955c\u3002\u6fc0\u6012\u65f6\u524d\u534a\u8eab\u7ad6\u8d77\uff0c\u9888\u90e8\u81a8\u5927\u3002\u6bd2\u6027\u5f88\u5f3a\u3002\u6355\u98df\u9cdd\u9c7c\u3001\u86d9\u7c7b\u3001\u9f20\u7c7b\u3001\u5176\u4ed6\u86c7\u7c7b\u548c\u5c0f\u9e1f\u7b49\u3002'},
        u'\u6d77\u9e25': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/108_seagull%E6%B5%B7%E9%B8%A5.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A08Z%2F-1%2F%2F26b82b44a6c2989e68673cdefba5266c1daa0006087d2b92864c3992fb4fc742',
            'name': u'\u6d77\u9e25',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/108_seagull%E6%B5%B7%E9%B8%A5.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A48Z%2F-1%2F%2F01454ab14e5db517501717a1b2da323e5ae8529d734a8cfd35924d4c42d2f79a',
            'desc': u'\u9e1f\uff0c\u5934\u548c\u9888\u90e8\u8910\u8272\uff0c\u7fc5\u8180\u5916\u7f18\u767d\u8272\uff0c\u5185\u7f18\u7070\u8272\uff0c\u8eaf\u5e72\u767d\u8272\uff0c\u722a\u9ed1\u8272\u3002 \u5e38\u6210\u7fa4\u5728\u6d77\u4e0a\u6216\u5185\u9646\u6cb3\u6d41\u9644\u8fd1\u98de\u7fd4\uff0c\u5403\u9c7c\u3001\u87ba\u3001\u6606\u866b\u7b49\uff0c\u4e5f\u5403\u8c37\u7269\u548c\u690d\u7269\u5ae9\u53f6\u3002'},
        u'\u4f01\u9e45': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/97_penguin%E4%BC%81%E9%B9%85.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A28Z%2F-1%2F%2F28abb3164603356fde79287e24525cb904b8b34160fce298de97c062d88de137',
            'name': u'\u4f01\u9e45',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/97_penguin%E4%BC%81%E9%B9%85.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2Fd3331470a50d907578456ccb4ef43f77b44267f85fd1f1f477ad7068b8684183',
            'desc': u'\u6c34\u9e1f\uff0c\u4f53\u957f\u8fd11\u7c73\uff0c\u5634\u5f88\u575a\u786c\uff0c\u5934\u548c\u80cc\u90e8\u9ed1\u8272\uff0c\u8179\u90e8\u767d\u8272\uff0c\u8db3\u77ed\uff0c\u5c3e\u5df4\u77ed\uff0c\u7fc5\u8180\u5c0f\uff0c\u4e0d\u80fd\u98de\uff0c\u5584\u4e8e\u6f5c\u6c34\uff0c\u5728\u9646\u5730\u4e0a\u76f4\u7acb\u65f6\u50cf\u6709\u6240\u4f01\u671b\u7684\u6837\u5b50\uff0c\u591a\u7fa4\u5c45\u5728\u5357\u6781\u6d32\u53ca\u9644\u8fd1\u5c9b\u5c7f\u4e0a\u3002'},
        u'\u8c6a\u732a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/70_porcupine%E8%B1%AA%E7%8C%AA.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A17Z%2F-1%2F%2F03ea0b39911cb9b674e9b85df0aab7aacdfe24218cb5b1c5f8e13d984be16842',
            'name': u'\u8c6a\u732a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/70_porcupine%E8%B1%AA%E7%8C%AA.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A18Z%2F-1%2F%2F6754d7796e7745a9bfc73b86976fa1ff602eea56565887546cca45d07dbe17df',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5168\u8eab\u9ed1\u8272\u6216\u8910\u8272\uff0c\u81ea\u80a9\u90e8\u4ee5\u540e\u957f\u7740\u8bb8\u591a\u957f\u800c\u786c\u7684\u523a\uff0c\u9047\u654c\u5bb3\u65f6\u7ad6\u8d77\uff0c\u7a74\u5c45\uff0c\u663c\u4f0f\u591c\u51fa\uff0c\u5403\u690d\u7269\u7b49\uff0c\u5e38\u76d7\u98df\u519c\u4f5c\u7269\u3002'},
        u'35\u79cd\u7ecf\u5178\u52a8\u7269\u5408\u96c6': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/1_35%E7%A7%8D%E5%8A%A8%E7%89%A9%E5%8F%AB%E5%A3%B0%E9%9F%B3%E6%95%88%E5%A4%A7%E5%85%A8%E5%90%88%E9%9B%86.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A30%3A01Z%2F-1%2F%2Faeaf1c245d1be7a260e9eb2af3f6153b22e9f59e7a4d7298a5de2d6cb7ddf457',
            'name': u'35\u79cd\u7ecf\u5178\u52a8\u7269\u5408\u96c6',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/1_35%E7%A7%8D%E5%8A%A8%E7%89%A9%E5%8F%AB%E5%A3%B0%E9%9F%B3%E6%95%88%E5%A4%A7%E5%85%A8%E5%90%88%E9%9B%86.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A52Z%2F-1%2F%2F6f9d3b63e22e61029f50cb2105f0438904b0e307bf9f723e758a1369b3e67885',
            'desc': u'\u5976\u725b\uff0c\u732b\uff0c\u9e2d\u5b50\uff0c\u9a6c\uff0c\u5927\u8c61\uff0c\u5927\u7329\u7329\uff0c\u5927\u516c\u9e21\uff0c\u5c71\u7f8a\uff0c\u957f\u9888\u9e7f\uff0c\u6591\u9a6c\uff0c\u72d7\uff0c\u72ee\u5b50\uff0c\u9ec4\u8702\uff0c\u53d8\u8272\u9f99\u7b49'},
        u'\u5c71\u7f8a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/15_goat%E5%B1%B1%E7%BE%8A.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A27Z%2F-1%2F%2F10d5a6aadff099c22f0652ecab06b7bf33161367e11ceef64804559ad3a1067d',
            'name': u'\u5c71\u7f8a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/15_goat%E5%B1%B1%E7%BE%8A.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A55Z%2F-1%2F%2Fcb113bde61abdd9a9919bfddb539e242cd5c0ab4f09e12ebb221c7a968b09fc4',
            'desc': u'\u7f8a\u7684\u4e00\u79cd\uff0c\u89d2\u7684\u57fa\u90e8\u7565\u4f5c\u4e09\u89d2\u5f62\uff0c\u89d2\u5c16\u5411\u540e\uff0c\u56db\u80a2\u5f3a\u58ee\uff0c\u5584\u4e8e\u8df3\u8dc3\uff0c\u6bdb\u4e0d\u5f2f\u66f2\uff0c\u516c\u7f8a\u6709\u987b\uff0c\u53d8\u79cd\u5f88\u591a\uff0c\u6709\u9ed1\u3001\u7070\u7b49\u989c\u8272\u3002'},
        u'\u559c\u9e4a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/101_magpie%E5%96%9C%E9%B9%8A.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A06Z%2F-1%2F%2Fdc9cce96b33de551feec99cd3918777df7759d9b2851c8965d07976eec8a0f3c',
            'name': u'\u559c\u9e4a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/101_magpie%E5%96%9C%E9%B9%8A.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A47Z%2F-1%2F%2F17ede3ad1fd0996170eb2d8a9672b1b26b296db388acd89442e00df78fffdaad',
            'desc': u'\u9e1f\uff0c\u5634\u5c16\uff0c\u5c3e\u957f\uff0c\u8eab\u4f53\u5927\u90e8\u4e3a\u9ed1\u8272\uff0c\u80a9\u548c\u8179\u90e8\u767d\u8272\uff0c\u53eb\u58f0\u5608\u6742\u3002\u6c11\u95f4\u4f20\u8bf4\u542c\u89c1\u5b83\u53eb\u5c06\u6709\u559c\u4e8b\u6765\u4e34\uff0c\u6240\u4ee5\u53eb\u559c\u9e4a\u3002\u4e5f\u53eb\u9e4a\u3002'},
        u'\u706b\u9e21': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/94_turkey%E7%81%AB%E9%B8%A1.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A28Z%2F-1%2F%2Fd73a0ed5baf618457570db61e4bac07a7c47269fa60fffd19c5d034c80795441',
            'name': u'\u706b\u9e21',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/94_turkey%E7%81%AB%E9%B8%A1.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2Ffed2bdc3c460f9e020e6ade63841c1ab8c5a2fe8cf7035c8fd7be29d782bc912',
            'desc': u'\u9e1f\uff0c\u5634\u5927\uff0c\u5934\u90e8\u6709\u7ea2\u8272\u8089\u8d28\u7684\u7624\u72b6\u7a81\u8d77\uff0c\u811a\u957f\u5927\uff0c\u7fbd\u6bdb\u6709\u9ed1\u3001\u767d\u3001\u6df1\u9ec4\u7b49\u8272\u3002\u4e5f\u53eb\u5410\u7ef6\u9e21\u3002'},
        u'\u8759\u8760': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/80_bat%E8%9D%99%E8%9D%A0.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A21Z%2F-1%2F%2F2cd5ffa8d2afc386d1ce03d43283d01dcb14ac45b5970690a5b7c5f39f81455d',
            'name': u'\u8759\u8760',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/80_bat%E8%9D%99%E8%9D%A0.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A19Z%2F-1%2F%2F7d3f08bedf54f688f9c20a33092e09832bcef066fdf1dd3162ca8747b7d19118',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5934\u90e8\u548c\u8eaf\u5e72\u50cf\u8001\u9f20\uff0c\u56db\u80a2\u548c\u5c3e\u90e8\u4e4b\u95f4\u6709\u76ae\u8d28\u7684\u819c\uff0c\u591c\u95f4\u5728\u7a7a\u4e2d\u98de\u7fd4\uff0c\u5403\u868a\u3001\u86fe\u7b49\u6606\u866b\u3002\u89c6\u529b\u5f88\u5f31\uff0c\u9760\u672c\u8eab\u53d1\u51fa\u7684\u8d85\u58f0\u6ce2\u6765\u5f15\u5bfc\u98de\u884c\u3002'},
        u'\u732b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/5_cat%E7%8C%AB.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A10Z%2F-1%2F%2F724e0316ccdf8a764b9e73e1bb0445d88cb85e058138ae1367454e8b78a64194',
            'name': u'\u732b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/5_cat%E7%8C%AB.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A53Z%2F-1%2F%2Fab54a7fa3489966c5cf6d4ba073a2e8be57cebdf1a2bbba5031ed68c2209a065',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u9762\u90e8\u7565\u5706\uff0c\u8eaf\u5e72\u957f\uff0c\u8033\u58f3\u77ed\u5c0f\uff0c\u773c\u5927\uff0c\u77b3\u5b54\u968f\u5149\u7ebf\u5f3a\u5f31\u800c\u7f29\u5c0f\u653e\u5927\uff0c\u56db\u80a2\u8f83\u77ed\uff0c\u638c\u90e8\u6709\u8089\u8d28\u7684\u57ab\uff0c\u884c\u52a8\u654f\u6377\uff0c\u5584\u8df3\u8dc3\uff0c\u80fd\u6355\u9f20\uff0c\u6bdb\u67d4\u8f6f\uff0c\u6709\u9ed1\u3001\u767d\u3001\u9ec4\u3001\u7070\u8910\u7b49\u8272\u3002\u79cd\u7c7b\u5f88\u591a'},
        u'\u8c5a\u9f20': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/17_guineapig%E8%B1%9A%E9%BC%A0.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A30Z%2F-1%2F%2F53871f452fd5a3769d9b5462e4d8001a83899fb1b78b38d0eacb6a48eac645a9',
            'name': u'\u8c5a\u9f20',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/17_guineapig%E8%B1%9A%E9%BC%A0.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A55Z%2F-1%2F%2F5a2fb047c0f843d17a280d2cbe768e294f1eed42a600140fa53c1ad7e8919a62',
            'desc': u'\u4e5f\u53eb\u5929\u7afa\u9f20\u3002\u54fa\u4e73\u52a8\u7269\u3002\u4f53\u957f\u7ea625\u5398\u7c73\uff0c\u65e0\u5c3e\u3002\u4f53\u8272\u767d\u3001\u9ed1\u3001\u9ec4\u8910\u4e0d\u4e00\u3002\u7a74\u5c45\uff0c\u591c\u95f4\u6d3b\u52a8\u3002\u98df\u690d\u7269\u6027\u98df\u7269\u3002'},
        u'\u9752\u86d9': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/13_frog%E9%9D%92%E8%9B%99.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A23Z%2F-1%2F%2F49e5651196fd3a52fa52f1c325542af7ba15862f549f93d0daa54fe3ef32bde9',
            'name': u'\u9752\u86d9',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/13_frog%E9%9D%92%E8%9B%99.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A54Z%2F-1%2F%2F067c7ad408bbb7a137fc6437cb6969d4ec60852633d2d67cd0880c05b51cea68',
            'desc': u'\u4e24\u6816\u52a8\u7269\uff0c\u5934\u90e8\u6241\u800c\u5bbd\uff0c\u53e3\u9614\uff0c\u773c\u5927\uff0c\u76ae\u80a4\u5149\u6ed1\uff0c\u989c\u8272\u56e0\u73af\u5883\u800c\u4e0d\u540c\uff0c\u901a\u5e38\u4e3a\u7eff\u8272\uff0c\u6709\u7070\u8272\u6591\u7eb9\uff0c\u8dbe\u95f4\u6709\u8e7c\u3002\u751f\u6d3b\u5728\u6c34\u4e2d\u6216\u8fd1\u6c34\u7684\u5730\u65b9\uff0c\u5584\u8df3\u8dc3\uff0c\u4f1a\u6e38\u6cf3\uff0c\u591a\u5728\u591c\u95f4\u6d3b\u52a8\uff0c\u96c4\u7684\u53eb\u58f0\u54cd\u4eae\u3002\u5403\u7530\u95f4\u7684\u5bb3\u866b\uff0c\u5bf9\u519c\u4e1a\u6709\u76ca\u3002\u901a\u79f0\u7530\u9e21\u3002'},
        u'\u5154\u5b50': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/44_Rabbit%E5%85%94%E5%AD%90.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A52Z%2F-1%2F%2F64c34d0615ce4770a65b04a896014304f74db1c135d275e3bfdba62e0743be6d',
            'name': u'\u5154\u5b50',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/44_Rabbit%E5%85%94%E5%AD%90.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A58Z%2F-1%2F%2Fcf50c2c892bada2a2573ae2f53f58c2c2ea8b56cacb91ad3e854f67aa33b04de',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5934\u90e8\u7565\u50cf\u9f20\uff0c\u8033\u5927\uff0c\u4e0a\u5507\u4e2d\u95f4\u5206\u88c2\uff0c\u5c3e\u77ed\u800c\u5411\u4e0a\u7fd8\uff0c\u524d\u80a2\u6bd4\u540e\u80a2\u77ed\uff0c\u5584\u4e8e\u8df3\u8dc3\uff0c\u8dd1\u5f97\u5f88\u5feb\u3002\u6709\u5bb6\u5154\u548c\u91ce\u5154\u7b49\u3002\u8089\u53ef\u4ee5\u5403\uff0c\u6bdb\u53ef\u4f9b\u7eba\u7ec7\uff0c\u6bdb\u76ae\u53ef\u4ee5\u5236\u8863\u7269\u3002\u901a\u79f0\u5154\u5b50\u3002'},
        u'\u877c\u86c4': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/120_molecricket-%E8%9D%BC%E8%9B%84.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A14Z%2F-1%2F%2F2b3c00d6782bdc1bf1dff5991a572961a032a63b933d2b32ed48f6f5dd711d29',
            'name': u'\u877c\u86c4',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/120_molecricket-%E8%9D%BC%E8%9B%84.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A49Z%2F-1%2F%2F81c457fa3720c6f4d6c13a52182902da7bfcc946a8ff5708c073fbb2b1f4a948',
            'desc': u'\u6606\u866b\uff0c\u80cc\u90e8\u8336\u8910\u8272\uff0c\u8179\u9762\u7070\u9ec4\u8272\u3002\u524d\u8db3\u53d1\u8fbe\uff0c\u5448\u94f2\u72b6\uff0c\u9002\u4e8e\u6398\u571f\uff0c\u6709\u5c3e\u987b\u3002\u751f\u6d3b\u5728\u6ce5\u571f\u4e2d\uff0c\u663c\u4f0f\u591c\u51fa\uff0c\u5403\u519c\u4f5c\u7269\u5ae9\u830e\u3002\u4e5f\u53eb__\u86c4'},
        u'\u9ebb\u96c0': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/48_sparrow%E9%BA%BB%E9%9B%80.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A55Z%2F-1%2F%2F25754245eaf567f91ad069fad47ea0ed87eaabb945bc46588eff00335de0a78a',
            'name': u'\u9ebb\u96c0',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/48_sparrow%E9%BA%BB%E9%9B%80.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A58Z%2F-1%2F%2F31e589d3b073a6a2e9e3fd3f7f77bcef8818df8b1fa38207f17e6b45e2af6a3d',
            'desc': u'\u9e1f\uff0c\u5934\u5706\uff0c\u5c3e\u77ed\uff0c\u5634\u5448\u5706\u9525\u72b6\uff0c\u5934\u9876\u548c\u9888\u90e8\u6817\u8910\u8272\uff0c\u80cc\u9762\u8910\u8272\uff0c\u6742\u6709\u9ed1\u8910\u8272\u6591\u70b9\uff0c\u5c3e\u7fbd\u6697\u8910\u8272\uff0c\u7fc5\u8180\u77ed\u5c0f\uff0c\u4e0d\u80fd\u8fdc\u98de\uff0c\u5584\u4e8e\u8df3\u8dc3\uff0c\u5544\u98df\u8c37\u7c92\u548c\u6606\u866b\u3002\u6709\u7684\u5730\u533a\u53eb\u5bb6\u96c0\u513f\u3002'},
        u'\u7fe0\u9e1f': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/105_kingfisher%E7%BF%A0%E9%B8%9F.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A07Z%2F-1%2F%2F7bd566143eaddf019e780094c5636269b6f1d05c6bba0e3d16fe2892c0bafd9d',
            'name': u'\u7fe0\u9e1f',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/105_kingfisher%E7%BF%A0%E9%B8%9F.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A47Z%2F-1%2F%2Fc10b8204374d137a0517bd393d13e449e4c0a828cbbd8db3548113764d222abd',
            'desc': u'\u4e5f\u53eb\u9493\u9c7c\u90ce\u3002 \u9e1f\u7c7b\u3002\u4f53\u957f\u7ea615\u5398\u7c73\u3002\u5934\u5927\uff0c\u4f53\u5c0f\uff0c\u5599\u5c16\u786c\u3002\u7fbd\u6bdb\u4ee5\u82cd\u7fe0\u3001\u6697\u7eff\u8272\u4e3a\u4e3b\uff0c\u5c3e\u7fbd\u77ed\u3002\u5e38\u6816\u606f\u4e8e\u6c34\u8fb9\u6811\u679d\u6216\u5ca9\u77f3\u4e0a\uff0c\u5f85\u9c7c\u867e\u6e38\u8fd1\u6c34\u9762\uff0c\u7a81\u7136\u5544\u53d6\u3002\u662f\u4e2d\u56fd\u4e1c\u90e8\u3001\u5357\u90e8\u5e38\u89c1\u7684\u7559\u9e1f\u3002'},
        u'\u4e4c\u9e26': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/4_blackbird%E4%B9%8C%E9%B8%A6.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A09Z%2F-1%2F%2F3ba820f732f58d67a01a0c137d2f8d4a9a94512e3fd680415ffa5bacf807915d',
            'name': u'\u4e4c\u9e26',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/4_blackbird%E4%B9%8C%E9%B8%A6.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A53Z%2F-1%2F%2F71d439537c1d65573d9150bb3e3ad9abc7a874b7fff86c39bc80e097eb494821',
            'desc': u'\u9e1f\uff0c\u5634\u5927\u800c\u76f4\uff0c\u5168\u8eab\u7fbd\u6bdb\u9ed1\u8272\uff0c\u7fc5\u8180\u6709\u7eff\u5149\u3002\u591a\u7fa4\u5c45\u5728\u6811\u6797\u4e2d\u6216\u7530\u91ce\u95f4\uff0c\u4ee5\u8c37\u7269\u3001\u679c\u5b9e\u3001\u6606\u866b\u7b49\u4e3a\u98df\u7269\u3002\u6709\u7684\u5730\u533a\u53eb\u8001\u9e39\u3001\u8001\u9e26\u3002'},
        u'\u888b\u9f20': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/65_kangaroo%E8%A2%8B%E9%BC%A0.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A58Z%2F-1%2F%2Ff4d10d39a723e87c0d1393eaee477043569cd399ff263128cf585b0289ded326',
            'name': u'\u888b\u9f20',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/65_kangaroo%E8%A2%8B%E9%BC%A0.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A17Z%2F-1%2F%2F2003f92a45997625de1a4b923641a514e64a5494bf6d41edf6aa77ede0facf0c',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u524d\u80a2 \u77ed\u5c0f\uff0c\u540e\u80a2\u7c97\u5927\uff0c\u5584\u4e8e\u8df3\u8dc3\u3002\u5c3e\u7c97\u5927\uff0c\u80fd\u652f\u6301\u8eab\u4f53\u3002\u96cc\u7684\u8179\u90e8\u6709\u80b2\u513f\u888b\uff0c\u80ce\u513f\u53d1\u80b2\u672a\u5b8c\u5168\u5373\u751f\u4ea7\uff0c\u5728\u80b2 \u513f\u888b\u5185\u54fa\u80b2\u3002\u4ee5\u690d\u7269\u4e3a\u98df\u3002\u5206\u5e03\u4e8e\u6fb3\u5927\u5229\u4e9a\u3002'},
        u'\u9e45': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/41_geese%E9%B9%85.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A49Z%2F-1%2F%2F063cffe18cb8a395a976151701329d24ea118b8791758eb8084911f6e1cd73e1',
            'name': u'\u9e45',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/41_geese%E9%B9%85.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2Fc241827652926a5ffcc0678feeb2b33915af169a85cfee6b3b49bf1cf9105dc9',
            'desc': u'\u5bb6\u79bd\uff0c\u7fbd\u6bdb\u767d\u8272\u6216\u7070\u8272\uff0c\u989d\u90e8\u6709\u6a59\u9ec4\u8272\u6216\u9ed1\u8910\u8272\u8089\u8d28\u7a81\u8d77\uff0c\u96c4\u7684\u7a81\u8d77\u8f83\u5927\u3002\u9888\u957f\uff0c\u5634\u6241\u800c\u9614\uff0c\u811a\u6709\u8e7c\uff0c\u80fd\u6e38\u6cf3\uff0c\u8010\u5bd2\uff0c\u5403\u9752\u8349\u3001\u8c37\u7269\u3001\u852c\u83dc\u3001\u9c7c\u867e\u7b49\u3002'},
        u'\u6c34\u725b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/62_buffalo%E6%B0%B4%E7%89%9B.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A13Z%2F-1%2F%2F573a9b9c9a0966361bfbc131b824f953929ab9fb7b8c3e074d8775fc9de28817',
            'name': u'\u6c34\u725b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/62_buffalo%E6%B0%B4%E7%89%9B.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A17Z%2F-1%2F%2F96fda97b0df734137c17a1b5a07de39ef1a871600cccc4a86e48064c305039c5',
            'desc': u'\u725b\u7684\u4e00\u79cd\uff0c\u89d2\u7c97\u5927\u5f2f\u66f2\uff0c\u4f5c\u65b0\u6708\u5f62\uff0c\u6bdb\u7070\u9ed1\u8272\uff0c\u6691\u5929\u559c\u6b22\u6d78\u5728\u6c34\u4e2d\uff0c\u5403\u9752\u8349\u7b49\u3002\u9002\u4e8e\u6c34\u7530\u8015\u4f5c\u3002'},
        u'\u7f9a\u7f8a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/61_antelope%E7%BE%9A%E7%BE%8A.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A13Z%2F-1%2F%2F863fa83614f29d664b34ada7db3a28e06c33cb8e63a38cc44cbfb030e0514cc4',
            'name': u'\u7f9a\u7f8a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/61_antelope%E7%BE%9A%E7%BE%8A.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A16Z%2F-1%2F%2Fdfd2731dffd82454bede58854b64bd4021c3ca7d242390c018cebec96c7c41a4',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u5f62\u72b6\u7565\u50cf\u5c71\u7f8a\uff0c\u4f46\u89d2\u7ec6\u5706\u6709\u8282\u3002\u751f\u6d3b\u5728\u8349\u539f\u548c\u534a\u8352\u6f20\u5730\u533a\u3002\u79cd\u7c7b\u8f83\u591a\uff0c\u4ea7\u4e8e\u4e2d\u56fd\u7684\u6709\u9ad8\u9f3b\u7f9a\u7f8a\u3001\u539f\u7f9a\u3001\u9e45\u5589\u7f9a\u548c\u85cf\u7f9a\u7b49\u3002\u662f\u4e2d\u56fd\u56fd\u5bb6\u91cd\u70b9\u4fdd\u62a4\u52a8\u7269\u3002'},
        u'\u91ce\u9e21': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/28_pheasant%E9%87%8E%E9%B8%A1.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A43Z%2F-1%2F%2F09b4a1f05ce6c103349466c21325281ecf2dc726529445e40cca56d03aafb771',
            'name': u'\u91ce\u9e21',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/28_pheasant%E9%87%8E%E9%B8%A1.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A56Z%2F-1%2F%2F441f33ece2225355b9e7e160c14b2912778c3a375a09ab872fdf73c485b56744',
            'desc': u'\u91ce\u9e21\u53c8\u540d\u96c9\u9e21\u3001\u4e03\u5f69\u9526\u9e21\u3001\u5c71\u9e21\u7b49\uff0c\u96c6\u8089\u7528\u3001\u89c2\u8d4f\u548c\u836f\u7528\u4e8e\u4e00\u8eab\u7684\u540d\u8d35\u91ce\u5473\u73cd\u79bd'},
        u'\u7334\u5b50': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/51_Monkey%E7%8C%B4%E5%AD%90.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A14Z%2F-1%2F%2Fdfcc89b963310c1ad25f4456ddd3dd34a2273021428475aabad45f5356e5f520',
            'name': u'\u7334\u5b50',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/51_Monkey%E7%8C%B4%E5%AD%90.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A15Z%2F-1%2F%2Fcf5230d272f2e29b135787e65057c755be00952ad4975de8c7acc3f36e3ce054',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u79cd\u7c7b\u5f88\u591a\uff0c\u5916\u5f62\u7565\u50cf\u4eba\uff0c\u8eab\u4e0a\u6709\u6bdb\uff0c\u591a\u4e3a\u7070\u8272\u6216\u8910\u8272\uff0c\u6709\u5c3e\u5df4\uff0c\u884c\u52a8\u7075\u6d3b\uff0c\u597d\u7fa4\u5c45\uff0c\u53e3\u8154\u6709\u50a8\u5b58\u98df\u7269\u7684\u988a\u56ca\uff0c\u5403\u679c\u5b9e\u3001\u91ce\u83dc\u3001\u9e1f\u5375\u548c\u6606\u866b\u7b49\u3002\u901a\u79f0\u7334\u5b50\u3002'},
        u'\u677e\u9f20': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/33_squirrel%E6%9D%BE%E9%BC%A0.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A46Z%2F-1%2F%2F16ca5e9219b3633bb69743ddda64dea1d809c92fbd2abb3ab7231c07ea297090',
            'name': u'\u677e\u9f20',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/33_squirrel%E6%9D%BE%E9%BC%A0.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2Fe18d4ccb6dbe8721eb26236417daba30349f1e3e7dc56ba57d24c46c5a078522',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u3002\u5916\u5f62\u7565\u50cf\u9f20\uff0c\u6bd4\u9f20\u5927\uff0c\u5c3e\u84ec\u677e\u800c\u7279\u522b\u957f\u5927\uff0c\u5584\u8df3\u8dc3\u3002\u751f\u6d3b\u5728\u677e\u6797\u4e2d\uff0c\u98df\u5e72\u679c\u3001\u6d46\u679c\u548c\u5ae9\u53f6\u7b49\u3002'},
        u'\u7280\u725b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/54_rhino%E7%8A%80%E7%89%9B.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A09Z%2F-1%2F%2F19bdda0515504cedf30c1cfcd65c8d5bfc6270a7b69dbcae2da254d229974ae4',
            'name': u'\u7280\u725b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/54_rhino%E7%8A%80%E7%89%9B.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A16Z%2F-1%2F%2F7d702a259e0d643c895383beb72279947514021362066f74e887a30b2e955705',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u5916\u5f62\u7565\u50cf\u725b\uff0c\u9888\u77ed\uff0c\u56db\u80a2\u7c97\u5927\uff0c\u9f3b\u5b50\u4e0a\u6709\u4e00\u4e2a\u6216\u4e24\u4e2a\u89d2\u3002\u76ae\u7c97\u800c\u539a\uff0c\u5fae\u9ed1\u8272\uff0c\u6ca1\u6709\u6bdb\u3002\u751f\u6d3b\u4e8e\u4e9a\u6d32\u548c\u975e\u6d32\u7684\u70ed\u5e26\u68ee\u6797\u91cc\uff0c\u5403\u690d\u7269\u3002'},
        u'\u9e2c\u9e5a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/96_cormorant%E9%B8%AC%E9%B9%9A.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A28Z%2F-1%2F%2F2d12c4e1b34c2b1430e177766113f392d13fda1b6c810c05e20304605c4e68fd',
            'name': u'\u9e2c\u9e5a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/96_cormorant%E9%B8%AC%E9%B9%9A.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2Fc890ac6db7f3f87ee7a4b4b63d1571d3b131a0c1665fb07e4f0277489f086a66',
            'desc': u'\u6c34\u9e1f\uff0c\u7fbd\u6bdb\u9ed1\u8272\uff0c\u6709\u7eff\u3001\u84dd\u3001\u7d2b\u8272\u5149\u6cfd\uff0c\u5634\u6241\u800c\u957f\uff0c\u6697\u9ed1\u8272\uff0c\u4e0a\u5634\u7684\u5c16\u7aef\u6709\u94a9\u3002 \u80fd\u6e38\u6cf3\uff0c\u5584\u4e8e\u6355\u9c7c\uff0c\u5589\u4e0b\u7684\u76ae\u80a4\u6269\u5927\u6210\u56ca\u72b6\uff0c\u6355\u5f97\u9c7c\u53ef\u4ee5\u653e\u5728\u56ca\u5185\u3002\u6211\u56fd\u5357\u65b9\u591a\u9972\u517b\u6765\u5e2e\u52a9\u6355\u9c7c\u3002\u901a\u79f0\u9c7c\u9e70\uff0c\u6709\u7684\u5730\u533a\u53eb\u58a8\u9e26'},
        u'\u6d77\u8c79': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/90_seal%E6%B5%B7%E8%B1%B9.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A25Z%2F-1%2F%2F5b93c3f88ee5a2dea6591ff44493825541961dbb09b440095a1a917198d64cdf',
            'name': u'\u6d77\u8c79',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/90_seal%E6%B5%B7%E8%B1%B9.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2F357ba9c7d5e114f49ac4d8ccbcf7782d7f1e93104358c89fe811415a8d62e857',
            'desc': u'\u54fa\u4e73\u52a8\u7269\u7684\u4e00\u79d1\u3002\u6709\u8bb8\u591a\u79cd\u3002\u4f53\u578b\u5927\u5c0f\u4e0d\u4e00\uff0c\u4e00\u822c\u957f\u7ea61.5\u7c73\uff0c\u6700\u5927\u7684\u8c61\u6d77\u8c79\u4f53\u957f\u53ef\u8fbe5\u20146\u7c73\u3002\u56db\u80a2\u5448\u9ccd\u72b6\u3002\u6e38\u901f\u5feb\uff0c\u5584\u6f5c\u6c34\u3002\u751f\u6d3b\u5728\u6e29\u5e26\u548c\u5bd2\u5e26\u6cbf\u6d77\u5730\u533a\uff0c\u591a\u6570\u5728\u5317\u534a\u7403\u3002\u4e3b\u98df\u9c7c\u7c7b\u548c\u8d1d\u7c7b\u3002'},
        u'\u8001\u9f20': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/43_mouse%E8%80%81%E9%BC%A0.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A50Z%2F-1%2F%2Fead36b833f4bd8999c1a530d6ddcaab6b1e62162859897d8613d8f192bffe206',
            'name': u'\u8001\u9f20',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/43_mouse%E8%80%81%E9%BC%A0.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A58Z%2F-1%2F%2F9a8fdc3f65a8b825eac522564cbd0643609152c52a9fb0de11384e37b907cc5a',
            'desc': u'\u8001\u9f20\u662f\u54fa\u4e73\u7eb2\u3001\u556e\u9f7f\u76ee\u3001\u9f20\u79d1\u7684\u556e\u9f7f\u7c7b\u52a8\u7269\uff0c\u4fd7\u79f0\u201c\u8017\u5b50\u201d\uff0c\u662f\u54fa\u4e73\u52a8\u7269\u4e2d\u7e41\u6b96\u6700\u5feb\u3001\u751f\u5b58\u80fd\u529b\u5f88\u5f3a\u7684\u52a8\u7269\u3002'},
        u'\u98de\u86fe': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/121_moth-%E9%A3%9E%E8%9B%BE.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A14Z%2F-1%2F%2Fb3f99797ede95a3a4dbca7a4d3027475dd4ee8bf2abf8caed720d95bda996fdf',
            'name': u'\u98de\u86fe',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/121_moth-%E9%A3%9E%E8%9B%BE.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A49Z%2F-1%2F%2Fc85785efaaa8c1177b23b1d2e1741c2a8eb4c87b9dc662227b785443bda8b813',
            'desc': u'\u98de\u86fe\u7c7b\uff0c\u6606\u866b\u7eb2\u9cde\u7fc5\u76ee\u6606\u866b\uff0c\u591a\u5728\u591c\u95f4\u6d3b\u52a8\uff0c\u559c\u6b22\u5728\u5149\u4eae\u5904\u805a\u96c6\uff0c'},
        u'\u7266\u725b': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/38_Yak%E7%89%A6%E7%89%9B.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A49Z%2F-1%2F%2Fb548107cf14ba0468bb98d68273d5150b8ad217dd6ce14075e2c1e9c9b702c40',
            'name': u'\u7266\u725b',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/38_Yak%E7%89%A6%E7%89%9B.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A57Z%2F-1%2F%2F21104bfadc6de70b2f705af8c0d618ccf9aef4630b41362bda950db7a62d0cac',
            'desc': u'\u725b\u7684\u4e00\u79cd\uff0c\u5168\u8eab\u6709\u957f\u6bdb\uff0c\u9ed1\u8910\u8272\u3001\u68d5\u8272\u6216\u767d\u8272\uff0c\u817f\u77ed\u3002\u662f\u6211\u56fd\u9752\u85cf\u9ad8\u539f\u5730\u533a\u7684\u4e3b\u8981\u529b\u755c\u3002'},
        u'\u4fe1\u5929\u7fc1': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/104_albatross%E4%BF%A1%E5%A4%A9%E7%BF%81.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A33%3A07Z%2F-1%2F%2Fe139998f2830e72ef30505a4d517dfff3f5fc5f49d744eff10b32719c565540e',
            'name': u'\u4fe1\u5929\u7fc1',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/104_albatross%E4%BF%A1%E5%A4%A9%E7%BF%81.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A47Z%2F-1%2F%2Faa4ee15ef1c073c6637fb3a70b6939533b6a05970e55921a65fdc9f839a56967',
            'desc': u'\u9e1f\uff0c\u4f53\u957f\u53ef\u8fbe1\u7c73\u4ee5\u4e0a\uff0c\u662f\u98de\u884c\u9e1f\u7c7b\u4e2d\u4f53\u5f62\u6700\u5927\u7684\uff0c\u5584\u4e8e\u98de\u884c\uff0c\u8dbe\u95f4\u6709\u8e7c\uff0c\u80fd\u6e38\u6cf3\u3002\u751f\u6d3b\u5728\u6d77\u8fb9\uff0c\u6355\u98df\u9c7c\u7c7b\u3002\u6709\u77ed\u5c3e\u4fe1\u5929\u7fc1\u548c\u9ed1\u811a\u4fe1\u5929\u7fc1\u3002'},
        u'\u53d8\u8272\u9f99': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/6_chameleon%E5%8F%98%E8%89%B2%E9%BE%99.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A11Z%2F-1%2F%2F7ec9f2017d64ba8dc9c49a5a5d453bb943a3da734d04d10653d72103b18f00ba',
            'name': u'\u53d8\u8272\u9f99',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/6_chameleon%E5%8F%98%E8%89%B2%E9%BE%99.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A54Z%2F-1%2F%2F049fd76d027f70737629b88fcde8acda8e655c2914db38edb4cf08afe6206d61',
            'desc': u'\u810a\u690e\u52a8\u7269\uff0c\u8eaf\u5e72\u7a0d\u6241\uff0c\u76ae\u7c97\u7cd9\uff0c\u56db\u80a2\u7a0d\u957f\uff0c\u8fd0\u52a8\u6781\u6162\u3002\u820c\u957f\uff0c\u53ef\u8214\u98df\u866b\u7c7b\u3002\u8868\u76ae\u4e0b\u6709\u591a\u79cd\u8272\u7d20\u5757\uff0c\u80fd\u968f\u65f6\u53d8\u6210\u4e0d\u540c\u7684\u4fdd\u62a4\u8272\u3002'},
        u'\u8c79': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/22_leopard%E8%B1%B9.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A29%3A38Z%2F-1%2F%2F63148803b8f16a6c4071c656be4753bdfaa776baab4b6f7fc06447d6ebc7d6fb',
            'name': u'\u8c79',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/22_leopard%E8%B1%B9.jpg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A20%3A56Z%2F-1%2F%2Fdfd3a4fa050b95a6e51a93473cd7f8b7dd03fd1603daa06a8b67fd58c20cb9cf',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u50cf\u864e\u800c\u8f83\u5c0f\uff0c\u8eab\u4e0a\u6709\u5f88\u591a\u6591\u70b9\u6216\u82b1\u7eb9\u3002\u6027\u51f6\u731b\uff0c\u80fd\u4e0a\u6811\uff0c\u6355\u98df\u5176\u4ed6\u517d\u7c7b\uff0c\u4f24\u5bb3\u4eba\u755c\u3002\u5e38\u89c1\u7684\u6709\u91d1\u94b1\u8c79\u3001\u4e91\u8c79\u3001\u96ea\u8c79\u3001\u730e\u8c79\u7b49\u3002\u901a\u79f0\u8c79\u5b50'},
        u'\u9e66\u9e49': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/93_Parrot%E9%B9%A6%E9%B9%89.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A27Z%2F-1%2F%2F6a499da589ea7f8699937c526fd38e747e1c4240170ceefb49b1dc47e18ba724',
            'name': u'\u9e66\u9e49',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/93_Parrot%E9%B9%A6%E9%B9%89.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A20Z%2F-1%2F%2Fb0b414f215028c1cc793b2bad353d33b05af457182618ec57fd43512308ab6c6',
            'desc': u'\u9e1f\uff0c\u5934\u90e8\u5706\uff0c\u4e0a\u5634\u5927\uff0c\u5448\u94a9\u72b6\uff0c\u4e0b\u5634\u77ed\u5c0f\uff0c\u7fbd\u6bdb\u7f8e\u4e3d\uff0c\u6709\u767d\u3001\u8d64\u3001\u9ec4\u3001\u7eff\u7b49\u8272\u3002\u751f\u6d3b\u5728\u70ed\u5e26\u6811\u6797\u91cc\uff0c\u5403\u679c\u5b9e\u3002\u80fd\u6a21\u4eff\u4eba\u8bf4\u8bdd\u7684\u58f0\u97f3\u3002'},
        u'\u6d77\u8c5a': {
            'sound': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/89_Dolphin%E6%B5%B7%E8%B1%9A.wav?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-11-05T12%3A31%3A25Z%2F-1%2F%2F57846142a6624e144363ac56afaf8d48ee8e4cff06a71828530024e96b90358f',
            'name': u'\u6d77\u8c5a',
            'img': 'http://dbp-resource.gz.bcebos.com/3b759ccf-2686-803d-bd94-d7847a94fbda/89_Dolphin%E6%B5%B7%E8%B1%9A.jpeg?authorization=bce-auth-v1%2Fa4d81bbd930c41e6857b989362415714%2F2018-09-29T09%3A21%3A19Z%2F-1%2F%2F7ed460b29cfc1eec114ab4aae33e9012a16cbd2e573ffab0b460b73538ebe1fc',
            'desc': u'\u54fa\u4e73\u52a8\u7269\uff0c\u8eab\u4f53\u7eba\u9524\u5f62\uff0c\u957f\u8fbe2\u7c73\u591a\uff0c\u9f3b\u5b54\u957f\u5728\u5934\u9876\u4e0a\uff0c\u5599\u7ec6\u957f\uff0c\u524d\u80a2\u5448\u9ccd\u72b6\uff0c\u80cc\u9ccd\u4e09\u89d2\u5f62\u3002\u80cc\u90e8\u9752\u9ed1\u8272\uff0c\u8179\u90e8\u767d\u8272\u3002\u751f\u6d3b\u5728\u6d77\u6d0b\u4e2d\uff0c\u5403\u9c7c\u3001\u4e4c\u8d3c\u3001\u867e\u7b49\u3002'}}

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


import sys
import Constants

sys.modules[__name__] = _Constants()


def createAnimalList():
    filename = 'animal_sounds_v2.csv'
    animals = dict()
    names = list()
    with open(filename, 'rU') as file:
        reader = csv.reader(file)
        head = next(reader)
        for item in reader:
            (name, desc, img, sound) = item
            name = name.decode('utf-8')
            desc = desc.decode('utf-8')
            print(name)
            names.append(name)
            animal = {'name': name, 'desc': desc, 'img': img, 'sound': sound}
            animals[name] = animal
    print(animals)
    return animals


if __name__ == '__main__':
    assert (Constants.ANIMALS == createAnimalList())
