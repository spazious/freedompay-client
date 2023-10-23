# freedompay-client.model.init_request.InitRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Button** | [**ButtonControl**](ButtonControl.md) | [**ButtonControl**](ButtonControl.md) |  | [optional] 
**ButtonType** | str,  | str,  |  | [optional] must be one of ["Unknown", "Buy", "BuyNow", "Donate", "Next", "Pay", "PayNow", "PayWithCard", "Save", "CompleteYourReservation", "PayByBank", "SubmitToHotel", "UpdateReservation", "CompleteReservation", ] 
**PayPal** | [**PayPalInitRequest**](PayPalInitRequest.md) | [**PayPalInitRequest**](PayPalInitRequest.md) |  | [optional] 
**PostalCode** | [**PostalCodeControl**](PostalCodeControl.md) | [**PostalCodeControl**](PostalCodeControl.md) |  | [optional] 
**PayByBank** | [**PayByBankInitRequest**](PayByBankInitRequest.md) | [**PayByBankInitRequest**](PayByBankInitRequest.md) |  | [optional] 
**FraudCheck** | [**FraudCheckOptions**](FraudCheckOptions.md) | [**FraudCheckOptions**](FraudCheckOptions.md) |  | [optional] 
**CardNumber** | [**CardNumberControl**](CardNumberControl.md) | [**CardNumberControl**](CardNumberControl.md) |  | [optional] 
**ConsumerAuthentication** | [**ConsumerAuthentication**](ConsumerAuthentication.md) | [**ConsumerAuthentication**](ConsumerAuthentication.md) |  | [optional] 
**Dcc** | [**DccOptions**](DccOptions.md) | [**DccOptions**](DccOptions.md) |  | [optional] 
**ExpirationDate** | [**ExpirationDateControl**](ExpirationDateControl.md) | [**ExpirationDateControl**](ExpirationDateControl.md) |  | [optional] 
**OrderDetails** | [**OrderDetails**](OrderDetails.md) | [**OrderDetails**](OrderDetails.md) |  | [optional] 
**SecurityCode** | [**SecurityCodeControl**](SecurityCodeControl.md) | [**SecurityCodeControl**](SecurityCodeControl.md) |  | [optional] 
**TokenInformation** | [**TokenInformation**](TokenInformation.md) | [**TokenInformation**](TokenInformation.md) |  | [optional] 
**CardIconDisplayType** | str,  | str,  |  | [optional] must be one of ["Unknown", "Dynamic", "Fixed", "Hidden", ] 
**PaymentType** | str,  | str,  |  | [optional] must be one of ["Unknown", "Card", "CardOnFile", "GiftCard", "RewardCard", "GooglePay", "ApplePay", "PrivateLabelCard", "PayPal", "PayByBank", ] 
**WorkflowType** | str,  | str,  |  | [optional] must be one of ["Unknown", "Standard", "VerifyAuth", "MultiUse", ] 
**CultureCode** | str,  | str,  |  | [optional] 
**EsKey** | str,  | str,  |  | [optional] 
**Legal** | [**LegalControl**](LegalControl.md) | [**LegalControl**](LegalControl.md) |  | [optional] 
**StoreId** | str,  | str,  |  | [optional] 
**Styles** | str,  | str,  |  | [optional] 
**TerminalId** | str,  | str,  |  | [optional] 
**ValidationMessageType** | str,  | str,  |  | [optional] must be one of ["Unknown", "None", "Feedback", "Tooltip", ] 
**ReferenceId** | str, uuid.UUID,  | str,  |  | [optional] value must be a uuid
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

