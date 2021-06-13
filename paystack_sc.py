"""Payment shit."""
import requests
import json

SECRET_KEY = "secret key"
headers = {
	"Authorization": f"Bearer {SECRET_KEY}",
	"content-type": "application/json",
}

# get all banks and codes
def get_bank_codes():
	url2 = 'https://api.paystack.co/'
	bank = 'bank'
	headers2 = {
		"Authorization": "Bearer SECRET_KEY",
	}

	response1 = requests.get(url2+bank, headers=headers2)
	print(response1.status_code)
	return (response1.text)

# Verify Account number

account_number = '0800744238'
bank_code = '044'
path = f'bank/resolve?account_number={account_number}&bank_code={bank_code}'
headers = {
	"Authorization": "Bearer SECRET_KEY",
}

url = 'https://api.paystack.co/'
response = requests.get(url+path, headers=headers)
print(response.status_code)
print(json.loads(response.text)['data']['account_name'])

# Create txn Receipt

url3 = 'https://api.paystack.co/transferrecipient'
headers3 = {
	"Authorization": "Bearer SECRET_KEY",
	"content-type": "application/json",
}
data = {
		"type": "nuban", 
		"name": "From me", 
		"account_number": "0000000", 
		"bank_code": "044", 
		"currency": "NGN",	
}

response3 = requests.post(url3, headers=headers3, data=json.dumps(data))
print(response3.text)
print()
recipient = json.loads(response3.text)['data']['recipient_code']




# Initiate Transfer
url4 = 'https://api.paystack.co/transfer'
headers4 = {
	"Authorization": "Bearer SECRET_KEY",
	"Content-Type": "application/json",
}
amount = 1500
data2 = {
	"source": "balance", 
	"amount": amount*100, 
	"recipient": recipient, 
	"reason": "Holiday Flexing"
}

response4 = requests.post(url4, headers=headers4, data=json.dumps(data2))
print(response4.text)
print()
print(json.loads(response4.text)['data']['status'])

# Bulk Transfers
url5 = 'https://api.paystack.co/transfer/bulk'
headers5 =  {
	"Authorization": "Bearer SECRET_KEY",
	"Content-Type": "application/json",
}
data3 = {
	"currency": "NGN", 
    "source": "balance", 
	"transfers": [
		{
			"amount": 20000,
			"reason": "Life go better for you",
			"recipient": recipient,
	    },
	    {
	        "amount": 20000,
	        "reason": "Easy does it",
	        "recipient": recipient,
	    },
   	] 
}

response5 = requests.post(url5, headers=headers5, data=json.dumps(data3))
print(response5.text)
print()

print(recipient)

# Payment subscription
url = 'https://api.paystack.co/transaction/initialize'

data = {
	"email": "exam@email.com", 
	"amount": "500000", 
	"plan": "PLN_wk39sn9u0mkdce0",
}

payment_response = requests.post(url, headers=headers, data=json.dumps(data))
print(payment_response.text)
print()



# verify payment
url = 'https://api.paystack.co/transaction/verify/cRe0tM11BvBI4xApvOLzoRdf5tdjJvLAfWglhJJghfu2c_5cyYoU8xJ1EUdUA9YOLA8'
# ref = 'ku0f2w30zb'

r = requests.get(url, headers=headers)
print(r.status_code)
