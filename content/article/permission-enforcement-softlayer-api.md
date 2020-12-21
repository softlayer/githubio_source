---
title: "Permission Enforcement in the SoftLayer API"
description: "The SoftLayer API is built around the same system of user permissions that power the SoftLayer customer portal. What the API exposes and allows depends on the user account that is making the call and that user's permission set."
date: "2011-06-20"
tags:
    - "article"
    - "sldn"
    - "permissions"
---


The SoftLayer API is built around the same system of user permissions that power the SoftLayer customer portal. What the API exposes and allows depends on the user's account that is making the call and that user's permission set. Your account's master user has full permissions to every service and method associated with your account. Please be wary if you choose to execute API method calls using your account's master user.


The SoftLayer API treats a permission error like an object not found error, returning an 404 [exception](article/exception-handling-softlayer-api/) stating that it can't find an object rather than say that the current user does not have permission to view it.

## Permission List

Use [SoftLayer_User_Customer_CustomerPermission_Permission::getAllObjects()](/reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/getAllObjects/) to get a full and current list.

| Description         | KeyName             |
|---------------------|---------------------|
| Access Virtual DedicatedHosts             | ACCESS_ALL_DEDICATEDHOSTS                   |
| All Guest Access                          | ACCESS_ALL_GUEST                            |
| All Hardware Access                       | ACCESS_ALL_HARDWARE                         |
| Add Brand Account                         | ACCOUNT_BRAND_ADD                           |
| Add Customer Account                      | ACCOUNT_CUSTOMER_ADD                        |
| Add Auxiliary Password                    | ACCOUNT_PASSWORD_AUXILIARY_ADD              |
| Delete Auxiliary Password                 | ACCOUNT_PASSWORD_AUXILIARY_DELETE           |
| Edit Auxiliary Password                   | ACCOUNT_PASSWORD_AUXILIARY_EDIT             |
| View Account Summary                      | ACCOUNT_SUMMARY_VIEW                        |
| Activate Partner Customer Account         | ACTIVATE_PARTNER_ACCOUNT                    |
| Add/Upgrade Storage (StorageLayer)        | ADD_SERVICE_STORAGE                         |
| Manage Antivirus/Spyware                  | ANTI_MALWARE_MANAGE                         |
| View Bandwidth Statistics                 | BANDWIDTH_MANAGE                            |
| Manage CDN Account                        | CDN_ACCOUNT_MANAGE                          |
| View CDN Bandwidth Statistics             | CDN_BANDWIDTH_VIEW                          |
| Manage CDN File Transfers                 | CDN_FILE_MANAGE                             |
| Edit Company Profile                      | COMPANY_EDIT                                |
| Manage Placement Group                    | CUSTOMER_PLACEMENT_GROUP_MANAGEMENT         |
| Manage Provisioning Scripts               | CUSTOMER_POST_PROVISION_SCRIPT_MANAGEMENT   |
| Manage Reserved Capacity Group            | CUSTOMER_RESERVED_CAPACITY_GROUP_MANAGEMENT |
| Manage SSH Keys                           | CUSTOMER_SSH_KEY_MANAGEMENT                 |
| Physically Access a Datacenter            | DATACENTER_ACCESS                           |
| Physically Access a Customer's Colo Cage  | DATACENTER_ROOM_ACCESS                      |
| View Virtual Dedicated Host Details       | DEDICATED_HOST_VIEW                         |
| Manage DNS                                | DNS_MANAGE                                  |
| Manage EU Supported Account Flag          | EU_LIMITED_PROCESSING_MANAGE                |
| Manage Firewalls                          | FIREWALL_MANAGE                             |
| Manage Firewall Rules                     | FIREWALL_RULE_MANAGE                        |
| forums                                    | FORUM_ACCESS                                |
| Manage Network Gateways                   | GATEWAY_MANAGE                              |
| View Hardware Details                     | HARDWARE_VIEW                               |
| Edit Hostname/Domain                      | HOSTNAME_EDIT                               |
| Host IDS                                  | HOST_ID_MANAGE                              |
| Add/Upgrade Cloud Instances               | INSTANCE_UPGRADE                            |
| Add IP Addresses                          | IP_ADD                                      |
| View licenses                             | LICENSE_VIEW                                |
| Manage Load Balancers                     | LOADBALANCER_MANAGE                         |
| Manage Lockbox                            | LOCKBOX_MANAGE                              |
| Manage Public Network                     | MANAGE_PUBLIC_NETWORK                       |
| Manage Security Groups                    | MANAGE_SECURITY_GROUPS                      |
| Manage Device Monitoring                  | MONITORING_MANAGE                           |
| Storage Manage                            | NAS_MANAGE                                  |
| Manage Network IDs                        | NETWORK_IDS_MANAGE                          |
| Manage E-mail Delivery Service            | NETWORK_MESSAGE_DELIVERY_MANAGE             |
| Manage Network Subnet Routes              | NETWORK_ROUTE_MANAGE                        |
| Manage IPSEC Network Tunnels              | NETWORK_TUNNEL_MANAGE                       |
| Manage Network VLAN Spanning              | NETWORK_VLAN_SPANNING                       |
| Manage Notification Subscribers           | NTF_SUBSCRIBER_MANAGE                       |
| Submit One-Time Payments                  | ONE_TIME_PAYMENTS                           |
| Manage Port Control                       | PORT_CONTROL                                |
| Upgrade Port                              | PORT_UPGRADE                                |
| Manage Public Images                      | PUBLIC_IMAGE_MANAGE                         |
| Add Compute with Public Network Port      | PUBLIC_NETWORK_COMPUTE                      |
| Manage Queue Service                      | QUEUE_MANAGE                                |
| IPMI Remote Management                    | REMOTE_MANAGEMENT                           |
| Request Compliance Report                 | REQUEST_COMPLIANCE_REPORT                   |
| Reset Password                            | RESET_PORTAL_PASSWORD                       |
| Manage SAML Authentication                | SAML_AUTHENTICATION_MANAGE                  |
| Manage Auto Scale Groups                  | SCALE_GROUP_MANAGE                          |
| Manage Certificates (SSL)                 | SECURITY_CERTIFICATE_MANAGE                 |
| View Certificates (SSL)                   | SECURITY_CERTIFICATE_VIEW                   |
| Security                                  | SECURITY_MANAGE                             |
| Add Server                                | SERVER_ADD                                  |
| Cancel Server                             | SERVER_CANCEL                               |
| OS Reloads and Rescue Kernel              | SERVER_RELOAD                               |
| Upgrade Server                            | SERVER_UPGRADE                              |
| Add/Upgrade Services                      | SERVICE_ADD                                 |
| Cancel Services                           | SERVICE_CANCEL                              |
| Upgrade Services                          | SERVICE_UPGRADE                             |
| Manage Firewall Software                  | SOFTWARE_FIREWALL_MANAGE                    |
| ssl vpn                                   | SSL_VPN_ENABLED                             |
| Add Tickets                               | TICKET_ADD                                  |
| Edit Tickets                              | TICKET_EDIT                                 |
| Add / Edit Tickets                        | TICKET_MANAGE                               |
| Search Tickets                            | TICKET_SEARCH                               |
| View Tickets                              | TICKET_VIEW                                 |
| View All Tickets                          | TICKET_VIEW_ALL                             |
| View Tickets by Hardware Access           | TICKET_VIEW_BY_HARDWARE                     |
| View Tickets by Computing Instance Access | TICKET_VIEW_BY_VIRTUAL_GUEST                |
| Update Payment Details                    | UPDATE_PAYMENT_DETAILS                      |
| View Event Log                            | USER_EVENT_LOG_VIEW                         |
| Manage Users                              | USER_MANAGE                                 |
| View cPanel                               | VIEW_CPANEL                                 |
| View Customer Software Password           | VIEW_CUSTOMER_SOFTWARE_PASSWORD             |
| View Helm                                 | VIEW_HELM                                   |
| View Plesk                                | VIEW_PLESK                                  |
| View QuantaStor                           | VIEW_QUANTASTOR                             |
| View Urchin                               | VIEW_URCHIN                                 |
| View Virtual Server Details               | VIRTUAL_GUEST_VIEW                          |
| VPN Administration                        | VPN_MANAGE                                  |
| Vulnerability Scanning                    | VULN_SCAN_MANAGE                            |


### Adding and Removing User Permissions

Version 5.7.0 and higher of the [slcli](https://github.com/softlayer/softlayer-python) support managing user permissions with the [slcli user](https://softlayer-python.readthedocs.io/en/latest/cli/users.html) set of commands

To change your user’s permission set using a direct API call, use the following guidelines based on the task you would like to accomplish:

* To add permissions, execute either the addPortalPermission or addBulkPortalPermission methods in the [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer/) service
* To remove permissions, execute either the removePortalPermission or removeBulkPortalPermission methods in the [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer/)


### Access Restrictions

It is also possible to limit user interactivity to only certain servers purchased by a customer account or to none of the servers listed on the account.  As with adding and removing user permissions, this task may also be completed through either the SoftLayer Customer Portal or by using a direct API call.

If a user has any of the `ACCESS_ALL_` type of permission, that will give them access to all of that resource. Otherwise they will need to be granted access on a per resource basis. Any resource a user orders will automatically be allowed to their account.

To change a user’s hardware restrictions using a direct API call, use the following guidelines based on the task you would like to accomplish:


* To add user hardware access, execute either the addHardwareAccess or addBulkHardwareAccess methods in the [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer/) service.
* To remove user hardware access execute either the removeHardwareAccess or removeBulkHardwareAccess methods in the [SoftLayer_User_Customer](/reference/services/SoftLayer_User_Customer/)  service.

The same applies for virtualGuest access as well, with just a different method to call.

### See Also

* [Permission Examples](/tags/permissions/)
* [Permission Service](/reference/services/SoftLayer_User_Customer_CustomerPermission_Permission/)
* [Customer Service](/reference/services/SoftLayer_User_Customer/)
* [Python Example](/python/user_customer_permissions.py/