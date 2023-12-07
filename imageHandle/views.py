from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Screenshot
from datetime import datetime
import base64, re, json


# Create your views here.
def camera_view(request):
    return render(request, 'camera.html')

def view_images(request):
    images = Screenshot.objects.all()
    content = {'images':images}
    return render(request, 'view.html',content)

@csrf_exempt
def save_screenshot(request):
    if request.method == 'POST':
        try:
            screenshot_data = json.loads(request.body)['screenshot']
            # Extract the base64 encoded data from the data URL
            screenshot_data = re.sub('^data:image/.+;base64,', '', screenshot_data)
            screenshot_data = base64.b64decode(screenshot_data)
            
            # Save the screenshot to the database
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot = Screenshot.create(image_data=screenshot_data, timestamp=timestamp)
            
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
        # return JsonResponse({'status': 'success'})