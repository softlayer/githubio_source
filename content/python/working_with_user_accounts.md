---
title: "Working with User Accounts"
description: "A few examples on interacting with User Accounts"
date: "2022-01-03"
classes: 
    - "SoftLayer_Account"
tags:
    - "User"
    - "Account"
    - "User_Account"
---

### Setup
All the functions defined in this article will be part of this `UserAccount` class. Which only sets up the SoftLayer Client, and configures the debugger, which allows you to see the exact API calls being made.

```python
import SoftLayer
from SoftLayer.CLI import environment
from SoftLayer.CLI import formatting
from pprint import pprint
class UserAccount:
    def __init__(self):
        self.client = SoftLayer.create_client_from_env()
        debugger = SoftLayer.DebugTransport(self.client.transport)
        self.user_customer_service = self.client['User_Customer']
        self.account_service = self.client['Account']
        self.user_customer_api_authentication_service = self.client['User_Customer_ApiAuthentication']
        self.client.transport = debugger
        self.env = environment.Environment()
    def debug(self):
        for call in self.client.transport.get_last_calls():
            pprint(self.client.transport.print_reproduceable(call))
```

## Get User status
To list the status of sub-users needs the user customer id, `list_sub_users(self, user_customer_id)` method calls to SoftLayer_User_Customer::getChildUsers method to retrieve the user list.

### Python
```python
    
    def list_sub_users(self, user_customer_id):
        mask = "mask[id,lastName,firstName,username,userStatusId,sslVpnAllowedFlag]"
        result = self.user_customer_service.getChildUsers(id=user_customer_id, mask=mask)
        self.env.fout(formatting.iter_to_table(result))
        return result
```

## Disable user can edit settings
To edit settings needs the username of user.

### Python
```python
    def disable_user_can_edit_settings(self, user_name):
        object_filter_user = {"users": {"username": {"operation": user_name}}}
        users = self.account_service.getUsers(filter=object_filter_user)
        users[0]['secondaryLoginManagementFlag'] = True
        result = self.user_customer_service.editObject(users[0], id=users[0]['id'])
        pprint(result)
        return result
```

## Duplicate User
To duplicate user needs the username of the user to copy and the username, office phone, user password, VPN password, first name, last name and email of the new user, the method create a new user with the same permissions, servers and virtual servers that the original user.
### Python
```python
    def get_user(self, username):
        object_filter = {"users": {"username": {"operation": username}}}
        try:
            users = self.account_service.getUsers(filter=object_filter)
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to get the user. " % (e.faultCode, e.faultString))
            exit(1)
        return users[0]
    def get_user_permissions(self, user):
        try:
            permissions = self.user_customer_service.getPermissions(id=user['id'])
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to get the user permissions. " % (e.faultCode, e.faultString))
            exit(1)
        return permissions
    def get_user_servers(self, user):
        try:
            servers = self.user_customer_service.getHardware(id=user['id'])
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to get the servers. " % (e.faultCode, e.faultString))
            exit(1)
        server_ids = []
        for server in servers:
            server_ids.append(server['id'])
        return server_ids
    def get_user_vsis(self, user):
        try:
            vsis = self.user_customer_service.getVirtualGuests(id=user['id'])
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to get the VSIs. " % (e.faultCode, e.faultString))
            exit(1)
        vsis_ids = []
        for vsi in vsis:
            vsis_ids.append(vsi['id'])
        return vsis_ids
    def duplicate_user(self, user_to_copy, newUserName, newOfficePhone, newUserPassword,
                      newVPNPassword, newFirstName, newLastName, newEmail):
        try:
            user = user_account.get_user(user_to_copy)
            permissions = user_account.get_user_permissions(user)
            server_access = user_account.get_user_servers(user)
            vsi_access = user_account.get_user_vsis(user)
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
            newUser = self.user_customer_service.createObject(templateObject, newUserPassword, newVPNPassword)
            print("user created")
            self.user_customer_service.addBulkPortalPermission(permissions, id=newUser['id'])
            print("permissions added")
            self.user_customer_service.addBulkHardwareAccess(server_access, id=newUser['id'])
            print("servers added")
            self.user_customer_service.addBulkVirtualGuestAccess(vsi_access, id=newUser['id'])
            print("VSIs added")
        except SoftLayer.SoftLayerAPIError as e:
            print("Unable to create new user. " % (e.faultCode, e.faultString))
            exit(1)
```

## Enable user can edit settings
To edit settings needs the username of user.

### Python
```python
    def enable_user_can_edit_settings(self, user_name):
        object_filter_user = {"users": {"username": {"operation": user_name}}}
        users = self.account_service.getUsers(filter=object_filter_user)
        users[0]['secondaryLoginManagementFlag'] = False
        result = self.user_customer_service.editObject(users[0], id=users[0]['id'])
        pprint(result)
        return result
```
## Toggle Security Questions
To disable and enable require security questions on log in needs the username of the user.

### Python
```python
    def toggle_security_questions(self, user_name):
        object_filter_user = {"users": {"username": {"operation": user_name}}}
        users = self.account_service.getUsers(filter=object_filter_user)
        # DISABLE
        users[0]['secondaryLoginRequiredFlag'] = False
        # ENABLE
        users[0]['secondaryLoginRequiredFlag'] = True
        result = self.user_customer_service.editObject(users[0], id=users[0]['id'])
        pprint(result)
        return result
```

## Show user accounts with and without two-factor enabled
The first method is to get the user accounts with two-factor enabled and the second to the user accounts with two-factor disabled.
### Python
```python
    def get_users_with_two_factor_authentication_enabled(self):
        mask = "mask[id,username,firstName,lastName,externalBindingCount,externalBindings]"
        object_filter = {
            'users': {
                'externalBindings': {
                    'active': {
                        'operation': '1'
                    }
                }
            }
        }
        result = self.account_service.getUsers(filter=object_filter, mask=mask)
        pprint(result)
        return result
    def get_users_with_two_factor_authentication_disabled(self):
        mask = "mask[id,username,firstName,lastName,externalBindingCount,externalBindings]"
        object_filter = {
            'users': {
                'externalBindings': {
                    'active': {
                        'operation': '0'
                    }
                }
            }
        }
        result = self.account_service.getUsers(filter=object_filter, mask=mask)
        pprint(result)
        return result
```

## Set user permissions
To set the user permission needs the user id, the method prints the initial permissions, adds TICKET_ADD permision to the user and prints the updated permissions.
### Python
```python
    def get_permissions(self, user_id):
        permissions = self.user_customer_service.getPermissions(id=user_id)
        return permissions
    def print_permissions(self, permissions):
        for permission in permissions:
            print("%s" % permission['keyName'])
    def add_ticket_permission(self, user_id):
        permissions = self.get_permissions(user_id)
        print("=== OLD PERMISSIONS ===")
        self.print_permissions(permissions)
        setperm = {'keyName': "TICKET_ADD"}
        self.user_customer_service.addPortalPermission(setperm, id=user_id)
        permissions = self.get_permissions(user_id)
        print("=== NEW PERMISSIONS ===")
        self.print_permissions(permissions)
```

## Change Passwords
The method use a prefix to find all matching users on your account and change their password, the method needs a prefix to find users and the new password.
### Python
```python
    def get_target_users(self, prefix):
        filter = {
            'users': {
                'username': {
                    'operation': '*= %s' % (prefix)
                }
            }
        }
        mask = "mask[id,username]"
        users = self.account_service.getUsers(filter=filter, mask=mask)
        return users
    def change_password_with_user_prefix(self, prefix, new_password):
        users = self.get_target_users(prefix)
        for user in users:
            print
            "Changing password for: " + str(user['id']) + " " + user['username']
            result = self.user_customer_service.updatePassword(new_password, id=user['id'])
            pprint(result)
        return users
```

## Create subscriber
To create a subscription to an unplanned incident needs the customer id and an array of delivery method keynames, `add_susbcription(self, delivery_method_key_names, customer_id)` method calls to SoftLayer_User_Customer::createSubscriberDeliveryMethods method to create subscriber.
### Python
```python
    def add_susbcription(self, delivery_method_key_names, customer_id):
        templates = self.user_customer_service.createSubscriberDeliveryMethods("UNPLANNED_INCIDENT", 
            delivery_method_key_names, id=customer_id)
        pprint(templates)
        return templates
```

## Toggle email invoice notifications
To disable and enable email invoice notifications needs the username of the user, `toggle_email_invoice_notifications(self, user_name)` method calls to SoftLayer_User_Customer::deactivateNotificationSubscriber method to disable notifications and SoftLayer_User_Customer::createNotificationSubscriber method to enable notifications.

### Python
```python
    def toggle_email_invoice_notifications(self, user_name):
        object_filter_user = {"users": {"username": {"operation": user_name}}}
        users = self.account_service.getUsers(filter=object_filter_user)
        # DISABLE
        result = self.user_customer_service.deactivateNotificationSubscriber(
            "BILLING_INVOICE_CREATED", users[0]['accountId'], id=users[0]['id'])
        # ENABLE
        # result = self.user_customer_service.createNotificationSubscriber(
        #   "BILLING_INVOICE_CREATED", users[0]['accountId'], id=users[0]['id'])
        pprint(result)
        return result
```

## Set restrict access to ip
To restrict the access from user to specific ip needs the username and the ip address, `set_restrict_access_to_ip(self, user_name, ip_address)` method calls to SoftLayer_User_Customer::editObject method to edit ipAddressRestriction attribute.

### Python
```python
    def set_restrict_access_to_ip(self, user_name, ip_address):
        object_filter_user = {"users": {"username": {"operation": user_name}}}
        users = self.account_service.getUsers(filter=object_filter_user)
        # Set the value to "" to delete the previous configured IP address.
        users[0]['ipAddressRestriction'] = ip_address
        result = self.user_customer_service.editObject(users[0], id=users[0]['id'])
        pprint(result)
        return result
```

## Set expire password
To set the expire password needs the username and the number of days that the password will be active, `set_expire_password_in(self, user_name, number_of_days)` method calls to SoftLayer_User_Customer::editObject method to edit secondaryPasswordTimeoutDays attribute.

### Python
```python
    def set_expire_password_in(self, user_name, number_of_days):
        object_filter_user = {"users": {"username": {"operation": user_name}}}
        users = self.account_service.getUsers(filter=object_filter_user)
        # Set the value to 0 for never
        users[0]['secondaryPasswordTimeoutDays'] = number_of_days
        result = self.user_customer_service.editObject(users[0], id=users[0]['id'])
        pprint(result)
        return result
```

## Set api ip address restriction
To set API IP address restriction needs the username and the ip address.

### Python
```python
    def set_api_ip_address_restriction(self, user_name, ip_address):
        object_filter_user = {"users": {"username": {"operation": user_name}}}
        users = self.account_service.getUsers(filter=object_filter_user)
        keys = self.user_customer_service.getApiAuthenticationKeys(id=users[0]['id'])
        keys[0]["ipAddressRestriction"] = ip_address
        result = self.user_customer_api_authentication_service.editObject(keys[0], id=keys[0]['id'])
        pprint(result)
        return result
```

## Get notification subscribers
To get notification subscribers needs the username, `get_notification_subscribers(self, user_name)` method calls to SoftLayer_User_Customer::getSubscribers method to list the notification subscribers.

### Python
```python
    def get_notification_subscribers(self, user_name):
        object_filter_user = {"users": {"username": {"operation": user_name}}}
        users = self.account_service.getUsers(filter=object_filter_user)
        result = self.user_customer_service.getSubscribers(id=users[0]['id'])
        pprint(result)
        return result
```

## Running the Example

### Python
```python
if __name__ == '__main__':
    user_account = UserAccount()
    test_username = "username0235"
    test_user_id = 12345678

    # Get User status
    user_account.list_sub_users(test_user_id)

    # Disable user can edit settings
    user_account.disable_user_can_edit_settings(test_username)
    
    # Duplicate User
    userToCopy = "originalUsername"
    newUserName = "target"
    newUserPassword = "Passwords2."
    newVPNPassword = "Passwords2."
    newOfficePhone = "512365485"
    newFirstName = "myFistName"
    newLastName = "myLastName"
    newEmail = "myemail@softlayer.com"
    user_account.duplicate_user(user_to_copy, newUserName, newOfficePhone, 
        newUserPassword, newVPNPassword, newFirstName, newLastName, newEmail)

    # Enable user can edit settings
    user_account.enable_user_can_edit_settings(test_username)

    # Toggle Security Questions
    user_account.toggle_security_questions(test_username)

    # Show user accounts with and without two-factor enabled
    user_account.get_users_with_two_factor_authentication_enabled()
    user_account.get_users_with_two_factor_authentication_disabled()

    # Set user permissions
    user_account.add_ticket_permission(test_user_id)

    # Change Passwords
    prefix = "PREFIX"
    password = "qweASDzxc!23"
    user_account.change_password_with_user_prefix(prefix, password)

    # Change Passwords
    delivery_method_key_names = [
        "EMAIL"
    ]
    user_account.add_susbcription(delivery_method_key_names, test_user_id)

    # Toggle email invoice notifications
    user_account.toggle_email_invoice_notifications(test_username)

    # Set restrict access to ip
    ip_address = "10.2.32.4"
    user_account.set_restrict_access_to_ip(test_username, ip_address)

    # Set expire password
    password_active_days = 90
    user_account.set_expire_password_in(test_username, password_active_days)
    
    # Set api ip address restriction
    ip_address = "10.10.10.10"
    user_account.set_restrict_access_to_ip(test_username, ip_address)
    
    # Get notification subscribers
    user_account.get_notification_subscribers(test_username)
```