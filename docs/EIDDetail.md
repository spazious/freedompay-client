# EIDDetail


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_key** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**qty** | **str** |  | [optional] 
**offset** | **str** |  | [optional] 
**total_amount** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.eid_detail import EIDDetail

# TODO update the JSON string below
json = "{}"
# create an instance of EIDDetail from a JSON string
eid_detail_instance = EIDDetail.from_json(json)
# print the JSON string representation of the object
print EIDDetail.to_json()

# convert the object into a dict
eid_detail_dict = eid_detail_instance.to_dict()
# create an instance of EIDDetail from a dict
eid_detail_form_dict = eid_detail.from_dict(eid_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


