---
title: "getUpgradeItemPrices"
description: "Retrieves a list of all upgrades available to a virtual server. Upgradeable items include, but are not limited to, number of cores, amount of RAM, storage configuration, and network port speed. 

This method exclude downgrade item prices by default. You can set the 'includeDowngradeItemPrices' parameter to true so that it can include downgrade item prices. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Virtual"
classes:
    - "SoftLayer_Virtual_Guest"
type: "reference"
layout: "method"
mainService : "SoftLayer_Virtual_Guest"
---

### [REST Example](#getUpgradeItemPrices-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#getUpgradeItemPrices-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Virtual_Guest/{SoftLayer_Virtual_GuestID}/getUpgradeItemPrices'
```
