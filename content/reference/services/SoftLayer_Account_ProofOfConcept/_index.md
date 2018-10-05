---
title: "SoftLayer_Account_ProofOfConcept"
description: "Approved IBM sales representatives can use this service to request and manage temporary access on behalf of clients. Thi... "
date: "2018-02-12"
layout: "service"
tags:
    - "service"
    - "sldn"
    - "Account"
classes:
    - "SoftLayer_Account_ProofOfConcept"
---
# SoftLayer_Account_ProofOfConcept
<div id='service-datatype'>
    <ul id='sldn-reference-tabs'>
    <li id='service'> <a href='/reference/services/SoftLayer_Account_ProofOfConcept' >Service</a></li>    <li id='datatype'> <a href='/reference/datatypes/SoftLayer_Account_ProofOfConcept' >Datatype</a></li>
    </ul>
</div>

## Description
Approved IBM sales representatives can use this service to request and manage temporary access on behalf of clients. This access is subject to multiple layers of approval and requires payment arrangement in advance. 

This service is unavailable to users outside of IBM and is not applicable to the majority of users. 



        
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
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/approveReview'> approveReview</a> </span>
            <div class='views-field-body'>Allows a reviewer to approve a request</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/denyReview'> denyReview</a> </span>
            <div class='views-field-body'>Allows reviewer to deny a request</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getAuthenticationUrl'> getAuthenticationUrl</a> </span>
            <div class='views-field-body'>Gets authentication URL</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getRequestsPendingIntegratedOfferingTeamReview'> getRequestsPendingIntegratedOfferingTeamReview</a> </span>
            <div class='views-field-body'>Retrieves a list of requests pending IOT review in the specified regions</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getRequestsPendingOverThresholdReview'> getRequestsPendingOverThresholdReview</a> </span>
            <div class='views-field-body'>Retrieves a list of requests pending over threshold review</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getReviewerAccessToken'> getReviewerAccessToken</a> </span>
            <div class='views-field-body'>Exchanges a token</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getReviewerEmailFromAccessToken'> getReviewerEmailFromAccessToken</a> </span>
            <div class='views-field-body'>Fetches an email address using a token</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getSubmittedRequest'> getSubmittedRequest</a> </span>
            <div class='views-field-body'>Retrieves full details of one PoC request submitted by an IBMer.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getSubmittedRequests'> getSubmittedRequests</a> </span>
            <div class='views-field-body'>Retrieves a summary of proof of concept requests submitted by an IBMer.</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getSupportEmailAddress'> getSupportEmailAddress</a> </span>
            <div class='views-field-body'>Gets email address users can use to ask for help/support</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getTotalRequestsPendingIntegratedOfferingTeamReview'> getTotalRequestsPendingIntegratedOfferingTeamReview</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/getTotalRequestsPendingOverThresholdReviewCount'> getTotalRequestsPendingOverThresholdReviewCount</a> </span>
            <div class='views-field-body'></div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/isCurrentReviewer'> isCurrentReviewer</a> </span>
            <div class='views-field-body'>Determines if the user is one of the reviewers currently able to act</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/isIntegratedOfferingTeamReviewer'> isIntegratedOfferingTeamReviewer</a> </span>
            <div class='views-field-body'>Retrieves Verifies a reviewer</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/isOverThresholdReviewer'> isOverThresholdReviewer</a> </span>
            <div class='views-field-body'>Verifies a reviewer</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/requestAccountTeamFundedAccount'> requestAccountTeamFundedAccount</a> </span>
            <div class='views-field-body'>Accepts new proof of concept requests</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/requestGlobalFundedAccount'> requestGlobalFundedAccount</a> </span>
            <div class='views-field-body'>Accepts new proof of concept requests</div>
        </div>
            <div class="method-row">
                        <span class='view-field-title'><a href='/reference/services/SoftLayer_Account_ProofOfConcept/verifyReviewer'> verifyReviewer</a> </span>
            <div class='views-field-body'>Validates a reviewer</div>
        </div>
        </div>
</div>

