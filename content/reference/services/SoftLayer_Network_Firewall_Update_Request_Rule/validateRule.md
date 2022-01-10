---
title: "validateRule"
description: "Validate the supplied firewall request rule against the object it will apply to. For IPv4 rules, pass in an instance of SoftLayer_Network_Firewall_Update_Request_Rule. for IPv6 rules, pass in an instance of SoftLayer_Network_Firewall_Update_Request_Rule_Version6. The ID of the applied to object can either be applyToComponentId (an ID of a SoftLayer_Network_Component_Firewall) or applyToAclId (an ID of a SoftLayer_Network_Firewall_Module_Context_Interface_AccessControlList). One, and only one, of applyToComponentId and applyToAclId can be specified. 

If validation is successful, nothing is returned. If validation is unsuccessful, an exception is thrown explaining the nature of the validation error. "
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Firewall_Update_Request_Rule"
type: "reference"
layout: "method"
mainService : "SoftLayer_Network_Firewall_Update_Request_Rule"
---
