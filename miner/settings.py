# -*- coding: utf-8 -*-

# Scrapy settings for miner project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
# http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'miner'

SPIDER_MODULES = ['miner.spiders']
NEWSPIDER_MODULE = 'miner.spiders'


DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'miner.middlewares.RandomUserAgentMiddleware': 100,
}

# Got this list from http://www.user-agents.org/
USER_AGENT_LIST = ('Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (FM Scene 4.6.1)',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729) (Prevx 3.0.5)',
                   'GenesisBrowser (HTTP 1.1; 0.9; XP SP2; .NET CLR 2.0.50727)',
                   'GreenBrowser',
                   'Haier-T10C/1.0 iPanel/2.0 WAP2.0 (compatible; UP.Browser/6.2.2.4; UPG1; UP/4.0; Embedded)',
                   'IBrowse/2.2 (Windows 3.1)',
                   'Opera/5.0 (Linux 2.0.38 i386; U) [en]',
                   'Opera/5.11 (Windows ME; U) [ru]',
                   'Opera/9.60 (Windows NT 5.1; U; de) Presto/2.1.1',
                   'Opera/9.00 (Windows NT 5.1; U; de)',
                   'Opera/8.xx (Windows NT 5.1; U; en)',
                   'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en-us) AppleWebKit/xxx.x (KHTML like Gecko) Safari/12x.x',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.1 Safari/525.19')