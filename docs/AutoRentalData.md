# AutoRentalData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_duration** | **str** |  | [optional] 
**agreement_number** | **str** |  | [optional] 
**checkout_date** | **str** |  | [optional] 
**checkin_date** | **str** |  | [optional] 
**rental_rate** | **str** |  | [optional] 
**rental_rate_unit** | **str** |  | [optional] 
**rental_class_id** | **str** |  | [optional] 
**no_show** | **str** |  | [optional] 
**renter_name** | **str** |  | [optional] 
**return_location_id** | **str** |  | [optional] 
**return_city** | **str** |  | [optional] 
**return_state** | **str** |  | [optional] 
**return_country** | **str** |  | [optional] 
**extra_charge_types** | **str** |  | [optional] 
**extra_charge_total** | **str** |  | [optional] 
**extra_charge_notified** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.auto_rental_data import AutoRentalData

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRentalData from a JSON string
auto_rental_data_instance = AutoRentalData.from_json(json)
# print the JSON string representation of the object
print AutoRentalData.to_json()

# convert the object into a dict
auto_rental_data_dict = auto_rental_data_instance.to_dict()
# create an instance of AutoRentalData from a dict
auto_rental_data_form_dict = auto_rental_data.from_dict(auto_rental_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


