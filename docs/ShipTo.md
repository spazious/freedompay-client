# ShipTo


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
**date_of_birth** | **str** |  | [optional] 
**shipping_company** | **str** |  | [optional] 
**shipping_method** | **str** |  | [optional] 
**tracking_number** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.ship_to import ShipTo

# TODO update the JSON string below
json = "{}"
# create an instance of ShipTo from a JSON string
ship_to_instance = ShipTo.from_json(json)
# print the JSON string representation of the object
print ShipTo.to_json()

# convert the object into a dict
ship_to_dict = ship_to_instance.to_dict()
# create an instance of ShipTo from a dict
ship_to_form_dict = ship_to.from_dict(ship_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


