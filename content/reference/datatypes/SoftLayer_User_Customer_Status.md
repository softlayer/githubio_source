---
title: "SoftLayer_User_Customer_Status"
description: "Each SoftLayer User Customer instance is assigned a status code that determines how it's treated in the customer portal. This status is reflected in the SoftLayer_User_Customer_Status data type. Status differs from user permissions in that user status applies globally to the portal while user permissions are applied to specific portal functions. 

Note that a status of 'PENDING' also has been added. This status is specific to users that are configured to use IBMid authentication. This would include some (not all) users on accounts that are linked to Platform Services (PaaS, formerly Bluemix) accounts, but is not limited to users in such accounts. Using IBMid authentication is optional for active users even if it is not required by the account type. PENDING status indicates that a relationship between an IBMid and a user is being set up but is not complete. To be complete, PENDING users need to perform an action ('accepting the invitation') before becoming an active user within IBM Cloud and/or IMS. PENDING is a system state, and can not be administered by users (including the account master user). SoftLayer Commercial is the only environment where IBMid and/or account linking are used. 

"
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "User"
classes:
    - "SoftLayer_User_Customer_Status"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_User_Customer_Status"
---
