---
title: "whois"
description: "Perform a WHOIS lookup from SoftLayer's application servers on the given IP address or hostname and return the raw results of that command. The returned result is similar to the result received from running the command `whois` from a UNIX command shell. A WHOIS lookup queries a host's registrar to retrieve domain registrant information including registration date, expiry date, and the administrative, technical, billing, and abuse contacts responsible for a domain. WHOIS lookups are useful for determining a physical contact responsible for a particular domain. WHOIS lookups are also useful for determining domain availability. Running a WHOIS lookup on an IP address queries ARIN for that IP block's ownership, and is helpful for determining a physical entity responsible for a certain IP address. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Utility"
classes:
    - "SoftLayer_Utility_Network"
type: "reference"
layout: "method"
mainService : "SoftLayer_Utility_Network"
---

### [REST Example](#whois-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#whois-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [string]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Utility_Network/whois'
```
