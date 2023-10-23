# ShipFrom


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from freedompay_client.models.ship_from import ShipFrom

# TODO update the JSON string below
json = "{}"
# create an instance of ShipFrom from a JSON string
ship_from_instance = ShipFrom.from_json(json)
# print the JSON string representation of the object
print ShipFrom.to_json()

# convert the object into a dict
ship_from_dict = ship_from_instance.to_dict()
# create an instance of ShipFrom from a dict
ship_from_form_dict = ship_from.from_dict(ship_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


