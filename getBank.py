# Goals ##
# 1. Prompt user for bank and account
# 2. Be able to charge bank
# 3. Be able to deposit into bank

import stripe

# 1. Prompt user for bank and account
customer_name = ''
account_type = ''
account_number = ''
routing_number = ''

# Using Plaid's Python bindings (https://github.com/plaid/plaid-python)
client = Client('{PLAID_CLIENT_ID}',
                '{PLAID_SECRET}',
                '{PLAID_PUBLIC_KEY}',
                'sandbox')

exchange_token_response = client.Item.public_token.exchange({PLAID_LINK_PUBLIC_TOKEN})
access_token = exchange_token_response['access_token']

stripe_response = client.Processor.stripeBankAccountTokenCreate(access_token, {ACCOUNT_ID})
bank_account_token = stripe_response['stripe_bank_account_token']
