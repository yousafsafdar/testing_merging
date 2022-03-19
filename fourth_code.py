import json


def dict_to_json(dic_json):
    """This function accepts data as a dictionary and converts it into json. If you have a Python object,
    you can convert it into a JSON string by using the json.dumps() method."""
    json_object = json.dumps(dic_json, indent=4, sort_keys=True)
    return json_object


def get_value(json_data):
    """json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. So in
    this function I am getting a json data from dict_to_json function and here I am converting json data to
    dictionary """
    data_value = json.loads(dict_to_json(json_data))
    return data_value['key2']


data = {"key1": "value1", "key2": "value2"}
response_dict_to_json = get_value(data)
print(response_dict_to_json)

