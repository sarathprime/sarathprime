from django.shortcuts import render, redirect
from .models import *
from client.models import *
from django.contrib import messages
from django.core.mail import send_mail

from technical.models import *

from donar.models import *




def view_reciptient(request):
    datas = money.objects.all()
    return render(request,'admin/view_reciptient.html', {'datas': datas})

def view_donor(request):
    datas = donor_purpose.objects.all()
    return render(request,'admin/view_donor.html', {'datas': datas})


def a_index(request):
    return render(request,'admin/admin_index.html')


def id_generator(request):
    datas = money.objects.all()
    return render(request,'admin/id.html', {'datas': datas})


def view_autenticator(request):
    datas = wallet_entry.objects.filter(bt=False)
    return render(request,'admin/view_team.html', {'datas': datas})




def ae_mail(request, id):
    datas = wallet_entry.objects.get(id=id)
    # datas2 = client_purpose.objects.get(id=id)
    # y= datas2.yourname
    t = datas.email
    send_mail(
        'Subject here',
        f'welcome team!!! , your team wallet id  is 1124   ',
        'sarath@gmail.com',
        [datas.teamname],
        fail_silently=False,

    )
    messages.info(request, "id successfully sent to technical email id")
    # datas.save()
    return redirect('/a_index/')



def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == "admin@gmail.com" and password == "admin":
            request.session['admin'] = 'admin@gmail.com'
            messages.info(request, "successfully login")
            return redirect('/a_index/')
        elif username != "admin@gmail.com":
            messages.error(request, "Wrong Admin Email")
            return redirect('/admin_login/')
        elif password != "admin":
            messages.error(request, "Wrong Admin Password")
            return render(request, 'admin/admin_login.html')
    return render(request, 'admin/admin_login.html')





def set_currency(request):
    if request.method == 'POST':
        administrator = request.POST['administrator']
        currency = request.POST['currency']
        what = request.POST['what']
        license = request.POST['license']
        value= request.POST['value']
        value_set(administrator=administrator, currency=currency, what=what, license=license,value=value).save()
        messages.info(request, "coin successfully created")
        return redirect('/set_currency/')
    return render(request, 'admin/currency.html')



def r_id(request):
    if request.method == 'POST':
        email = request.POST['email']
        generate_id = request.POST['generate_id']
        r_w(email=email, generate_id=generate_id).save()
        messages.info(request, "wallet id stored in database")
        return redirect('/r_id/')
    return render(request, 'admin/id.html')


def generate_donor(request):
    datas = donor_purpose.objects.all()
    if request.method == 'POST':
        email = request.POST['email']
        id_donor = request.POST['id_donor']
        donor_id_generate(email=email, id_donor=id_donor).save()
        messages.info(request, "wallet id for donor successfully saved in the database")
        return redirect('/generate_donor/')
    return render(request, 'admin/donorid.html',{'datas':datas})


def re_mail(request, id):
    z = r_w.objects.get(id=id)
    # datas2 = client_purpose.objects.get(id=id)
    # y= datas2.yourname
    t= datas.generate_id
    print(t)
    # print(y)
    # print(datas.email)
    # # print(datas.refer)
    send_mail(
        'Subject here',
        f'CONGRATS FOLK!!! , You have been Approved for accessing our wallet, your wallet id  is {t}   ',
        'sarath@gmail.com',
        [datas.email],
        fail_silently=False,
    )

    messages.info(request, "wallet id successfully forwarded to reciptient mail")
    # datas.save()
    return redirect('/a_index/')


def de_mail(request, id):
    datas = donor_id_generate.objects.get(id=id)
    # datas2 = client_purpose.objects.get(id=id)
    # y= datas2.yourname
    t= datas.id_donor
    print(t)
    # print(y)
    # print(datas.email)
    # # print(datas.refer)
    send_mail(
        'Subject here',
        f'CONGRATS FOLK!!! , You have been Approved for accessing our wallet, your wallet id  is {t}   ',
        'sarath@gmail.com',
        [datas.email],
        fail_silently=False,
    )
    messages.info(request, "wallet id successfully forwarded to donor mail")

    # datas.save()
    return redirect('/a_index/')









def d_send(request):
    datas = donor_id_generate.objects.all()
    return render(request,'admin/send_donor_id.html', {'datas': datas})





def r_send(request):
    datas = r_w.objects.all()
    return render(request,'admin/send_r_id.html', {'datas': datas})





def A_logout(request):
    if 'admin' in request.session:
        request.session.pop('admin',None)
        messages.success(request,'logout already successfully')
        return redirect('/')
    else:
        messages.success(request, 'session logged out')
        return redirect('/admin/')