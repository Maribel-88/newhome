from django.shortcuts import render
# Create your views here.
def get_apartment_list(request):
    return render(request, 'apartments/apartment_list.html')
