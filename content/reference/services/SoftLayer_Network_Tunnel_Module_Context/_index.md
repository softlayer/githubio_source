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



        
<div id="properties" class="content">
    <h2>Methods</h2>
    <div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Datatype Filter" onkeyup="titleSearch(inputId='edit-combine', divId='method-div', elementClass='method-row')" 
                    type="text" id="edit-combine" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
    </div>
    <div id="method-div">
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/addCustomerSubnetToNetworkTunnel'> addCustomerSubnetToNetworkTunnel</a> </span>
            <div class='views-field-body'>Associate a remote subnet to a network tunnel</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/addPrivateSubnetToNetworkTunnel'> addPrivateSubnetToNetworkTunnel</a> </span>
            <div class='views-field-body'>Associate a private subnet to a network tunnel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/addServiceSubnetToNetworkTunnel'> addServiceSubnetToNetworkTunnel</a> </span>
            <div class='views-field-body'>Associate a service subnet to a network tunnel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/applyConfigurationsToDevice'> applyConfigurationsToDevice</a> </span>
            <div class='views-field-body'>Apply current configuration settings to the network device</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslation'> createAddressTranslation</a> </span>
            <div class='views-field-body'>Create an address translation for a network tunnel</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/createAddressTranslations'> createAddressTranslations</a> </span>
            <div class='views-field-body'>Create address translations for a network tunnel</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/deleteAddressTranslation'> deleteAddressTranslation</a> </span>
            <div class='views-field-body'>Delete an address translation from a network tunnel</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/downloadAddressTranslationConfigurations'> downloadAddressTranslationConfigurations</a> </span>
            <div class='views-field-body'>Returns IPSec VPN tunnel address translation configurations in a text file.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/downloadParameterConfigurations'> downloadParameterConfigurations</a> </span>
            <div class='views-field-body'>Returns IPSec VPN tunnel configurations in a text file.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslation'> editAddressTranslation</a> </span>
            <div class='views-field-body'>Edit an address translation for a network tunnel</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/editAddressTranslations'> editAddressTranslations</a> </span>
            <div class='views-field-body'>Edit address translations for a network tunnel</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/editObject'> editObject</a> </span>
            <div class='views-field-body'>Edit various settings for a network tunnel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAccount'> getAccount</a> </span>
            <div class='views-field-body'>Retrieve the account that a network tunnel belongs to.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getActiveTransaction'> getActiveTransaction</a> </span>
            <div class='views-field-body'>Retrieve the transaction that is currently applying configurations for the network tunnel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAddressTranslationConfigurations'> getAddressTranslationConfigurations</a> </span>
            <div class='views-field-body'>Build and returns IPsec VPN  tunnel address translation configurations</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAddressTranslations'> getAddressTranslations</a> </span>
            <div class='views-field-body'>Retrieve a network tunnel's address translations.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAllAvailableServiceSubnets'> getAllAvailableServiceSubnets</a> </span>
            <div class='views-field-body'>Retrieve subnets that provide access to SoftLayer services such as the management portal and the SoftLayer API.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAuthenticationDefault'> getAuthenticationDefault</a> </span>
            <div class='views-field-body'>Returns the authentication default.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getAuthenticationOptions'> getAuthenticationOptions</a> </span>
            <div class='views-field-body'>Returns the authentication options.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getBillingItem'> getBillingItem</a> </span>
            <div class='views-field-body'>Retrieve the current billing item for network tunnel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getCustomerSubnets'> getCustomerSubnets</a> </span>
            <div class='views-field-body'>Retrieve remote subnets that are allowed access through a network tunnel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getDatacenter'> getDatacenter</a> </span>
            <div class='views-field-body'>Retrieve the datacenter location for one end of the network tunnel that allows access to account's private subnets.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getDiffieHellmanGroupDefault'> getDiffieHellmanGroupDefault</a> </span>
            <div class='views-field-body'>Returns the diffie hellman group default.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getDiffieHellmanGroupOptions'> getDiffieHellmanGroupOptions</a> </span>
            <div class='views-field-body'>Returns the diffie-hellman group options.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getEncryptionDefault'> getEncryptionDefault</a> </span>
            <div class='views-field-body'>Returns the encryption default.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getEncryptionOptions'> getEncryptionOptions</a> </span>
            <div class='views-field-body'>Returns the encryption options.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getInternalSubnets'> getInternalSubnets</a> </span>
            <div class='views-field-body'>Retrieve private subnets that can be accessed through the network tunnel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getKeylifeLimits'> getKeylifeLimits</a> </span>
            <div class='views-field-body'>Returns the keylife min and max limits.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getObject'> getObject</a> </span>
            <div class='views-field-body'>Retrieve a SoftLayer_Network_Tunnel_Module_Context record.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getParameterConfigurationsForCustomerView'> getParameterConfigurationsForCustomerView</a> </span>
            <div class='views-field-body'>Build and returns IPsec VPN tunnel configurations</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getPhaseOneKeylifeDefault'> getPhaseOneKeylifeDefault</a> </span>
            <div class='views-field-body'>Returns the phase one keylife default.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getPhaseTwoKeylifeDefault'> getPhaseTwoKeylifeDefault</a> </span>
            <div class='views-field-body'>Returns phase two keylife default.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getServiceSubnets'> getServiceSubnets</a> </span>
            <div class='views-field-body'>Retrieve service subnets that can be access through the network tunnel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getStaticRouteSubnets'> getStaticRouteSubnets</a> </span>
            <div class='views-field-body'>Retrieve subnets used for a network tunnel's address translations.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/getTransactionHistory'> getTransactionHistory</a> </span>
            <div class='views-field-body'>Retrieve the transaction history for this network tunnel.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeCustomerSubnetFromNetworkTunnel'> removeCustomerSubnetFromNetworkTunnel</a> </span>
            <div class='views-field-body'>Disassociate a customer (remote) subnet from a network tunnel</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/removePrivateSubnetFromNetworkTunnel'> removePrivateSubnetFromNetworkTunnel</a> </span>
            <div class='views-field-body'>Disassociate a private subnet from a network tunnel</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Network_Tunnel_Module_Context/removeServiceSubnetFromNetworkTunnel'> removeServiceSubnetFromNetworkTunnel</a> </span>
            <div class='views-field-body'>Disassociate service subnet from a network tunnel</div>
        </div>
        </div>
</div>

