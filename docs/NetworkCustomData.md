# NetworkCustomData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[str]** |  | [optional] 
**code** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.network_custom_data import NetworkCustomData

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkCustomData from a JSON string
network_custom_data_instance = NetworkCustomData.from_json(json)
# print the JSON string representation of the object
print NetworkCustomData.to_json()

# convert the object into a dict
network_custom_data_dict = network_custom_data_instance.to_dict()
# create an instance of NetworkCustomData from a dict
network_custom_data_form_dict = network_custom_data.from_dict(network_custom_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


