__author__ = 'Hamid FzM'

# python import
import random
from scrapy import log

# project import
from miner.settings import USER_AGENT_LIST


# 30% user agent change
class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        if random.choice(xrange(1, 100)) <= 30:
            log.msg('Changing UserAgent')
            ua = random.choice(USER_AGENT_LIST)
            if ua:
                request.headers.setdefault('User-Agent', ua)
            log.msg('>>>> UserAgent changed')