---
title: "SoftLayer_Network_Tunnel_Module_Context"
description: "The SoftLayer_Network_Tunnel_Module_Context data type contains general information relating to a single SoftLayer networ... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Tunnel_Module_Context"
---

# SoftLayer_Network_Tunnel_Module_Context
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Tunnel_Module_Context data type contains general information relating to a single SoftLayer network tunnel.  The SoftLayer_Network_Tunnel_Module_Context is useful to gather information such as related customer subnets (remote) and internal subnets (local) associated with the network tunnel as well as other information needed to manage the network tunnel.  Account and billing information related to the network tunnel can also be retrieved. 

### External Links


* [IPSec at Wikipedia](http://en.wikipedia.org/wiki/IPsec)






<!-- Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Filer END -->

<div id="properties" class="content">
<div id="localProperties" class="prop-content" >

## Local
<div class="prop-row">

-----
[accountId]: #accountid
#### [accountId]
A network tunnel's account identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[advancedConfigurationFlag]: #advancedconfigurationflag
#### [advancedConfigurationFlag]
A flag used to specify when advanced configurations, complex configurations that require manual setup, are being applied to network devices for a network tunnel. When the flag is set to true (1), a network tunnel cannot be configured through the management portal nor the API.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
The date a network tunnel was created.  
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[customerPeerIpAddress]: #customerpeeripaddress
#### [customerPeerIpAddress]
The remote end of a network tunnel. This end of the network tunnel resides on an outside network and will be sending and receiving the IPSec packets.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[friendlyName]: #friendlyname
#### [friendlyName]
The name giving to a network tunnel by a user.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A network tunnel's unique identifier.  
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[internalPeerIpAddress]: #internalpeeripaddress
#### [internalPeerIpAddress]
The local  end of a network tunnel. This end of the network tunnel resides on the SoftLayer networks and allows access to remote end of the tunnel to subnets on SoftLayer networks.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date a network tunnel was last modified. 

NOTE:  This date should NOT be used to determine when the network tunnel configurations were last applied to the network device.   
<span class="type-label">Type: </span>**dateTime**


</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A network tunnel's unique name used on the network device.  
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[phaseOneAuthentication]: #phaseoneauthentication
#### [phaseOneAuthentication]
Authentication used to generate keys for protecting the negotiations for a network tunnel.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[phaseOneDiffieHellmanGroup]: #phaseonediffiehellmangroup
#### [phaseOneDiffieHellmanGroup]
Determines the strength of the key used in the key exchange process.  The higher the group number the stronger the key is and the more secure it is.  However, processing time will increase as the strength of the key increases.  Both peers in the must use the Diffie-Hellman Group.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[phaseOneEncryption]: #phaseoneencryption
#### [phaseOneEncryption]
Encryption used to generate keys for protecting the negotiations for a network tunnel.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[phaseOneKeylife]: #phaseonekeylife
#### [phaseOneKeylife]
Amount of time (in seconds) allowed to pass before the encryption key expires.  A new key is generated without interrupting service. Valid times are from 120 to 172800 seconds.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[phaseTwoAuthentication]: #phasetwoauthentication
#### [phaseTwoAuthentication]
The authentication used in phase 2 proposal negotiation process.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[phaseTwoDiffieHellmanGroup]: #phasetwodiffiehellmangroup
#### [phaseTwoDiffieHellmanGroup]
Determines the strength of the key used in the key exchange process.  The higher the group number the stronger the key is and the more secure it is.  However, processing time will increase as the strength of the key increases.  Both peers must use the Diffie-Hellman Group.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[phaseTwoEncryption]: #phasetwoencryption
#### [phaseTwoEncryption]
The encryption used in phase 2 proposal negotiation process.   
<span class="type-label">Type: </span>**string**


</div>
<div class="prop-row">

-----
[phaseTwoKeylife]: #phasetwokeylife
#### [phaseTwoKeylife]
Amount of time (in seconds) allowed to pass before the encryption key expires.  A new key is generated without interrupting service. Valid times are from 120 to 172800 seconds.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[phaseTwoPerfectForwardSecrecy]: #phasetwoperfectforwardsecrecy
#### [phaseTwoPerfectForwardSecrecy]
Determines if the generated keys are made from previous keys.  When PFS is specified, a Diffie-Hellman exchange occurs each time a new security association is negotiated.   
<span class="type-label">Type: </span>**integer**


</div>
<div class="prop-row">

-----
[presharedKey]: #presharedkey
#### [presharedKey]
A key used so that peers authenticate each other.  This key is hashed by using the phase one encryption and phase one authentication.   
<span class="type-label">Type: </span>**string**


</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[account]: #account
#### [account]
The account that a network tunnel belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**


</div>
<div class="prop-row">

-----
[activeTransaction]: #activetransaction
#### [activeTransaction]
DEPRECATED  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a>**


</div>
<div class="prop-row">

-----
[addressTranslations]: #addresstranslations
#### [addressTranslations]
A network tunnel's address translations.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a>**


</div>
<div class="prop-row">

-----
[allAvailableServiceSubnets]: #allavailableservicesubnets
#### [allAvailableServiceSubnets]
Subnets that provide access to SoftLayer services such as the management portal and the SoftLayer API.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[billingItem]: #billingitem
#### [billingItem]
The current billing item for network tunnel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a>**


</div>
<div class="prop-row">

-----
[customerSubnets]: #customersubnets
#### [customerSubnets]
Remote subnets that are allowed access through a network tunnel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet'>SoftLayer_Network_Customer_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[datacenter]: #datacenter
#### [datacenter]
The datacenter location for one end of the network tunnel that allows access to account's private subnets.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a>**


</div>
<div class="prop-row">

-----
[internalSubnets]: #internalsubnets
#### [internalSubnets]
Private subnets that can be accessed through the network tunnel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[serviceSubnets]: #servicesubnets
#### [serviceSubnets]
Service subnets that can be access through the network tunnel.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[staticRouteSubnets]: #staticroutesubnets
#### [staticRouteSubnets]
Subnets used for a network tunnel's address translations.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a>**


</div>
<div class="prop-row">

-----
[transactionHistory]: #transactionhistory
#### [transactionHistory]
DEPRECATED  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a>**


</div>

## Count
<div class="prop-row">

-----
[addressTranslationCount]: #addresstranslationcount
#### [addressTranslationCount]
A count of a network tunnel's address translations.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[allAvailableServiceSubnetCount]: #allavailableservicesubnetcount
#### [allAvailableServiceSubnetCount]
A count of subnets that provide access to SoftLayer services such as the management portal and the SoftLayer API.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[customerSubnetCount]: #customersubnetcount
#### [customerSubnetCount]
A count of remote subnets that are allowed access through a network tunnel.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[internalSubnetCount]: #internalsubnetcount
#### [internalSubnetCount]
A count of private subnets that can be accessed through the network tunnel.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[serviceSubnetCount]: #servicesubnetcount
#### [serviceSubnetCount]
A count of service subnets that can be access through the network tunnel.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[staticRouteSubnetCount]: #staticroutesubnetcount
#### [staticRouteSubnetCount]
A count of subnets used for a network tunnel's address translations.   
<span class="type-label">Type: </span>**unsigned long**


</div>
<div class="prop-row">

-----
[transactionHistoryCount]: #transactionhistorycount
#### [transactionHistoryCount]
A count of dEPRECATED   
<span class="type-label">Type: </span>**unsigned long**


</div>
</div>


