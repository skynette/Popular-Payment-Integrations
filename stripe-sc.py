import stripe
stripe.api_key = "secret"

# `source` is obtained with Stripe.js; see https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token
pay = stripe.Charge.create(
  amount=100*100,
  currency="usd",
  source="tok_mastercard",
  description="API test charge",
  receipt_email="exam@gmail.com",
)

print("success")