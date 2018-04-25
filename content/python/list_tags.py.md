---
title: "list_tags.py"
description: "list_tags.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "tags"
---


```
"""
List the tags for a VSI

The scripts list all the tags set in an arbitrary  VSI,
it uses the SoftLayer_Virtual_Guest::getTagReferences method
to get the tags. For more information please see below

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/getTagReferences

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username and API key.
USERNAME = 'set me'
API_KEY = 'set me'

# The virtual guestId you wish to get the tags
virtualGuestId = 7844984

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

# Send the request to get the tags
try:
    result = virtualGuestService.getTagReferences(id=virtualGuestId)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to list the tags faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
