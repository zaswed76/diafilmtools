#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

ext = ('png', 'jpg', 'jpeg')
p = "|".join(ext)


string = 'This is a simple test message for 23rq34t.PNG'
string2 = 'test'

pattern1 = re.compile('{}$'.format(p), re.IGNORECASE)
pattern2 = '^test'
pattern3 = '^test$'

print()
