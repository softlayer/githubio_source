---
title: "Show user accounts with and without two-factor enabled"
description: "Get a list of users with two-factor authentication enabled/disabled. "
date: "2017-08-04"
classes: 
    - "SoftLayer_Account"
tags:
    - "objectFilter"
    - "objectMask"
---

To get a list of users *with* Two-Factor authentication enabled. 

```
"""
@author Ryan TIffany
"""

import SoftLayer
from pprint import pprint as pp 

client = SoftLayer.Client()
mask = mask"[id,username,firstName,lastName,externalBindingCount,externalBindings]"
theFilter = {
'users': {
	'externalBindings':{
		'active':{
			'operation':'1'
		}}}
}

getUsers = client['SoftLayer_Account'].getUsers(filter=theFilter, mask=mask)
pp(getUsers)

```

To get a list of users *without* Two-Factor authentication enabled. 

```
"""
@author Ryan TIffany
"""

import SoftLayer
from pprint import pprint as pp 

client = SoftLayer.Client()
mask = mask"[id,username,firstName,lastName,externalBindingCount,externalBindings]"
theFilter = {
'users': {
	'externalBindings':{
		'active':{
			'operation':'0'
		}}}
}

getUsers = client['SoftLayer_Account'].getUsers(filter=theFilter, mask=mask)
pp(getUsers)

```