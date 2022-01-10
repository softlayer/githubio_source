---
title: "SoftLayer_Billing_Order_Item"
description: "Every individual item that a SoftLayer customer is billed for is recorded in the SoftLayer_Billing_Item data type. Billing items range from server chassis to hard drives to control panels, bandwidth quota upgrades and port upgrade charges. SoftLayer [SoftLayer_Billing_Invoice](reference/datatypes/SoftLayer_Billing_Invoice) are generated from the cost of a customer's billing items. Billing items are copied from the product catalog as they're ordered by customers to create a reference between an account and the billable items they own. 

Billing items exist in a tree relationship. Items are associated with each other by parent/child relationships. Component items such as CPU's, RAM, and software each have a parent billing item for the server chassis they're associated with. Billing Items with a null parent item do not have an associated parent item. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Billing"
classes:
    - "SoftLayer_Billing_Order_Item"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Billing_Order_Item"
---
