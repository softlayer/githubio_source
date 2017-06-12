---
title: "Provision Times"
description: "Generates a report of how long servers took to provision"
date: "2017-06-12"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Billing_Order"
    - "SoftLayer_Billing_Order_Item"
    - "SoftLayer_Billing_Item"
    - "SoftLayer_Provisioning_Version1_Transaction"

tags:
    - "provisionTransaction"
    - "resultLimit"
    - "objectFilter"
    - "objectMask"

---

Goes through orders and prints out each transaction that provisioned a server or virtual server. Calculates provision time from the time the order was placed, till the time the transaction went to COMPLETE. 

```python
"""
@author Christopher Gallo
"""
import SoftLayer
from pprint import pprint as pp
from datetime import datetime

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class example():

    def __init__(self):

        self.client = SoftLayer.Client()

    def main(self):
        # Accounts with a large number of orders will want to use this filter.
        startDate = "04/01/2017 01:00:00"
        endDate = "06/12/2017 01:00:00"
        theFilter1 = {
            'orders': {
                'createDate': {
                    'operation': 'betweenDate',
                    'options': [
                        {'name': 'startDate', 'value': [startDate]},
                        {'name': 'endDate', 'value': [endDate]}
                    ]
                }
            }
        }
        mask = "mask[items[hostName, domainName, categoryCode, billingItem[id,provisionTransaction]]]"
        items = 10
        offset = 0
        limit = 10
        while items == 10:
            orders = self.client['SoftLayer_Account'].getOrders(filter=theFilter1, offset=offset, limit=limit, mask=mask)
            items = len(orders)
            offset = offset + limit
            self.printOrderTimes(orders)

    def printOrderTimes(self, orders):
        for order in orders:
            print("Order: %s - %s " % (order['id'], order['createDate']))
            print("\tFQDN, Status, transaction id, elapsed time")
            # pp(order)
            createDate = order['createDate']
            timeWarn = 600
            timeRed = 1200
            for item in order['items']:
                if item['categoryCode'] == 'server':
                    # 1 hour
                    timeWarn = 3600
                    # 4 hours 
                    timeRed = 14400
                elif item['categoryCode'] == 'guest_core':
                    # 10 minutes
                    timeWarn = 600
                    # 20 minutes
                    timeRed = 1200

                if item['categoryCode'] == 'server' or item['categoryCode'] == 'guest_core':

                    try:
                        transaction = item['billingItem']['provisionTransaction']
                    except KeyError:
                        # Likely a canceled order
                        continue

                    #python timezones are weird and I don't want to deal with them. 
                    t_s = createDate[:-6] 
                    t_e = transaction['statusChangeDate'][:-6] 


                    FMT = '%Y-%m-%dT%H:%M:%S'
                    tdelta = datetime.strptime(t_e,FMT) - datetime.strptime(t_s,FMT)
                    fqdn = "%s.%s" % (item['hostName'], item['domainName'])
                    seconds =  tdelta.total_seconds()
                    if seconds > timeWarn and seconds < timeRed:
                        color = bcolors.WARNING
                    elif seconds >= timeRed:
                        color = bcolors.FAIL
                    else:
                        color = bcolors.OKGREEN
                    print("\t%s%s, %s, %s, %s%s" % 
                        (color,fqdn, transaction['transactionStatus']['name'], transaction['id'], seconds ,bcolors.ENDC)
                    )

if __name__ == "__main__":
    main = example()
    main.main()
```
