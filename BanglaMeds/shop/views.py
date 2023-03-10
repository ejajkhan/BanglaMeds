from django.shortcuts import render
from django.http import HttpResponse
from .models import Medicine,Medtype,Disease



def home(request):
    try:
        medTypes = Medtype.objects.all()

        diseases = Disease.objects.all()
        medicines=[]
        for i in diseases:
            Obj = Medicine.objects.filter(disease=i)
            if len(Obj):
                medicines.append((i.name,Obj))
        print(medTypes)
        params = {'medicines': medicines,'medTypes':medTypes,'diseases':diseases}
        return render(request, 'shop/home.html', params)
    except:
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        params = {'medTypes':medTypes,'diseases':diseases}
        return render(request, 'shop/error.html',params)


def about(request):
    medTypes = Medtype.objects.all()
    diseases = Disease.objects.all()
    params = {'medTypes':medTypes,'diseases':diseases}
    return render(request, 'shop/about.html',params)


def contact(request):
    medTypes = Medtype.objects.all()
    diseases = Disease.objects.all()
    params = {'medTypes':medTypes,'diseases':diseases}
    return render(request, 'shop/contact.html',params)


def medicineView(request):
    try:
        medId = int(request.GET.get('val'))
        medicine = Medicine.objects.get(pk=medId)
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        params = {'medTypes':medTypes,'diseases':diseases,'medicine':medicine}
        return render(request, 'shop/medicineView.html',params)
        
    except:
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        params = {'medTypes':medTypes,'diseases':diseases}
        return render(request,"shop/error.html",params)


def typeView(request):
    try:
        medTypeId = int(request.GET.get('val'))
        typeObj = Medtype.objects.get(id=medTypeId)
        medicines = Medicine.objects.filter(type=typeObj)
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        empty=int(0)
        if len(medicines)==0:
            empty=int(1)
        params = {'empty':empty,'medicines': medicines, 'diseases':diseases,'medTypes':medTypes,'category':typeObj.name}

        return render(request, 'shop/typeView.html', params)
    except:
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        params = {'diseases':diseases,'medTypes':medTypes}
        return render(request,"shop/error.html",params)

def diseaseView(request):
    try:
        diseaseTypeId = int(request.GET.get('val'))
        typeObj = Disease.objects.get(id=diseaseTypeId)
        medicines = Medicine.objects.filter(disease=typeObj)
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        empty=int(0)
        if len(medicines)==0:
            empty=int(1)
        params = {'empty':empty,'medicines': medicines, 'diseases':diseases,'medTypes':medTypes,'category':typeObj.name}

        return render(request, 'shop/diseaseView.html', params)
    except:
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        params = {'diseases':diseases,'medTypes':medTypes}
        return render(request,"shop/error.html",params)


def search(request):
    try:
        medicines= Medicine.objects.all()
        search_key=request.POST
        search_key = search_key.get('search_key', False)
        search_key=list(search_key.split())
        data=[]
        for i in medicines:
             name=str(i.name)
             for j in search_key:
                 if j.lower() in str(name).lower():
                     data.append(i)
                     break
        empty=int(0)
        if len(data)==0:
             empty=int(1)
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        params={'data':data,'empty':empty,'medTypes':medTypes,'diseases':diseases}
        return render(request,"shop/search.html",params)
    except:
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        params = {'diseases':diseases,'medTypes':medTypes}
        return render(request, "shop/error.html", params)



def error(request):
    medTypes = Medtype.objects.all()
    diseases = Disease.objects.all()
    params = {'medTypes':medTypes,'diseases':diseases}
    return render(request, "shop/error.html",params)


def addcart(request):
    try:
        a = request.GET.get('val')
        a=int(a)
        product = Medicine.objects.get(pk=a)
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        params={'medTypes':medTypes,'diseases':diseases,'id':a,'prod':product}
        return render(request, "shop/addcart.html", params)
    except:
        medTypes = Medtype.objects.all()
        diseases = Disease.objects.all()
        params = {'medTypes':medTypes,'diseases':diseases}
        return render(request,"shop/error.html",params)



def confirmBuying(request):
    customer_name=request.POST['customer_name']
    customer_email = request.POST['customer_email']
    customer_mobile = request.POST['customer_mobile']
    customer_address = request.POST['customer_address']
    prod_id = request.POST['prod_id']
    med_quantity = int(request.POST['totalMed'])
    prod = Medicine.objects.get(pk=prod_id)
    total_cost = prod.price*med_quantity
    medTypes = Medtype.objects.all()
    diseases = Disease.objects.all()


    params={'medTypes':medTypes,'diseases':diseases,
            'total_cost':total_cost,'prod':prod,'customer_name':customer_name,
           'customer_email':customer_email,'customer_mobile':customer_mobile,'customer_address':customer_address}
    return render(request,"shop/confirmBuying.html",params)

