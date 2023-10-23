# DccInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **str** |  | [optional] 
**exchange_rate** | **str** |  | [optional] 
**foreign_amount** | **str** |  | [optional] 
**foreign_currency** | **str** |  | [optional] 
**host_data** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.dcc_info import DccInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DccInfo from a JSON string
dcc_info_instance = DccInfo.from_json(json)
# print the JSON string representation of the object
print DccInfo.to_json()

# convert the object into a dict
dcc_info_dict = dcc_info_instance.to_dict()
# create an instance of DccInfo from a dict
dcc_info_form_dict = dcc_info.from_dict(dcc_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


