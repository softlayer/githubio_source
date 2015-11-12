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

```bash
openssl genrsa -out domain.key 2048
openssl req -new -sha256 -key domain.key -out domain.csr
```

```
import SoftLayer
import pprint
import logging

class example():

    def __init__(self):
        self.client = SoftLayer.Client()

    def main(self):
        logger = logging.getLogger()
        logger.addHandler(logging.StreamHandler())
        logger.setLevel(3)
        pp = pprint.PrettyPrinter(indent=4)
        filename = './domain.csr'

        cert = self.file_get_contents(filename)
        cert64 = base64.b64encode(cert)
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
