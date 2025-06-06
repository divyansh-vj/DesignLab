from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404,render, redirect
from .models import ChatMessage
import json
from django.core.files.base import ContentFile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ChatMessageSerializer
from django.conf import settings
import urllib.parse

chat_name = ""

class ChatMessageListCreateView(APIView):
    def get(self, request):
        """Fetch paginated chat messages"""
        page = int(request.GET.get("page", 1))
        messages = ChatMessage.objects.all().order_by("-created_at")[(page-1)*5: page*5]
        serializer = ChatMessageSerializer(messages, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Send a new chat message"""
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .models import ChatMessage

@csrf_exempt
def chat_messages(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode("utf-8")) 
            title = data.get("title", "").strip()
            description = data.get("description", "").strip()
            location = data.get("location", "").strip()

            if not title or not description or not location:
                return JsonResponse({"error": "All fields are required"}, status=400)

            new_message = ChatMessage.objects.create(title=title, description=description, location=location)

            return JsonResponse({
                "title": new_message.title,
                "description": new_message.description,
                "location": new_message.location,
                "created_at": new_message.created_at.strftime("%Y-%m-%d %H:%M:%S")
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format"}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)

@csrf_exempt
def upload_image(request):
    if request.method == "POST" and request.FILES.get("image"):
        image_file = request.FILES["image"]
        
        file_path = f"chat_images/{image_file.name}"
        saved_path = default_storage.save(file_path, ContentFile(image_file.read()))

        # Generate proper media URL
        image_url = settings.MEDIA_URL + saved_path

        
        encoded_url = urllib.parse.quote(image_url, safe='/:')

        return JsonResponse({"image_url": encoded_url})

    return JsonResponse({"error": "Invalid request"}, status=400)

def chat_widget(request):
    # print(f"--- chat_widget view: Retrieving session 'user_name'. Value: {request.session.get('user_name', 'DefaultValueCheck')} ---") # DEBUG
    user_name_value = request.session.get('user_name', 'Anonymous')
    messages = ChatMessage.objects.order_by('-created_at')[:10][::-1]

    context = {
        'messages': messages,
        'user_name': user_name_value  # <-- Ensure this key is exactly 'user_name'
    }

    # --- Add this print statement ---
    # print(f"--- chat_widget view: Context being passed to template: {context} ---")
    # --------------------------------

    return render(request, 'chat_widget.html', context)

    




def chat_name(request):
    if request.method == "POST":
        print("--- chat_name view: POST request received ---")

        # --- Add this line to print the raw POST data ---
        print(f"--- Raw request.POST data: {request.POST} ---")
        # -------------------------------------------------

        name = request.POST.get('userName', '').strip()
        # Optional: Print the retrieved value explicitly
        print(f"--- Value retrieved for 'userName': '{name}' ---")

        request.session['user_name'] = name if name else "Anonymous"
        print(f"--- Session 'user_name' set to: {request.session['user_name']} ---")
        print(f"--- Redirecting to chat_widget for user: {request.session['user_name']} ---")
        return redirect('chat_widget')
    else:
         print("--- chat_name view: GET request received ---")
         return render(request, 'chat_name.html')

