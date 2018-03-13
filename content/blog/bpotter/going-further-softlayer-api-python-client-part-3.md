---
title: "Going Further with the SoftLayer API Python Client - Part 3"
description: "In my first two blog posts in this series, <a href=http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-P"
date: "2015-03-11"
author: "bpotter"
tags:
    - "blog"
---

In my first two blog posts in this series, <a href="http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-1">Part 1</a> and <a href="http://sldn.softlayer.com/blog/bpotter/Going-Further-SoftLayer-API-Python-Client-Part-2">Part 2</a>, I covered many general aspects of how to use the SoftLayer API effectively. In this post, we'll dive into how to order SoftLayer resources using the SoftLayer API. [For ordering virtual servers, read <a href="http://sldn.softlayer.com/blog/phil/Simplified-CCI-Creation">Simplified CCI Creation</a> for a great explanation of the simplified virtual server ordering process.] 

<h2>Understanding How to Order SoftLayer Resources</h2>

  <p>First, it is probably obvious, but to order a resource means to begin renting it, and to cancel a resource means to stop renting it. Some more terminology is necessary: What you actually order is called a product package since a SoftLayer resource is usually made up of many piece parts. Each part of a package is identified by a category, and then you can choose usually one item, in that category. Since each item has a price associated with it, items are usually called item prices. 
</p>

  <p>You need to refer to product packages, categories, and item prices by their id values (integer numbers), so you first have to query the SoftLayer API to figure out what those are. Most of the id values can vary from SoftLayer account to account, so the id number your buddy used is not necessarily the id you should use. Also, the id values can change over time, so you can't query the id values ahead of time and hard-code them in your code. Instead, you have to query, and use the keyNames to get the id values on the fly. I'll show you how to do this.
</p>

<strong>Product Packages</strong>

  <p>The first thing you need to do is figure out what product package you want to order. The package id values <strong>do</strong> seem to be constant across SoftLayer accounts and don't have a keyName property – I think it is safe to query the package id values once, and hard code the one id you want to use. Here's how to get the list of product packages with id and description: 
</p>

  <code>import SoftLayer
import pprint

# Get the SoftLayer API client object
client = SoftLayer.Client(username=myuser, api_key=mykey, endpoint_url=SoftLayer.API_PUBLIC_ENDPOINT)

# Get the list of packages
pkgs = client['Product_Package'].getAllObjects(mask='id, name')
pprint.pprint(pkgs)
</code>

<strong>Categories and Item Prices</strong>

  <p>Now for the package you have selected: Get a list of the categories that can be specified and the item prices within each category that you can choose from. We are going to put the information into a dictionary so you can look at it visually (via pprint) to choose the items you want, and use the dictionary in your code to get the correct id values. 
 </p>

  <code>import SoftLayer
import pprint

# Get the SoftLayer API client object
client = SoftLayer.Client(username=myuser, api_key=mykey, endpoint_url=SoftLayer.API_PUBLIC_ENDPOINT)

def getItems(pkgId):
    '''Get a list of the categories that can be specified and the item prices within each category that you can choose from.'''
    # Build a dict of each category id and what its categoryCode is.  This is only used to build the item dict below.
    categories = client['Product_Package'].getConfiguration(id=pkgId, mask='isRequired, itemCategory.id, itemCategory.name, itemCategory.categoryCode')
    cats = {}
    for cat in categories:
        catid = cat['itemCategory']['id']
        cats[catid] = {'code':cat['itemCategory']['categoryCode'], 'name':cat['itemCategory']['name'], 'isRequired':(cat['isRequired'] == 1)}

    # Go thru the items for this pkg and put the key/id pair in the correct category
    # Note: the keys are only unique within categories, not between categories
    mask = 'id, itemId, recurringFee, hourlyRecurringFee, item.description, item.keyName, categories.id'
    itemPrices = client['Product_Package'].getItemPrices(id=pkgId, mask=mask)
    items = {}          # this is a 2 level dict: 1st key is categoryCode, 2nd key is item keyName, value is item price id and other info
    for itemP in itemPrices:
        if 'categories' not in itemP:  continue
        itemId = itemP['id']
        itemDesc = itemP['item']['description']
        itemKeyName = itemP['item']['keyName']
        if 'recurringFee' in itemP:  itemFee = itemP['recurringFee']
        else:  itemFee = '0'
        if 'hourlyRecurringFee' in itemP:  itemHourlyFee = itemP['hourlyRecurringFee']
        else:  itemHourlyFee = None
        # Go thru this item's supported categories
        for itemCat in itemP['categories']:
            itemCatId = itemCat['id']
            # We correlate the categories and items by the category id
            if itemCatId in cats:
                # This item supports a category in this package, so add it to the structure under this category
                categoryCode = cats[itemCatId]['code']
                # If we haven't yet added an entry for this categoryCode, create it now
                if categoryCode not in items:  items[categoryCode] = {'catName':cats[itemCatId]['name'], 'isRequired':cats[itemCatId]['isRequired'], 'items':{}}
                entry = {'id':itemId, 'description':itemDesc, 'fee':itemFee}
                if itemHourlyFee:  entry['hourlyFee'] = itemHourlyFee
                if itemKeyName in items[categoryCode]['items']:  print 'Warning: items['+categoryCode+"]['items']["+itemKeyName+'] already has a value of '+str(items[categoryCode]['items'][itemKeyName])+' and we are overwriting it with '+str(entry)
                # Now add the item to this category
                items[categoryCode]['items'][itemKeyName] = entry
    return items

pkgId = 174     # specify the package id you want
items = getItems(pkgId)
pprint.pprint(items)
</code>

  <p>In the data structure that is displayed, you will see that the first level key is the category code, and the second level key is the keyName for the item price. For each required category, note the category code, and choose the item price within that category that you want. Then in your code, you can get the id for each item price by specifying the category code key and the item price key. See how this is done in the ordering example below. 
</p>

<strong>Ordering a SoftLayer Resource</strong>

  <p>As an example for ordering a SoftLayer resource, I'll order a network gateway. The code below assumes you have defined the getItems() function above. 
  </p>

  <code>import SoftLayer
import pprint

# Get the SoftLayer API client object
client = SoftLayer.Client(username=myuser, api_key=mykey, endpoint_url=SoftLayer.API_PUBLIC_ENDPOINT)

# The location of the gateway is determined by the first VLAN to be associated with it.
# Find the correct VLAN id using the VLAN number and router, since there can be duplicate VLAN numbers
myVlanNum = 2536   # set it to your vlan number
router = 'bcr01a.sjc01'
vlans = client['Account'].getNetworkVlans(mask='id, vlanNumber, primaryRouter.hostname, primaryRouter.datacenter.id',
                                          filter={'networkVlans': {'vlanNumber': {'operation': myVlanNum}, 'primaryRouter': {'hostname': {'operation': router} } }})
vlanId = vlans[0]['id']
locationId = vlans[0]['primaryRouter']['datacenter']['id']

pkgId = 236
items = getItems(pkgId)      # this function was defined in the previous example

# Build the order structure
productOrder = {
    'orderContainers' : [{
        "quantity" : 1,
        "hardware": [{
            "hostname": 'myhostname', 
            "domain": 'mydomain.com',
            "networkVlans" : [{"id" : vlanId}]
        }], 
        "location": locationId,
        "packageId": pkgId, 
        "prices": [
            {'id': items['server']['items']['INTEL_XEON_2650_2_00']['id']},
            {'id': items['os']['items']['OS_VYATTA_6_X_SUBSCRIPTION_EDITION_64_BIT']['id']},
            {'id': items['ram']['items']['RAM_16_GB_DDR3_1333_ECC_REG']['id']},
            {'id': items['disk_controller']['items']['DISK_CONTROLLER_RAID']['id']},
            {'id': items['disk0']['items']['HARD_DRIVE_500GB_SATA_II']['id']},
            {'id': items['bandwidth']['items']['BANDWIDTH_20000_GB']['id']},
            {'id': items['port_speed']['items']['1_GBPS_REDUNDANT_PUBLIC_PRIVATE_NETWORK_UPLINKS']['id']},
            {'id': items['remote_management']['items']['REBOOT_KVM_OVER_IP']['id']},
            {'id': items['pri_ip_addresses']['items']['1_IP_ADDRESS']['id']},
            {'id': items['power_supply']['items']['REDUNDANT_POWER_SUPPLY']['id']},
            {'id': items['monitoring']['items']['MONITORING_HOST_PING_AND_TCP_SERVICE']['id']},
            {'id': items['notification']['items']['NOTIFICATION_EMAIL_AND_TICKET']['id']},
            {'id': items['response']['items']['AUTOMATED_NOTIFICATION']['id']},
            {'id': items['vpn_management']['items']['UNLIMITED_SSL_VPN_USERS_1_PPTP_VPN_USER_PER_ACCOUNT']['id']},
            {'id': items['vulnerability_scanner']['items']['NESSUS_VULNERABILITY_ASSESSMENT_REPORTING']['id']},
        ],
    }]
}

# Right now we are just verifying that we built the order correctly.
# Uncomment the placeOrder() call if you really want to order the gateway.
order = client['Product_Order'].verifyOrder(productOrder)
# order = client['Product_Order'].placeOrder(productOrder, False)

# order will be a large structure that SoftLayer fills out, representing the complete order and pricing
pprint.pprint(order)
</code>

<strong>Checking the Status of Your Order</strong>

  <p>Now that you've ordered a SoftLayer resource, you probably want to find out, via the API, when the resource will be available. One of the properties returned in the order data structure in the ordering example above is the orderId (if you actually ordered the resource and didn't just verify the order). You can use this to check the order status, with this call: 
  </p>

  <code>status = client['Billing_Order'].getObject(id=orderId, mask='status')</code>

  <p>But this actually isn't that useful because the order status usually goes to APPROVED pretty
quickly, and I've never seen it go to COMPLETED. Instead, you should query to see if the resource you ordered is actually available; in our case, by looking for the network gateway we ordered:
</p>

  <code>import SoftLayer
import pprint

# Get the SoftLayer API client object
client = SoftLayer.Client(username=myuser, api_key=mykey, endpoint_url=SoftLayer.API_PUBLIC_ENDPOINT)

mygateway = 'v1'
gateways = client['Account'].getNetworkGateways(mask='id, name, status.name', filter={'networkGateways': {'name': {'operation': mygateway}}})
if len(gateways) > 0:
    pprint.pprint(gateways)
</code>

  <p>In the case of network gateways, they have a status value that is "Pending" while it is still being provisioned and "Active" when it is ready. Not all SoftLayer resources have a status value like this. 
  </p>

I hope this series has been informative. If you have any questions, please send an email to [social@softlayer.com](mailto:social@softlayer.com).

-Bruce

