__author__ = 'Hamid FzM'

from scrapy import cmdline
from sys import argv

# scrapy startproject miner

if __name__ == '__main__':
    if argv[1:]:
        cmdline.execute(argv)
    else:
        cmdline.execute(['scrapy', 'shell'])