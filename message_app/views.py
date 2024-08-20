from multiprocessing import context
from django.shortcuts import redirect, render,HttpResponse
from .models import Msg
def demo(request):
    return HttpResponse("hello !!!")

def create(request):
    #print("Request is:",request.method)
    if request.method=='POST':
      n=request.POST['uname']
      id=request.POST['id']
      mail=request.POST['uemail']
      mob=request.POST['mobile']
      msg=request.POST['msg']
      m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
      m.save()
      return redirect('/')
      '''
      print("Nmae:",n)
      print("Email:",mail)
      print("mobile:",mob)
      print("Message",msg)
      '''
      return HttpResponse("fetched values successfuly!!!")
    else:
        return render(request,'create.html')
      
      
      
def dashboard(request):
    m=Msg.objects.all()
   # print(m)
    context={}
    context['data'] = m
    return render(request,'dashboard.html',context)
    #return HttpResponse("Data fetched from database!!")
    
def delete(request,rid):
    #print("Id to be deleted:",rid)
    #return HttpResponse("Id to be deleted: "+rid)
    m=Msg.objects.filter(id=rid)
    print(m)
    m.delete()
    return redirect('/')
  
  
def edit(request,rid):
    #print("Id To be edited:",rid)
    if request.method=='POST':
        un=request.POST['uname']
        umail=request.POST['uemail']
        umob=request.POST['mobile']
        umsg=request.POST['msg']
        #print(un,"-",umail,"-",umob,"-",umsg)
        m=Msg.objects.filter(id=rid)
        m.update(name=un,email=umail,mobile=umob,msg=umsg)
        return redirect("/")

    else:
        #display form with previous fileds
        #m=Msg.objects.filter(id=rid)
        m=Msg.objects.get(id=rid)
        print(m)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    #return HttpResponse("Id to be edited"+rid)