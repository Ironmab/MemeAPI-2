from django.shortcuts import render
from .models import Meme 
import requests
# Create your views here.
def get_meme(request):
    url = 'https://api.imgflip.com/get_memes'
    response = requests.get(url)
    data = response.json() 
    memes = data['data']['memes']
    for i in memes:
        meme_data = Meme(
            slugid = i['id'],
            name = i['name'],
            url = i['url'],
            width = i['width'],
            height = i['height'],
            box_count = i['box_count']
        )
        meme_data.save()
        all_meme = Meme.objects.all().order_by('id')[0:10]
    return render(request,'home.html',{'all_meme':all_meme})

