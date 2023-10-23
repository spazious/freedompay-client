# HotelData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_occupant_count** | **str** |  | [optional] 
**room_type** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**properties** | [**List[UserDefinedField]**](UserDefinedField.md) |  | [optional] 
**expected_duration** | **str** |  | [optional] 
**folio_number** | **str** |  | [optional] 
**no_show** | **str** |  | [optional] 
**program_code** | **str** |  | [optional] 
**checkin_date** | **str** |  | [optional] 
**checkout_date** | **str** |  | [optional] 
**extra_charge_types** | **str** |  | [optional] 
**room_rate** | **str** |  | [optional] 
**room_rate_unit** | **str** |  | [optional] 
**room_tax** | **str** |  | [optional] 
**extra_charge_total** | **str** |  | [optional] 
**renter_name** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.hotel_data import HotelData

# TODO update the JSON string below
json = "{}"
# create an instance of HotelData from a JSON string
hotel_data_instance = HotelData.from_json(json)
# print the JSON string representation of the object
print HotelData.to_json()

# convert the object into a dict
hotel_data_dict = hotel_data_instance.to_dict()
# create an instance of HotelData from a dict
hotel_data_form_dict = hotel_data.from_dict(hotel_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


