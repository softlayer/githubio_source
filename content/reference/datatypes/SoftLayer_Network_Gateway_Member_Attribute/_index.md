---
title: "SoftLayer_Network_Gateway_Member_Attribute"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Gateway_Member_Attribute"
---

# SoftLayer_Network_Gateway_Member_Attribute
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_Gateway_Member_Attribute' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Gateway_Member_Attribute' >Datatype</a></li>
    </ul>
</div>

## Description 






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

## Local
-----
[id]: #id
#### [id]
A gateway member's internal identifier.   
<span class="type-label">Type: </span>**integer**

-----
[lastvSRXVersion]: #lastvsrxversion
#### [lastvSRXVersion]
The previous vSRX version of the gateway software   
<span class="type-label">Type: </span>**string**

-----
[licenseKey]: #licensekey
#### [licenseKey]
  
<span class="type-label">Type: </span>**string**

-----
[memberId]: #memberid
#### [memberId]
The gateway member for this attribute.   
<span class="type-label">Type: </span>**integer**

-----
[networkModel]: #networkmodel
#### [networkModel]
Network model of the gateway.  
<span class="type-label">Type: </span>**string**

-----
[password]: #password
#### [password]
Password of the user name.  
<span class="type-label">Type: </span>**string**

-----
[sshKeyId]: #sshkeyid
#### [sshKeyId]
The SSH key id of key assigned to Gateway.   
<span class="type-label">Type: </span>**integer**

-----
[username]: #username
#### [username]
Username associated with the gateway.  
<span class="type-label">Type: </span>**string**

-----
[vSRXVersion]: #vsrxversion
#### [vSRXVersion]
The vSRX version of the gateway software   
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[gatewayMember]: #gatewaymember
#### [gatewayMember]
The gateway member has these attributes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Gateway_Member'>SoftLayer_Network_Gateway_Member </a>**

-----
[sshKey]: #sshkey
#### [sshKey]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key </a>**


## Count
</div>


