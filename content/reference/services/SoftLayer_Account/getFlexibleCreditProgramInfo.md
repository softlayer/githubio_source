---
title: "getFlexibleCreditProgramInfo"
description: "[DEPRECATED] Please use SoftLayer_Account::getFlexibleCreditProgramsInfo. 

This method will return a [SoftLayer_Container_Account_Discount_Program](/reference/datatypes/SoftLayer_Container_Account_Discount_Program) object containing the Flexible Credit Program information for this account. To be considered an active participant, the account must have an enrollment record with a monthly credit amount set and the current date must be within the range defined by the enrollment and graduation date. The forNextBillCycle parameter can be set to true to return a SoftLayer_Container_Account_Discount_Program object with information with relation to the next bill cycle. The forNextBillCycle parameter defaults to false. Please note that all discount amount entries are reported as pre-tax amounts and the legacy tax fields in the [SoftLayer_Container_Account_Discount_Program](/reference/datatypes/SoftLayer_Container_Account_Discount_Program) are deprecated. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account"
type: "reference"
layout: "method"
mainService : "SoftLayer_Account"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getFlexibleCreditProgramInfo'
```
