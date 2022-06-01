from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django import forms
from django.shortcuts import redirect
from django.contrib.auth.models import User

from .models import Blog, Comment


class BlogView(ListView):
    model = Blog
    template_name = 'blog/blog.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        blog = Blog.objects.all()
        for article in blog:
            article.image = article.image.name
            article.extra_image = article.extra_image.name
        context = {
            'blog': blog
        }
        return context


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=500, widget=forms.Textarea)


class ArticleDetailView(DetailView):
    model = Blog
    template_name = 'blog/article.html'

    def get_context_data(self, **kwargs):
        article = kwargs['object']
        comments = Comment.objects.filter(article=article)
        context = {
            'article': article,
            'comments': comments,
            'form': CommentForm()
        }
        return context


class ArticleFormView(SingleObjectMixin, FormView):
    model = Blog
    template_name = 'blog/article.html'
    form_class = CommentForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('users:dashboard'))
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            new_comment = Comment.objects.create(
                user=User.objects.get(id=request.user.id),
                article=self.object,
                text=form['comment'].value())
            new_comment.save()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('blog:article', kwargs={'pk': self.object.pk})


class ArticleView(View):

    def get(self, request, *args, **kwargs):
        view = ArticleDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ArticleFormView.as_view()
        return view(request, *args, **kwargs)
