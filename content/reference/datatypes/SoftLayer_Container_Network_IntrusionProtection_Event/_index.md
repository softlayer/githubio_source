---
title: "SoftLayer_Container_Network_IntrusionProtection_Event"
description: "The IntrusionProtection_Event object stores information about individual intrusion protection events. 

It is a data con... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Container"
classes:
    - "SoftLayer_Container_Network_IntrusionProtection_Event"
---

# SoftLayer_Container_Network_IntrusionProtection_Event
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Container_Network_IntrusionProtection_Event' >Datatype</a></li>
    </ul>
</div>

## Description 
The IntrusionProtection_Event object stores information about individual intrusion protection events. 

It is a data container that cannot be edited, deleted, or saved. 

It is returned by many methods in the TippingPointReporting object, but never directly, always as a child of another container object. 





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
[CVEId]: #cveid
#### [CVEId]
The CVE ID(s), if any, associated with this attack signature.  
<span class="type-label">Type: </span>**string**

-----
[actionTaken]: #actiontaken
#### [actionTaken]
The action that was taken when this attack was discovered.  Can be either "Block" or "Permit"  
<span class="type-label">Type: </span>**string**

-----
[attackCount]: #attackcount
#### [attackCount]
The number of attacks in this block.  Attacks are grouped differently based on the query performed on the tippingPointReporting object.  
<span class="type-label">Type: </span>**integer**

-----
[attackLongDescription]: #attacklongdescription
#### [attackLongDescription]
Long description of the attack.  May contain links to more information  
<span class="type-label">Type: </span>**string**

-----
[attackName]: #attackname
#### [attackName]
Name of the attack  
<span class="type-label">Type: </span>**string**

-----
[beginTime]: #begintime
#### [beginTime]
The starting timestamp of the attack recorded, in Y-m-d H:i:s format.  May not be set, depending on the type of query performed.  
<span class="type-label">Type: </span>**string**

-----
[bugtraqId]: #bugtraqid
#### [bugtraqId]
The BugTraq ID(s), if any, associated with this attack signature.  
<span class="type-label">Type: </span>**string**

-----
[classification]: #classification
#### [classification]
The human-readable classification of the attack  
<span class="type-label">Type: </span>**string**

-----
[destinationIpAddress]: #destinationipaddress
#### [destinationIpAddress]
The IP Address (as a dotted decimal string) of the machine that was the target of the attack  
<span class="type-label">Type: </span>**string**

-----
[destinationPort]: #destinationport
#### [destinationPort]
The port the attack was directed at  
<span class="type-label">Type: </span>**integer**

-----
[endTime]: #endtime
#### [endTime]
The ending timestamp of the attack recorded, in Y-m-d H:i:s format.  May not be set, depending on the type of query performed.  
<span class="type-label">Type: </span>**string**

-----
[platform]: #platform
#### [platform]
The platform affected by the attack  
<span class="type-label">Type: </span>**string**

-----
[protocol]: #protocol
#### [protocol]
The protocol used in the attack  
<span class="type-label">Type: </span>**string**

-----
[severity]: #severity
#### [severity]
The human-readable severity of this attack, from "Low" to "Critical"  
<span class="type-label">Type: </span>**string**

-----
[signatureId]: #signatureid
#### [signatureId]
Unique ID of the "Signature" in question.  The signature determines the type of attack recorded.  SignatureId is used in the drillDown() function on the TippingPointReporting service  
<span class="type-label">Type: </span>**string**

-----
[sourceIpAddress]: #sourceipaddress
#### [sourceIpAddress]
The IP Address (as a dotted decimal string) of the machine originating the attack  
<span class="type-label">Type: </span>**string**

-----
[sourcePort]: #sourceport
#### [sourcePort]
The port the attack originated from  
<span class="type-label">Type: </span>**integer**

</div>
<!-- LOCAL PROPERTY END -->

</div>


