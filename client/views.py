from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
# from administrator.models import *
from django.http import HttpResponse
from django.contrib import messages
from client.models import *
from administator.models import *


# from molding.models import *
# from consumer.models import *


def c_register(request):
    if request.method == 'POST':
        yourname = request.POST['yourname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        client(username=username, email=email, password=password, contact=contact, yourname=yourname
               ).save()
        messages.info(request, "successfully registered")
        return redirect('/c_login/')
    return render(request, 'client/c_register.html')


def c_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            emp = client.objects.get(email=email, password=password)
            request.session['recipient'] = emp.email

            messages.info(request, "successfully login")

            return redirect('/c_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'client/c_login.html')


def upload_requirement(request):
    if request.method == 'POST':
        yourname = request.POST['yourname']
        email = request.POST['email']
        buisness = request.POST['buisness']
        targetamount = request.POST['targetamount']
        employers = request.POST['employers']
        file = request.FILES['file']
        money(yourname=yourname, email=email, buisness=buisness, targetamount=targetamount, employers=employers,
              file=file).save()
        messages.info(request, "requirement updated")
        return redirect('/c_index/')
    return render(request, 'client/requirement.html')


def c_index(request):
    return render(request, 'client/client_index.html')




def currency_converter(request):
    return render(request, 'client/currency_converter.html')


def walletid(request):
    if request.method == 'POST':
        walletid = request.POST['walletid']
        emp1 = r_w.objects.get()
        y = emp1.generate_id
        print(y)
        a = walletid
        print(type(y))
        print(type(walletid))
        if int(walletid) == int(y):

            messages.info(request, "congrats!! your wallet id is correct")
            print('hi')
            return redirect('/reciptient_Wallet/')
        else:

            messages.error(request, "your wallet is Wrong ")
            print('no')
            return redirect('/walletid/')
    return render(request, 'client/walletid.html')


def purpose_form(request):
    if request.method == 'POST':
        yourname = request.POST['yourname']
        organisation = request.POST['organisation']
        email = request.POST['email']
        purpose = request.POST['purpose']
        contact = request.POST['contact']
        client_purpose(yourname=yourname, organisation=organisation, email=email, purpose=purpose, contact=contact
                       ).save()
        messages.info(request, "your request updated to technical team")
        return redirect('/purpose_form/')
    return render(request, 'client/purpose_form.html')


def reciptient_Wallet(request):
    datas = link_amount.objects.all()
    return render(request, 'client/requirement_wallet.html',{'datas':datas})


def link_account_details(request):
    if request.method == 'POST':
        name = request.POST['name']
        ifsc = request.POST['ifsc']
        state = request.POST['state']
        city = request.POST['city']
        dob = request.POST['dob']
        number = request.POST['number']
        type = request.POST['type']
        cash = request.POST['cash']
        link_amount(name=name, ifsc=ifsc, state=state, city=city, dob=dob, number=number, type=type, cash=cash
                    ).save()
        messages.info(request, "congrats!! your account successfully added to the wallet")
        return redirect('/link_account_details/')
    return render(request, 'client/link_account.html')


def C_logout(request):
    if 'recipient' in request.session:
        request.session.pop('recipient', None)
        messages.success(request, 'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/')
