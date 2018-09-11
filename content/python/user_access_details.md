---
title: "User Access Details"
description: "Prints out a list of users, and what devices they have access to view."
date: "2018-09-11"
classes: 
    - "SoftLayer_Account"
    - "SoftLayer_Virtual_DedicatedHost"
    - "SoftLayer_Hardware"
    - "SoftLayer_User_Customer"
tags:
    - "users"
    - "permissions"
---

This script gets each user, and which dedicatedHosts, hardware, and virtual guests they have permissions to view. 

The hasFullAccessFlags are used to determine if a user has access to ALL hosts of that type or not. We are using that flag here to condense the output, but each user will still have the full list of hardware under their account if they have access to all.

```python
"""
List of users that have access to a certain set of devices.
"""
import SoftLayer

# For nice debug output:
from pprint import pprint as pp
from prettytable import PrettyTable


from click import formatting
from SoftLayer.CLI import formatting


objectMask = """mask[id, username, 
    dedicatedHosts[id,name,datacenter],
    virtualGuests[id,hostname,domain,datacenter],
    hardware[id,hostname,domain,datacenter],
    hasFullDedicatedHostAccessFlag,
    hasFullHardwareAccessFlag,
    hasFullVirtualGuestAccessFlag]"""

client = SoftLayer.create_client_from_env()


# Gets all users on the account, 10 at a time. Accounts with a lot of devices may need to turn limit down to 1
all_users = client.call(
    'SoftLayer_Account', 'getUsers', mask = objectMask, iter=False, limit=15, offset=35)

table = PrettyTable(['ID', 'NAME', 'DATACENTER'])

print("-------------------- List of users that have access to a certain set of devices ---------------")

# Iterate through each user, getting what devices they each have access to and printing that.
for user in all_users:
    userId = user['id']
    username = user['username']
    print("\nTHE USER: %s  WITH ID: %s HAS ACCESS TO THE FOLLOWING DEVICES\n" % (username, userId))
    if user.get('hasFullDedicatedHostAccessFlag', False):
        table.add_row(["*","Full Access", "*"])

    elif 'dedicatedHosts' in user:
        dedicatedHosts = user['dedicatedHosts']
        for dedicatedHost in dedicatedHosts:
            table.add_row([
                dedicatedHost['id'], 
                dedicatedHost['name'], 
                dedicatedHost['datacenter'].get('name')
            ])
    else:
        table.add_row(["*","No Access", "*"])
    table.clear_rows()
    print(table.get_string(title="DEDICATED HOST"))

    if user.get('hasFullVirtualGuestAccessFlag', False):
        table.add_row(["*","Full Access", "*"])
    elif 'virtualGuests' in user:
        virtualGuests = user['virtualGuests']
        for host in virtualGuests:
            print(host)
            table.add_row([
                host['id'], 
                "%s.%s" % (host['hostname'], host['domain']),
                host.get('datacenter', {}).get('name')
            ])
    else:
        table.add_row(["*","No Access", "*"])
    print(table.get_string(title="VIRTUAL GUEST"))
    table.clear_rows()

    if user.get('hasFullVirtualGuestAccessFlag', False):
        table.add_row(["*","Full Access", "*"])
    elif 'hardware' in user:
        hardware = user['hardware']
        for host in hardware:
            table.add_row([
                host['id'], 
                "%s.%s" % (host['hostname'], host['domain']) , 
                host.get('datacenter', {}).get('name')
            ])
    else:
        table.add_row(["*","No Access", "*"])
    print(table.get_string(title="HARDWARE"))
    table.clear_rows()

print("Done")

```