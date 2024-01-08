---
title: "editObject"
description: "Negotiation parameters for both phases one and two are editable. Here are the phase one and two parameters that can modified: 


*Phase One
**Authentication
***Default value is set to MD5.
***Valid Options are: MD5, SHA1, SHA256.
**Encryption
***Default value is set to 3DES.
***Valid Options are: DES, 3DES, AES128, AES192, AES256.
**Diffie-Hellman Group
***Default value is set to 2.
***Valid Options are: 0 (None), 1, 2, 5.
**Keylife
***Default value is set to 3600.
***Limits are:  MIN = 120, MAX = 172800
**Preshared Key
*Phase Two
**Authentication
***Default value is set to MD5.
***Valid Options are: MD5, SHA1, SHA256.
**Encryption
***Default value is set to 3DES.
***Valid Options are: DES, 3DES, AES128, AES192, AES256.
**Diffie-Hellman Group
***Default value is set to 2.
***Valid Options are: 0 (None), 1, 2, 5.
**Keylife
***Default value is set to 28800.
***Limits are:  MIN = 120, MAX = 172800
**Perfect Forward Secrecy
***Valid Options are: Off = 0, On = 1.
***NOTE:  If perfect forward secrecy is turned On (set to 1), then a phase 2 diffie-hellman group is required.


The remote peer address for the network tunnel may also be modified if needed.  Invalid options will not be accepted and will cause an exception to be thrown.  There are properties that provide valid options and limits for each negotiation parameter.  Those properties are as follows: 
* encryptionDefault
* encryptionOptions
* authenticationDefault
* authenticationOptions
* diffieHellmanGroupDefault
* diffieHellmanGroupOptions
* phaseOneKeylifeDefault
* phaseTwoKeylifeDefault
* keylifeLimits


Configurations cannot be modified if a network tunnel's requires complex manual setups/configuration modifications by the SoftLayer Network department.  If the former is required, the configurations for the network tunnel will be locked until the manual configurations are complete. A network tunnel's configurations are applied via a transaction.  If a network tunnel configuration change transaction is currently running, the network tunnel's setting cannot be modified until the running transaction completes. 

NOTE:  A network tunnel's configurations must be applied to the network device in order for the modifications made to take effect. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Tunnel_Module_Context"
---

### [REST Example](#editObject-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#editObject-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Network_Tunnel_Module_Context]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Network_Tunnel_Module_Context/{SoftLayer_Network_Tunnel_Module_ContextID}/editObject'
```
