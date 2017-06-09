---
title: "Get bills by user"
description: "Goes through the upcoming invoice, collects billing items by their user, and prints out the results along with a sum of costs"
date: "2017-06-09"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Billing_Order_Item"
    - "SoftLayer_Billing_Order"
    - "SoftLayer_User_Customer"

tags:
    - "getbillingitem"
    - "billing"
    - "getnextinvoicetotalamount"
    - "usercustomer"
---


This is a rough script, it doesn't include some of the tax fees and some of the other one off fee fields that you will find in http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item

Example Output

```bash
chris-cde - 840.0
    123.cdetesting.com : Dual Intel Xeon E5-2620 v3 (12 Cores, 2.40 GHz) $345.0
    234.cdetesting.com : Dual Intel Xeon E5-2620 v3 (12 Cores, 2.40 GHz) $495.0
    chris.testing.com : 2 x 2.0 GHz Cores $0.0
    4 Portable Private IP Addresses - $0.0
    8 Portable Private IP Addresses - $0.0
```

Source

```python
"""
@author Christopher Gallo
Goes through the next invoice. Collections billing items by the user that orderd them.
Prints out each user and how much they caused in billing, along with what they ordered.
"""
import SoftLayer
from pprint import pprint as pp

class bills():

    def __init__(self):

        self.client = SoftLayer.Client()
        self.mgr = SoftLayer.VSManager(self.client)

    def main(self):

        """
        Not all billing items have a user record, these are collected under the master account
        http://sldn.softlayer.com/reference/services/SoftLayer_Account/getNextInvoiceTopLevelBillingItems returns
        http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item -> taps orderItem for
        http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Order_Item -> taps order for 
        http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Order -> taps userRecord for
        http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
        """
        mask="mask[orderItem[order[id,userRecord[displayName,username]]]]"
        billingItems = self.client['SoftLayer_Account'].getNextInvoiceTopLevelBillingItems(mask=mask)

        users = {'masterUser': []}
        for item in billingItems:
            if 'orderItem' in item:
                username = item['orderItem']['order']['userRecord']['username']
                del item['orderItem']
                if username not in users:
                    users[username] = []
                users[username].append(item)
            else:
                users['masterUser'].append(item)


        # prints everything out, and finds the sum of items.
        for user in users:
            servers = []
            everything_else = []
            total_cost = 0

            for item in users[user]:

                # this doens't include Tax fees, or setup fees because I'm lazy
                cost = float(item['recurringFee']) + float(item['oneTimeFee'])
                if 'hostName' in item:
                    fqdn = "%s.%s : %s $%s" % (item['hostName'], item['domainName'], item['description'], cost)
                    servers.append(fqdn)
                else:
                    item = "%s - $%s" % (item['description'], cost)
                    everything_else.append(item)
                total_cost = total_cost + cost
            print("%s - %s" % (user , total_cost))
            for server in servers:
                print("\t%s" % server)
            for thing in everything_else:
                print("\t%s" % thing)




if __name__ == "__main__":
    main = bills()
    main.main()
```
