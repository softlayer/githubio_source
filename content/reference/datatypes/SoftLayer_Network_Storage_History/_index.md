---
title: "SoftLayer_Network_Storage_History"
description: "The SoftLayer_Network_Storage_History contains the username/password past history for Storage services except Evault. In... "
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Storage_History"
---

# SoftLayer_Network_Storage_History
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
        <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_Storage_History' >Datatype</a></li>
    </ul>
</div>

## Description 
The SoftLayer_Network_Storage_History contains the username/password past history for Storage services except Evault. Information such as the username, passwords, notes and the date of the password change may be retrieved. 





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
Date the password was changed.  
<span class="type-label">Type: </span>**dateTime**

-----
[notes]: #notes
#### [notes]
Past notes for the Storage service.  
<span class="type-label">Type: </span>**string**

-----
[password]: #password
#### [password]
Password for the Storage service that was used in the past.  
<span class="type-label">Type: </span>**string**

-----
[username]: #username
#### [username]
Username for the Storage service.  
<span class="type-label">Type: </span>**string**

</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
-----
[account]: #account
#### [account]
The account that the Storage services belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Account'>SoftLayer_Account </a>**

-----
[nasVolume]: #nasvolume
#### [nasVolume]
The Storage service that the password history belongs to.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_Storage'>SoftLayer_Network_Storage </a>**


## Count
</div>


