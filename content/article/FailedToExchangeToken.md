---
title: "Failed to Exchange Token"
description: "How to fix the 'SoftLayer_Exception: Failed to exchange token (HTTP 500)' error"
date: "2025-02-28"
tags:
    - "article"
    - "sldn"
    - "authentication"
    - "errors"
---


# The Fix

The user getting this error will need to have their [IBMid Updated](https://cloud.ibm.com/docs/account?topic=account-iamuserinv&interface=ui#change-ibm-id). 

Basically, just press this button on the users profile page, and link it to a currently valid IBMid


<img src="/img/articles/UpdateIBMid.png" alt="Update IBMid" width="100%"/> 

# The Problem

`SoftLayer_Exception: Failed to exchange token (HTTP 500)` Happens because the user on your account is linked to an IBMid that is no longer valid.
On January 22 2025, an update went out allowing better integration with IBM's IAM policies for Classic Infrastructure users, which requires users be linked to a valid IBMid now. 