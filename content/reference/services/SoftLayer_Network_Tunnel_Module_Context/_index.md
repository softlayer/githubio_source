---
title: "SoftLayer_Network_Tunnel_Module_Context"
description: "A SoftLayer network tunnel allows customer to authenticate and encrypt all IP traffic between two locations. 

Manage th... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
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


A SoftLayer network tunnel allows customer to authenticate and encrypt all IP traffic between two locations. 

Manage the entire network tunnel using this service.  The SoftLayer_Network_Tunnel_Module_Context allows customers to manage subnets on both ends of the network tunnel.  Address translations can also be managed.  SoftLayer also provides the ability to apply the network tunnel configurations on the SoftLayer network devices. 



        
<div id="properties" class="content service-content">

## Methods

<div class="view-filters">
    <div class="clearfix">
        <div class="search-input-box">
            <input placeholder="Method Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

<div id="method-div">

<div class="method-row">

#### [addCustomerSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addCustomerSubnetToNetworkTunnel)
Associate a remote subnet to a network tunnel

</div>

<div class="method-row">

#### [addPrivateSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addPrivateSubnetToNetworkTunnel)
Associate a private subnet to a network tunnel.

</div>

<div class="method-row">

#### [addServiceSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addServiceSubnetToNetworkTunnel)
Associate a service subnet to a network tunnel.

</div>

<div class="method-row">

#### [applyConfigurationsToDevice](/reference/services/SoftLayer_Network_Tunnel_Module_Context/applyConfigurationsToDevice)
Apply current configuration settings to the network device

</div>

<div class="method-row">

#### [createAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslation)
Create an address translation for a network tunnel

</div>

<div class="method-row">

#### [createAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslations)
Create address translations for a network tunnel

</div>

<div class="method-row">

#### [deleteAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/deleteAddressTranslation)
Delete an address translation from a network tunnel

</div>

<div class="method-row">

#### [downloadAddressTranslationConfigurations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/downloadAddressTranslationConfigurations)
Returns IPSec VPN tunnel address translation configurations in a text file.

</div>

<div class="method-row">

#### [downloadParameterConfigurations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/downloadParameterConfigurations)
Returns IPSec VPN tunnel configurations in a text file.

</div>

<div class="method-row">

#### [editAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslation)
Edit an address translation for a network tunnel

</div>

<div class="method-row">

#### [editAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslations)
Edit address translations for a network tunnel

</div>

<div class="method-row">

#### [editObject](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editObject)
Edit various settings for a network tunnel.

</div>

<div class="method-row">

#### [getAccount](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAccount)
Retrieve the account that a network tunnel belongs to.

</div>

<div class="method-row">

#### [getActiveTransaction](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getActiveTransaction)
Retrieval: DEPRECATED

</div>

<div class="method-row">

#### [getAddressTranslationConfigurations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAddressTranslationConfigurations)
Build and returns IPsec VPN  tunnel address translation configurations

</div>

<div class="method-row">

#### [getAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAddressTranslations)
Retrieve a network tunnel's address translations.

</div>

<div class="method-row">

#### [getAllAvailableServiceSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAllAvailableServiceSubnets)
Retrieve subnets that provide access to SoftLayer services such as the management portal and the SoftLayer API.

</div>

<div class="method-row">

#### [getAuthenticationDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAuthenticationDefault)
Returns the authentication default.

</div>

<div class="method-row">

#### [getAuthenticationOptions](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAuthenticationOptions)
Returns the authentication options.

</div>

<div class="method-row">

#### [getBillingItem](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getBillingItem)
Retrieve the current billing item for network tunnel.

</div>

<div class="method-row">

#### [getCustomerSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getCustomerSubnets)
Retrieve remote subnets that are allowed access through a network tunnel.

</div>

<div class="method-row">

#### [getDatacenter](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getDatacenter)
Retrieve the datacenter location for one end of the network tunnel that allows access to account's private subnets.

</div>

<div class="method-row">

#### [getDiffieHellmanGroupDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getDiffieHellmanGroupDefault)
Returns the diffie hellman group default.

</div>

<div class="method-row">

#### [getDiffieHellmanGroupOptions](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getDiffieHellmanGroupOptions)
Returns the diffie-hellman group options.

</div>

<div class="method-row">

#### [getEncryptionDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getEncryptionDefault)
Returns the encryption default.

</div>

<div class="method-row">

#### [getEncryptionOptions](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getEncryptionOptions)
Returns the encryption options.

</div>

<div class="method-row">

#### [getInternalSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getInternalSubnets)
Retrieve private subnets that can be accessed through the network tunnel.

</div>

<div class="method-row">

#### [getKeylifeLimits](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getKeylifeLimits)
Returns the keylife min and max limits.

</div>

<div class="method-row">

#### [getObject](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getObject)
Retrieve a SoftLayer_Network_Tunnel_Module_Context record.

</div>

<div class="method-row">

#### [getParameterConfigurationsForCustomerView](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getParameterConfigurationsForCustomerView)
Build and returns IPsec VPN tunnel configurations

</div>

<div class="method-row">

#### [getPhaseOneKeylifeDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getPhaseOneKeylifeDefault)
Returns the phase one keylife default.

</div>

<div class="method-row">

#### [getPhaseTwoKeylifeDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getPhaseTwoKeylifeDefault)
Returns phase two keylife default.

</div>

<div class="method-row">

#### [getServiceSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getServiceSubnets)
Retrieve service subnets that can be access through the network tunnel.

</div>

<div class="method-row">

#### [getStaticRouteSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getStaticRouteSubnets)
Retrieve subnets used for a network tunnel's address translations.

</div>

<div class="method-row">

#### [getTransactionHistory](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getTransactionHistory)
Retrieval: DEPRECATED

</div>

<div class="method-row">

#### [removeCustomerSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeCustomerSubnetFromNetworkTunnel)
Disassociate a customer (remote) subnet from a network tunnel

</div>

<div class="method-row">

#### [removePrivateSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removePrivateSubnetFromNetworkTunnel)
Disassociate a private subnet from a network tunnel

</div>

<div class="method-row">

#### [removeServiceSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeServiceSubnetFromNetworkTunnel)
Disassociate service subnet from a network tunnel

</div>
</div>

</div>

