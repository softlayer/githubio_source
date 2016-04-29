---
title: "Get Invoice for PowerShell"
description: "Retrieves the PDF and Excel current invoices with a powershell script"

date: "2016-04-25"
classes: ["SoftLayer_Billing_Invoice"]
tags:
  - "invoice"
  - "powershell"
---

This powershell script will get the filename for the PDF and Excel invoices and save them locally. Requires [PowerShell Version 4](http://social.technet.microsoft.com/wiki/contents/articles/21016.how-to-install-windows-powershell-4-0.aspx) for the Invoke-WebRequest and ConvertFrom-Json functions.

```ps1
# Start SL script
$MyScriptName = "_Call_SL_Rest"
$HomeDir = pwd
$date4file = get-date -uformat "%Y-%m-%d_%H%M%S"
$log = "$HomeDir\"+$date4file+$MyScriptName+".log"
$BaseURL = "https://api.softlayer.com/rest/v3"
Add-Content $log "$(Get-Date -format s) : Start"

$SLUser = "SLUSERNAME"
$SLapikey =  "APIKEY"

$LoginPair = "$($SLUser):$($SLapikey)"
$encodedCreds = [System.Convert]::ToBase64String([System.Text.Encoding]::ASCII.GetBytes($LoginPair))
$basicAuthValue = "Basic $encodedCreds"
$Headers = @{
    Authorization = $basicAuthValue
}

$GSTURL="$($BaseURL)/SoftLayer_Account/getObject"
#$GSTURL="$($BaseURL)/SoftLayer_Account/getObject?objectMask=mask[companyName,hardware[hostname]]"
Add-Content $log "$(Get-Date -format s) : Authenticate as User $($SLUser) at URL $($GSTURL)"
$GSTRequest = Invoke-WebRequest $GSTURL  -Headers $Headers -SessionVariable slsession
#Write-host $GSTRequest.content
$GSTanswerConv = ConvertFrom-Json $($GSTRequest.content)
Add-Content $log "$(Get-Date -format s) : Account Info: $($GSTanswerConv | select companyName , country , id)"

#########################
function CallURL($URL) {   
 Add-Content $log "$(Get-Date -format s) : Call URL $($URL)"
$Request = Invoke-WebRequest $URL  -WebSession $slsession 
$answerConv = ConvertFrom-Json $($Request.content)
 return $answerConv
 }
#########################
$URLcall="$($BaseURL)/SoftLayer_Account/getLatestRecurringInvoice"
$Callanswer = CallURL($URLcall)

Add-Content $log "$(Get-Date -format s) : Invoice Info: $($Callanswer | select companyName , id,typeCode, modifyDate , createDate)"

$LastIvoiceID = $Callanswer.id

$URLcall="$($BaseURL)/SoftLayer_Billing_Invoice/$($LastIvoiceID)/getPdfDetailedFilename"
$Callanswer = CallURL($URLcall)
Add-Content $log "$(Get-Date -format s) : Invoice FileName: $($Callanswer)"

$PdfDetailedFilename = $Callanswer
$FileDest = "$HomeDir\$PdfDetailedFilename"

$URLcall="$($BaseURL)/SoftLayer_Billing_Invoice/$($LastIvoiceID)/getPdfDetailed"
$Callanswer = CallURL($URLcall)
$FileData = $Callanswer

$bytes=[System.Convert]::FromBase64String($FileData)
$decoded=[System.Text.Encoding]::Default.GetString($bytes)
[Byte[]]$bytes_FileData=[System.Text.Encoding]::Default.GetBytes($decoded)
set-content -encoding byte -Path $FileDest -value $bytes_FileData
$PdfFile = $FileDest

$URLcall="$($BaseURL)/SoftLayer_Billing_Invoice/$($LastIvoiceID)/getXlsFilename"
$Callanswer = CallURL($URLcall)
Add-Content $log "$(Get-Date -format s) : Invoice FileName: $($Callanswer)"

$XlsFilename = $Callanswer
$FileDest = "$HomeDir\$XlsFilename"


$URLcall="$($BaseURL)/SoftLayer_Billing_Invoice/$($LastIvoiceID)/getExcel"
$Callanswer = CallURL($URLcall)
$FileData = $Callanswer

$bytes=[System.Convert]::FromBase64String($FileData)
$decoded=[System.Text.Encoding]::Default.GetString($bytes)
[Byte[]]$bytes_FileData=[System.Text.Encoding]::Default.GetBytes($decoded)
set-content -encoding byte -Path $FileDest -value $bytes_FileData
$XlsFile = $FileDest

Add-Content $log "$(Get-Date -format s) : End"
#End
```