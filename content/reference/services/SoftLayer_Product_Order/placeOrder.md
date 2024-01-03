---
title: "placeOrder"
description: "
Use this method to place bare metal server, virtual server and additional service orders with SoftLayer. 
Upon success, your credit card or PayPal account will incur charges for the monthly order total 
(or prorated value if ordered mid billing cycle). If all products on the order are only billed hourly, 
you will be charged on your billing anniversary date, which occurs monthly on the day you ordered your first 
service with SoftLayer. For new customers, you are required to provide billing information when you place an order. 
For existing customers, the credit card on file will be charged. If you're a PayPal customer, a URL will be 
returned from the call to [SoftLayer_Product_Order::placeOrder](/reference/services/SoftLayer_Product_Order/placeOrder) which is to be used to finish the authorization 
process. This authorization tells PayPal that you indeed want to place an order with SoftLayer. 
From PayPal's web site, you will be redirected back to SoftLayer for your order receipt. 


When an order is placed, your order will be in a 'pending approval' state. When all internal checks pass, 
your order will be automatically approved. For orders that may need extra attention, a Sales representative 
will review the order and contact you if necessary. Once the order is approved, your server or service will 
be provisioned and available to you shortly thereafter. Depending on the type of server or service ordered, 
provisioning times will vary. 


## Order Containers



When placing API orders, it's important to order your server and services on the appropriate 
[SoftLayer_Container_Product_Order](/reference/datatypes/SoftLayer_Container_Product_Order). Failing to provide the correct container may delay your server or service 
from being provisioned in a timely manner. Some common order containers are included below. 


**Note:** `SoftLayer_Container_Product_Order_` has been removed from the containers in the table below for readability.


| Product | Order Container | Package Type |
| ------- | --------------- | ------------ |
| Bare metal server by CPU | [SoftLayer_Container_Product_Order_Hardware_Server](/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server) | BARE_METAL_CPU |
| Bare metal server by core | [SoftLayer_Container_Product_Order_Hardware_Server](/reference/datatypes/SoftLayer_Container_Product_Order_Hardware_Server) | BARE_METAL_CORE |
| Virtual server | [SoftLayer_Container_Product_Order_Virtual_Guest](/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Guest) | VIRTUAL_SERVER_INSTANCE |
| DNS domain registration | [SoftLayer_Container_Product_Order_Dns_Domain_Registrationn](/reference/datatypes/SoftLayer_Container_Product_Order_Dns_Domain_Registrationn) | ADDITIONAL_SERVICES |
| Local & dedicated load balancers | [SoftLayer_Container_Product_Order_Network_LoadBalancer](/reference/datatypes/SoftLayer_Container_Product_Order_Network_LoadBalancer) | ADDITIONAL_SERVICES_LOAD_BALANCER |
| Content delivery network | [SoftLayer_Container_Product_Order_Network_ContentDelivery_Account](/reference/datatypes/SoftLayer_Container_Product_Order_Network_ContentDelivery_Account) | ADDITIONAL_SERVICES_CDN |
| Content delivery network Addon | [SoftLayer_Container_Product_Order_Network_ContentDelivery_Account_Addon](/reference/datatypes/SoftLayer_Container_Product_Order_Network_ContentDelivery_Account_Addon) | ADDITIONAL_SERVICES_CDN_ADDON |
| Hardware & software firewalls | [SoftLayer_Container_Product_Order_Network_Protection_Firewall](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall) | ADDITIONAL_SERVICES_FIREWALL |
| Dedicated firewall | [SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Protection_Firewall_Dedicated) | ADDITIONAL_SERVICES_FIREWALL |
| Object storage | [SoftLayer_Container_Product_Order_Network_Storage_Object](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Object) | ADDITIONAL_SERVICES_OBJECT_STORAGE |
| Object storage (hub) | [SoftLayer_Container_Product_Order_Network_Storage_Hub](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Hub) | ADDITIONAL_SERVICES_OBJECT_STORAGE |
| Network attached storage | [SoftLayer_Container_Product_Order_Network_Storage_Nas](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Nas) | ADDITIONAL_SERVICES_NETWORK_ATTACHED_STORAGE |
| Iscsi storage | [SoftLayer_Container_Product_Order_Network_Storage_Iscsi](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Iscsi) | ADDITIONAL_SERVICES_ISCSI_STORAGE |
| Evault | [SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Vault) | ADDITIONAL_SERVICES |
| Evault Plugin | [SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Plugin](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Storage_Backup_Evault_Plugin) | ADDITIONAL_SERVICES |
| Application delivery appliance | [SoftLayer_Container_Product_Order_Network_Application_Delivery_Controller](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Application_Delivery_Controller) | ADDITIONAL_SERVICES_APPLICATION_DELIVERY_APPLIANCE |
| Network subnet | [SoftLayer_Container_Product_Order_Network_Subnet](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet) | ADDITIONAL_SERVICES |
| Global IPv4 | [SoftLayer_Container_Product_Order_Network_Subnet](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet) | ADDITIONAL_SERVICES_GLOBAL_IP_ADDRESSES |
| Global IPv6 | [SoftLayer_Container_Product_Order_Network_Subnet](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Subnet) | ADDITIONAL_SERVICES_GLOBAL_IP_ADDRESSES |
| Network VLAN | [SoftLayer_Container_Product_Order_Network_Vlan](/reference/datatypes/SoftLayer_Container_Product_Order_Network_Vlan) | ADDITIONAL_SERVICES_NETWORK_VLAN |
| Portable storage | [SoftLayer_Container_Product_Order_Virtual_Disk_Image](/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_Disk_Image) | ADDITIONAL_SERVICES_PORTABLE_STORAGE |
| SSL certificate | [SoftLayer_Container_Product_Order_Security_Certificate](/reference/datatypes/SoftLayer_Container_Product_Order_Security_Certificate) | ADDITIONAL_SERVICES_SSL_CERTIFICATE |
| External authentication | [SoftLayer_Container_Product_Order_User_Customer_External_Binding](/reference/datatypes/SoftLayer_Container_Product_Order_User_Customer_External_Binding) | ADDITIONAL_SERVICES |
| Dedicated Host | [SoftLayer_Container_Product_Order_Virtual_DedicatedHost](/reference/datatypes/SoftLayer_Container_Product_Order_Virtual_DedicatedHost) | DEDICATED_HOST |


## Server example



This example includes a single bare metal server being ordered with monthly billing. 


**Warning:** the price ids provided below may be outdated or unavailable, so you will need to determine the

available prices from the bare metal server [SoftLayer_Product_Package::getAllObjects](/reference/services/SoftLayer_Product_Package/getAllObjects), which have a 
[SoftLayer_Product_Package_Type](/reference/datatypes/SoftLayer_Product_Package_Type) of `BARE_METAL_CPU` or `BARE_METAL_CORE`. You can get a full list of 
package types with [SoftLayer_Product_Package_Type::getAllObjects](/reference/services/SoftLayer_Product_Package_Type/getAllObjects). 


### Bare Metal Ordering

```xml 
<SOAP-ENV:Envelope xmlns:SOAP-ENV='http://schemas.xmlsoap.org/soap/envelope/' xmlns:ns1='http://api.service.softlayer.com/soap/v3/' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:SOAP-ENC='http://schemas.xmlsoap.org/soap/encoding/' SOAP-ENV:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/'> 
  <SOAP-ENV:Header> 
    <ns1:authenticate> 
      <username>your username</username> 
      <apiKey>your api key</apiKey> 
    </ns1:authenticate> 
  </SOAP-ENV:Header> 
  <SOAP-ENV:Body> 
    <ns1:placeOrder> 
      <orderData xsi:type='ns1:SoftLayer_Container_Product_Order_Hardware_Server'> 
        <hardware SOAP-ENC:arrayType='ns1:SoftLayer_Hardware[1]' xsi:type='ns1:SoftLayer_HardwareArray'> 
          <item xsi:type='ns1:SoftLayer_Hardware'> 
            <domain xsi:type='xsd:string'>example.com</domain> 
            <hostname xsi:type='xsd:string'>server1</hostname> 
          </item> 
        </hardware> 
        <location xsi:type='xsd:string'>138124</location> 
        <packageId xsi:type='xsd:int'>142</packageId> 
        <prices SOAP-ENC:arrayType='ns1:SoftLayer_Product_Item_Price[14]' xsi:type='ns1:SoftLayer_Product_Item_PriceArray'> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>58</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>22337</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>21189</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>876</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>57</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>55</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>21190</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>36381</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>21</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>22013</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>906</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>420</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>418</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>342</id> 
          </item> 
        </prices> 
        <useHourlyPricing xsi:type='xsd:boolean'>false</useHourlyPricing> 
      </orderData> 
      <saveAsQuote xsi:nil='true' /> 
    </ns1:placeOrder> 
  </SOAP-ENV:Body> 
</SOAP-ENV:Envelope> 
``` 


## Virtual server example



This example includes 2 identical virtual servers (except for hostname) being ordered for hourly billing. 
It includes an optional image template id and VLAN data specified on the virtualGuest objects - 
`primaryBackendNetworkComponent` and `primaryNetworkComponent`. 


**Warning:** the price ids provided below may be outdated or unavailable, so you will need to determine the

available prices from the virtual server package with [SoftLayer_Product_Package::getAllObjects](/reference/services/SoftLayer_Product_Package/getAllObjects), 
which has a [SoftLayer_Product_Package_Type](/reference/datatypes/SoftLayer_Product_Package_Type) of `VIRTUAL_SERVER_INSTANCE`. 


#### Virtual Ordering

```xml 
<SOAP-ENV:Envelope xmlns:SOAP-ENV='http://schemas.xmlsoap.org/soap/envelope/' xmlns:ns1='http://api.service.softlayer.com/soap/v3/' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:SOAP-ENC='http://schemas.xmlsoap.org/soap/encoding/' SOAP-ENV:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/'> 
  <SOAP-ENV:Header> 
    <ns1:authenticate> 
      <username>your username</username> 
      <apiKey>your api key</apiKey> 
    </ns1:authenticate> 
  </SOAP-ENV:Header> 
  <SOAP-ENV:Body> 
    <ns1:placeOrder> 
      <orderData xsi:type='ns1:SoftLayer_Container_Product_Order_Virtual_Guest'> 
        <imageTemplateId xsi:type='xsd:int'>13251</imageTemplateId> 
        <location xsi:type='xsd:string'>37473</location> 
        <packageId xsi:type='xsd:int'>46</packageId> 
        <prices SOAP-ENC:arrayType='ns1:SoftLayer_Product_Item_Price[13]' xsi:type='ns1:SoftLayer_Product_Item_PriceArray'> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>2159</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>55</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>13754</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>1641</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>905</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>1800</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>58</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>21</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>1645</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>272</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>57</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>418</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>420</id> 
          </item> 
        </prices> 
        <quantity xsi:type='xsd:int'>2</quantity> 
        <useHourlyPricing xsi:type='xsd:boolean'>true</useHourlyPricing> 
        <virtualGuests SOAP-ENC:arrayType='ns1:SoftLayer_Virtual_Guest[1]' xsi:type='ns1:SoftLayer_Virtual_GuestArray'> 
          <item xsi:type='ns1:SoftLayer_Virtual_Guest'> 
            <domain xsi:type='xsd:string'>example.com</domain> 
            <hostname xsi:type='xsd:string'>server1</hostname> 
            <primaryBackendNetworkComponent xsi:type='ns1:SoftLayer_Virtual_Guest_Network_Component'> 
              <networkVlan xsi:type='ns1:SoftLayer_Network_Vlan'> 
                <id xsi:type='xsd:int'>12345</id> 
              </networkVlan> 
            </primaryBackendNetworkComponent> 
            <primaryNetworkComponent xsi:type='ns1:SoftLayer_Virtual_Guest_Network_Component'> 
              <networkVlan xsi:type='ns1:SoftLayer_Network_Vlan'> 
                <id xsi:type='xsd:int'>67890</id> 
              </networkVlan> 
            </primaryNetworkComponent> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Virtual_Guest'> 
            <domain xsi:type='xsd:string'>example.com</domain> 
            <hostname xsi:type='xsd:string'>server2</hostname> 
            <primaryBackendNetworkComponent xsi:type='ns1:SoftLayer_Virtual_Guest_Network_Component'> 
              <networkVlan xsi:type='ns1:SoftLayer_Network_Vlan'> 
                <id xsi:type='xsd:int'>12345</id> 
              </networkVlan> 
            </primaryBackendNetworkComponent> 
            <primaryNetworkComponent xsi:type='ns1:SoftLayer_Virtual_Guest_Network_Component'> 
              <networkVlan xsi:type='ns1:SoftLayer_Network_Vlan'> 
                <id xsi:type='xsd:int'>67890</id> 
              </networkVlan> 
            </primaryNetworkComponent> 
          </item> 
        </virtualGuests> 
      </orderData> 
      <saveAsQuote xsi:nil='true' /> 
    </ns1:placeOrder> 
  </SOAP-ENV:Body> 
</SOAP-ENV:Envelope> 
``` 


## VLAN example


**Warning:** the price ids provided below may be outdated or unavailable, so you will need to determine the

available prices from the additional services pacakge with [SoftLayer_Product_Package::getAllObjects](/reference/services/SoftLayer_Product_Package/getAllObjects), 
which has a [SoftLayer_Product_Package_Type](/reference/datatypes/SoftLayer_Product_Package_Type) of `ADDITIONAL_SERVICES`. 
You can get a full list of [SoftLayer_Product_Package_Type::getAllObjects](/reference/services/SoftLayer_Product_Package_Type/getAllObjects) to find other available additional 
service packages.<br/><br/> 


### VLAN Ordering

```xml 
<SOAP-ENV:Envelope xmlns:SOAP-ENV='http://schemas.xmlsoap.org/soap/envelope/' xmlns:ns1='http://api.service.softlayer.com/soap/v3/' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:SOAP-ENC='http://schemas.xmlsoap.org/soap/encoding/' SOAP-ENV:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/'> 
  <SOAP-ENV:Header> 
    <ns1:authenticate> 
      <username>your username</username> 
      <apiKey>your api key</apiKey> 
    </ns1:authenticate> 
  </SOAP-ENV:Header> 
  <SOAP-ENV:Body> 
    <ns1:placeOrder> 
      <orderData xsi:type='ns1:SoftLayer_Container_Product_Order_Network_Vlan'> 
        <location xsi:type='xsd:string'>154820</location> 
        <packageId xsi:type='xsd:int'>0</packageId> 
        <prices SOAP-ENC:arrayType='ns1:SoftLayer_Product_Item_Price[2]' xsi:type='ns1:SoftLayer_Product_Item_PriceArray'> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>2021</id> 
          </item> 
          <item xsi:type='ns1:SoftLayer_Product_Item_Price'> 
            <id xsi:type='xsd:int'>2018</id> 
          </item> 
        </prices> 
        <useHourlyPricing xsi:type='xsd:boolean'>true</useHourlyPricing> 
      </orderData> 
      <saveAsQuote xsi:nil='true' /> 
    </ns1:placeOrder> 
  </SOAP-ENV:Body> 
</SOAP-ENV:Envelope> 
``` 


## Multiple products example



This example includes a combination of the above examples in a single order. Note that all the configuration 
options for each individual order container are the same as above, except now we encapsulate each one within 
the `orderContainers` property on the base [SoftLayer_Container_Product_Order](/reference/datatypes/SoftLayer_Container_Product_Order). 


**Warning:** not all products are available to be ordered with other products. For example, since

SSL certificates require validation from a 3rd party, the approval process may take days or even weeks, 
and this would not be acceptable when you need your hourly virtual server right now. To better accommodate 
customers, we restrict several products to be ordered individually. 


### Bare metal server + virtual server + VLAN



```xml 
<SOAP-ENV:Envelope xmlns:SOAP-ENV='http://schemas.xmlsoap.org/soap/envelope/' xmlns:ns1='http://api.service.softlayer.com/soap/v3/' xmlns:xsd='http://www.w3.org/2001/XMLSchema' xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance' xmlns:SOAP-ENC='http://schemas.xmlsoap.org/soap/encoding/' SOAP-ENV:encodingStyle='http://schemas.xmlsoap.org/soap/encoding/'> 
  <SOAP-ENV:Header> 
    <ns1:authenticate> 
      <username>your username</username> 
      <apiKey>your api key</apiKey> 
    </ns1:authenticate> 
  </SOAP-ENV:Header> 
  <SOAP-ENV:Body> 
    <ns1:placeOrder> 
      <orderData xsi:type='ns1:SoftLayer_Container_Product_Order'> 
        <orderContainers SOAP-ENC:arrayType='ns1:SoftLayer_Container_Product_Order[3]' xsi:type='ns1:SoftLayer_Container_Product_OrderArray'> 
          <item xsi:type='ns1:SoftLayer_Container_Product_Order_Hardware_Server'> 
            ... 
          </item> 
          <item xsi:type='ns1:SoftLayer_Container_Product_Order_Virtual_Guest'> 
            ... 
          </item> 
          <item xsi:type='ns1:SoftLayer_Container_Product_Order_Network_Vlan'> 
            ... 
          </item> 
        </orderContainers> 
      </orderData> 
      <saveAsQuote xsi:nil='true' /> 
    </ns1:placeOrder> 
  </SOAP-ENV:Body> 
</SOAP-ENV:Envelope> 
``` 

"
date: "2018-02-12"
tags:
    - "method"
    - "sldn"
    - "Product"
classes:
    - "SoftLayer_Product_Order"
type: "reference"
layout: "method"
mainService : "SoftLayer_Product_Order"
---

# [REST Example](#placeOrder-example) <a href="/article/rest/"><i class="fas fa-question"></i></a> {#placeOrder-example .anchor-link} 
```bash
curl -g -u $SL_USER:$SL_APIKEY -X POST -d '{"parameters": [SoftLayer_Container_Product_Order, boolean]}' \
'https://api.softlayer.com/rest/v3.1/SoftLayer_Product_Order/placeOrder'
```
