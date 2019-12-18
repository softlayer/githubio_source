---
title: "SoftLayer_Resource_Group_Member_Network_Vlan"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Group_Member_Network_Vlan"
---

# SoftLayer_Resource_Group_Member_Network_Vlan
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Network_Vlan' >Datatype</a></li>
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
[createDate]: #createdate
#### [createDate]
A resource group member's creation date.  
<span class="type-label">Type: </span>**dateTime**

-----
[id]: #id
#### [id]
A resource group member's ID.  
<span class="type-label">Type: </span>**integer**

-----
[status]: #status
#### [status]
A resource group member's status.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[attributes]: #attributes
#### [attributes]
A resource group member's associated attributes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Attribute'>SoftLayer_Resource_Group_Member_Attribute[] </a>**

-----
[descendantMembers]: #descendantmembers
#### [descendantMembers]
A resource group member's associated member descendants.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**

-----
[group]: #group
#### [group]
A resource group member's resource group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group </a>**

-----
[resource]: #resource
#### [resource]
A resource group member's associated network VLAN.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Vlan'>SoftLayer_Network_Vlan </a>**

-----
[roles]: #roles
#### [roles]
A resource group member's associated roles.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Role'>SoftLayer_Resource_Group_Role[] </a>**

-----
[type]: #type
#### [type]
A resource group member's type.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member_Type'>SoftLayer_Resource_Group_Member_Type </a>**


## Count

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of a resource group member's associated attributes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[descendantMemberCount]: #descendantmembercount
#### [descendantMemberCount]
A count of a resource group member's associated member descendants.   
<span class="type-label">Type: </span>**unsigned long**


-----
[roleCount]: #rolecount
#### [roleCount]
A count of a resource group member's associated roles.   
<span class="type-label">Type: </span>**unsigned long**

</div>


