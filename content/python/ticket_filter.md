---
title: "Get tickets using an objectFilter"
description: "Pulls down all the cancellation tickets created after a set date, along with any updates"
date: "2016-02-26"
classes: ["SoftLayer_Account"]
tags:
    - "tickets"
    - "objectFilter"
    - "objectMask"
---



```
import SoftLayer
from pprint import pprint as pp
import logging

class example():

    def __init__(self):

        self.client = SoftLayer.Client()

    def main(self):

        # logger = logging.getLogger()
        # logger.addHandler(logging.StreamHandler())
        # logger.setLevel(3)
        theDate = "02/25/2016 01:00:00"
        endDate = "02/29/2016 01:00:00"

        mask = "mask[updates,group[name]]"


        theFilter1 = {
            'tickets': {
                'createDate': {
                    'operation': 'betweenDate',
                    'options': [
                        {'name': 'startDate', 'value': [theDate]},
                        {'name': 'endDate', 'value': [endDate]}
                    ]
                }
            }
        }

        theFilter2 = {
            'tickets': {
                'createDate': {
                    'operation': 'greaterThanDate',
                    'options': [
                        {'name': 'date', 'value': [theDate]}
                    ]
                },
                'group' : {
                    'name': {
                        'operation': 'Cancellations'
                    }
                    
                }
            }
        }

        result = self.client['SoftLayer_Account'].getTickets(filter=theFilter2, mask=mask)
        for ticket in result:
            print("===============")
            print("%s - %s (%s)" % (ticket['createDate'], ticket['title'], ticket['group']['name']))
            for update in ticket['updates']:
                print("===============%s=============== " % (update['createDate']))
                print("%s" % update['entry'])
                print("===============")

        # pp(result)

if __name__ == "__main__":
    main = example()
    main.main()
```