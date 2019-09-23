from .models import Picture
from .models import Image
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def pictures(request, id):
    print("=======")
    context = {'images': Image.objects.filter(owner=request.user)}
    print("+++++")
    print(id)
    if id == "":
        print("At Pictures home")
    else:
        context['image'] = Image.objects.get(uuid=id)
        # assert False
    print("+++++")
    print(context)
    return render(request, 'images.html', context)


def xpictures(request, id):
    print("=======")
    context = {'pictures': Picture.objects.filter(owner=request.user)}
    print("+++++")
    print(id)
    if id == "":
        print("At Pictures home")
    else:
        context['picture'] = Picture.objects.get(id=id)
        # assert False
    print("+++++")
    print(context)
    return render(request, 'pictures.html', context)
