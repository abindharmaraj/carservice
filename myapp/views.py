from django.shortcuts import render,redirect
from random import random
from django.core.files.storage import FileSystemStorage
from .models import *
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

# Create your views here.

def fn_index(req):
    return render(req,'index.html')

def prohome(request):
    return render(request,'prohome.html')

def proser(request):
    return render(request,'proser.html')
def adm(req):
    return render(req,'ad.html')

def admn(req):
    return render(req,'fom.html')

def lo(request):
    if(request.method == "POST"):
        # return HttpResponse("this is post")
        name=request.POST['name']
        place=request.POST['place']
        number=request.POST['num']
        address=request.POST['adrs']
        email=request.POST['email']
        password=request.POST['pswd']

        dat=log(name=name,palce=place,number=number,address=address,email=email,password=password)
        dat.save()
        return HttpResponse("done")

    else:
        return render(request,'log.html')

def tab(req):
    see=log.objects.all()
    return render(req,'table.html',{'datas':see})

def textdel(req,id):
    log.objects.get(id=id).delete()
    return redirect('tab')

def textup(req,id):
    updat=log.objects.get(id=id)
    return render(req,'update.html',{'datas':updat})

def updateform(request,id):
    name=request.POST['name']
    place=request.POST['place']
    number=request.POST['num']
    address=request.POST['adrs']
    email=request.POST['email']
    password=request.POST['pswd']
    log.objects.filter(id=id).update(name=name,palce=place,number=number,address=address,email=email,password=password)
    return redirect('tab')

def user(request):
    if(request.method == "POST"):
        username=request.POST['username']
        password=request.POST['password']
        try:
            ulog=log.objects.get(email=username)
            repass=str(ulog.password)
            reemail=str(ulog.email)
            if reemail == username and repass==password:
                request.session['logid']=ulog.id
                return redirect('home')
                
            else:
                return render(request,'user.html',{'error':'incorrect password'})
        except log.DoesNotExist:
            return render(request,'user.html',{'error':'incorrect user'})
            

    else:
        return render(request,'user.html')

def home(request):
    ses=request.session['logid']
    updat=log.objects.get(id=ses)
    return render(request,'homeview.html',{'datas':updat})

def lout(request):
    del request.session['logid'],
    return render(request,'user.html')

def file(request):
    return render(request,'file.html')

def fileup(request):
    if(request.method=='POST'):
        email=request.POST['email']
        password=request.POST['password']
        myfile=request.FILES['image']
        filename=str(random())+ myfile.name
        fs=FileSystemStorage()
        fs.save(filename,myfile)
        fileupload=File(image=filename,email=email,password=password)
        fileupload.save()
        return render(request,'file.html')
    else:
        return render(request,'file.html')

def save(request):
    sa=File.objects.all()
    return render(request,'save.html',{'not':sa})

def ajform(request):
    return render(request,'ajform.html')

def ajf(request):
    name=request.POST['name']
    address=request.POST['address']
    email=request.POST['email']
    password=request.POST['password']
    ajaxin=Ajreg(name=name,address=address,email=email,password=password)
    ajaxin.save()
    return JsonResponse({'message':'data sucess'})    

def ajtab(request):
    return render(request,'ajtab.html')

def displaydata(request):
    selectdata=Ajreg.objects.all()
    ajdis = [{'id': blog.id, 'name': blog.name,'address':blog.address,'email':blog.email,'password':blog.password} for blog in selectdata]
    return JsonResponse({'data':ajdis})

def delaj(request):
    id=request.POST['key_id']
    Ajreg.objects.get(id=id).delete()
    return JsonResponse({'message':'data deleted'})

@api_view(['POST'])
def apiins(request):
    data=request.data
    saveapidata=Ajreg(name=data['apiname'],address=data['apiaddress'],email=data['apiemail'],password=data['apipassword'])
    saveapidata.save()
    return Response('success')

@api_view(['GET'])
def apiget(request):
    gett=Ajreg.objects.all()
    data=[{'id':blog.id,'name':blog.name,'address':blog.address,'email':blog.email,'password':blog.password}for blog in gett]
    return JsonResponse({'data':data})

@api_view(['DELETE'])
def apidel(request):
    data=request.data
    Ajreg.objects.get(id=data['id']).delete()
    return Response("deleted")



    





    


