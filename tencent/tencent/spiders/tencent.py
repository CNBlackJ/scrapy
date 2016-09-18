# coding:utf-8

from scrapy.spiders import XMLFeedSpider
from ..items import TencentItem
from os import path


class TencentFeedSpider(XMLFeedSpider):
    name = 'tencent'
    allowed_domains = ['http://news.qq.com/']
    file_names = [(u'国内新闻', 'newsgn/rss_newsgn'),
                  (u'国际新闻', 'newsgj/rss_newswj'),
                  # (u'社会新闻', 'newsshrss_newssh'),
                  # (u'图片站', 'photon/rss_photo'),
                  # (u'评论站', 'newscomments/rss_comment'),
                  # (u'军事站', 'milite/rss_milit'),
                  # (u'史海钩沉', 'histor/rss_history'),
                  # (u'新闻语录', 'xwyl/rss_xwyl'),
                  # (u'QQ连线', 'lianxian/rss_lx'),
                  # (u'数字说话', 'sash/rss_szsh'),
                  # (u'内幕黑幕', 'nehemu/rss_nmhm'),
                  # (u'人物站', 'person/rss_person'),
                  # (u'即时消息', 'zmd/rss_now'),
                  # (u'地方站-上海', 'bj/rss_bj'),
                  # (u'地方站-广东', 'gd/rss_gd'),
                  # (u'地方站-浙江', 'zj/rss_zj'),
                  # (u'地方站-江苏', 'js/rss_js'),
                  # (u'地方站-山东', 'sd/rss_sd')
                  ]
    func_name = lambda (ns): 'http://news.qq.com/%s.xml' % ns
    start_urls = [func_name(n) for t, n in file_names]

    iterator = 'iternodes'  # This is actually unnecessary, since it's the default value
    itertag = 'item'

    def parse_node(self, response, node):
        category_name = path.basename(response.url).split('.')[0]

        item = TencentItem()
        item['title'] = node.xpath('title/text()').extract_first()
        item['link'] = node.xpath('link/text()').extract_first()
        item['desc'] = node.xpath('description/text()').extract_first()
        item['published'] = node.xpath('pubDate/text()').extract_first()

        for _title, _cat_name in self.file_names:
            if _cat_name == category_name:
                item['category'] = _title
                break

        return item
