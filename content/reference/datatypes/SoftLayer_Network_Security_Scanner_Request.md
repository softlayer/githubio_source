---
title: "SoftLayer_Network_Security_Scanner_Request"
description: "SoftLayer gives customers the ability to manage vulnerability scans for each of their servers.  This service provides the ability to create a new scan request, view the status of a current request, and finally view the report of a finished scan. 

A vulnerability scan attempts to find potential security problems on a server by first searching for open ports and the services that run on them.  If any services are found the scanner will then check for version and patch information of each service found.  Lastly, the scanner will use the information gathered to search its database of known vulnerabilities and generate a report. Reports typically take five to ten minutes to run but allow for up to thirty minutes in rare cases. 

A vulnerability report will typically include the following information: 
*Number of security holes and warnings.
*The hosts that were scanned.
*The port/service and the corresponding issue.
*Detailed information about the issue, risk factor, and possible fixes.


If you have a firewall, SoftLayer's administrative networks need to be allowed for the vulnerability scan to be effective.  If a firewall is blocking all ports, the report may not show any problems even if some exist.  In addition you may have some indication in your firewall logs of the scan taking place as ports on your system are investigated. "
date: "2018-02-12"
tags:
    - "datatype"
    - "sldn"
    - "Network"
classes:
    - "SoftLayer_Network_Security_Scanner_Request"
type: "reference"
layout: "datatype"
mainService : "SoftLayer_Network_Security_Scanner_Request"
---
