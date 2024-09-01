from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImagePromptForm
from .models import ImageRequest
from .image_utils import generate_image 
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ImagePromptForm

def home(request):
    generatedimages=ImageRequest.objects.all()
    data={
        'images':generatedimages,
    }
    return render(request, 'pixora/home.html',data)

def generate_image_view(request):
    if request.method == 'POST':
        form = ImagePromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            generated_image = ImageRequest.objects.create(prompt=prompt, status='processing')
            img_id=generated_image.id
            try:
                image_path = generate_image(prompt,img_id)
                generated_image.image = image_path
                generated_image.status = 'completed'
                if request.user.is_authenticated:
                    generated_image.user=request.user
                generated_image.save()
                return redirect('home')

            except Exception as e:
                generated_image.status = f'failed: {str(e)}'
                generated_image.save()
                return HttpResponse(f"Error generating image: {str(e)}")
    else:
        form = ImagePromptForm()

    return render(request, 'pixora/generate_image.html', {'form': form})






