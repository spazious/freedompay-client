# TenderType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.tender_type import TenderType

# TODO update the JSON string below
json = "{}"
# create an instance of TenderType from a JSON string
tender_type_instance = TenderType.from_json(json)
# print the JSON string representation of the object
print TenderType.to_json()

# convert the object into a dict
tender_type_dict = tender_type_instance.to_dict()
# create an instance of TenderType from a dict
tender_type_form_dict = tender_type.from_dict(tender_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


