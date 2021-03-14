import json, codecs
# import os
# from dotenv import load_dotenv
from boto3_client import Boto3Client
from utils import filterData, fetchOutput, fetchInputs

data = json.load(open('sceneriao1.json', 'r'))

# print(data)
# r53 = Boto3Client('route53')
# hostedZones = r53.execMethod('list_hosted_zones_by_name', {'DNSName':'cloudcops.io'}, 'HostedZones')
# print(hostedZones)
# HostedZoneId = hostedZones[0]['Id']
# print(HostedZoneId)
# RecordSets = r53.execMethod('list_resource_record_sets', {'HostedZoneId': HostedZoneId}, 'ResourceRecordSets')

# print(RecordSets)

def startTroubleShoot():
    steps = data.keys()
    for step in steps:
        with open('data.txt', 'wb') as f:
            json.dump(data, codecs.getwriter('utf-8')(f), ensure_ascii=False)
        currentStep = data[step]
        print("executing "+ step + " : " + currentStep['name'])
        #client init
        client = Boto3Client(currentStep['client'])
        #input formatter
        currentStep['inputs'] = fetchInputs(currentStep['inputs'], data) if 'inputs' in currentStep else {}
        print('####Inputs###')
        print(currentStep['inputs'])
        response = client.execMethod(currentStep['method'], currentStep['inputs'], currentStep['value'])
        print(response)
        response = filterData(response, currentStep['filters'])
        print("###filtered data###")
        print(response)
        currentStep["outputs"] = fetchOutput(response, currentStep["outputs"])
        print(currentStep["outputs"])
        #match 
        

startTroubleShoot()