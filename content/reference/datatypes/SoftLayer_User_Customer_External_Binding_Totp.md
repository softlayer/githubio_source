---
title: "SoftLayer_User_Customer_External_Binding_Totp"
description: "SoftLayer provides its customers the ability to add an additional layer of security to the SoftLayer customer portal by requiring that a user login and authenticate with a trusted 3rd party before they are given access to their SoftLayer account.  This is accomplished by creating an external binding for a specific vendor, in this case Time-based One Time Password.  When the SoftLayer user attempts to log in to the SoftLayer customer portal they will first be prompted for their normal SoftLayer username and password.  Once that information is verified they will be asked to generate and provide a security code from their Time-based One Time Password application. Once the security code has been authenticated the user will be allowed access to the SoftLayer customer portal. 

The time-based one time password external binding service allows a user to create an external binding, enable, disable, and delete an external binding. 

Once a SoftLayer user has a valid and active time-based one time password external binding, they will be required to always use their credential to login to the SoftLayer customer portal.  In addition any user with an active external binding will be prohibited from using the API. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_External_Binding_Totp"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_User_Customer_External_Binding_Totp"
---
