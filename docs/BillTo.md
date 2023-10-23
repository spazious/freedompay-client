# BillTo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | [optional] 
**customer_id** | **str** |  | [optional] 
**date_of_birth** | **str** |  | [optional] 
**drivers_license_number** | **str** |  | [optional] 
**drivers_license_state** | **str** |  | [optional] 
**company** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**middle_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**suffix** | **str** |  | [optional] 
**street1** | **str** |  | [optional] 
**street2** | **str** |  | [optional] 
**street3** | **str** |  | [optional] 
**street4** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**fax_number** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**ssn** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.bill_to import BillTo

# TODO update the JSON string below
json = "{}"
# create an instance of BillTo from a JSON string
bill_to_instance = BillTo.from_json(json)
# print the JSON string representation of the object
print BillTo.to_json()

# convert the object into a dict
bill_to_dict = bill_to_instance.to_dict()
# create an instance of BillTo from a dict
bill_to_form_dict = bill_to.from_dict(bill_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


