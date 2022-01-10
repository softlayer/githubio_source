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
[createDate]: #createdate
#### [createDate]
A resource group's creation date.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[description]: #description
#### [description]
A resource group's description.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
A resource group's ID.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[keyName]: #keyname
#### [keyName]
A resource group's keyname.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
A resource group's name.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[rootResourceGroupId]: #rootresourcegroupid
#### [rootResourceGroupId]
  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[templateId]: #templateid
#### [templateId]
A resource group's template ID.  
<span class="type-label">Type: </span>**integer**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[ancestorGroups]: #ancestorgroups
#### [ancestorGroups]
A resource group's associated group ancestors.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group[] </a>**  



</div>
<div class="prop-row">

-----
[attributes]: #attributes
#### [attributes]
A resource group's associated attributes.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Attribute'>SoftLayer_Resource_Group_Attribute[] </a>**  



</div>
<div class="prop-row">

-----
[hardwareMembers]: #hardwaremembers
#### [hardwareMembers]
A resource group's associated hardware members.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**  



</div>
<div class="prop-row">

-----
[members]: #members
#### [members]
A resource group's associated members.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**  



</div>
<div class="prop-row">

-----
[rootResourceGroup]: #rootresourcegroup
#### [rootResourceGroup]
A resource group's associated root resource group.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group'>SoftLayer_Resource_Group </a>**  



</div>
<div class="prop-row">

-----
[subnetMembers]: #subnetmembers
#### [subnetMembers]
A resource group's associated subnet members.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**  



</div>
<div class="prop-row">

-----
[template]: #template
#### [template]
A resource group's associated template.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Template'>SoftLayer_Resource_Group_Template </a>**  



</div>
<div class="prop-row">

-----
[vlanMembers]: #vlanmembers
#### [vlanMembers]
A resource group's associated VLAN members.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Resource_Group_Member'>SoftLayer_Resource_Group_Member[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[ancestorGroupCount]: #ancestorgroupcount
#### [ancestorGroupCount]
A count of a resource group's associated group ancestors.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[attributeCount]: #attributecount
#### [attributeCount]
A count of a resource group's associated attributes.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[hardwareMemberCount]: #hardwaremembercount
#### [hardwareMemberCount]
A count of a resource group's associated hardware members.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[memberCount]: #membercount
#### [memberCount]
A count of a resource group's associated members.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[subnetMemberCount]: #subnetmembercount
#### [subnetMemberCount]
A count of a resource group's associated subnet members.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
<div class="prop-row">

-----
[vlanMemberCount]: #vlanmembercount
#### [vlanMemberCount]
A count of a resource group's associated VLAN members.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


