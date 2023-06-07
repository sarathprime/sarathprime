from django.shortcuts import render,redirect
from.models import *
from client.models import *
from administator.models import *
from django.core.mail import send_mail
from django.contrib import messages


def donor_index(request):
    return render(request, 'donor/donotor_index.html')




def d_register(request):
    if request.method == 'POST':
        yourname = request.POST['yourname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        donor(username=username, email=email, password=password, contact=contact, yourname=yourname
               ).save()
        messages.info(request, "successfully registered")
        return redirect('/d_login/')
    return render(request, 'donor/donor_register.html')


def d_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            emp = donor.objects.get(email=email, password=password)
            request.session['donor'] = emp.email

            messages.info(request, "successfully login")

            return redirect('/donor_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'donor/donor_login.html')





def view_reciptient_request(request):
    datas=money.objects.all()
    return render(request, 'donor/view_reciptient_request.html',{'datas':datas})



def donor_purpose_form(request):
    if request.method == 'POST':
        yourname = request.POST['yourname']
        organisation = request.POST['organisation']
        email = request.POST['email']
        purpose = request.POST['purpose']
        contact = request.POST['contact']
        donor_purpose(yourname=yourname, organisation=organisation, email=email, purpose=purpose, contact=contact
                       ).save()
        messages.info(request, "your request updated, forwarded to technical team")
        return redirect('/donor_index/')

    return render(request, 'donor/donor_purpose.html')


def donor_wallet(request):
    if request.method == 'POST':
        walletid = request.POST['walletid']
        emp1 = donor_id_generate.objects.get()
        y = emp1.id_donor
        print(y)
        a = walletid
        print(type(y))
        print(type(walletid))
        print(walletid)
        if int(walletid) == int(y):

            messages.info(request, "congrats!! your wallet id is correct")
            print('hi')
            return redirect('/donor_current_wallet/')
        else:

            messages.error(request, "please enter valid wallet id! ")
            print('no')
            return redirect('/donor_wallet/')
    return render(request, 'donor/donor_walletid.html')




def donor_current_wallet(request):
    datas=donor_link_amount.objects.all()
    return render(request, 'donor/donor_current_wallet.html',{'datas':datas})




def donor_tax_pay(request):
    if request.method == 'POST':
        amount = request.POST['amount']
        tax_amount(amount=amount).save()
        messages.error(request, "tax ammount successfully paid! ")
        return redirect('/donor_current_wallet/')
    return render(request,'donor/donor_current_wallet.html')




def donor_send_reciptient(request):
    if request.method == 'POST':
        recipitent = request.POST['recipitent']
        amount = request.POST['amount']
        reciptient_amount(amount=amount,recipitent=recipitent).save()
        messages.error(request, "money will be sent reciptient! ")
        return redirect('/donor_current_wallet/')
    return render(request,'donor/donor_current_wallet.html')



def donate(request):
    return render(request, 'donor/donate.html')





def donor_logout(request):
    if 'donor' in request.session:
        request.session.pop('recipient', None)
        messages.success(request, 'SESSION LOGOUT SUCCESSFULLY')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/')




def currency_converter(request):
    return render(request, 'client/currency_converter.html')




def donar_link_account(request):
    if request.method == 'POST':
        name = request.POST['name']
        ifsc = request.POST['ifsc']
        email = request.POST['email']
        state = request.POST['state']
        city = request.POST['city']
        dob = request.POST['dob']
        number = request.POST['number']
        type = request.POST['type']
        cash = request.POST['cash']
        donor_link_amount(name=name, ifsc=ifsc, state=state, city=city, dob=dob, number=number, type=type, cash=cash
                    ).save()
        messages.info(request, "your request updated")
        return redirect('/donar_link_account/')
    return render(request, 'donor/donor_link.html')



