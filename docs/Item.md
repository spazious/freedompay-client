# Item


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discount_amount** | **str** |  | [optional] 
**discount_flag** | **str** |  | [optional] 
**tax_included_flag** | **str** |  | [optional] 
**product_code** | **str** |  | [optional] 
**product_upc** | **str** |  | [optional] 
**product_sku** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**product_description** | **str** |  | [optional] 
**product_make** | **str** |  | [optional] 
**product_model** | **str** |  | [optional] 
**product_part_number** | **str** |  | [optional] 
**commodity_code** | **str** |  | [optional] 
**product_year** | **str** |  | [optional] 
**product_serial1** | **str** |  | [optional] 
**product_serial2** | **str** |  | [optional] 
**product_serial3** | **str** |  | [optional] 
**customer_asset_id** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**sub_category** | **str** |  | [optional] 
**unit_price** | **str** |  | [optional] 
**quantity** | **str** |  | [optional] 
**total_amount** | **str** |  | [optional] 
**tax_amount** | **str** |  | [optional] 
**promo_code** | **str** |  | [optional] 
**freight_amount** | **str** |  | [optional] 
**unit_of_measure** | **str** |  | [optional] 
**sale_code** | **str** |  | [optional] 
**custom_format_id** | **str** |  | [optional] 
**custom1** | **str** |  | [optional] 
**custom2** | **str** |  | [optional] 
**custom3** | **str** |  | [optional] 
**custom4** | **str** |  | [optional] 
**custom5** | **str** |  | [optional] 
**custom6** | **str** |  | [optional] 
**custom7** | **str** |  | [optional] 
**custom8** | **str** |  | [optional] 
**custom9** | **str** |  | [optional] 
**pay_alloc** | **str** |  | [optional] 
**alloc_code** | **str** |  | [optional] 
**eid_indicator** | **str** |  | [optional] 
**orig_unit_price** | **str** |  | [optional] 
**orig_total_amount** | **str** |  | [optional] 
**eid_detail** | [**List[EIDDetail]**](EIDDetail.md) |  | [optional] 
**tax_detail** | [**List[TaxDetailItem]**](TaxDetailItem.md) |  | [optional] 
**id** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from freedompay_client.models.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print Item.to_json()

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_form_dict = item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


