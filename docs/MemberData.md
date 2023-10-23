# MemberData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enrollment_date** | **str** |  | [optional] 
**is_new_member** | **str** |  | [optional] 
**member_identification** | **str** |  | [optional] 
**member_identification_type** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**street1** | **str** |  | [optional] 
**street2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**additional_data** | **str** |  | [optional] 
**additional_data_type** | **str** |  | [optional] 
**properties** | [**List[UserDefinedField]**](UserDefinedField.md) |  | [optional] 

## Example

```python
from freedompay_client.models.member_data import MemberData

# TODO update the JSON string below
json = "{}"
# create an instance of MemberData from a JSON string
member_data_instance = MemberData.from_json(json)
# print the JSON string representation of the object
print MemberData.to_json()

# convert the object into a dict
member_data_dict = member_data_instance.to_dict()
# create an instance of MemberData from a dict
member_data_form_dict = member_data.from_dict(member_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


