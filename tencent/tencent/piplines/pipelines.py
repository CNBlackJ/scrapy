# -*- coding: utf-8 -*-
from tencent.cassdb.connect import connect

import uuid
import time
from cassandra.cqlengine import columns
from datetime import datetime
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.models import Model

session = connect(['192.168.99.100'], "news", 12345)


# keyspace = 'news'
#
# # session.execute(
# #     "CREATE KEYSPACE IF NOT EXISTS %s "
# #     "WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 3 };"
# #     % keyspace
# # )
# session.set_keyspace(keyspace)
#
# session.execute(
#     "create columnfamily if not exists news ("
#     "title varchar primary key,"
#     "description varchar,"
#     "link varchar,"
#     "published varchar)"
# )


class TencentModel(Model):
    title = columns.Text(primary_key=True)
    description = columns.Text()
    link = columns.Text()
    published = columns.Text()


sync_table(TencentModel)


class TencentPipeline(object):
    def process_item(self, item, spider):
        TencentModel.create(title=item['title'],
                            description=item['desc'],
                            link=item['link'],
                            published=item['published'])
        return item
