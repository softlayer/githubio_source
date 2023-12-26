---
title: "createObject"
description: "
createObject() allows the creation of a new brand. This will also create an `account` 
to serve as the owner of the brand. 


In order to create a brand, a template object must be sent in with several required values. 


### Input [SoftLayer_Brand](/reference/datatypes/SoftLayer_Brand)



- `name` 
    + Name of brand 
    + Required 
    + Type: string 
- `keyName` 
    + Reference key name 
    + Required 
    + Type: string 
- `longName` 
    + More descriptive name of brand 
    + Required 
    + Type: string 
- `account.firstName` 
    + First Name of account contact 
    + Required 
    + Type: string 
- `account.lastName` 
    + Last Name of account contact 
    + Required 
    + Type: string 
- `account.address1` 
    + Street Address of company 
    + Required 
    + Type: string 
- `account.address2` 
    + Street Address of company 
    + Optional 
    + Type: string 
- `account.city` 
    + City of company 
    + Required 
    + Type: string 
- `account.state` 
    + State of company (if applicable) 
    + Conditionally Required 
    + Type: string 
- `account.postalCode` 
    + Postal Code of company 
    + Required 
    + Type: string 
- `account.country` 
    + Country of company 
    + Required 
    + Type: string 
- `account.officePhone` 
    + Office Phone number of Company 
    + Required 
    + Type: string 
- `account.alternatePhone` 
    + Alternate Phone number of Company 
    + Optional 
    + Type: string 
- `account.companyName` 
    + Name of company 
    + Required 
    + Type: string 
- `account.email` 
    + Email address of account contact 
    + Required 
    + Type: string 


REST Example: 
``` 
curl -X POST -d '{ 
    'parameters':[{ 
        'name': 'Brand Corp', 
        'keyName': 'BRAND_CORP', 
        'longName': 'Brand Corporation', 
        'account': { 
            'firstName': 'Gloria', 
            'lastName': 'Brand', 
            'address1': '123 Drive', 
            'city': 'Boston', 
            'state': 'MA', 
            'postalCode': '02107', 
            'country': 'US', 
            'companyName': 'Brand Corp', 
            'officePhone': '857-111-1111', 
            'email': 'noreply@example.com' 
        } 
    }] 
}' https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/createObject.json 
``` "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Brand"
classes:
    - "SoftLayer_Brand"
type: "reference"
layout: "method"
mainService : "SoftLayer_Brand"
---

### Curl Example
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Brand]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Brand/createObject'
```
