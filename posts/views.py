from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment

# Create your views here.
def browse_recent(request):
    uploads = Post.objects.all()
    public_uploads = Post.objects.filter(private_status=False).all()
    context = {
    "uploads": uploads,
    "public_uploads": public_uploads,
    }
    return render(request, 'posts/browse_recent.html', context)

# Render form for upload
def new_upload(request):
    if (request.method == "POST" and "confirm" in request.POST):
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                submission = post_form.save(commit=False)
                submission.user = request.user
                submission.save()
                post_form.save_m2m()    #save for many-to-many
                return redirect("upload_success")
            else:
                context = {
                "post_form": post_form
                }
                return render(request, 'posts/new_upload.html', context)
    else:
        post_form = PostForm()
        context = {
        "post_form": post_form,
        }
        return render(request, 'posts/new_upload.html', context)

# Called when upload is successful
@login_required(login_url="/login/")
def upload_success(request):
    return render(request, 'posts/upload_success.html')

# Renders user's previous uploads
def user_uploads(request):
    # Don't do anything if the user isn't logged in
    if not request.user.is_authenticated:
        return render(request, 'posts/user_uploads.html')

    if(request.method == "GET"):
        user_uploads = Post.objects.filter(user=request.user).all()
        context = {
        "user_uploads": user_uploads,
        }
        return render(request, 'posts/user_uploads.html', context)

    else:
        return render(request, 'posts/user_uploads.html')

# Class-based view for more detailed look at posts
class PostDetailed(DetailView):
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comment_form'] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            c_user = request.user
            text = comment_form.cleaned_data['comment']
            comment = Comment(user=c_user, post=self.get_object(), text=text)
            comment.save()
        else:
            raise Exception
        return redirect(self.request.path_info)
