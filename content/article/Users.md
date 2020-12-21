---
title: "User Management"
description: "How to interact with users on your account. Breaks down a lot of the various API calls required to manage an account, such as getting login attempts, event logs, permissions and more."
date: "2020-12-21"
tags:
    - "article"
    - "sldn"
    - "users"
    - "permissions"
---


# Hierarchy

Each account will have a "Master" user. This "Master" user is the main user for the account, considered the account owner, and can do anything possible for an account. This user is a bit special, in that it needs no permissions set, as it has them all. So when looking at permissions set for this user, you will notice that none are set, which is normal for this specific type of user.

This user account will have the username like SL12345, or for newer accounts, IBM12345. The [isMasterUserFlag](/reference/datatypes/SoftLayer_User_Customer/#ismasteruserflag) will let you know if a user in question is the master user or not.

You can also use the [SoftLayer_Account::getCurrentUser()](m/reference/services/SoftLayer_Account/getCurrentUser/) method to determine some information about the user you are currently authenticated with.

```bash
curl -g -u API_USER:API_KEY 'https://api.softlayer.com/rest/v3.1/SoftLayer_Account/getCurrentUser.json?objectMask=mask[id,username,isMasterUserFlag]'

{"id": 167758, "isMasterUserFlag": true, "username": "SL12345"}
```

## [Child Users](#child-users) {#child-users .anchor-link}

As the master user, you can create, or invite, additional users to access this account. If this new user has the `ADD_USER` permission, they can then create additional users as well. However these new users will only be able to be given permissions their parent user has.

> [Permission enforcement with the SoftLayer API](/article/permission-enforcement-softlayer-api/)

Calling [SoftLayer_User_Customer::getChildUsers()](/reference/services/SoftLayer_User_Customer/getChildUsers/) will display any children the specified user (12345 here) has, and `childUserCount` will let you know if THAT account has any more children.

```bash
curl -g -u $SL_USER:$SL_APIKEY  'https://api.softlayer.com/rest/v3.1/SoftLayer_User_Customer/12345/getChildUsers.json?objectMask=mask[id,username,childUserCount]'

[
    {
        "childUserCount": 0,
        "id": 8344222,
        "username": "12345_testuser+123@gmail.com"
    },
    {
        "childUserCount": 1,
        "id": 8724518,
        "username": "testuser@jp.ibm.com"
    }
]
```

### Creating users

Use the [SoftLayer_User_Customer::createObject()](/reference/services/SoftLayer_User_Customer/createObject/) API to make a new user. It takes in 3 parameters.

1. a `SoftLayer_User_Customer` object. Its not obvious from the documentation which fields are required to create a new object, but this template is a good starting point.

```json
 {
        "username": "NewUserName", // If left blank, will be automatically assigned, usually as <accountId>_<email>
        "firstName": "API",
        "lastName": "Learner",
        "email": "someone@somewhere.com", // An invite will be sent to this email to acctive the user.
        "companyName": "IBM",
        "address1": "123 api road",
        "city": "Houston",
        "country": "US",
        "postalCode": "TX 77002",
        "userStatusId": 1001, // ACTIVE
        "timezoneId": 107
    }
```
> [SoftLayer_Locale_Timezone::getAllObjects](/reference/services/SoftLayer_Locale_Timezone/getAllObjects/) will list all timezones. If a timezone is specified, times displayed in API responses will be in that timezone.

2. (optional) A password to give the user. The user will still get an invitation email, with a link to reset their password. Failing to reset the password will leave the user with the specified password. If no password is set, the user will not be able to login until they click the link in their email. The password parameter is ignored for VPN_ONLY users or for IBMid authenticated user
3. (optional) VPN password. If the vpnPassword is provided, then the user’s vpnPassword will be set to the provided password.  When creating a vpn only user, the vpnPassword MUST be supplied.  If the vpnPassword is not provided, then the user will need to use the portal to edit their profile and set the vpnPassword.

>The [SLCLI](https://github.com/softlayer/softlayer-python) has a command called [slcli user create](https://softlayer-python.readthedocs.io/en/latest/cli/users/#user-create) which is really handy in creating new user accounts.

>[Python Manage User Example](/python/manageUsers/)


### User Statuses

You can get this list of statuses from [SoftLayer_User_Customer_Status::getAllObjects](/reference/services/SoftLayer_User_Customer_Status/getAllObjects/).

|  Id  | Key Name | Notes |
|--- | --- | --- |
| 1001 |     ACTIVE     | The normal status|
| 1002 |    DISABLED    | Turned off for now |
| 1003 |    INACTIVE    | Not really used|
| 1004 |    PENDING     | Waiting for user to click their invitation link|
| 1005 |   SUSPENDED    | Suspended by IBM |
| 1006 | IAMID_INVALID  | Something went wrong with linking this user |
| 1021 | CANCEL_PENDING | About to be deleted |
| 1022 |    VPN_ONLY    | User can only access the VPN|


### Deleting Users

To delete a user, call [SoftLayer_User_Customer::editObject()](/reference/services/SoftLayer_User_Customer/editObject/) and set their `statusId` to `1021`. This will immediately disable their account, and eventually be removed from your account.

# [Managing Users](#manage_users) {#manage_users .anchor-link}

To start with, [SoftLayer_Account::getUsers()](/reference/services/SoftLayer_Account/getUsers/) will list all current users on your account. 

>Python example for [getting details on servers ordered by user](/python/billsByUser/)

## Important [User_Customer](/reference/datatypes/SoftLayer_User_Customer/) Fields

- [Id](/reference/datatypes/SoftLayer_User_Customer/#id) Used in any interaction with the user directly.
- [Email](/reference/datatypes/SoftLayer_User_Customer/#email) How to get in touch with this user.
- [passwordExpireDate](/reference/datatypes/SoftLayer_User_Customer/#passwordexpiredate) When their password will expire
- [externalBindings](/reference/datatypes/SoftLayer_User_Customer/#externalbindings) If the user has any 2 Factor Authentication (2FA) devices configured they will show up here
- [permissions](/reference/datatypes/SoftLayer_User_Customer/#permissions) Lists all permissions this user has.
- [successfulLogins](/reference/datatypes/SoftLayer_User_Customer/#successfullogins) / [unsuccessfulLogins](/reference/datatypes/SoftLayer_User_Customer/#unsuccessfullogins) / [loginAttempts](/reference/datatypes/SoftLayer_User_Customer/#loginattempts) A record of all the recent logins for this account. For a full list of logins, see the `Event_Log` service.
- [childUsers](/reference/datatypes/SoftLayer_User_Customer/#childusers) Lists any users this specific user has created.
- [hardware](/reference/datatypes/SoftLayer_User_Customer/#hardware) / [virtualGuests](/reference/datatypes/SoftLayer_User_Customer/#virtualguests) / [dedicatedHosts](/reference/datatypes/SoftLayer_User_Customer/#dedicatedhosts) Lists the specific devices this user has access to view information about. Will be empty if the corresponding `hasFullHardwareAccessFlag` / `hasFullVirtualGuestAccessFlag` / `hasFullDedicatedHostAccessFlag` flag is set to `True`.
- [openTickets](/reference/datatypes/SoftLayer_User_Customer/#opentickets) If this user has created any tickets.
- [roles](/reference/datatypes/SoftLayer_User_Customer/#roles) If the user has been assigned any access roles. Roles provide access and permissions that might not show up directly on the user account.
- [timezone](/reference/datatypes/SoftLayer_User_Customer/#timezone) how the user will see time related information.

## [User Event Log](#user_event_log) {#user_event_log .anchor-link}
Information about user logins, among other things, is kept in the [SoftLayer_Event_Log](reference/services/SoftLayer_Event_Log/) service. This service can be a bit unwieldy, but here are a few quick examples on how to filter for only specific bits of data.

### User Events

The SLCLI has a [slcli event-log](https://softlayer-python.readthedocs.io/en/latest/cli/event_log/) command, which is very useful in navigating this data.

There are usually a lot of Event_Logs, so using a `resultLimit` is very important here.

#### All User Type Events

```bash
curl -u $SL_USER:$SL_APIKEY  -g 'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?resultLimit=0,20&objectFilter={"objectName":{"operation":"User"}}'
```
```json
[
    {
        "accountId": 307608,
        "eventCreateDate": "2020-12-21T05:46:47.386584-06:00",
        "eventName": "Login Successful",
        "ipAddress": "123.141.123.251",
        "label": "12345_tester@ibm.com",
        "metaData": "",
        "objectId": 8150224,
        "objectName": "User",
        "openIdConnectUserName": "12345_tester@ibm.com",
        "resource": {
            # The user object will be in here.
        },
        "traceId": "5fe08b275e622",
        "userId": 8150224,
        "userType": "CUSTOMER",
        "username": "12345_tester@ibm.com"
    },
```

> [SoftLayer_Event_Log::getAllEventObjectNames](/reference/services/SoftLayer_Event_Log/getAllEventObjectNames/) lists all the types of events you can filter by.

#### Events for a specific user

```bash
curl -u $SL_USER:$SL_APIKEY  -g 'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?resultLimit=0,20&objectFilter={"objectId":{"operation":"123456"},"objectName":{"operation":"User"}}'
```

#### Events for a specific time frame

```bash
curl -u $SL_USER:$SL_APIKEY  -g 'https://api.softlayer.com/rest/v3.1/SoftLayer_Event_Log/getAllObjects.json?resultLimit=0,20&objectFilter={"eventCreateDate":{"operation":"betweenDate","options":[{"name":"startDate","value":["2020-12-01T00:00:00.000000-00:00"]},{"name":"endDate","value":["2020-12-21T00:00:00.000000-00:00"]}]}}'
```

# IBMid

Users are now linked to [IBMid](https://cloud.ibm.com/apidocs/user-management), which controls a users access between accounts, and across the wider IBM Cloud platform.  You can determine more information about the user link with the [SoftLayer_User_Customer::IBMidLink](/reference/datatypes/SoftLayer_User_Customer/#ibmidlink) property. 

[SoftLayer_User_Customer::inviteUserToLinkOpenIdConnect()](/reference/services/SoftLayer_User_Customer/inviteUserToLinkOpenIdConnect/) can be used to link a user on your account to IBMid if needed.


# Further Reading
- [User API examples](/tags/users/)
- [SLCLI User Commands](https://softlayer-python.readthedocs.io/en/latest/cli/users/)
- [IBMCLOUD CLI User Commands](https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#classic-service-commands)
- [Authenticating with the SLAPI](/article/authenticating-softlayer-api/)
- [Account Access Overview](https://cloud.ibm.com/docs/account?topic=account-iamoverview)
- [Access Basics](https://cloud.ibm.com/docs/account?topic=account-account-getting-started)