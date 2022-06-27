from pars import news_parser

URL = 'https://www.autocentre.ua/avtosport'

news_list = {"news": news_parser(URL)[0].title,
             "url": news_parser(URL)[0].url,
             "img": news_parser(URL)[0].img}
