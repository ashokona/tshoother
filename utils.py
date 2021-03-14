import re
import os
import json
from types import SimpleNamespace
from dotenv import load_dotenv
load_dotenv()
# steps = json.load(open('sceneriao1.json', 'r'))


DOMAIN_NAME = os.getenv('DOMAIN_NAME')
print(DOMAIN_NAME)
with open('data.txt') as json_file:
    steps = json.load(json_file)

# print(data)

def fetchInputs(inputs, steps):
    input_ = {}
    for input in inputs:
        input_[input['key']] = fetchReference(input['reference'], input['value'])
        # if(input['reference'] and input['reference'] == 'env'):
        #     input_[input['key']] = os.getenv(input['value'])
        # if(input['reference'] and input['reference'].find('step') > -1):
        #     input_[input['key']] = steps[input["reference"]
        #         ]["outputs"][input['value']]
        # elif not input['reference']:
        #     input_[input['key']] = input['value']
    # return json.loads(input_)
    return input_


def filterData(data, filters):
    filteredData = []
    print(filteredData)
    for filter in filters:
        if filter['type'] == 'substring':
            # print(data)
            # print(filter)
            filter["value"] = fetchReference(filter['reference'], filter['value']) if "reference" in filter else filter["value"]
            filteredData = [x for x in data if filter["value"].find(x[filter["key"]]) > -1]
            # filteredData = next((x for x in data if filter["value"].find(x[filter["key"]]) > -1), None)
            # return next((x for x in data if filter["value"].find(x[filter["key"]]) > -1), None)
            # return [x for x in data if x[filter["key"]] == filter["value"]]
            # return [x for x in data if re.search(x[filter["key"]], filter["value"])]
            # s.find("is") == -1
            # filter('cloudcops.io', data)
            # return next((x for x in data if x[filter["key"]] == filter["value"]), None)
    return filteredData[0]


def fetchOutput(data, outputs):
    keys = outputs.keys()
    for key in keys:
        outputs[key] = fetchKey(key, data)
        # outputs[key] = data[key]
    return outputs


def fetchKey(k, d):
    if k in d: return d[k]
    for v in d.values():
        if isinstance(v, dict):
            a = fetchKey(k, v)
            if a is not None: return a
    return None

def fetchReference(reference, value):
    print(reference, value)
    if(reference and reference == 'env'):
        return os.getenv(value)
    if(reference and reference.find('step') > -1):
        return steps[reference]["outputs"][value]
    elif not reference:
        return value

def gen_dict_extract(key, var):
    if hasattr(var,'iteritems'):
        for k, v in var.iteritems():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result

def fun(d, key):
    if key in d:
        return d[key]
    for k in d.keys():
        print(type(k))
        if isinstance(k, dict):
            print("yes")
            # for k in d.keys():
            return fun(d[k], key)
    
    # for k in d:
    #     if isinstance(d[k], list):
    #         for i in d[k]:
    #             for j in fun(i,key):
    #                 yield j

# print(data.iteritems())

# d = gen_dict_extract('key2', data)
# d =
# data = { "key1": "value1", "nestes": {"key2": "value2"} }
# data = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
# print(fun(ew, 'key2'))
# datax = { "key1": "value1", "nestes": {"key2": "value2"}, "arr": [{"key1": "value1"}] }

# print(hasattr(datax,'iteritems'))



# print(recursive_lookup("key2", datax))
