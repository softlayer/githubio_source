---
title: "Determining your next bill"
description: "Example on how to use getNextInvoiceTotalAmount to retrieve the pre-tax total amount of an account's next invoice measured in US Dollars ($USD)"
date: "2016-01-29"
classes: ["SoftLayer_Account"]
tags:
    - "invoice"
---

```ruby
# SoftLayer library will look to see if these global variables are set when making a connection
# more information here: https://github.com/softlayer/softlayer-ruby/blob/master/lib/softlayer/Config.rb#L11-L58

require 'softlayer_api'
require 'pp'

client = SoftLayer::Client.new

total_amount = client['Account'].getNextInvoiceTotalAmount
puts "Next invoice total amount: #{total_amount}"
```

## Example Output

```
Next invoice total amount: 250.26
```
