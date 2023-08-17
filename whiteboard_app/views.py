from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .models import Whiteboard, DrawingAction
from .serializers import WhiteboardSerializer, DrawingActionSerializer
from whiteboard_app.models import CustomUser
from .forms import CustomUserCreationForm


# Register user view
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
# Whiteboard list view
@login_required(login_url='login')  # Apply the login_required decorator
def whiteboard_list(request):
    whiteboards = Whiteboard.objects.filter(owner=request.user)
    # return HttpResponse("Hello")
    return render(request, 'whiteboard_list.html', {'whiteboards': whiteboards})

# Whiteboard detail view
@login_required(login_url='login')  # Apply the login_required decorator
def whiteboard_detail(request, whiteboard_id):
    whiteboard = Whiteboard.objects.get(id=whiteboard_id, owner=request.user)
    actions = DrawingAction.objects.filter(whiteboard=whiteboard)
    return render(request, 'whiteboard_detail.html', {'whiteboard': whiteboard, 'actions': actions})
# API endpoints
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_whiteboard(request):
    name = request.data.get('name')
    whiteboard = Whiteboard.objects.create(owner=request.user, name=name)
    return Response(WhiteboardSerializer(whiteboard).data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_whiteboard_actions(request, whiteboard_id):
    actions = DrawingAction.objects.filter(whiteboard_id=whiteboard_id)
    serializer = DrawingActionSerializer(actions, many=True)
    return Response(serializer.data)
