from lxml import etree
import requests

request = etree.Element("request")
header = etree.SubElement(request, "header")
soaCorrelationId = etree.SubElement(header, "soaCorrelationId")
soaMsgVersion = etree.SubElement(header, "soaMsgVersion")
soaAppId = etree.SubElement(header, "soaAppId")
soaUserId = etree.SubElement(header, "soaUserId")
soaPassword = etree.SubElement(header, "soaPassword")
requestData = etree.SubElement(request, "requestData")
requestPayload = etree.SubElement(requestData, "requestPayload")
transactions = etree.SubElement(requestPayload, "transactions")
leadId = etree.SubElement(transactions, "leadId")
docType = etree.SubElement(transactions, "docType")
fileFormat = etree.SubElement(transactions, "fileFormat")
atchmnt = etree.SubElement(transactions, "atchmnt")
date = etree.SubElement(transactions, "date")
validationType=etree.SubElement(transactions, "validationType")



soaCorrelationId.text='12074542'
soaMsgVersion.text='1.0'
soaAppId.text='NEO'
soaUserId.text='NEO123'
soaPassword.text='bmVvQDEyMw=='
leadId.text='12497397'
docType.text='176'
fileFormat.text='pdf'
date.text='15-02-2017'
validationType.text='DFS'

url = 'https://gatewayuat.maxlifeinsurance.com/apimgm/sb/soa/dfsuploadxml/v2'
req_data = etree.tostring(request)
res = requests.post(url, data=req_data)
