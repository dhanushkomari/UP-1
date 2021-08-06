from simpleApp.models import Achievement
from django.shortcuts import render
from django.http import HttpResponse
from .forms import AchievementForm

# from .forms import PersonForm


# Create your views here.
# def form(request):
#     if request.method == "POST":
#         form = PersonForm(request.POST)
#         if form.is_valid():
#             print(form.data)
#             form.save()

#             return HttpResponse('form is saved into db')

#     else:
#         form  = PersonForm
#     return render(request, 'simpleApp/form.html', {'form':form})


def test(request):
    if request.method == "POST":
        print('post method activated')
        form = AchievementForm(request.POST)
        # print(form)
        # form.save()
        if form.is_valid():
            # print(form.data)
            form.save()
            return HttpResponse('form is saved into db')
        else:
            print('form not valid')
    else:
        print('else is executed')
        form = AchievementForm
    
    # return render(request, 'simpleApp/index.html')
    return render(request, 'simpleApp/12.html', {'form':form})