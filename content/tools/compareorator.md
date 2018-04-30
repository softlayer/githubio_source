---
title: "IBM Cloud for AWS professionals"
description: "This article will hopefully help anyone coming from the AWS ecosystem translate their workloads into IBM Cloud. "
date: "2017-07-17"
tags:
    - "tools"
---


## IBM Cloud for AWS professionals
This article will hopefully help anyone coming from the AWS ecosystem translate their workloads into IBM Cloud. 
 
## Basic Concepts
[IBM Cloud](https://console.ng.bluemix.net/docs/overview/whatisbluemix.html#bluemixoverview) has three main silos. [Infrastructure](https://console.ng.bluemix.net/catalog/?category=infrastructure) , [Applications](https://console.ng.bluemix.net/catalog/?category=applications) , and [Services](https://console.ng.bluemix.net/catalog/?category=services). 

_Infrastructure_ is built on [SoftLayer](htts://www.softlayer.com) and is available in over 30 [SoftLayer Datacenters](http://www.softlayer.com/data-centers) across the world. All of which are interconnect with our unmetered [private network](http://www.softlayer.com/network).

_Applications_ can be either [Cloud Foundry](https://www.ibm.com/cloud-computing/bluemix/runtimes), [Docker](https://console.ng.bluemix.net/docs/containers/container_index.html), or [Open Whisk](https://console.ng.bluemix.net/openwhisk/)

[_Services_](https://console.ng.bluemix.net/catalog/?category=services) contain a huge catalog of pay as you go addons to your application, such as Watson, Databases and Analytics to name a few.


## [Network](http://www.softlayer.com/network)
On IBM Cloud Infrastructure (SoftLayer) you are only charged for bandwidth that leaves your account. Incoming traffic, and everything on the private network is unmetered, allowing you to take full advantage of our worldwide private network for shipping data between locations. For more information on bandwidth costs see our [pricing page](http://www.softlayer.com/info/pricing).

See [Deconstructing SoftLayer's Three Tiered Network](http://blog.softlayer.com/2013/deconstructing-softlayers-three-tiered-network) for some more information on how it all works.

## [Bare Metal](http://www.softlayer.com/bare-metal-servers)
Standard-configuration servers available within 20-30 minutes, and fully customizable servers available within 4 hours. [Power8 servers](http://www.softlayer.com/power-servers) are available as well, built on IBM OpenPOWER architecture. [GPU](http://www.softlayer.com/GPU%20) cards and [SAP certified servers](https://www.ibm.com/cloud-computing/bluemix/sap-bare-metal-servers) are also available

## [Watson](https://www.ibm.com/cloud-computing/bluemix/watson)
With Watson on IBM Cloud, you have access to the widest range of cognitive technologies available today to quickly and securely build smart applications. From analyzing images and video to understanding sentiment, keywords and entities from text, our Watson services enable cognitive within your applications.

## API
Everything in IBM Cloud can be managed with an API, for infrastructure this is done through the [SoftLayer API](http://sldn.softlayer.com/) and IBM Cloud Apps and Services can be managed through the [IBM Cloud CLI](https://console.ng.bluemix.net/docs/cli/reference/cfcommands/index.html) which is an implementation of the [Cloud Foundry API](https://apidocs.cloudfoundry.org/247/)

## [Pricing](https://www.ibm.com/cloud-computing/bluemix/pricing)
Most IBM Cloud services have a very aggressive free trail / tier to get you started, and transparent pricing plans for when you need to scale up. More information on [IBM Cloud Pricing](https://console.ng.bluemix.net/docs/pricing/index.html#pricing) and [SoftLayer Pricing Calculator](http://www.softlayer.com/tco/)

------------

What follows is a rough comparison between IBM Cloud, AWS and Azure. Not all of these services will line up 1:1, but most of them are fairly close. Of course, if you have questions about anything in here, please [Contact Us](https://www.ibm.com/cloud-computing/bluemix/contact-us)

## Infrastructure
### Compute

IBM Cloud | AWS | Azure 
 ------ | ----- | ----- 
 [Virtual Server](https://console.ng.bluemix.net/catalog/infrastructure/virtual-server-hourly/) | EC2   |  Virtual Machines   
 [Dedicated Virtual Serviers](https://www.ibm.com/cloud-computing/bluemix/virtual-servers) | Dedicated EC2 | N/A
 [Bare Metal Server](https://console.ng.bluemix.net/catalog/infrastructure/bare-metal-server-monthly/) |  N/A | N/A 
 [nVidia GPU](http://www.softlayer.com/gpu) | EC2 Elastic GPUs | N/A
 [Vmware Solution](https://www.ibm.com/cloud-computing/solutions/ibm-vmware/console/) | VMware on AWS Cloud| N/A 
 [SAP HANA](https://www.ibm.com/cloud-computing/bluemix/sap-bare-metal-servers) | SAP HANA | SAP HANA
 [Hardware Security Module](https://www.ibm.com/cloud-computing/bluemix/hardware-security-module) | Cloud HSM | Azure Key Vault
 [Intel TXT](https://www.ibm.com/cloud-computing/bluemix/intel-txt) | N/A | N/A
 [IBM CloudPrivate Cloud](https://www.ibm.com/cloud-computing/bluemix/bluemix-private-cloud) | N/A | N/A



### Storage
IBM Cloud | AWS | Azure 
 ------ | --- | ----- 
 [Block Storage](https://console.ng.bluemix.net/catalog/infrastructure/block-storage---performance/) | Elastic Block Storage|  Page Blog Premium Storage 
 [File Storage](https://console.ng.bluemix.net/catalog/infrastructure/file-storage---performance/) | Elastic File System | File Storage  
 [Content Delivery Network](https://console.ng.bluemix.net/catalog/infrastructure/content-delivery-network/) | CloudFront | Content Delivery Network  
 [IBM Cloud Object Storage](https://console.ng.bluemix.net/catalog/infrastructure/ibm-cloud-object-storage--s3-api-open-trial/) | S3 | Blob Storage  
 [Mass Storage Servers](https://www.ibm.com/cloud-computing/bluemix/mass-storage-servers) | N/A | N/A
 [Quantastor](https://www.ibm.com/cloud-computing/bluemix/quantastor) | N/A | N/A

### Backup
IBM Cloud| AWS | Azure 
------ | --- | -----   
 [Veeam](https://www.ibm.com/cloud-computing/bluemix/veeam) | N/A | N/A
 [Evault](https://knowledgelayer.softlayer.com/topic/evault-backup) | Backup and Recovery | Cloud Backup
 [r1soft](https://knowledgelayer.softlayer.com/topic/r1soft-cdp) | N/A | N/A

### Network
IBM Cloud| AWS | Azure 
------ | --- | -----   
[Local Load Balancing](https://console.ng.bluemix.net/catalog/infrastructure/local-load-balancing/) | Elastic Load Balancing | Load balancer Application Gateway 
[Dedicated Netscaler VPX/MPX](https://console.ng.bluemix.net/catalog/infrastructure/citrix-netscaler-vpx-dedicated-load-balancer/)| N/A | N/A 
[DNS](https://console.ng.bluemix.net/catalog/infrastructure/domain-name-service/) | Route 53 | DNS (preview) traffic manager 
[Direct Link](https://console.ng.bluemix.net/catalog/infrastructure/direct-link-cloud-exchange/) | Direct Connect | Express Route  
[Vyatta Gateway Appliance](https://console.ng.bluemix.net/catalog/infrastructure/vyatta-gateway-appliance/) | N/A | N/A  
[Private Network ](https://console.ng.bluemix.net/catalog/infrastructure/vlan-spanning/)| Virtual Private Cloud | Virtual Network  

### Network Security  

IBM Cloud| AWS | Azure  
 ------ | --- | -----   
 [Fortigate Security Appliance](https://console.ng.bluemix.net/catalog/infrastructure/fortigate-security-appliance/) | N/A  | N/A 
 [Dedicated Hardware Firewall](https://console.ng.bluemix.net/catalog/infrastructure/hardware-firewall-dedicated/) | N/A  | N/A 
 [Hardware Firewall](https://console.ng.bluemix.net/catalog/infrastructure/fortigate-security-appliance/) | Security Groups  | Network Security Groups 
 [SSL Certificates](https://console.ng.bluemix.net/catalog/infrastructure/ssl-certificates/) | N/A | N/A  

## Applications

IBM Cloud| AWS | Azure 
 ------ | --- | ----- 
 [Cloud Foundry](https://console.ng.bluemix.net/catalog/?category=runtimes)| Elastic Beanstalk | Web Apps Cloud Services
 [Kubernetes](https://console.ng.bluemix.net/docs/containers/container_index.html) | EC2 Container Service/ Blox  | Container Service 
 [OpenWhisk ](https://console.ng.bluemix.net/openwhisk/)| Lambda | Functions Web Jobs Logic Apps 

### Mobile
IBM Cloud| AWS | Azure  
 ------ | --- | ----- 
 [Mobile Foundation](https://console.ng.bluemix.net/catalog/services/mobile-foundation/) | Mobile Hub | Mobile Apps 
 [Mobile Analytics](https://console.ng.bluemix.net/catalog/services/mobile-analytics/) |Mobile Analytics | Mobile Engagement
 [Push Notifications](https://console.ng.bluemix.net/catalog/services/push-notifications/) | Simple Notification Service  | Notification Hubs 
 [App ID](https://console.bluemix.net/catalog/services/app-id) | IAM | Azure Active Directory

## Services

### Data and Analytics
IBM Cloud| AWS | Azure 
 ------ | --- | -----
 [Apache Spark ](https://console.ng.bluemix.net/catalog/services/apache-spark/)| N/A | N/A |
 [BigInsights for Hadoop](https://console.ng.bluemix.net/catalog/services/biginsights-for-apache-hadoop/) | N/A |N/A 
 [Cloudant NoSQL ](https://console.ng.bluemix.net/catalog/services/cloudant-nosql-db/) | DynamoDB | DocumentDB 
 [Compose Enterprise](https://console.bluemix.net/catalog/services/compose-enterprise) | N/A | N/A 
 [Compose Elasticsearch ](https://console.ng.bluemix.net/catalog/services/compose-for-elasticsearch/) | Elasticsearch Service | Search 
 [Compose etcd](https://console.ng.bluemix.net/catalog/services/compose-for-etcd/) | N/A | N/A 
 [Compose MongoDB](https://console.ng.bluemix.net/catalog/services/compose-for-mongodb/) |  DynamoDB | DocumentDB 
 [Compose MySQL](https://console.bluemix.net/catalog/services/compose-for-mysql) | Amazon RDS | Azure Database for MySQL
 [Compose PostgreSQL](https://console.ng.bluemix.net/catalog/services/compose-for-postgresql/) | RDS | SQL Database
 [Compose RabbitMQ ](https://console.ng.bluemix.net/catalog/services/compose-for-rabbitmq/) | Simple Queue Service | Queue Storage 
 [Compose Redis](https://console.ng.bluemix.net/catalog/services/compose-for-redis/) | ElastiCache |Azure Redis Cache 
 [Compose RethinkDB](https://console.ng.bluemix.net/catalog/services/compose-for-rethinkdb/) |  N/A | N/A 
 [Compose ScyllaDB](https://console.bluemix.net/catalog/services/compose-for-scylladb) | N/A | N/A
 [dashDB](https://console.ng.bluemix.net/catalog/services/dashdb/) | Redshift | SQL Data Warehouse (Preview) 
 [dashDB for Transactions](https://console.ng.bluemix.net/catalog/services/dashdb-for-transactions-sql-database/) |Redshift | SQL Data Warehouse (Preview) 
 [Data connect](https://console.ng.bluemix.net/catalog/services/data-connect/) |N/A | N/A 
 [Data Science Experience](https://console.bluemix.net/catalog/services/data-science-experience) | N/A | N/A
 [Decision Optimization](https://console.ng.bluemix.net/catalog/services/decision-optimization/) | N/A | N/A 
 [Geospatial Analytics](https://console.ng.bluemix.net/catalog/services/geospatial-analytics/)  | Earth on AWS | N/A 
 [IBM DB2 CLOUD](https://console.ng.bluemix.net/catalog/services/ibm-db2-on-cloud/) |N/A | N/A 
 [IBM Graph](https://console.ng.bluemix.net/catalog/services/ibm-graph/) | N/A | N/A 
 [IBM Master Data Management](https://console.ng.bluemix.net/catalog/services/ibm-master-data-management-on-cloud/) | N/A | N/A 
 [IBM Watson Machine Learning](https://console.ng.bluemix.net/catalog/services/ibm-master-data-management-on-cloud/) |  Machine Learning | Machine Learning
 [Information Server](https://console.ng.bluemix.net/catalog/services/information-server-on-cloud/) | N/A | N/A 
 [Informix](https://console.ng.bluemix.net/catalog/services/informix-on-cloud/) | N/A | N/A 
 [Lift](https://console.ng.bluemix.net/catalog/services/lift/) | Data Pipeline | Data Factory 
 [Master Data Management](https://console.bluemix.net/catalog/services/master-data-management-on-cloud) | N/A | N/A
 [Streaming Analyics ](https://console.ng.bluemix.net/catalog/services/streaming-analytics/) |  Kinesis Analytics (Preview) | Data Lake Analytics (Preview) 
 [Weather Company Data](https://console.ng.bluemix.net/catalog/services/weather-company-data/) | N/A | N/A 
 [API Connect](https://console.ng.bluemix.net/catalog/services/api-connect/) |API Gateway | API Management

### Watson
IBM Cloud| AWS | Azure 
 ------ | --- | ----- 
 [Conversation](https://console.ng.bluemix.net/catalog/services/conversation/)  | Lex | Bing Speech API
 [Discovery](https://console.bluemix.net/catalog/services/discovery) | N/A | Bing Autosuggest API
 [Document Conversion](https://console.ng.bluemix.net/catalog/services/document-conversion/) | N/A | N/A 
 [Language Translator](https://console.ng.bluemix.net/catalog/services/language-translator/) | Polly | Translator API
 [Natural Language Classifier](https://console.ng.bluemix.net/catalog/services/natural-language-classifier/)  | Polly | Speech Recognition API
 [Personality Insights ](https://console.ng.bluemix.net/catalog/services/personality-insights/) | N/A | N/A 
 [Retrieve and Rank](https://console.ng.bluemix.net/catalog/services/retrieve-and-rank/)  | N/A | N/A 
 [Speech to Text](https://console.ng.bluemix.net/catalog/services/speech-to-text/) | Polly | Bing Speech API
 [Text to Speech](https://console.ng.bluemix.net/catalog/services/text-to-speech/) | Polly | Bing Speech API
 [Tone Analyzer](https://console.ng.bluemix.net/catalog/services/tone-analyzer/)  | Polly | Linguistic Analysis API
 [Visual Recognition](https://console.ng.bluemix.net/catalog/services/visual-recognition/) | Rekognition | Computer Vision API

### Internet of Things (IoT)
IBM Cloud| AWS | Azure
 ------ | --- | ----- 
 [IoT Platform ](https://console.ng.bluemix.net/catalog/services/internet-of-things-platform/) | IoT (Preview)/ Kinesis Firehose | IoT Hub / Event Hubs 
 [Context Mapping](https://console.ng.bluemix.net/catalog/services/context-mapping/) | N/A | N/A 
 [Driver Behavior](https://console.ng.bluemix.net/catalog/services/driver-behavior/) | N/A | N/A 
 [IoT for Electronics](https://console.ng.bluemix.net/catalog/services/iot-for-electronics/) | N/A | N/A 
 [IoT for Insurance](https://console.ng.bluemix.net/catalog/services/iot-for-insurance/) | N/A | N/A 

### Application Security
IBM Cloud| AWS | Azure 
 ------ | --- | ----- 
 [Activity Tracker](https://console.bluemix.net/catalog/services/activity-tracker) | N/A | N/A 
 [App ID](https://console.bluemix.net/catalog/services/app-id) | Identity and Access Management  | Azure AD/Role-based access control 
 [Application security](https://console.ng.bluemix.net/catalog/services/application-security-on-cloud/) | Inspector (Preview) | Security Center (Preview) 
 [Key Protect ](https://console.ng.bluemix.net/catalog/services/key-protect/) |Key Management Service | Key Vault 
 [Single Sign On](https://console.ng.bluemix.net/catalog/services/single-sign-on/) | Directory Service | Azure Active Directory  

### DevOps
IBM Cloud| AWS | Azure  
 ------ | --- | ----- 
 [Auto-Scaling](https://console.ng.bluemix.net/catalog/services/auto-scaling/) | Autoscaling | Autoscaling 
 [Availability Monitoring](https://console.ng.bluemix.net/catalog/services/availability-monitoring/) | CloudWatch / CloudTrail | Log Analytics Application Insights 
 [Continuous Delivery](https://console.ng.bluemix.net/catalog/services/continuous-delivery/) | AWS CodeDeploy / OpsWorks CloudFormation< |Resource Manager Automation 
 [Continous Release](https://console.bluemix.net/catalog/services/continuous-release) | AWS Config | N/A 
 [DevOps Insights](https://console.bluemix.net/catalog/services/devops-insights?env_id=ibm:yp:us-south) | N/A | N/A
 [Globalization Pipeline](https://console.ng.bluemix.net/catalog/services/globalization-pipeline/) | N/A | N/A 
 [IBM Alert Notification](https://console.ng.bluemix.net/catalog/services/ibm-alert-notification/) | N/A | N/A 
 [Monitoring and Analytics](https://console.ng.bluemix.net/catalog/services/monitoring-and-analytics/) | CloudWatch / CloudTrail | Log Analytics Application Insights 

### Application Services
IBM Cloud| AWS | Azure  
 ------ | --- | -----  
 [Blockchain](https://console.ng.bluemix.net/catalog/services/blockchain/) | N/A | Blockchain as a Service
 [Business Rules](https://console.ng.bluemix.net/catalog/services/business-rules/) | N/A | N/A 
 [Cloud Automation Manager](https://console.bluemix.net/catalog/services/cloud-automation-manager) | N/A | N/A
 [Message Hub](https://console.ng.bluemix.net/catalog/services/message-hub/) | Simple Queue Service| Queue Storage 
 [WebSphere Application Server](https://console.ng.bluemix.net/catalog/services/websphere-application-server/) | N/A | N/A 
 [Workload Scheduler](https://console.ng.bluemix.net/catalog/services/workload-scheduler/) | N/A | N/A 




## Helpful Links
+ https://ibm-bluemix.github.io/
+ https://softlayer.github.io/
+ https://console.ng.bluemix.net/catalog/
+ https://mycatalog.mybluemix.net/
+ https://github.com/softlayer/
+ https://github.com/IBM-Bluemix/
+ https://www.ibm.com/cloud-computing/bluemix/


