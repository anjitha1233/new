from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import movie
from . forms import MovieForm

# Create your views here.
def index(request):
    mov=movie.objects.all()
    contest={'movie_list':mov}

    return render(request,'index.html',contest)
def detail(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':mov})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        movie1=movie(name=name,desc=desc,year=year,img=img)
        movie1.save()
        print("saved")
    return render(request,'add.html')
def update(request,id):
    Movie=movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=Movie)
    if form.is_valid():
        form.save()
        return redirect ('/')
    return render(request,'edit.html',{'form':form,'movie':Movie})
def delete(request,id):
    if request.method=='POST':
       Movie=movie.objects.get(id=id)
       Movie.delete()
       return redirect('/')
    return render(request,'delete.html')