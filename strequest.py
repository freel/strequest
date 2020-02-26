#!/usr/bin/python

import http.client
import random
import time

url = '104.155.141.20'
ports = [19200,80]
endpoints = ['_cluster/health', '_nodes/health']
params = {'pretty'}

while True:
    port = random.choice(ports)
    endpoint = random.choice(endpoints)
    conn = http.client.HTTPConnection('{}:{}'.format(url, port))
    conn.request("GET", '/{}?pretty'.format(endpoint))
    print(conn.port)
    r = conn.getresponse()
    data = r.read()
    print(data)
    with open('responses.log', 'a+') as f:
        f.write('{}\n'.format(data))
    time.sleep(30)
