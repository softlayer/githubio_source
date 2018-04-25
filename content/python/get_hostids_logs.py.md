---
title: "get_hostids_logs.py"
description: "get_hostids_logs.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_Software_Component_HostIpsInitParameters"
    - "SoftLayer_Software_Component_HostIps"
    - "SoftLayer_Software_Component_HostIpsObjectMask"
tags:
    - "security"
---


```
"""
Get the host IDS logs.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_HostIps
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_HostIps/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Software_Component_HostIps

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

hostidsId = 2665230

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
hostidsService = client['SoftLayer_Software_Component_HostIps']

objectMask = "mask[ipsEvents[signature],blockedApplicationEvents]"

try:
    response = hostidsService.getObject(id=hostidsId, mask=objectMask)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the logs. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

"""
Note: currently the ipsEvents and blockedApplicationEvents are not
visible via REST customer needs to use a SOAP request.

<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns="http://www.w3.org/2001/XMLSchema-instance" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <SOAP-ENV:Header>
    <authenticate xsi:type="ns1:authenticate">
      <username xsi:type="xsd:string">username</username>
      <apiKey xsi:type="xsd:string">token</apiKey>
    </authenticate>
    <ns1:SoftLayer_Software_Component_HostIpsInitParameters xmlns:default="http://www.w3.org/2001/XMLSchema-instance" default:type="ns1:SoftLayer_Software_Component_HostIpsInitParameters">
      <id>6114923</id>
    </ns1:SoftLayer_Software_Component_HostIpsInitParameters>
    <ns1:SoftLayer_Software_Component_HostIpsObjectMask>
      <mask>
        <ipsEvents>
          <signature/>
        </ipsEvents>
        <blockedApplicationEvents/>
        <virtualGuest>
          <managedResourceFlag/>
        </virtualGuest>
      </mask>
    </ns1:SoftLayer_Software_Component_HostIpsObjectMask>
  </SOAP-ENV:Header>
  <SOAP-ENV:Body>
    <ns1:getObject/>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""

```
