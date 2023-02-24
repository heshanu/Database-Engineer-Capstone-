from django.shortcuts import render
from django.http import HttpResponse
from .models import Menu,MenuItem,Cart,Order,OrderItem
from rest_framework.decorators import api_view,permission_classes,throttle_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.throttling import AnonRateThrottle
from rest_framework.throttling import UserRateThrottle
from .throttles import TenCallsPerMinute

# Create your views here.
def home(request):
   # html = "<html><body>It is now %s.</body></html>" % now
    return render(request,'i.html')

def menu(request):
    menu_data = Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})


@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return HttpResponse({"message":"Some secret message"})

@api_view()
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name="Manager").exists():
        return Response({'message':'Only Manager should See this'})
    else:
        return Response({'message':'You are not authorized!'},403)

@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return HttpResponse({"message":"successful"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def managers(request):
    username=request.data['username']
    if username:
        user=get_object_or_404(User,username=username)
        managers=Group.objects.get(name="Manager")
        if request.method=="POST":
            managers.user_set.add(user)
        elif request.method=='DELETE':
            managers.user_set.remove(user)
        return Response({'Message':'OK'})
    return Response({"message":"error"},status.HTTP_400_BAD_REQUEST)   