---
title: "duplicate_user.py"
description: "duplicate_user.py"
date: "2017-11-23"
classes: 
    - "SoftLayer_User_Customer"
    - "SoftLayer_Virtual_Guest"
    - "SoftLayer_Hardware"
    - "SoftLayer_Account"
    - "SoftLayer_User_Customer_CustomerPermission_Permission"
tags:
    - "users"
---


```
"""
Duplicate user

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_User_Customer
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getVirtualGuests
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getHardware
http://sldn.softlayer.com/reference/services/SoftLayer_User_Customer/getPermissions

License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

def get_user(username, accountService):
    """Get an user.
        :param string username: The username of the user you wish to get.
        :param Softlayer_Account accountService: The Softlayer account service.
        :returns: A Softlayer_User_Customer object with the information about the user.
    """
    objectFilter = {"users": { "username": {"operation": username}}}
    try:
        users = accountService.getUsers(filter=objectFilter)
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the user. " % (e.faultCode, e.faultString))
        exit(1)
    
    return users[0]

def get_user_permissions(user, userService):
    """Get the permissions for an user.
        :param Softlayer_User_Customer user: The user from who you wish to get the permissions.
        :param Softlayer_User_Customer userService: The Softlayer_User_Customer service.
        :returns: A list of SoftLayer_User_Customer_CustomerPermission_Permission object with the information about
                  the permissions for the user.
    """
    try:
        permissions = userService.getPermissions(id=user['id'])
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the user permissions. " % (e.faultCode, e.faultString))
        exit(1)
    
    return permissions

def get_user_servers(user, userService):
    """Get the servers for an user.
        :param Softlayer_User_Customer user: The user from who you wish to get the servers.
        :param Softlayer_User_Customer userService: The Softlayer_User_Customer service.
        :returns: A list of SoftLayer_Hardware object with the information about
                  the servers for the user.
    """
    try:
        servers = userService.getHardware(id=user['id'])
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the servers. " % (e.faultCode, e.faultString))
        exit(1)
    
    serverIds = []
    for server in servers:
        serverIds.append(server['id'])
    
    return serverIds

def get_user_vsis(user, userService):
    """Get the VSIs for an user.
        :param Softlayer_User_Customer user: The user from who you wish to get the VSIs.
        :param Softlayer_User_Customer userService: The Softlayer_User_Customer service.
        :returns: A list of SoftLayer_Virtual_Guest object with the information about
                  the VSIs for the user.
    """
    try:
        vsis = userService.getVirtualGuests(id=user['id'])
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to get the VSIs. " % (e.faultCode, e.faultString))
        exit(1)
    
    vsisIds = []
    for vsi in vsis:
        vsisIds.append(vsi['id'])
    
    return vsis

def duplicateUser(user, permissions, serverAccess, vsiAccess, newUserName, newOfficePhone, newUserPasswrod, newVPNPassword, newFirstName, newLastName, newEmail, userService):
    """Create an user using the data from another user.
        :param Softlayer_User_Customer user: The user from who you wish duplicate the data.
        :param SoftLayer_User_Customer_CustomerPermission_Permission permissions: An array with the permissions for the new user.
        :param SoftLayer_Hardware serverAccess: An array with the servers for the new user.
        :param SoftLayer_Virtual_Guest vsiAccess: An array with the VSIs for the new user.
        :param string newUserName: The username for the new user.
        :param string newOfficePhone: The office phone for the new user.
        :param string newUserPasswrod: The password for the new user.
        :param string newVPNPassword: The VPN password for the new user.
        :param string newFirstName: The fisrt name for the new user.
        :param string newLastName: The last name for the new user.
        :param string newEmail: The email for the new user.
        :param Softlayer_User_Customer userService: The Softlayer_User_Customer service.
    """
    try:
        templateObject = {
            "accountId": user['accountId'],
            "address1": user['address1'],
            "city": user['city'],
            "companyName": user['companyName'],
            "country": user['country'],
            "daylightSavingsTimeFlag": user['daylightSavingsTimeFlag'],
            "email": newEmail,
            "firstName": newFirstName,
            "lastName": newLastName,
            "officePhone": newOfficePhone,
            # The user ID of the user which is creating this user
            "parentId": user['parentId'],
            "postalCode": user['postalCode'],
            "state": user['state'],
            "timezoneId": user['timezoneId'],
            # 1001 = Active; 1002 = Disable; 1003 = Inactive; 1021 = Delete ; 1022 = VPN Only
            "userStatusId": user['userStatusId'],
            "username": newUserName
        }
        newUser = userService.createObject(templateObject, newUserPasswrod, newVPNPassword)
        print("user created")
        userService.addBulkPortalPermission(permissions ,id=newUser['id'])
        print("permissions added")
        userService.addBulkHardwareAccess(serverAccess ,id=newUser['id'])
        print("servers added")
        userService.addBulkVirtualGuestAccess(serverAccess ,id=newUser['id'])
        print("VSIs added")
    except SoftLayer.SoftLayerAPIError as e:
        print("Unable to create new user. " % (e.faultCode, e.faultString))
        exit(1)
    

USERNAME = 'set me'
API_KEY = 'set me'

userToCopy = "source"
newUserName = "target"
newUserPasswrod = "Passwords2."
newVPNPassword = "Passwords2."
newOfficePhone = "512365485"
newFirstName = "myFistName"
newLastName = "myLastName"
newEmail = "myemail@softlayer.com"

# Declares the API services.
client = SoftLayer.create_client_from_env(username=USERNAME, api_key=API_KEY)
userService = client['SoftLayer_User_Customer']
accountService = client['SoftLayer_Account']

user =  get_user(userToCopy, accountService)
permissions = get_user_permissions(user, userService)
serverAccess = get_user_servers(user, userService)
vsiAccess = get_user_vsis(user, userService)
duplicateUser(user, permissions, serverAccess, vsiAccess, newUserName, newOfficePhone, newUserPasswrod, newVPNPassword, newFirstName, newLastName, newEmail, userService)

```
