import os,sys
from scrapy.cmdline import execute


def main():

    sys.path.append(os.path.dirname(os.path.abspath(__file__)))

    execute(['scrapy','crawl','yisaSpider'])

if __name__ == '__main__':
    main()