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






<!-- Service Filer BEGIN -->
<div class="view-filters">
        <div class="clearfix">
            <div class="search-input-box">
                <input placeholder="Method Filter" onkeyup="titleSearch(inputId='prop-input', divId='properties', elementClass='prop-row')" 
                    type="text" id="prop-input" value="" size="30" maxlength="128" class="form-text">
            </div>
        </div>
</div>
<!-- Service Filer END -->

<div id="properties" class="content">
    <div id="localProperties" class="prop-content" >
        <h2>Local</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#accountId" name=accountId>accountId</a>
            </span>
            <div class='views-field-body'>A network tunnel's account identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#advancedConfigurationFlag" name=advancedConfigurationFlag>advancedConfigurationFlag</a>
            </span>
            <div class='views-field-body'>A flag used to specify when advanced configurations, complex configurations that require manual setup, are being applied to network devices for a network tunnel. When the flag is set to true (1), a network tunnel cannot be configured through the management portal nor the API.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#createDate" name=createDate>createDate</a>
            </span>
            <div class='views-field-body'>The date a network tunnel was created. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#customerPeerIpAddress" name=customerPeerIpAddress>customerPeerIpAddress</a>
            </span>
            <div class='views-field-body'>The remote end of a network tunnel. This end of the network tunnel resides on an outside network and will be sending and receiving the IPSec packets.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#friendlyName" name=friendlyName>friendlyName</a>
            </span>
            <div class='views-field-body'>The name giving to a network tunnel by a user. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#id" name=id>id</a>
            </span>
            <div class='views-field-body'>A network tunnel's unique identifier. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#internalPeerIpAddress" name=internalPeerIpAddress>internalPeerIpAddress</a>
            </span>
            <div class='views-field-body'>The local  end of a network tunnel. This end of the network tunnel resides on the SoftLayer networks and allows access to remote end of the tunnel to subnets on SoftLayer networks.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#modifyDate" name=modifyDate>modifyDate</a>
            </span>
            <div class='views-field-body'>The date a network tunnel was last modified. 

NOTE:  This date should NOT be used to determine when the network tunnel configurations were last applied to the network device.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>dateTime</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#name" name=name>name</a>
            </span>
            <div class='views-field-body'>A network tunnel's unique name used on the network device. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phaseOneAuthentication" name=phaseOneAuthentication>phaseOneAuthentication</a>
            </span>
            <div class='views-field-body'>Authentication used to generate keys for protecting the negotiations for a network tunnel.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phaseOneDiffieHellmanGroup" name=phaseOneDiffieHellmanGroup>phaseOneDiffieHellmanGroup</a>
            </span>
            <div class='views-field-body'>Determines the strength of the key used in the key exchange process.  The higher the group number the stronger the key is and the more secure it is.  However, processing time will increase as the strength of the key increases.  Both peers in the must use the Diffie-Hellman Group.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phaseOneEncryption" name=phaseOneEncryption>phaseOneEncryption</a>
            </span>
            <div class='views-field-body'>Encryption used to generate keys for protecting the negotiations for a network tunnel.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phaseOneKeylife" name=phaseOneKeylife>phaseOneKeylife</a>
            </span>
            <div class='views-field-body'>Amount of time (in seconds) allowed to pass before the encryption key expires.  A new key is generated without interrupting service. Valid times are from 120 to 172800 seconds.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phaseTwoAuthentication" name=phaseTwoAuthentication>phaseTwoAuthentication</a>
            </span>
            <div class='views-field-body'>The authentication used in phase 2 proposal negotiation process.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phaseTwoDiffieHellmanGroup" name=phaseTwoDiffieHellmanGroup>phaseTwoDiffieHellmanGroup</a>
            </span>
            <div class='views-field-body'>Determines the strength of the key used in the key exchange process.  The higher the group number the stronger the key is and the more secure it is.  However, processing time will increase as the strength of the key increases.  Both peers must use the Diffie-Hellman Group.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phaseTwoEncryption" name=phaseTwoEncryption>phaseTwoEncryption</a>
            </span>
            <div class='views-field-body'>The encryption used in phase 2 proposal negotiation process.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phaseTwoKeylife" name=phaseTwoKeylife>phaseTwoKeylife</a>
            </span>
            <div class='views-field-body'>Amount of time (in seconds) allowed to pass before the encryption key expires.  A new key is generated without interrupting service. Valid times are from 120 to 172800 seconds.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#phaseTwoPerfectForwardSecrecy" name=phaseTwoPerfectForwardSecrecy>phaseTwoPerfectForwardSecrecy</a>
            </span>
            <div class='views-field-body'>Determines if the generated keys are made from previous keys.  When PFS is specified, a Diffie-Hellman exchange occurs each time a new security association is negotiated.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>integer</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#presharedKey" name=presharedKey>presharedKey</a>
            </span>
            <div class='views-field-body'>A key used so that peers authenticate each other.  This key is hashed by using the phase one encryption and phase one authentication.  </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>string</p>
            </div>
        </div>
            </div>
        <div id="relationalProperties"  class="prop-content" >
        <h2>Relational</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#account" name=account>account</a>
            </span>
            <div class='views-field-body'>The account that a network tunnel belongs to. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#activeTransaction" name=activeTransaction>activeTransaction</a>
            </span>
            <div class='views-field-body'>The transaction that is currently applying configurations for the network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#addressTranslations" name=addressTranslations>addressTranslations</a>
            </span>
            <div class='views-field-body'>A network tunnel's address translations. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Tunnel_Module_Context_Address_Translation'>SoftLayer_Network_Tunnel_Module_Context_Address_Translation[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#allAvailableServiceSubnets" name=allAvailableServiceSubnets>allAvailableServiceSubnets</a>
            </span>
            <div class='views-field-body'>Subnets that provide access to SoftLayer services such as the management portal and the SoftLayer API. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#billingItem" name=billingItem>billingItem</a>
            </span>
            <div class='views-field-body'>The current billing item for network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Billing_Item'>SoftLayer_Billing_Item </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#customerSubnets" name=customerSubnets>customerSubnets</a>
            </span>
            <div class='views-field-body'>Remote subnets that are allowed access through a network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Customer_Subnet'>SoftLayer_Network_Customer_Subnet[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#datacenter" name=datacenter>datacenter</a>
            </span>
            <div class='views-field-body'>The datacenter location for one end of the network tunnel that allows access to account's private subnets. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Location'>SoftLayer_Location </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#internalSubnets" name=internalSubnets>internalSubnets</a>
            </span>
            <div class='views-field-body'>Private subnets that can be accessed through the network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#serviceSubnets" name=serviceSubnets>serviceSubnets</a>
            </span>
            <div class='views-field-body'>Service subnets that can be access through the network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#staticRouteSubnets" name=staticRouteSubnets>staticRouteSubnets</a>
            </span>
            <div class='views-field-body'>Subnets used for a network tunnel's address translations. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Network_Subnet'>SoftLayer_Network_Subnet[] </a></p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#transactionHistory" name=transactionHistory>transactionHistory</a>
            </span>
            <div class='views-field-body'>The transaction history for this network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p><a href='/reference/datatypes/SoftLayer_Provisioning_Version1_Transaction'>SoftLayer_Provisioning_Version1_Transaction[] </a></p>
            </div>
        </div>
                <h2>Count</h2>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#addressTranslationCount" name=addressTranslationCount>addressTranslationCount</a>
            </span>
            <div class='views-field-body'>A count of a network tunnel's address translations. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#allAvailableServiceSubnetCount" name=allAvailableServiceSubnetCount>allAvailableServiceSubnetCount</a>
            </span>
            <div class='views-field-body'>A count of subnets that provide access to SoftLayer services such as the management portal and the SoftLayer API. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#customerSubnetCount" name=customerSubnetCount>customerSubnetCount</a>
            </span>
            <div class='views-field-body'>A count of remote subnets that are allowed access through a network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#internalSubnetCount" name=internalSubnetCount>internalSubnetCount</a>
            </span>
            <div class='views-field-body'>A count of private subnets that can be accessed through the network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#serviceSubnetCount" name=serviceSubnetCount>serviceSubnetCount</a>
            </span>
            <div class='views-field-body'>A count of service subnets that can be access through the network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#staticRouteSubnetCount" name=staticRouteSubnetCount>staticRouteSubnetCount</a>
            </span>
            <div class='views-field-body'>A count of subnets used for a network tunnel's address translations. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
                <div class='prop-row views-row'>
            <span class='views-field-title'>
                <a href="#transactionHistoryCount" name=transactionHistoryCount>transactionHistoryCount</a>
            </span>
            <div class='views-field-body'>A count of the transaction history for this network tunnel. </div>
            <span class="type-label">Type:</span> 
            <div class='type-content'>
                <p>unsignedLong</p>
            </div>
        </div>
            </div>
</div>


