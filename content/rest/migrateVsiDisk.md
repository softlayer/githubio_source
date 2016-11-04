---
title: "Migrating a VSI from SAN to Local Storage and vice-versa"
description: "Example on how to call verifyOrder / placeOrder via REST to migrate a Virtual_Guest from SAN to Local storage and vice-versa. Replace the verifyOrder call with placeOrder when you are actually ready to start the migration process.

"
date: "2016-11-04"
classes: ["SoftLayer_Product_Order"]
tags:
  - "upgrade"
  - "placeOrder"
  - "verifyOrder"
---

Operation: `POST`

Method: [`SoftLayer_Product_Order::placeOrder()`](http://sldn.softlayer.com/reference/services/SoftLayer_Product_Order/placeOrder/)

URL: SoftLayer_Product_Order/verifyOrder`

#### Getting the proper priceId
You can use the following [python example](https://softlayer.github.io/python/list_packages/) to get a list of all the available priceId's for the Virtual_Guest package. You need to change the second to last line from `main.getPackage(126)` to `main.getPackage(46)`. The priceId you need will depend on if you are moving to or from Local Storage and the size of the current primary drive.

Example CURL:
```
curl --user "$SOFTLAYER_USERNAME:$SOFTLAYER_API_KEY" -X POST --data @migrate.json
https://api.softlayer.com/rest/v3/SoftLayer_Product_Order/verifyOrder
```


Input JSON:
```json
{  
   "parameters":[  
      {  
         "complexType":"SoftLayer_Container_Product_Order_Virtual_Guest_Upgrade",
         "packageId":46,
         "prices":[  
            {  
               "id":13899,
               "categories":[  
                  {  
                     "categoryCode":"guest_disk0",
                     "id":81,
                     "name":"First Disk"
                  }
               ]
            }
         ],
         "properties":[  
            {  
               "name":"MAINTENANCE_WINDOW",
               "value":"now"
            }
         ],
         "virtualGuests":[  
            {  
               "id":25367125
            }
         ]
      }
   ]
}
```
