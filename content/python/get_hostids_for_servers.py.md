---
title: "get_hostids_for_servers.py"
description: "get_hostids_for_servers.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_AccountObjectMask"
    - "SoftLayer_Account"
tags:
    - "security"
---


```
"""
Get the host IDS for the servers in the account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getHardware

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
accountService = client['SoftLayer_Account']

objectMask = "mask[hostIpsSoftwareComponent, operatingSystem]"

try:
    response = accountService.getHardware(mask=objectMask)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the servers.. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

"""
Note: currently the hostIpsSoftwareComponent is not
visible via REST customer needs to use a SOAP request.

<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns="http://www.w3.org/2001/XMLSchema-instance" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <SOAP-ENV:Header>
    <authenticate xsi:type="ns1:authenticate">
      <username xsi:type="xsd:string">username</username>
      <apiKey xsi:type="xsd:string">token</apiKey>
    </authenticate>
    <ns1:SoftLayer_AccountObjectMask>
      <mask>
        <hardware>
          <datacenter/>
          <operatingSystem/>
          <hostIpsSoftwareComponent/>
        </hardware>
      </mask>
    </ns1:SoftLayer_AccountObjectMask>
  </SOAP-ENV:Header>
  <SOAP-ENV:Body>
    <ns1:getHardware/>
  </SOAP-ENV:Body>
"""

```
