---
title: "Working with Quotes"
description: "A few examples on interacting with Quotes"
date: "2021-02-26"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Order_Quote"
tags:
    - "quotes"
---

### Setup
All the functions defined in this article will be part of this `Example` class. Which only sets up the SoftLayer Client, and configures the debugger, which allows you to see the exact API calls being made.

```python
import SoftLayer
from SoftLayer.managers.ordering import OrderingManager
from pprint import pprint

class Example:

    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        self.mgr = OrderingManager(self.client)
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.client.transport = debugger

    def debug(self):
        for call in self.client.transport.get_last_calls():
            pprint(self.client.transport.print_reproduceable(call))

```

## Creating a Quote

### Python
```python

    def create_quote(self):
        package = 'PUBLIC_CLOUD_SERVER'
        location = 'DALLAS13'
        preset = 'B1_2X8X100'
        items = ['BANDWIDTH_0_GB_2',
                 'MONITORING_HOST_PING',
                 'NOTIFICATION_EMAIL_AND_TICKET',
                 'OS_DEBIAN_9_X_STRETCH_LAMP_64_BIT',
                 '1_IP_ADDRESS',
                 '1_IPV6_ADDRESS',
                 '1_GBPS_PUBLIC_PRIVATE_NETWORK_UPLINKS',
                 'REBOOT_REMOTE_CONSOLE',
                 'AUTOMATED_NOTIFICATION',
                 'UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT',
                 ]

        complex_type = 'SoftLayer_Container_Product_Order_Virtual_Guest'

        extras = {"virtualGuests": [{"hostname": "gq-test", "domain": "test.com"}],
                  "provisionScripts": ["https://examples.provisioning.org"],
                  "sshKeys": [{"sshKeyIds": [123456]}]
                  }

        quote_details = self.mgr.place_quote(package,
                                             location,
                                             items,
                                             complex_type=complex_type,
                                             preset_keyname=preset,
                                             extras=extras,
                                             quantity=1,
                                             quote_name='test-quote-gq')

        pprint(quote_details)

```

## Retrieving all Active Quotes

### Python
```python

    def list_active_quotes(self):
        quotes = self.mgr.get_quotes()
        pprint(quotes)
```

## Retrieving Quote Details

### Python
```python

    def get_quote_details(self, quote_id):
        quote_detail = self.mgr.get_quote_details(quote_id)
        pprint(quote_detail)
```

## Ordering a Quote

### Python
```python

    def order_quote(self, quote_id, verify=True):
        extras = {"virtualGuests": [{"hostname": "gq-test", "domain": "cloud.com"}],
                  "provisionScripts": ["https://examples.provisioning.org"],
                  "sshKeys": [{"sshKeyIds": [123456]}]
                  }
        if verify:
            order = self.mgr.verify_quote(quote_id, extras)
        else:
            order = self.mgr.order_quote(quote_id, extras)
        pprint(order)

```
## Saving a Quote

### Python
```python

     def save_quote(self, quote_id):
         result = self.client['SoftLayer_Billing_Order_Quote'].saveQuote(id=quote_id)
         pprint(result)

```

## Deleting a Quote

### Python
```python

     def delete_quote(self, quote_id):
         result = self.client['SoftLayer_Billing_Order_Quote'].deleteQuote(id=quote_id)
         pprint(result)

```

## Running the Example

### Python
```python

if __name__ == '__main__':
    quote_identifier=12345
    quote = Example()
    quote.create_quote()
    quote.list_active_quotes()
    quote.get_quote_details(quote_identifier)
    #Set verify to False to order quote
    quote.order_quote(quote_identifier, verify=True)
    quote.save_quote(quote_identifier)
    quote.delete_quote(quote_identifier)
    quote.debug()

```