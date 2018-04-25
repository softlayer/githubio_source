---
title: "set_tags_virtual_server.py"
description: "set_tags_virtual_server.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Virtual_Guest"
tags:
    - "virtualserver"
---


```
"""
Set tags to a virtual server

The script set the tags for an arbitrary VSI
it makes a single call to the SoftLayer_Virtual_Guest::setTags
for more information see below.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/setTags

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# Your SoftLayer API username and key.
API_USERNAME = 'set me'

# Generate one at https://control.softlayer.com/account/users
API_KEY = 'set me'

# the virtual guest ID where you wish to add the tags
virtualGuestID = 35747489

# the tags you wish to add
tags = "tag1,tag2,tag3"

client = SoftLayer.create_client_from_env(username=API_USERNAME, api_key=API_KEY)
virtualGuestService = client['SoftLayer_Virtual_Guest']

try:
    result = virtualGuestService.setTags(tags, id=virtualGuestID)
    print (result)
except SoftLayer.SoftLayerAPIError as e:
    """
    If there was an error returned from the SoftLayer API then bomb out with the
    error message.
    """
    print("Unable to set the tags"
          % (e.faultCode, e.faultString))

```
