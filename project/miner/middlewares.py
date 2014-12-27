__author__ = 'Hamid FzM'

# python import
import random

from scrapy import log


# project import
from settings import USER_AGENT_LIST


class RandomUserAgentMiddleware(object):
    @staticmethod
    def process_request(request, spider):
        # if random.choice(xrange(1, 100)) <= 30:
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)
            log.msg('Changing UserAgent to %s' % ua)