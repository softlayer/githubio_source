---
title: "search_tag.py"
description: "search_tag.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Account"
tags:
    - "tags"
---


```
"""
Search VSI by tag

The script retrieve all the VSIs which contain an
arbitrary list of tags

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
# Example to search tags for a VSI
import SoftLayer.API
from pprint import pprint as pp

# Your SoftLayer API username.
USERNAME = 'set me'
API_KEY = 'set me'

# List of tags to look for
tags = ["mytag1", "tag2"]

# Declare the API client
client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

# Declaring an object filter to get only the virtual servers which contain the tags that we are looking for
objectFilter = {'virtualGuests': {'tagReferences': {'tag': {'name': {'operation': 'in', 'options': [{'name': 'data', 'value': tags}]}}}}}

# Send the request to get the virtual guest using the filter
try:
    result = accountService.getVirtualGuests(filter=objectFilter)
    pp(result)
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to retrieve the virtual guests faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))
    exit(1)

```
