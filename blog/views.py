from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404,redirect,render
from .forms import CommentForm,PostForm,RegisterForm
from .models import Post,Tag
def home(request):
    qs=Post.objects.filter(published=True).select_related('author').prefetch_related('tags'); q=request.GET.get('q','').strip(); tag=request.GET.get('tag','').strip()
    if q:qs=qs.filter(Q(title__icontains=q)|Q(excerpt__icontains=q)|Q(content__icontains=q)|Q(tags__name__icontains=q)).distinct()
    if tag:qs=qs.filter(tags__slug=tag)
    page=Paginator(qs,5).get_page(request.GET.get('page')); return render(request,'blog/home.html',{'page':page,'q':q,'tag':tag,'tags':Tag.objects.all()})
def post_detail(request,slug):
    post=get_object_or_404(Post.objects.select_related('author').prefetch_related('tags'),slug=slug,published=True); comments=post.comments.filter(approved=True).select_related('author'); form=CommentForm()
    if request.method=='POST':
        if not request.user.is_authenticated:return redirect('login')
        form=CommentForm(request.POST)
        if form.is_valid():c=form.save(commit=False);c.post=post;c.author=request.user;c.save();messages.success(request,'Comment submitted for moderation.');return redirect(post.get_absolute_url())
    return render(request,'blog/post_detail.html',{'post':post,'comments':comments,'form':form})
@login_required
def post_create(request):
    form=PostForm(request.POST or None)
    if form.is_valid():p=form.save(commit=False);p.author=request.user;p.save();form.save_m2m();messages.success(request,'Post published.');return redirect(p.get_absolute_url())
    return render(request,'blog/post_form.html',{'form':form,'heading':'Write a post'})
@login_required
def post_edit(request,slug):
    post=get_object_or_404(Post,slug=slug,author=request.user);form=PostForm(request.POST or None,instance=post)
    if form.is_valid():form.save();messages.success(request,'Post updated.');return redirect(post.get_absolute_url())
    return render(request,'blog/post_form.html',{'form':form,'heading':'Edit post'})
def register(request):
    if request.user.is_authenticated:return redirect('home')
    form=RegisterForm(request.POST or None)
    if form.is_valid():user=form.save();login(request,user);messages.success(request,'Welcome! Your account is ready.');return redirect('home')
    return render(request,'registration/register.html',{'form':form})
