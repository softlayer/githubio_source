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
            <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
        </div>
    </div>
</div>

#### [addCustomerSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addCustomerSubnetToNetworkTunnel)
Associate a remote subnet to a network tunnel

#### [addPrivateSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addPrivateSubnetToNetworkTunnel)
Associate a private subnet to a network tunnel.

#### [addServiceSubnetToNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/addServiceSubnetToNetworkTunnel)
Associate a service subnet to a network tunnel.

#### [applyConfigurationsToDevice](/reference/services/SoftLayer_Network_Tunnel_Module_Context/applyConfigurationsToDevice)
Apply current configuration settings to the network device

#### [createAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslation)
Create an address translation for a network tunnel

#### [createAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslations)
Create address translations for a network tunnel

#### [deleteAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/deleteAddressTranslation)
Delete an address translation from a network tunnel

#### [downloadAddressTranslationConfigurations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/downloadAddressTranslationConfigurations)
Returns IPSec VPN tunnel address translation configurations in a text file.

#### [downloadParameterConfigurations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/downloadParameterConfigurations)
Returns IPSec VPN tunnel configurations in a text file.

#### [editAddressTranslation](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslation)
Edit an address translation for a network tunnel

#### [editAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslations)
Edit address translations for a network tunnel

#### [editObject](/reference/services/SoftLayer_Network_Tunnel_Module_Context/editObject)
Edit various settings for a network tunnel.

#### [getAccount](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAccount)
Retrieve the account that a network tunnel belongs to.

#### [getActiveTransaction](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getActiveTransaction)
Retrieve the transaction that is currently applying configurations for the network tunnel.

#### [getAddressTranslationConfigurations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAddressTranslationConfigurations)
Build and returns IPsec VPN  tunnel address translation configurations

#### [getAddressTranslations](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAddressTranslations)
Retrieve a network tunnel's address translations.

#### [getAllAvailableServiceSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAllAvailableServiceSubnets)
Retrieve subnets that provide access to SoftLayer services such as the management portal and the SoftLayer API.

#### [getAuthenticationDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAuthenticationDefault)
Returns the authentication default.

#### [getAuthenticationOptions](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAuthenticationOptions)
Returns the authentication options.

#### [getBillingItem](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getBillingItem)
Retrieve the current billing item for network tunnel.

#### [getCustomerSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getCustomerSubnets)
Retrieve remote subnets that are allowed access through a network tunnel.

#### [getDatacenter](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getDatacenter)
Retrieve the datacenter location for one end of the network tunnel that allows access to account's private subnets.

#### [getDiffieHellmanGroupDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getDiffieHellmanGroupDefault)
Returns the diffie hellman group default.

#### [getDiffieHellmanGroupOptions](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getDiffieHellmanGroupOptions)
Returns the diffie-hellman group options.

#### [getEncryptionDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getEncryptionDefault)
Returns the encryption default.

#### [getEncryptionOptions](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getEncryptionOptions)
Returns the encryption options.

#### [getInternalSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getInternalSubnets)
Retrieve private subnets that can be accessed through the network tunnel.

#### [getKeylifeLimits](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getKeylifeLimits)
Returns the keylife min and max limits.

#### [getObject](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getObject)
Retrieve a SoftLayer_Network_Tunnel_Module_Context record.

#### [getParameterConfigurationsForCustomerView](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getParameterConfigurationsForCustomerView)
Build and returns IPsec VPN tunnel configurations

#### [getPhaseOneKeylifeDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getPhaseOneKeylifeDefault)
Returns the phase one keylife default.

#### [getPhaseTwoKeylifeDefault](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getPhaseTwoKeylifeDefault)
Returns phase two keylife default.

#### [getServiceSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getServiceSubnets)
Retrieve service subnets that can be access through the network tunnel.

#### [getStaticRouteSubnets](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getStaticRouteSubnets)
Retrieve subnets used for a network tunnel's address translations.

#### [getTransactionHistory](/reference/services/SoftLayer_Network_Tunnel_Module_Context/getTransactionHistory)
Retrieve the transaction history for this network tunnel.

#### [removeCustomerSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeCustomerSubnetFromNetworkTunnel)
Disassociate a customer (remote) subnet from a network tunnel

#### [removePrivateSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removePrivateSubnetFromNetworkTunnel)
Disassociate a private subnet from a network tunnel

#### [removeServiceSubnetFromNetworkTunnel](/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeServiceSubnetFromNetworkTunnel)
Disassociate service subnet from a network tunnel

</div>

