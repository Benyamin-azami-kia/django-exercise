from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from datetime import date
from .models import Post, Author, Comment
from . form import CommentForm


class HomePageView(ListView):
	model=Post
	template_name='blog/index.html'
	context_object_name='posts'
	ordering=["-date"]

	def get_queryset(self):
		return super().get_queryset()[:3]


class PostsView(ListView):
	model=Post
	template_name='blog/post.html'
	context_object_name='posts'
	ordering=["-date"]


class PostDetailView(View):
	def is_stored(self, request, post_id):
		stored_posts=request.session.get("stored_posts")
		if stored_posts is not None:
			is_saved_for_later= post_id in stored_posts
		else:
			is_saved_for_later=False
		return is_saved_for_later


	def get(self, request, slug):
		form=CommentForm()
		identified_post=Post.objects.get(slug=slug)
		tags=identified_post.tag.all()
		
		return render(request,'blog/post_detail.html',{
			"form":form,
			"identified_post":identified_post,
			"post_tag":tags,
			"saved_for_later":self.is_stored(request,identified_post.id)
			})


	def post(self, request, slug):
		form=CommentForm(request.POST)
		identified_post=Post.objects.get(slug=slug)

		if form.is_valid():
			comment=form.save(commit=False)
			comment.post=identified_post
			comment.save()
			return redirect('post_detail', slug=slug)

		tags=identified_post.tag.all()
		return render(request,'blog/post_detail.html',{
			"form":form,
			"identified_post":identified_post,
			"post_tag":tags,
			"saved_for_later":self.is_stored(request,identified_post.id)
			})


class ReadLaterView(View):
	def get(self, request):
		stored_posts=request.session.get("stored_posts")
		context={}
		if stored_posts is None or len(stored_posts)==0 :
			context["posts"]=[]
			context["has_post"]=False
		else:
			context["posts"]=Post.objects.filter(id__in=stored_posts)
			context["has_post"]=True

		return render(request, 'blog/stored_posts.html', context)


	def post(self, request):
		stored_posts=request.session.get("stored_posts")
		if stored_posts is None:
			stored_posts=[]
		post_id=int(request.POST['post_id'])
		if post_id not in stored_posts:
			stored_posts.append(post_id)
		else:
			stored_posts.remove(post_id)
		request.session["stored_posts"]=stored_posts

		return redirect("index")





# class PostDetailView(DetailView):
# 	model=Post
# 	template_name='blog/post_detail.html'
# 	context_object_name='identified_post'


# 	def get_context_data(self, **kwargs):
# 		context=super().get_context_data(**kwargs)
# 		post=self.object
# 		context['post_tag']=post.tag.all()
# 		context['form']=CommentForm
# 		return context