from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from client.models import *
from donar.models import *
from cryptography.fernet import Fernet
from cryptography.fernet import Fernet
import string,random,hmac
import rsa
# from Crypto.PublicKey import RSA
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.db import IntegrityError
# Create your views here.
from .models import *

import random
import tkinter
from tkinter import *
from tkinter import messagebox

# from hashlib import *
from hashlib import *
import hashlib

def b_index(request):
    return render(request, 'block_chain/block_chain_index.html')





def B_register(request):
    if request.method == 'POST':
        yourname = request.POST['yourname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        block_chain(username=username, email=email, password=password, contact=contact, yourname=yourname
               ).save()
        messages.info(request, "successfully registered")
        return redirect('/b_login/')
    return render(request, 'block_chain/B_register.html')


def b_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            emp = block_chain.objects.get(email=email, password=password)
            request.session['blockchain'] = emp.email

            messages.info(request, "successfully login")

            return redirect('/b_index/')
        except:
            messages.info(request, "Wrong Credentials")
    return render(request, 'block_chain/b_login.html')




def view_transaction(request):
    datas = reciptient_amount.objects.filter(b5=True)
    return render(request, 'block_chain/view_transaction.html',{'datas': datas})




def block_logout(request):
    if 'blockchain' in request.session:
        request.session.pop('blockchain',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/')




def encryption_data(request):
    datas=reciptient_amount.objects.all()
    key = Fernet.generate_key()
    print(key)
    f = Fernet(key)
    f.encrypt(datas)
    datas.save()
    return render(request,'block_chain/view_transaction.html',{'datas': datas})







def encryption(request):
    ledger=reciptient_amount.objects.all()
    encryptid=int(''.join(random.sample(string.digits,k=6)))
    key=Fernet.generate_key()
    f = Fernet(key)
    value=''
    for i in ledger:
        value+=(str(i).encode()).decode()+"@"
    encrypted_value=f.encrypt(value.encode())
    key=key.decode()
    ledger1=reciptient_amount.objects.all()
    ledger1.encryptid=encryptid
    print(ledger1)
    ledger1.save()
    encrypt(encryptid=encryptid,encrypted_value=encrypted_value.decode(),key=key).save()
    messages.success(request, "ENCRYPTION PROCESS HAS BEEN DONE")
    return redirect('/view_transaction/')


import rsa



def enc(request,id):
    get = reciptient_amount.objects.get(id=id)
    publicKey, privateKey = rsa.newkeys(512)
    r = get.id
    inputvar = []
    get.save()

    a = get.amount
    b = get.recipitent
    # c = get.year
    # d = get.condition
    # e = get.gear_condition
    print(a)
    print(b)
    inputvar.append(a)
    inputvar.append(b)
    # inputvar.append(c)
    # inputvar.append(e)
    # inputvar.append(d)
    x = []
    for i in inputvar:
        encMessage = rsa.encrypt(i.encode(), publicKey)
        # print("original string: ", i)
        # print("encrypted string: ", encMessage)
        x.append(encMessage)

        # print(a)

        decMessage = rsa.decrypt(encMessage, privateKey).decode()
        # print("decrypted string: ", decMessage)
    #     datas = mechanical_analysis.objects.get(id=id)
    #     datas.car_encrypt = a
    #     datas.save()
    print(x)
    a = x[0]
    b = x[1]
    # c = x[2]
    # d = x[3]
    # e = x[4]
    st = reciptient_amount.objects.filter(id=r).update(amount=a, recipitent=b)
    print(a, b)
    messages.info(request, "data encrypted successfully , ready for hashing...")

    return redirect('/view_encrypted/')




def view_encrypted(request):
    datas = reciptient_amount.objects.all()
    return render(request, 'block_chain/view_encrypted.html',{'datas':datas})


def view_hashed(request):
    datas = reciptient_amount.objects.all()
    return render(request, 'block_chain/view_hashed.html',{'datas':datas})










def hash(request,id):
        data = reciptient_amount.objects.get(id=id)
        # a = userAccount.objects.get()
        # c = a.user_pin
        d = data.amount
        # print(c)
        print(d)
        k = random.randint(100000000000000,1000000000000000)
        data.trans_id = k

        a_string = str(data.amount)
        hashed_string = hashlib.sha256(a_string.encode('utf-8')).hexdigest()
        data.hash_id = hashed_string
        data.save()
        ledger = reciptient_amount.objects.all()
        print(ledger)
        messages.info(request, "Data hashed sucessfully transaction is secured!!")
        return redirect('/view_hashed/')



