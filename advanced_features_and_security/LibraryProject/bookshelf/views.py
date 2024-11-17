from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Post
from django.http import HttpResponseForbidden

# View to create a post
@permission_required('app_name.can_create', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        # Create a new post logic here
        pass
    return render(request, 'create_post.html')

# View to edit a post
@permission_required('app_name.can_edit', raise_exception=True)
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        # Edit the post logic here
        pass
    return render(request, 'edit_post.html', {'post': post})

# View to delete a post
@permission_required('app_name.can_delete', raise_exception=True)
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
    return render(request, 'delete_post.html', {'post': post})