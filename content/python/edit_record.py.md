---
title: "edit_record.py"
description: "edit_record.py"
date: "2018-04-25"
classes: 
    - "SoftLayer_Dns_Domain_ResourceRecord"
    - "SoftLayer_Dns_Domain"
tags:
    - "dns"
---


```
"""
Edit a Record. It edits an existing domain resource record

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain_ResourceRecord/editObject
http://sldn.softlayer.com/reference/services/SoftLayer_Dns_Domain/getResourceRecords
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain_ResourceRecord
License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = ''
API_KEY = 'apikey_goes_here'

recordId = 55687207

client = SoftLayer.Client(
    username=API_USERNAME,
    api_key=API_KEY)

# Create a object template to edit the Resource Record.
objectTemplate = {
                  "data": "127.2.2.3",
                  "host": "@",
                  "ttl": 900
                  }
try:
    # Edit an existing domain resource record
    result = client['SoftLayer_Dns_Domain_ResourceRecord'].editObject(objectTemplate, id=recordId)
    pp(result)
    
except SoftLayer.SoftLayerAPIError as e:
    pp('Failed ... Unable to edit the record faultCode=%s, faultString=%s'
       % (e.faultCode, e.faultString))

```
