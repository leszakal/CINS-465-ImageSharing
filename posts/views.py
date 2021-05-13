from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin #for generic views
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from posts.forms import PostForm, CommentForm
from posts.models import Post, Comment
from django.urls import reverse

# Create your views here.
def browse_recent(request):
    user = request.user
    if user.is_authenticated:
        uploads = Post.objects.all()
    else:
        uploads = Post.objects.filter(private_status=False).all()
    context = {
    "uploads": uploads,
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
                return redirect("/user_uploads/")
            else:
                context = {
                "post_form":post_form
                }
                return render(request, 'posts/new_upload.html', context)
    else:
        post_form = PostForm()
        context = {
        "post_form":post_form,
        }
        return render(request, 'posts/new_upload.html', context)

# Renders user's previous uploads
def user_uploads(request):
    # Don't do anything if the user isn't logged in
    if not request.user.is_authenticated:
        return render(request, 'posts/user_uploads.html')

    if(request.method == "GET"):
        user_uploads = Post.objects.filter(user=request.user).all()
        context = {
        "user_uploads":user_uploads,
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

class PostUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Post
    fields = ['title', 'description', 'tags', 'private_status']
    template_name_suffix = '_update'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse('post_detailed', kwargs={'pk':pk})

@login_required(login_url="/login/")
def delete_post(request, post_id=None):
    if (request.method == 'POST'):
        post = Post.objects.get(id=post_id)
        post.delete()
        return render(request, 'posts/delete_success.html')
    else:
        return redirect('/user_uploads/')

@login_required(login_url="/login/")
def delete_comment(request, post_id=None, comment_id=None):
    pk = int(post_id)
    if (request.method == 'GET' and 'delcom' in request.GET):
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return redirect('post_detailed', pk=pk)
    else:
        return redirect('post_detailed', pk=pk)
