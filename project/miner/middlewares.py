__author__ = 'Hamid FzM'

# python import
import random
import time
import telnetlib

from scrapy import log


# project import
from settings import USER_AGENT_LIST


class RetryChangeProxyMiddleware(object):
    @staticmethod
    def process_request(request, spider):
        # set password for tor with this command: tor --hash-password password
        # enable control port using this command: tor --controlport 9051
        # if random.choice(xrange(1, 100)) <= 15:
        log.msg('Changing proxy')
        tn = telnetlib.Telnet('127.0.0.1', 9051)
        tn.read_until("Escape character is '^]'.", 2)
        tn.write('AUTHENTICATE "hamidfzmcrawler"\r\n')
        tn.read_until("250 OK", 2)
        tn.write("signal NEWNYM\r\n")
        tn.read_until("250 OK", 2)
        tn.write("quit\r\n")
        tn.close()
        log.msg('>>>> Proxy changed. Sleep Time')
        time.sleep(10)


class RandomUserAgentMiddleware(object):
    @staticmethod
    def process_request(request, spider):
        # if random.choice(xrange(1, 100)) <= 30:
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)
            log.msg('Changing UserAgent to %s' % ua)