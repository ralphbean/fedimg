#!/bin/env python
# -*- coding: utf8 -*-

"""
You must have fedmsg-relay installed to your system and started
via `systemctl start fedmsg-relay` in order to use this script.
"""

import fedmsg
import requests

fedmsg.init(active=True, name="relay_inbound")

idx = '2014-707e188d-fc5e-4c9a-a4a2-9499beaafffe'

datagrepper_url = 'https://apps.fedoraproject.org/datagrepper/id?id=%s' % idx

resp = requests.get(datagrepper_url)
msg = resp.json()

tokens = msg['topic'].split('.')
modname = tokens[3]
topic = '.'.join(tokens[4:])

print "Faking {}\n".format('.'.join(tokens))

fedmsg.publish(modname=modname, topic=topic, msg=msg['msg'])
