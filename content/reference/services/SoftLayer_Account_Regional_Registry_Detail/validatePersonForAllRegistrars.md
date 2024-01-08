---
title: "validatePersonForAllRegistrars"
description: "Validates this person detail against all supported external registrars (APNIC/ARIN/RIPE). The validation uses the most restrictive rules ensuring that any person detail passing this validation would be acceptable to any supported registrar. 

The person detail properties are validated against - Non-emptiness - Minimum length - Maximum length - Maximum words - Supported characters - Format of data 

If the person detail validation succeeds, then an empty list is returned indicating no errors were found and that this person detail would work against all three registrars during a subnet registration. 

If the person detail validation fails, then an array of validation errors (SoftLayer_Container_Message[]) is returned. Each message container contains error messages grouped by property type and a message type indicating the person detail property type object which failed validation. It is possible to create a subnet registration using a person detail which does not pass this validation, but at least one registrar would reject it for being invalid. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_Regional_Registry_Detail"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account_Regional_Registry_Detail"
---

### [REST Example](#validatePersonForAllRegistrars-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#validatePersonForAllRegistrars-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X GET \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Regional_Registry_Detail/{SoftLayer_Account_Regional_Registry_DetailID}/validatePersonForAllRegistrars'
```
