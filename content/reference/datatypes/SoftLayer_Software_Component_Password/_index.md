---
title: "SoftLayer_Software_Component_Password"
description: "This SoftLayer_Software_Component_Password data type contains a password for a specific software component instance."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Software"
classes:
    - "SoftLayer_Software_Component_Password"
---

# SoftLayer_Software_Component_Password
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Software_Component_Password' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Software_Component_Password' >Datatype</a></li>
    </ul>
</div>

## Description 


This SoftLayer_Software_Component_Password data type contains a password for a specific software component instance. 



### seeAlso

* [SoftLayer_Software_Component](/reference/services/SoftLayer_Software_Component )


* [SoftLayer_Software_Password_History](/reference/datatypes/SoftLayer_Software_Password_History )




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
The date this username/password pair was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
An id number for this specific username/password pair.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
The date of the last modification to this username/password pair.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[notes]: #notes
#### [notes]
A note string stored for this username/password pair.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[password]: #password
#### [password]
The password part of the username/password pair.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[port]: #port
#### [port]
The application access port for the Software Component.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[softwareId]: #softwareid
#### [softwareId]
An id number for the software component this username/password pair is valid for.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[username]: #username
#### [username]
The username part of the username/password pair.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[software]: #software
#### [software]
The SoftLayer_Software_Component instance that this username/password pair is valid for.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Software_Component'>SoftLayer_Software_Component </a>**  



</div>
<div class="prop-row">

-----
[sshKeys]: #sshkeys
#### [sshKeys]
SSH keys to be installed on the server during provisioning or an OS reload.  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Security_Ssh_Key'>SoftLayer_Security_Ssh_Key[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[sshKeyCount]: #sshkeycount
#### [sshKeyCount]
A count of sSH keys to be installed on the server during provisioning or an OS reload.   
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


