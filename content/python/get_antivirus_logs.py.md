---
title: "Anti-virus"
description: "Some examples for working with the Anti-Virus software."
date: "2017-11-23"
classes: 
    - "SoftLayer_Software_Component_AntivirusSpyware"
    - "SoftLayer_Software_Component_AntivirusSpywareObjectMask"
    - "SoftLayer_Software_Component_AntivirusSpywareInitParameters"
tags:
    - "security"
---


```python
"""
Get the anti-virus logs.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_AntivirusSpyware
http://sldn.softlayer.com/reference/services/SoftLayer_Software_Component_AntivirusSpyware/getObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Software_Component_AntivirusSpyware

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""

import SoftLayer
import json

# Your SoftLayer API username and key.
USERNAME = 'set me'
API_KEY = 'set me'

antivirusSpywareId = 2665230

client = SoftLayer.Client(username=USERNAME, api_key=API_KEY)
antivirusSpywareService = client['SoftLayer_Software_Component_AntivirusSpyware']

objectMask = "mask[latestAccessProtectionEvents,latestAntivirusEvents[virusActionTaken]]"

try:
    response = antivirusSpywareService.getObject(id=antivirusSpywareId, mask=objectMask)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the logs. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

"""
Note: currently the latestAccessProtectionEvents and latestAntivirusEvents are not
visible via REST customer needs to use a SOAP request.

<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://api.service.softlayer.com/soap/v3/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns="http://www.w3.org/2001/XMLSchema-instance" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
  <SOAP-ENV:Header>
    <authenticate xsi:type="ns1:authenticate">
      <username xsi:type="xsd:string">username</username>
      <apiKey xsi:type="xsd:string">token</apiKey>
    </authenticate>
    <ns1:SoftLayer_Software_Component_AntivirusSpywareInitParameters xmlns:default="http://www.w3.org/2001/XMLSchema-instance" default:type="ns1:SoftLayer_Software_Component_AntivirusSpywareInitParameters">
      <id>2665230</id>
    </ns1:SoftLayer_Software_Component_AntivirusSpywareInitParameters>
    <ns1:SoftLayer_Software_Component_AntivirusSpywareObjectMask>
      <mask>
        <latestAntivirusEvents>
          <virusActionTaken/>
        </latestAntivirusEvents>
        <latestAccessProtectionEvents/>
      </mask>
    </ns1:SoftLayer_Software_Component_AntivirusSpywareObjectMask>
  </SOAP-ENV:Header>
  <SOAP-ENV:Body>
    <ns1:getObject/>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""

```

### Spyware for servers

```python
"""
Get the anti-virus and spywares for the servers in the account.

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

objectMask = "mask[antivirusSpywareSoftwareComponent, operatingSystem]"

try:
    response = accountService.getHardware(mask=objectMask)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the servers.. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

"""
Note: currently the antivirusSpywareSoftwareComponent is not
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
          <antivirusSpywareSoftwareComponent/>
        </hardware>
      </mask>
    </ns1:SoftLayer_AccountObjectMask>
  </SOAP-ENV:Header>
  <SOAP-ENV:Body>
    <ns1:getHardware/>
  </SOAP-ENV:Body>
"""

```


### Spyware for VSI

```python
"""
Get the anti-virus and spywares for the VSIs in the account.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Account
http://sldn.softlayer.com/reference/services/SoftLayer_Account/getVirtualGuests

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

objectMask = "mask[antivirusSpywareSoftwareComponent, operatingSystem]"

try:
    response = accountService.getVirtualGuests(mask=objectMask)
    print(json.dumps(response, sort_keys=True, indent=2, separators=(',', ': ')))
except SoftLayer.SoftLayerAPIError as e:
    print("Unable to get the VSIs.. faultCode=%s, faultString=%s" % (e.faultCode, e.faultString))

"""
Note: currently the antivirusSpywareSoftwareComponent is not
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
        <virtualGuest>
          <datacenter/>
          <operatingSystem/>
          <antivirusSpywareSoftwareComponent/>
        </virtualGuest>
      </mask>
    </ns1:SoftLayer_AccountObjectMask>
  </SOAP-ENV:Header>
  <SOAP-ENV:Body>
    <ns1:getVirtualGuests/>
  </SOAP-ENV:Body>
"""

```