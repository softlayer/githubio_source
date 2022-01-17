---
title: "Get Notifications"
description: "Gets a list of upcoming maintenance events"
date: "2017-04-02"
classes: ["SoftLayer_Notification_Occurrence_Event"]
tags:
    - "notification"
    - "objectfilter"
---

Retrieves all notifications that were created on January 1, 2016.

```ruby
require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new(:timeout => 120)

theDate = '01/01/2017 01:00:00'
theFilter = {
                'startDate'=> { 
                    'operation'=> 'greaterThanDate',
                    'options'=> [
                        {'name'=> 'date', 'value' => [theDate]}
                    ]
                }
            }



getresults = client['SoftLayer_Notification_Occurrence_Event'].getAllObjects(filter=theFilter)
pp getresults
```
