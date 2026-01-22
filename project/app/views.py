from django.shortcuts import render

# Create your views here.
def my_render(req):
    x = 10
    y = 'php'
    z = [1,2,3,4,5]
    return render(req,'index.html',{'p':x,'q':y,'r':z})
