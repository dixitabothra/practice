import requests
import json

url = "https://gatewayuat.maxlifeinsurance.com/apimgm/sb/soa/nb/uw/schedulemedical/appointmentslot/v1?client_id=%s&client_secret=%s"
client_id = "e453efc3-1437-40d2-a7fc-d82b991c32c1"
client_secert = "jC6uQ7bB3xN1kE1mX4nT7wV1bG2fV2rX5kK1xY1lF8uC8fA8iH" 

headers={"Content-Type": "application/json"}


data='{ "request": { "header": { "soaCorrelationId": "12345", "soaAppId": "NEO" }, "payload": { "state": "Delhi", "commPincode": "12695116", "sumAssured": "10000000", "wopPremium": "1000", "policyTerm": "40", "age": "26", "dob": "20/07/1991", "channelName": "M", "productCode": "TCOT60", "nationality": "I", "education": "GRADUATE", "income": "600000", "occupation": "SALARIED", "wop": "Y", "smoker": "N", "city": "Delhi", "customerType": "Max", "bloodPressure": "N", "chestPain": "N", "heartAttack": "N", "stroke": "N", "heartCondition": "N", "highBloodSugar": "N", "diabetes": "N", "thyroid": "N", "hormonalDisorder": "N", "asthma": "N", "tuberculosis": "N", "respiratoryDisorder": "N", "cancer": "N", "tumourOrMalignantGrowth": "N", "leukemia": "N", "bloodDisorder": "N", "stomachOrIntestinal": "N", "jaundice": "N", "kidneyDisorders": "N", "mentalOrPsychiatricAilment": "N", "nervousSystem": "N", "bonesOrJointsOrLimbs": "N", "spine": "N", "muscle": "N", "eyeOrEarOrNoseOrThroat": "N", "hepatitisB": "N", "hepatitisC": "N", "hivInfection": "N", "aidsOrAidsRelated": "N", "sexuallyTransmitted": "N", "gynaecologicalDisorder": "N", "absentFromWork": "N", "hospitalised": "N", "medicalCondition": "N", "frequencyOfPayment": "Semi-Annually" } } }'

url = url % (client_id, client_secert)
res = requests.post(url, data=data, headers=headers, timeout=10)
print "\nURL: ", res.url
print "\nHeaders: ", res.headers
print "\nData",res.request.body
print "\nCookies", res.cookies
print "\nResponse: ", res.content
print "\nStatus Code", res.status_code

