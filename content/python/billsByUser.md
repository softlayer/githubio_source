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
    - "objectfilter"
---


This is a rough script, it doesn't include some of the tax fees and some of the other one off fee fields that you will find in http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_Item

Example Output for billsByUser()

```bash
chris-cde - 840.0
    123.cdetesting.com : Dual Intel Xeon E5-2620 v3 (12 Cores, 2.40 GHz) $345.0
    234.cdetesting.com : Dual Intel Xeon E5-2620 v3 (12 Cores, 2.40 GHz) $495.0
    chris.testing.com : 2 x 2.0 GHz Cores $0.0
    4 Portable Private IP Addresses - $0.0
    8 Portable Private IP Addresses - $0.0
```

Example Output of upcoming_hourly()
```bash
ItemID  Info    Host    Domain  Hours   Hourly Cost Cost
143131173   Dual Intel Xeon E5-2620 v3 (12 Cores, 2.40 GHz) jd-cos-testing-sjc03    secore.com  489 .309    151.101
==> 143131179   64 GB RAM   291.933
==> 143131183   1.00 TB SATA    17.604
==> 143131185   1.00 TB SATA    17.604
==> 143131189   10 Gbps Dual Public & Private Network Uplinks (Unbonded)    147.189
TOTAL: 625.431
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

    def billsByUser(self):

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


    def upcoming_hourly(self):
    """
    Filters upcoming billing items for only hourly WITH a hostname that contains the string 'test'
    Each hourly server will also have some children that need to be added for the total cost, those are included with the nonZeroNextInvoiceChildren property
    NOTE: 
    ObjectMask starts at http://sldn.softlayer.com/reference/datatypes/SoftLayer_Billing_item
    ObjectFilter starts at http://sldn.softlayer.com/reference/datatypes/SoftLayer_Account
    hourlyFlag needs to be 1 or 0.

    """
        mask="mask[hourlyFlag,nonZeroNextInvoiceChildren]"
        objectFilter =  {
            'nextInvoiceTopLevelBillingItems': {
                'hourlyFlag': {'operation': 1},
                'hostName': {'operation': '*= test'}
            }
        }
        billingItems = self.client['SoftLayer_Account'].getNextInvoiceTopLevelBillingItems(mask=mask, filter=objectFilter)
        print("ItemID\tInfo\tHost\tDomain\tHours\tHourly Cost\tCost")
        for item in billingItems:
            itemId = item['id']
            hostName = item['hostName']
            domainName = item['domainName']
            description = item['description']
            hours = item['hoursUsed']
            hourly_cost = item['hourlyRecurringFee']
            cost = int(hours) * float(hourly_cost)
            total_cost = cost
            print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % (itemId, description, hostName,domainName, hours, hourly_cost, cost ))
            for child in item['nonZeroNextInvoiceChildren']:
                childId = child['id']
                childDesc = child['description']
                childCost = int(child['hoursUsed']) * float(child['hourlyRecurringFee'])
                total_cost = total_cost + childCost
                print("==> %s\t%s\t%s" % (childId,childDesc,childCost))
            print("TOTAL: %s" % (total_cost))


if __name__ == "__main__":
    main = bills()
    main.billsByUser()
```
