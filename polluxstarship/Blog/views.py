# from django.shortcuts import render
# from .forms import Blogforms
# # Create your views here.
#
# def blog_detail_view(request):
#     return render(request, 'article_detail.html',{})
#
#
# def blog_list_view(request):
#     return render(request, 'article_list.html',{})
#
# def blog_create_view(request):
#     form = Blogforms(request.POST or None)
#     if form.is_valid():
#         form.save()
#     context = {
#         'form':form,
#     }
#     return render(request, 'article_create.html', context)
#
