---
title: "SoftLayer_Resource_Group"
description: ""
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Resource"
classes:
    - "SoftLayer_Resource_Group"
---

# SoftLayer_Resource_Group
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Resource_Group' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Resource_Group' >Datatype</a></li>
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
A resource group's creation date.  
<span class="type-label">Type: </span>**dateTime**

-----
[description]: #description
#### [description]
A resource group's description.  
<span class="type-label">Type: </span>**string**

-----
[id]: #id
#### [id]
A resource group's ID.  
<span class="type-label">Type: </span>**integer**

-----
[keyName]: #keyname
#### [keyName]
A resource group's keyname.  
<span class="type-label">Type: </span>**string**

-----
[name]: #name
#### [name]
A resource group's name.  
<span class="type-label">Type: </span>**string**

-----
[rootResourceGroupId]: #rootresourcegroupid
#### [rootResourceGroupId]
  
<span class="type-label">Type: </span>**integer**

-----
[templateId]: #templateid
#### [templateId]
A resource group's template ID.  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[ancestorGroups]: #ancestorgroups
#### [ancestorGroups]
A resource group's associated group ancestors.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group[] </a>**

-----
[attributes]: #attributes
#### [attributes]
A resource group's associated attributes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Attribute'>SoftLayer_Resource_Group_Attribute[] </a>**

-----
[hardwareMembers]: #hardwaremembers
#### [hardwareMembers]
A resource group's associated hardware members.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**

-----
[members]: #members
#### [members]
A resource group's associated members.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**

-----
[rootResourceGroup]: #rootresourcegroup
#### [rootResourceGroup]
A resource group's associated root resource group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group </a>**

-----
[subnetMembers]: #subnetmembers
#### [subnetMembers]
A resource group's associated subnet members.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**

-----
[template]: #template
#### [template]
A resource group's associated template.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Template'>SoftLayer_Resource_Group_Template </a>**

-----
[vlanMembers]: #vlanmembers
#### [vlanMembers]
A resource group's associated VLAN members.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**


## Count

-----
[ancestorGroupCount]: #ancestorgroupcount
#### [ancestorGroupCount]
A count of a resource group's associated group ancestors.   
<span class="type-label">Type: </span>**unsigned long**


-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of a resource group's associated attributes.   
<span class="type-label">Type: </span>**unsigned long**


-----
[hardwareMemberCount]: #hardwaremembercount
#### [hardwareMemberCount]
A count of a resource group's associated hardware members.   
<span class="type-label">Type: </span>**unsigned long**


-----
[memberCount]: #membercount
#### [memberCount]
A count of a resource group's associated members.   
<span class="type-label">Type: </span>**unsigned long**


-----
[subnetMemberCount]: #subnetmembercount
#### [subnetMemberCount]
A count of a resource group's associated subnet members.   
<span class="type-label">Type: </span>**unsigned long**


-----
[vlanMemberCount]: #vlanmembercount
#### [vlanMemberCount]
A count of a resource group's associated VLAN members.   
<span class="type-label">Type: </span>**unsigned long**

</div>


