def process_bank_info(public_token, account_id):
    # Converts Plaid public token and account ID into Plaid access token and Stripe token for processing.
    from plaid import Client

    # Change `sandbox` to `development` to test with live users and change
    # to `production` when you're ready to go live!
    client = Client(client_id='5a54dbbdefe64e49ca4ae233', secret='e46141f14d9a73d68f2dc58a7a9c3b',
                    public_key='cc5eca9a7b42c6fd2dee4ebad4e959', environment='sandbox')

    exchange_token_response = client.Item.public_token.exchange(public_token)
    access_token = exchange_token_response['access_token']

    stripe_response = client.Processor.stripeBankAccountTokenCreate(access_token, account_id)
    bank_account_token = stripe_response['stripe_bank_account_token']

    return [access_token, bank_account_token]


def account_data(plaid_access_token):
    # Returns all account data for plaid_access_token account
    from plaid import Client

    client = Client(client_id='5a54dbbdefe64e49ca4ae233', secret='e46141f14d9a73d68f2dc58a7a9c3b',
                    public_key='cc5eca9a7b42c6fd2dee4ebad4e959', environment='sandbox')

    # Retrieve Auth information for the Item, which includes high-level
    # account information and account numbers for depository accounts.
    auth_response = client.Auth.get(plaid_access_token)
    return auth_response

def update_account_db(username, stripe_token, plaid_access_token):
    # Updates db with user account. Assumes user account exists already.
    from cbs_renmo.models import User, bankAccount

    # TODO find matching User object using username and set it to user_object
    user_object = ''

    # TODO check if account already exists. If it does, do nothing and return message.

    account_object = bankAccount(plaid_token=plaid_access_token, stripe_token=stripe_token, user=user_object)
    account_object.save()

    return None

