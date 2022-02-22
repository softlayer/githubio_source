---
title: "SoftLayer_Network_Service_Vpn_Overrides"
description: "Use to manually decide which subnets within your virtual private address space a SoftLayer portal VPN user may access.  Stores a 'white list' consisting of a collection of subnet ids matched up against user ids. This class will reject any subnets or users, that don't belong to the account holder.  Note that simply assigning overrides to a user does not enforce the rule change.  You must set the manual override flag for the VPN user in the SoftLayer_User_Customer class.  It is recommended that before you create new VPN subnet overrides, you delete any old ones for a user, since the VPN authentication system limits the number of accessible subnets by a single user to sixty four.  This holds true regardless of whether the VPN user accesses the network via SSL or PPTP.  After making any changes to a user's VPN settings, you should call SoftLayer_User_Customer::updateVpnUser() on that customer object. 

"
date: "2018-02-12"
tags:
    - "service"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Service_Vpn_Overrides"
type: "reference"
layout: "service"
mainService : "SoftLayer_Network_Service_Vpn_Overrides"
---
