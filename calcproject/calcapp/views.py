from django.shortcuts import render
def indexf(request):
    return render(request,'index.html')
# Create your views here.
def operationf(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    sum=x+y
    return render((request,'result.html',{'Sum':sum}))
def operationf(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    difference=x-y
    return render((request,'result.html',{'Difference':difference}))
def operationf(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    product=x+y
    return render((request,'result.html',{'Product':product}))
def operationf(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    quotient=x+y
    return render((request,'result.html',{'Quotient':quotient}))
    # return render(request,'result.html',{'Sum':sum,'Difference':difference,'Product':product,'Quotient':quotient})