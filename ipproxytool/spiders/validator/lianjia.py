#-*- coding: utf-8 -*-

from validator import Validator


class LianJiaSpider(Validator):
    name = 'lianjia'
    concurrent_requests = 8

    def __init__(self, name = None, **kwargs):
        super(LianJiaSpider, self).__init__(name, **kwargs)

        self.urls = [
            'https://bj.lianjia.com/ershoufang/'
        ]

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.110 Safari/537.36',
        }

        self.success_mark = 'dongcheng'
        self.is_record_web_page = False
        self.init()
