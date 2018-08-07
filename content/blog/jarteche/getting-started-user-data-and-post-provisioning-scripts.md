---
title: "Getting Started With User Data and Post Provisioning Scripts"
description: "The SoftLayer platform lets you add dynamic data and scripts when you place your order.  The scripts are executed after "
date: "2014-08-21"
author: "jarteche"
classes: 
    - "SoftLayer_Product_Package"
    - "SoftLayer_Product_Order"
    - "SoftLayer_Product_Item_Price"
tags:
    - "blog"
    - "order"
    - "provisionscripts"
    - "metadata"
---

The SoftLayer platform lets you add dynamic data and scripts when you place your order.  The scripts are executed after the machine is booted. 

To place a script on a virtual server, the script must be available through a URL.

Note: For HTTP URLs, the script is injected in the server and manually executed. For HTTPS URLs, the script is injected and automatically executed.

In this article, we use <em>https://x.x.x.x/</em> as the URL where the scripts are available and <em>time.sh</em> as the script. If you place the URL on the browser, the result should be:

```
#!/bin/bash
echo "time : " >> /root/startup
date >> /root/startup
```
</br>
### **The Order Template**
This order template will inject the script placed on URL <a href=“https://x.x.x.x/time.sh”>https://x.x.x.x/time.sh</a> on the new virtual server.

```ruby
    'virtualGuests' => [
      {
          'hostname' => 'test',      # in your own code you would replace this with your own hostname
          'domain' => 'test.com'  # in your own code you would replace this with your own domain name
      }
    ],
 
    # These are fields we'll fill in with more explanation 
 
    'location' => location,    
    'packageId' => Virtual_Guest_Package_ID,   
    'prices' => nil,   
    'useHourlyPricing'=> 1,
    'provisionScripts'=>['https://x.x.x.x/time.sh']
##the script must be available on a server where the ip is xxx.xxx.xxx.xxx
}
```

If you need to add user data:
```ruby
$product_order = {
    'complexType' => 'SoftLayer_Container_Product_Order_Virtual_Guest',  
# a constant that will tell the server what type of thing we're sending it.
 
    'quantity' => 1,      # We only want 1 virtual guest.
 
    'virtualGuests' => [
      {
          'hostname' => 'test',      # in your own code you would replace this with your own hostname
          'domain' => 'test.com',  # in your own code you would replace this with your own domain name
              'userData' =>[{"value"=>"{'your_value': 'your_value', 'your_user-data': 'your_userdata value'}","type"=>{"keyname"=>"USER_DATA","name"=>"User Data"}}]
      
      }
    ],
 
    # These are fields we'll fill in with more explanation 
 
    'location' => location,    
    'packageId' => Virtual_Guest_Package_ID,   
    'prices' => nil,     
    'useHourlyPricing'=> 1,
}
```

The final code to provision the virtual server would be adding userData and provisioning scripts:
```ruby
require 'rubygems'
require 'softlayer_api'
 
$SL_API_USERNAME = "xxxxx"     
$SL_API_KEY = "xxxx"
 
# These are the services we'll be using
softlayer_product_package = SoftLayer::Service.new("SoftLayer_Product_Package");
softLayer_product_item_price = SoftLayer::Service.new("SoftLayer_Product_Item_Price");
softLayer_product_order = SoftLayer::Service.new( "SoftLayer_Product_Order");

location=265592
Virtual_Guest_Package_ID = 46

$product_order = {
    'complexType' => 'SoftLayer_Container_Product_Order_Virtual_Guest',  # a constant that will tell the server what type of thing we're sending it.
 
    'quantity' => 1,      # We only want 1 virtual guest.
 
    'virtualGuests' => [
      {
          'hostname' => 'test',      # in your own code you would replace this with your own hostname
          'domain' => 'test.com',  # in your own code you would replace this with your own domain name
          'userData' =>[{"value"=>"{'your_value': 'your_value', 'your_user-data': 'your_userdata value'}","type"=>{"keyname"=>"USER_DATA","name"=>"User Data"}}]
      },

    ],
 
    # These are fields we'll fill in with more explanation 
 
    'location' => location,    
    'packageId' => Virtual_Guest_Package_ID,   
    'prices' => nil,   
    'useHourlyPricing'=> 1,
    'provisionScripts'=>['https://x.x.x.x/time.sh']##the script must be available on a server where the ip is xxx.xxx.xxx.xxx
}
 
#$product_order["packageId"] = Virtual_Guest_Package_ID

# This creates a proxy of the product package service with the virtual guest package ID already
# "integrated" into it.
$virtual_guest_package = softlayer_product_package.object_with_id(Virtual_Guest_Package_ID)
 
$product_order["prices"] = [
    { "id" => 26125 }, 
    { "id" => 27884 }, 
    { "id" => 23070 },  
    { "id" => 26737 },  
    { "id" => 34183 },  
    { "id" => 34807 },   
    { "id" => 24013 }, 
    { "id" => 28309 }, 
    { "id" => 34241 },   
    { "id" => 32500 },   
    { "id" => 32627 },   
    { "id" => 33483 },  
    { "id" => 35310 },   
    { "id" => 32139 }   
]
puts $product_order.inspect 
 
begin
    result = softLayer_product_order.verifyOrder($product_order) 
    # use placeOrder instead of verifyOrder if you want really to spin up the vm
    puts "The order was verified successfully"
    # softLayer_product_order.placeOrder($product_order)
rescue => error_reason
    puts "The order could not be verified by the server #{error_reason}"
end
```

Once you provision the server, you will see this on the root folder:

- The Script
```
root@test:~# more post_install.kxmO 
#!/bin/bash
echo "time : " >> /root/startup
date >> /root/startup
```

- The Script's Output
```
root@test:~# more startup 
time : 
Wed Jul  2 20:11:29 CDT 2014
```

Also, if the partition /dev/xvdh1 is mounted, you will see the file meta.js on this partition:

```
root@test:~# mkdir temp
root@test:~# mount /dev/xvdh1 temp/
root@test:~# ls temp/
meta.js
root@test:~# more temp/meta.js 
["{'your_value': 'your_value', 'your_user-data': 'your_userdata value'}"]
```

Another method to push or pull the userData is using the API methods on the Virtual_Guest service.

- To push data:

```ruby
#!/usr/bin/ruby
require 'rubygems'
require 'softlayer_api'
$SL_API_USERNAME = "xxxx"         # enter your username here
$SL_API_KEY = "xxxx"   # enter your apiKey here
 
 vm = SoftLayer::Service.new("SoftLayer_Virtual_Guest") 
 testdata=[ "data_here_1 "]
 vm.object_with_id(server_id).setUserMetadata(testdata)
```

- To pull data:

```ruby
#!/usr/bin/ruby
require 'rubygems'
require 'softlayer_api'
require 'pp'
$SL_API_USERNAME = "xxxx"         # enter your username here
$SL_API_KEY = "xxxx"   # enter your apiKey here
 
 vm = SoftLayer::Service.new("SoftLayer_Virtual_Guest") 
 
 pp vm.object_with_id(server_id).getUserData()
```

\- Chechu (Jesus Arteche)

