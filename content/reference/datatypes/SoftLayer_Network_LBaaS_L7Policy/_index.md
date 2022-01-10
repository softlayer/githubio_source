---
title: "SoftLayer_Network_LBaaS_L7Policy"
description: "The SoftLayer_Network_LBaaS_L7Policy represents the policy for a listener."
layout: "datatype"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_LBaaS_L7Policy"
---

# SoftLayer_Network_LBaaS_L7Policy
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Network_LBaaS_L7Policy' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Policy' >Datatype</a></li>
    </ul>
</div>

## Description 


The SoftLayer_Network_LBaaS_L7Policy represents the policy for a listener. 





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
[action]: #action
#### [action]
The Action to take if the rules belonging to this policy match. It can be set to any of the following values: REDIRECT_URL, REDIRECT_POOL, REDIRECT_HTTPS, REJECT.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[createDate]: #createdate
#### [createDate]
Specifies when a L7 Policy was created.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[id]: #id
#### [id]
The unique identifier of a policy.  
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[modifyDate]: #modifydate
#### [modifyDate]
Specifies when a L7 Policy was updated previously.  
<span class="type-label">Type: </span>**dateTime**  



</div>
<div class="prop-row">

-----
[name]: #name
#### [name]
Name of a Policy.  
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[priority]: #priority
#### [priority]
The order in which the policy is evaluated. Each policy should have a unique priority   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[redirectL7PoolId]: #redirectl7poolid
#### [redirectL7PoolId]
The L7 pool id to which traffic is redirected   
<span class="type-label">Type: </span>**integer**  



</div>
<div class="prop-row">

-----
[redirectL7PoolUuid]: #redirectl7pooluuid
#### [redirectL7PoolUuid]
The UUID of the L7 pool object referenced by the policy when the policy action is set to REDIRECT_POOL   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[redirectUrl]: #redirecturl
#### [redirectUrl]
The URL to which traffic is redirected when the action is set to REDIRECT_URL. Or the port to which listener traffic is redirected to when the action is set to REDIRECT_HTTPS.   
<span class="type-label">Type: </span>**string**  



</div>
<div class="prop-row">

-----
[uuid]: #uuid
#### [uuid]
The UUID of a Policy.  
<span class="type-label">Type: </span>**string**  



</div>
</div>
<!-- LOCAL PROPERTY END -->

<div id="relationalProperties"  class="prop-content" >

## Relational
<div class="prop-row">

-----
[l7Rules]: #l7rules
#### [l7Rules]
  
<span class="type-label">Type: </span>**<a href='/reference/datatypes/SoftLayer_Network_LBaaS_L7Rule'>SoftLayer_Network_LBaaS_L7Rule[] </a>**  



</div>

## Count
<div class="prop-row">

-----
[l7RuleCount]: #l7rulecount
#### [l7RuleCount]
A count of    
<span class="type-label">Type: </span>**unsigned long**  



</div>
</div>


