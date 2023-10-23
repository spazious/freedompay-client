# TaxDetailItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**amount** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.tax_detail_item import TaxDetailItem

# TODO update the JSON string below
json = "{}"
# create an instance of TaxDetailItem from a JSON string
tax_detail_item_instance = TaxDetailItem.from_json(json)
# print the JSON string representation of the object
print TaxDetailItem.to_json()

# convert the object into a dict
tax_detail_item_dict = tax_detail_item_instance.to_dict()
# create an instance of TaxDetailItem from a dict
tax_detail_item_form_dict = tax_detail_item.from_dict(tax_detail_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


