# Check


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bank_transit_number** | **str** |  | [optional] 
**account_number** | **str** |  | [optional] 
**account_type** | **str** |  | [optional] 
**check_number** | **str** |  | [optional] 
**ach_accepted** | **str** |  | [optional] 
**check_type** | **str** |  | [optional] 
**full_micr** | **str** |  | [optional] 
**reader_status** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.check import Check

# TODO update the JSON string below
json = "{}"
# create an instance of Check from a JSON string
check_instance = Check.from_json(json)
# print the JSON string representation of the object
print Check.to_json()

# convert the object into a dict
check_dict = check_instance.to_dict()
# create an instance of Check from a dict
check_form_dict = check.from_dict(check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


