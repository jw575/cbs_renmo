from django.shortcuts import render
import cbs_renmo
import cbs_renmo.app_logic


def home(request):
    context = dict()
    context['options'] = [
        ['bankInfo', 'Enter your bank information'],
        ['loginFunction', 'Login'],
    ]
    return render(request, "home.html", context)
    # renders home.html using whatever inside the context dictionary


def get_bank(request):
    context = dict()
    return render(request, "bankInfo.html", context)


def login(request):
    context = dict()
    return render(request, "loginFunction.html", context)


def receiver(request):
    from django.urls import reverse
    from django.http import HttpResponseRedirect

    context = dict()
    try:
        if request.POST:
            token = request.POST['token']
            id = request.POST['id']
            # print('received id: ' + id)
            plaid_access_token = cbs_renmo.app_logic.process_bank_info(token, id)[0]
            stripe_tokenID = cbs_renmo.app_logic.process_bank_info(token, id)[1]
            # print(plaid_access_token)
            # print(stripe_tokenID)
            account_data = cbs_renmo.app_logic.account_data(plaid_access_token)
            # print("exited account_data()")
            # print(account_data)

            for item in account_data['accounts']:
                if id == item['account_id']:
                    account_id = item['account_id']
                    available_balance = item['balances']['available']
                    nickname = item['name']
                    official_name = item['official_name']
                    subtype = item['subtype']
                else:
                    continue
            for account in account_data['numbers']:
                if id == account['account_id']:
                    account_number = account['account']
                    routing = account['routing']
                    wire_routing = account['wire_routing']
                else:
                    pass

            context['account_data'] = {'plaid_token': plaid_access_token,
                                       'stripe_token': stripe_tokenID,
                                       'account_id': account_id,
                                       'available_balance': available_balance,
                                       'nickname': nickname,
                                       'official_name': official_name,
                                       'subtype': subtype,
                                       'account_number': account_number,
                                       'routing': routing,
                                       'wire_routing': wire_routing
                                       }
        else:
            print('No POST data')
    except:
        print("Exception Occured")
    print('before context')
    print(context)
    print('after context')
    return render(request, "management.html", context)
