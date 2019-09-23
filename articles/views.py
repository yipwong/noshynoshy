from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.shortcuts import redirect


@login_required
def articles(request, id):
    # context = {'article_list': Article.objects.all()}
    # context = {'article_list': Article.objects.filter(owner="test")}
    context = {'article_list': Article.objects.filter(owner=request.user)}
    print("+++++")
    print(id)
    if id == "":
        print("At Articles home")
    else:
        context['article'] = Article.objects.get(id=id)
        # assert False
    print("+++++")
    print(context)
    return render(request, 'articles.html', context)


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = request.user
            post.save()
            # return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            # return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form, 'art_id': pk})
