---
title: "Order an SSL Certificate"
description: "Explains how to get the information requried to order an SSL Certificate"
date: "2015-11-11"
classes: 
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Package"
    - "SoftLayer_Container_Product_Order_Security_Certificate"
    - "SoftLayer_Security_Certificate_Request_ServerType"
tags:
    - "ordering"
    - "ssl"
    - "placeOrder"
    - "debugging"
---


#### Generating a CSR
You will need a csr to make this request, it should be on your local file system. 

The contents of the CSR *MATTER*, they need to match the information for what you are ordering.
+ orderApproverEmailAddress must match the Email Address of the CSR
+ The CSR Common name must be set and must be a part of the orderApproverEmailAddress
```bash
$ openssl genrsa -out domain.key 2048
$ openssl req -new -sha256 -key domain.key -out domain.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:TX
Locality Name (eg, city) []:Houston
Organization Name (eg, company) [Internet Widgits Pty Ltd]:SoftLayer
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:lablayer.info
Email Address []:admin@lablayer.info

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:

$
```

```
import SoftLayer
import pprint
import logging

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):
        pp = pprint.PrettyPrinter(indent=4)
        filename = './domain.csr'

        cert = self.file_get_contents(filename)
        addressInfo =  {
                    "addressLine1" : "1234 fleet street",
                    "city" : "Houston",
                    "countryCode" : "US",
                    "postalCode" : "77090",
                    "state" : "TX"
                }
        contactInfo = {
                "address": addressInfo,
                "emailAddress": "chgallo@lablayer.info",
                "firstName": "Christopher",
                "lastName": "Gallo",
                "organizationName": "SoftLayer",
                "phoneNumber": "281-123-4567",
                "title": "Dev"
            }
        sslContainer= {'orderContainers': [
        {
            "complexType": "SoftLayer_Container_Product_Order_Security_Certificate",
            "packageId":0,
            "quantity":1,
            "serverCount":1,
            "certificateSigningRequest": cert,
            "serverType": "apacheopenssl",
            # Needs to be a VERY specific email @ the domain you are registering
            # admin / administrator / hostmaster / root / webmaster / mailmaster
            "orderApproverEmailAddress": "admin@lablayer.info",
            "technicalContact": contactInfo,
            "administrativeContact": contactInfo,
            "billingContact": contactInfo,
            "organizationInformation": {
                "address" :addressInfo,
                "organizationName" : "SoftLayer",
                "phoneNumber": "281-123-4567"
            },
            "prices": [
                #SSL_CERTIFICATE_RAPIDSSL_1_YEAR
                {'id':1836}
            ]
        }
        ]
        }

        pp.pprint(sslContainer)

        result = self.client['SoftLayer_Product_Order'].verifyOrder(sslContainer)
        pp.pprint(result)

    def file_get_contents(self,filename):
        with open(filename) as f:
            return f.read()

if __name__ == "__main__":
    main = example()
    main.main()

```
