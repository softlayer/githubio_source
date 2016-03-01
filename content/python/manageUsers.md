---
title: "Manage Users"
description: "A script to create users and a script to disable users. Used mostly for setting up lab users and then cleaning up after."
date: "2016-03-01"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Account"
tags:
  - "ordering"
  - "users"
  - "permissions"
---


Creates a user, sets up proper permissions, sets up devices access restrictions, creates API keys and orders the user a server.
```
import SoftLayer.API
from pprint import pprint as pp


def create_user(username, password):
    user_template = {
        'username': username,
        'firstName': 'API',
        'lastName': 'Learner',
        'email': 'someone@somewhere.com',
        'companyName': 'IBM',
        'address1': '123 api road',
        'city': 'Houston',
        'country': 'US',
        'postalCode': 'TX 77002',
        'userStatusId': 1001,
        'timezoneId': 107
    }
    created_user = client['User_Customer'].createObject(
        user_template,
        password,
        password)
    return created_user

def get_permissions(_id):
    permissions = client['User_Customer'].getPermissions(id=_id)
    return permissions

def set_permissions(_id, permissions):
    """
    To get permissions correct, I take the existing permissions of a user
    that I already have, and set my new user's permissions to be the same
    with addBulkPortalPermission
    """
    return client['User_Customer'].addBulkPortalPermission(
        permissions, id=_id)

def fix_permissions(user,permissions):
    # I only want users to have access to this one host
    virtualGuestId = 22334455
    t = user['id']
    set_permissions(user['id'], permissions)
    client['User_Customer'].removeAllVirtualAccessForThisUser(id=t)
    client['User_Customer'].removeAllHardwareAccessForThisUser(id=t)
    client['User_Customer'].addApiAuthenticationKey(id=t)
    client['User_Customer'].addVirtualGuestAccess(virtualGuestId,id=t)

def orderUserServer(user, apiKey):
    """
    Orders a server as the newly created user. 
    """
    hostname = user + "-lab-server"
    guest = {}
    guest['startCpus'] = 1
    guest['maxMemory'] = 1024
    guest['localDiskFlag'] = False
    guest['hostname'] = hostname
    guest['domain'] = user + ".lablayer.info"
    guest['hourlyBillingFlag'] = True
    guest['datacenter'] = {}
    guest['datacenter']['name'] = 'tok02'
    guest['blockDeviceTemplateGroup'] = {'globalIdentifier': "6c64f59a-edeb-4ba4-b992-d04972597357"}
    userClient = SoftLayer.Client(
        username = user,
        api_key = apiKey )
    result = userClient['Virtual_Guest'].createObject(guest)
    print "Added server id: %s  ( %s )" % (result['id'],result['fullyQualifiedDomainName']) 
    return
   

if __name__ == "__main__":
    import argparse
    argsparse = argparse.ArgumentParser(description='Number of users')
    argsparse.add_argument('--num-users', dest='num_users', type=int,
                           help='Number of users to provision.')
    argsparse.add_argument('--offset', dest="offset", type=int,
                           default=1, help='Username offset')
    argsparse.add_argument('--prefix',
                           help='Username prefix', default=False)
    args = argsparse.parse_args()

    ##### CHANGE THESE ##########
    template_user_id = 123456
    password = 'APAsswordGoes!!!H3r3' 

    client = SoftLayer.Client()
    
    userPerms = client['User_Customer'].getPermissions(id=template_user_id)
   
    start_user_num = args.offset

    for i in range(args.num_users):
        target_username = '%s-%s' % (args.prefix,start_user_num)
        try:
            new_user = create_user(target_username,password)
            fix_permissions(new_user,userPerms)
            client['User_Customer'].addApiAuthenticationKey(id=new_user['id'])

        except SoftLayer.exceptions.SoftLayerAPIError as error:
            """
            If the user already exists, an exception is thrown. 
            Just reset their permissions and continue on.
            """
            oFilter = {}
            oFilter['users'] = {}
            oFilter['users']['username'] = {}
            oFilter['users']['username']['operation'] = target_username
            new_user = client['Account'].getUsers(filter=oFilter)[0]
            fix_permissions(new_user,userPerms)

        newApiKey = client['User_Customer'].getApiAuthenticationKeys(id=new_user['id'])
        print "username = %s" % (newApiKey[0]['user']['username'])
        print "api_key =  %s" % (newApiKey[0]['authenticationKey'])
        orderUserServer(newApiKey[0]['user']['username'],newApiKey[0]['authenticationKey'])
        start_user_num = start_user_num + 1


```

Disable user, changes their password, cancels their servers, and removes any sshKeys

```
import SoftLayer.API
from pprint import pprint as pp

def get_target_users(prefix):
    _filter = {
        'users': {
            'username': {
                'operation': '*= %s' % (prefix)
            }
        }
    }
    _mask = "mask[id,username]"
    _users = client['Account'].getUsers(filter=_filter, mask=_mask)
    return _users

def get_target_keys(prefix):
    _filter = {
        'sshKeys': {
            'label': {
                'operation': '*= %s' % (prefix)
            }
        }
    }

    _mask = "mask[id,label]"
    _users = client['Account'].getSshKeys(filter=_filter, mask=_mask)
    return _users

def print_result(result, thing):
    if result == True:
        print "OK"
    else:
        print "ERROR: "
        pp(thing)
    return

if __name__ == "__main__":
    import argparse
    argsparse = argparse.ArgumentParser(description='Number of users')
    argsparse.add_argument('--prefix',
                           help='Username prefix', default=False)
    argsparse.add_argument('--password',
                           help='New Password', default=False)
 
    args = argsparse.parse_args()

    client = SoftLayer.Client()
  
    users = get_target_users(args.prefix)

    for user in users:
        password =  args.password
        print 'User: ' + user['username'] + ' Password: ' + password 
        # status 1021 disables the user
        template = {
            'id': user['id'],
            'userStatusId': 1021
        }

        # Cancel any servers the user created
        servers = client['User_Customer'].getVirtualGuests(id=user['id'])
        result = True
        for virt in servers: 
            # the "," and the end of print removes the automatic newline
            print("\tCanceling host... " + virt['fullyQualifiedDomainName'] + " (" + str(virt['id']) + ")\t"),
            try:
                result = client['Virtual_Guest'].deleteObject(id=virt['id'])
                print_result(result,virt)
            except SoftLayer.exceptions.SoftLayerAPIError as error:
                print("\tException, host might already be canceling...")
                pp(error)

        print("\tChanging password for..." + user['username'] + " (" + str(user['id']) + ")\t"),
        result = client['User_Customer'].updatePassword(password, id=user['id'])
        print_result(result,user)
 
    sshkeys = get_target_keys(args.prefix)
    print 'SSH Key Removal'
    for key in sshkeys:
        print("Deleting key... " + key['label'] + " (" + str(key['id']) + ")\t"),
        result = client['SoftLayer_Security_Ssh_Key'].deleteObject(id=key['id'])
        print_result(result,key)

    print 'Complete'
```
