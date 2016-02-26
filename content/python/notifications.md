---
title: "Get Notifications"
description: "Gets a list of upcoming maintenance events"
date: "2016-02-26"
classes: ["SoftLayer_Notification_Occurrence_Event"]
tags:
    - "notification"
    - "objectFilter"
---

Retrieves all notifications that were created on January 1, 2016.

```
import SoftLayer
from pprint import pprint as pp

class example():

    def __init__(self):

        self.client = SoftLayer.Client()

    def main(self):
        theDate = '01/01/2016 01:00:00'
        _filter = {
                'startDate': { 
                    'operation': 'greaterThanDate',
                    'options': [
                        {'name': 'date', 'value': [theDate]}
                    ]
                }
            }
        result = self.client['SoftLayer_Notification_Occurrence_Event'].getAllObjects(filter=_filter)
        pp(result)

if __name__ == "__main__":
    main = example()
    main.main()
```
