---
title: "Compliance Report Request"
description: "How to create a Compliance Report Request."
date: "2021-01-18"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Account_Contact"
    - "SoftLayer_Compliance_Report_Type"
    - "SoftLayer_Account_Reports_Request"
tags:
    - "compliance-report"
---

This article will cover how to use the API to create a compliance report request.


### Setup
All the functions defined in this article will be part of this `ComplianceReport` class. Which only sets up the SoftLayer Client, and configures the debugger, which allows you to see the exact API calls being made.

```python
import SoftLayer
from pprint import pprint as pp

class ComplianceReport:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def debug(self):
        for call in self.client.transport.get_last_calls():
            print(self.client.transport.print_reproduceable(call))

if __name__ == "__main__":
    main = ComplianceReport()
    main.debug()
```

## Retrieving all Contacts types
To retrieve all contacts types, we use [SoftLayer_Account_Contact::getAllContactTypes()](https://sldn.softlayer.com/reference/services/SoftLayer_Account_Contact/getAllContactTypes/).

### Python
```python

    def get_all_contact_types(self):
        mask = 'mask[id,keyName,name,description]'
        return self.client['SoftLayer_Account_Contact'].getAllContactTypes(mask=mask)
```

### REST
```bash
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Contact/getAllContactTypes.json?objectMask=mask%5Bid%2CkeyName%2Cname%2Cdescription%5D'
```

### Output example
```bash
[{'id': 1, 'keyName': 'ADMIN', 'name': 'Administrative'},
 {'description': 'Contact type used for Compliance Report sent to external '
                 'parties',
  'id': 6,
  'keyName': 'EXTERNAL',
  'name': 'Compliance Report Recipient'},
 {'description': 'Contact type used to keep record who requested Compliance '
                 'Report if it is different from the recipient.',
  'id': 11,
  'keyName': 'EXTERNAL_REQUESTOR',
  'name': 'Compliance Report Requestor'}]
```

## Retrieving all Compliance Report Types
To retrieve all  Compliance Report Types, we use [SoftLayer_Compliance_Report_Type::getAllObjects()](https://sldn.softlayer.com/reference/services/SoftLayer_Compliance_Report_Type/getAllObjects/).

### Python
```python

    def get_all_report_types(self):
        return self.client['SoftLayer_Compliance_Report_Type'].getAllObjects()
```

### REST
```bash
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Compliance_Report_Type/getAllObjects.json'
```

### Output example
```bash
[{'id': 1, 'keyName': 'SOC1', 'name': 'SOC1'},
 {'id': 2, 'keyName': 'SOC2', 'name': 'SOC2'},
 {'id': 3, 'keyName': 'PCI_DSS_AOC', 'name': 'PCI DSS AOC'},
 {'id': 4, 'keyName': 'ISO_27001_SOA', 'name': 'ISO 27001 SOA'},
 {'id': 5, 'keyName': 'HIPAA_BRIDGE_LETTER', 'name': 'HIPAA Bridge Letter'}]
```
## Creating a Recipient Contact 
To create a Recipient contact, we use [SoftLayer_Account_Contact::createObject()](https://sldn.softlayer.com/reference/services/SoftLayer_Account_Contact/createObject/) and pass in a structure of type [SoftLayer_Account_Contact](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain/). You should set in the template a typeId by matching with a type used for `Compliance Report Recipient`. See [Retrieving all Contacts types](#retrieving-all-Contacts-types).

### Python
```python

    def create_account_contact(self):
        template = {
            'companyName': 'SoftLayer Internal',
            'email': 'test@mail.com',
            'firstName': 'German',
            'jobTitle': 'Tester',
            'lastName': 'Test',
            'typeId': 6  # "Contact type used for Compliance Report sent to external parties"
        }
        return self.client['SoftLayer_Account_Contact'].createObject(template)

```


### REST
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": [{"companyName": "SoftLayer Internal", "email": "test@mail.com", "firstName": "German", "jobTitle": "Tester", "lastName": "Test", "typeId": 6}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Contact/createObject.json'
```

## Getting a Requestor Contact 
To get a Requestor contact, we use [SoftLayer_Account::getAccountContacts()](https://sldn.softlayer.com/reference/services/SoftLayer_Account/getAccountContacts/). However,you will need a Contact with typeId by matching with a type used for `Compliance Report Requestor`. See [Retrieving all Contacts types](#retrieving-all-contacts-types).

### Python
```python

    def get_account_contacts(self):
        mask = 'mask[id,companyName,firstName,lastName,jobTitle,typeId,type[name,keyName,id]]'
        return self.client['SoftLayer_Account'].getAccountContacts(mask=mask)

```

### REST
```bash
curl -u $SL_USER:$SL_APIKEY -X GET -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress"  'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getAccountContacts.json?objectMask=mask%5Bid%2CcompanyName%2CfirstName%2ClastName%2CjobTitle%2CtypeId%2Ctype%5Bname%2CkeyName%2Cid%5D%5D'
```

### Output example
```bash
[{'companyName': 'Company One',
  'firstName': 'Test Requestor',
  'id': 345678,
  'jobTitle': 'REQUEST TEST',
  'lastName': 'Testerson',
  'type': {'id': 11,
           'keyName': 'EXTERNAL_REQUESTOR',
           'name': 'Compliance Report Requestor'},
  'typeId': 11}]
```


## Creating Compliance Report request
To create a Compliance Report request, we use [SoftLayer_Account_Reports_Request::createRequest()](https://sldn.softlayer.com/reference/services/SoftLayer_Account_Reports_Request/createRequest/) and pass in a structure of type [SoftLayer_Account_Contact](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain/) as `recipientContact`, a `reason` string, a `reportType` string (Retrieving all Compliance Report Types), and a [SoftLayer_Account_Contact](https://sldn.softlayer.com/reference/datatypes/SoftLayer_Dns_Domain/) as `requestorContact`.

### Python
```python

    def create_request(self):
        recipient = self.create_account_contact()
        requestor = self.get_account_contacts()[0]
        # first item is type EXTERNAL_REQUESTOR,typeId:11

        reason = "Only for testing purposes"
        reportType = 'SOC1'

        pp(self.client['SoftLayer_Account_Reports_Request'].
           createRequest(recipient, reason, reportType, requestor))
        
if __name__ == "__main__":
    main = ComplianceReport()
    try:
        pp(main.get_all_contact_types())
        pp(main.get_all_report_types())
        main.create_request()
    except Exception as e:
        print("There was an error:\n")
        print(e)
    main.debug()

```

### REST
```bash
curl -u $SL_USER:$SL_APIKEY -X POST -H "Accept: */*" -H "Accept-Encoding: gzip, deflate, compress" -d '{"parameters": [{"accountId": 307608, "companyName": "SoftLayer Internal", "createDate": "2021-01-18T14:56:29-06:00", "email": "test@mail.com", "firstName": "German", "id": 345678, "jobTitle": "Tester", "lastName": "Test", "modifyDate": null, "typeId": 6}, "Only for testing purposes", "SOC1", {"companyName": "Company One", "firstName": "Test Requestor", "id": 345123, "jobTitle": "REQUEST TEST", "lastName": "Testerson", "typeId": 11, "type": {"description": "Contact type used to keep record who requested Compliance Report if it is different from the recipient.", "id": 11, "keyName": "EXTERNAL_REQUESTOR"}}]}' 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account_Reports_Request/createRequest.json'
```





