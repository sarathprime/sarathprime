from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
# from administrator.models import *
from django.http import HttpResponse
from django.contrib import messages
from . models import *
from django.core.mail import send_mail
import random
import math
from client.models import *
from donar.models import *
def t_index(request):
    return render(request,'technical/t_index.html')


def table(request):
    datas = client_purpose.objects.filter(booleann=False)
    return render(request,'technical/table.html', {'datas': datas})


def tableaccept(request,id):
    datas = client_purpose.objects.get(id=id)
    datas.booleann = True
    datas.save()
    messages.info(request, "analysed and access forwarded to admin")
    return redirect('/t_index/')



def t_register(request):
    if request.method == 'POST':
        yourname = request.POST['yourname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        technical(username=username, email=email, password=password, contact=contact,yourname=yourname
                    ).save()
        messages.info(request, "successfully registered")
        return redirect('/t_login/')
    return render(request, 'technical/t_register.html')




def t_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            emp = technical.objects.get(email=email, password=password)
            request.session['technical'] = emp.email

            messages.info(request, "successfully login")

            return redirect('/t_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'technical/t_login.html')





def access_Wallet(request):
    if request.method=='POST':
        teamname = request.POST['teamname']
        purpose = request.POST['purpose']
        wallet_entry(teamname=teamname,purpose=purpose).save()
        messages.info(request,"wallet request updated to admin")
        return redirect('/access_Wallet/')

    return render(request, 'technical/access_Wallet_id.html')





def c_walletid(request):
    if request.method == 'POST':
        walletid = request.POST['walletid']
        # emp1 = wallet_entry.objects.get()
        # y = emp1.generate_id
        # print(y)
        # a = walletid
        # print(type(y))
        # print(type(walletid))
        if int(walletid) == int(1124):

            messages.info(request, "correct wallet id ")
            print('hi')
            return redirect('/tech_Wallet/')
        else:

            messages.error(request, "please enter correct Access id ")
            print('no')
            return redirect('/c_walletid/')
    return render(request, 'technical/company_Wallet.html')



















def approve_project(request, id):
    otp = random.randrange(1000, 2000, 1)
    print(otp)
    ott='ser'
    datas = client_purpose.objects.get(id=id)
    t= datas.contact
    print(t)
    print(datas.email)
    # print(datas.refer)
    send_mail(
        'Subject here',
        f'Congrats! ,your otp number is {otp}  You{t}  have been Approved ',
        'sarath@gmail.com',
        [datas.email],
        fail_silently=False,
    )

    datas.save()
    return redirect('/t_index/')



def tech_Wallet(request):
    datas=tax_amount.objects.all()
    return render(request,'technical/technical_Wallet.html',{'datas':datas})



def view_donor(request):
    datas = donor_purpose.objects.filter(b3=False)
    return render(request,'technical/view_donor.html', {'datas': datas})



def donor_accept(request,id):
    datas = donor_purpose.objects.get(id=id)
    datas.b3 = True
    datas.save()
    messages.info(request, "analysed and access forwarded to admin")
    return redirect('/t_index/')


def view_transaction(request):
        datas = reciptient_amount.objects.filter(b5=False)
        return render(request,'technical/view transaction.html', {'datas': datas})




def transaction_update(request,id):
    datas = reciptient_amount.objects.get(id=id)
    datas.b5 = True
    datas.save()
    messages.info(request, "analysed and access forwarded to encryption team")
    return redirect('/t_index/')



def view_transaction1(request):
    datas = reciptient_amount.objects.get()
    datas1 = donor_link_amount.objects.filter(update=False)
    # print(datas1.id)
    print(datas1.name)
    r =datas.id
    datas.update=True
    datas.save()

    datas1.update= True
    datas1.Save()
    name = datas1.name
    print(name)
    s=reciptient_amount.objects.filter(id=r).update(name=name)
    return redirect('/view_transaction/')






def technical_logout(request):
    if 'technical' in request.session:
        request.session.pop('admin',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/t_index/')



def analysing(request):
    return render(request,'technical/analysing.html')

