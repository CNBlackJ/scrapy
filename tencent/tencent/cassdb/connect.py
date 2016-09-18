# -*- coding: utf-8 -*-
from cassandra.cqlengine import connection


def connect(ip, keyspace, port):
    # connection.setup(['192.168.99.100'], "demodb", protocol_version=3, port=12345)
    connection.setup(ip, keyspace, protocol_version=3, port=port)
