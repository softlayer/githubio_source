---
title: "set_tags.py"
description: "set_tags.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "tags"
---


```
"""
Set tags for a VSI

The script sets the tags for an arbitrary VSI,
it makes a single call to the SoftLayer_Virtual_Guest::setTags method
For more information please see below.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setTags

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

# The virtual guestID you wish to get the tags
virtualGuestId = 7844984

# The list of tags you wish to set to the VSI
tags = "mytag1,mytag2,mytag3"

# Send the request to get the tags
try:
    result = virtualGuestService.setTags(tags, id=virtualGuestId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to set the tags faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
