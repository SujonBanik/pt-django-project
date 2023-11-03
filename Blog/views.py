from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView

# blog_post = [
#     {
#         'title' : 'ভালো শুরুর পরও বাংলাদেশ ২৫৬',
#         'content' : 'ঊরুর চোটের কারণে ম্যাচটা খেলছেন না সাকিব আল হাসান। তাতে বিশ্বকাপের মঞ্চে বাংলাদেশ দলকে নেতৃত্ব দেওয়ার সুযোগ আসে নাজমুল হোসেনের। পুনের ব্যাটিং স্বর্গে টস ভাগ্য গেছে তাঁর পক্ষেই। কিন্তু আগে ব্যাটিংয়ের সিদ্ধান্ত নেওয়া বাংলাদেশ মহারাষ্ট্র ক্রিকেট অ্যাসোসিয়েশন স্টেডিয়ামের ব্যাটিং কন্ডিশনের সুবিধা কতটা কাজে লাগাতে পারল, সে প্রশ্ন থেকেই যায়।',
#         'author' : 'রয়টার্স',
#         'post_create_date': '19-oct-2023'
#
#     },
#
# {
#         'title' : 'বাবরদের ক্যাচ ছাড়া নিয়ে যা বললেন ক্ষুব্ধ শোয়েব',
#         'content' : 'ঊরুর চোটের কারণে ম্যাচটা খেলছেন না সাকিব আল হাসান। তাতে বিশ্বকাপের মঞ্চে বাংলাদেশ দলকে নেতৃত্ব দেওয়ার সুযোগ আসে নাজমুল হোসেনের। পুনের ব্যাটিং স্বর্গে টস ভাগ্য গেছে তাঁর পক্ষেই। কিন্তু আগে ব্যাটিংয়ের সিদ্ধান্ত নেওয়া বাংলাদেশ মহারাষ্ট্র ক্রিকেট অ্যাসোসিয়েশন স্টেডিয়ামের ব্যাটিং কন্ডিশনের সুবিধা কতটা কাজে লাগাতে পারল, সে প্রশ্ন থেকেই যায়।',
#         'author' : 'Sujon',
#         'post_create_date': '19-oct-2023'
#
#     },
#
# {
#         'title' : 'ভালো শুরুর পরও বাংলাদেশ ২৫৬',
#         'content' : 'পাকিস্তানের বিপক্ষে টস হেরে ব্যাটিং করতে নেমে শুরু থেকেই আগ্রাসী ছিলেন দুই অস্ট্রেলিয়ান ওপেনার ডেভিড ওয়ার্নার ও মিচেল মার্শ। এ দুজন মিলে গড়েন ২৫৯ রানের বিধ্বংসী জুটি। অথচ পঞ্চম ওভারেই ওয়ার্নারকে ফেরাতে পারত পাকিস্তান। কিন্তু শাহিন শাহ আফ্রিদির বলে ১০ রানে থাকা ওয়ার্নারের ক্যাচ ছাড়েন উসামা মির।',
#         'author' : 'Sujon',
#         'post_create_date': '19-oct-2023'
#
#     }
# ]



# def home(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/home.html', {'posts':posts})
    # return HttpResponse("Hello")

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title':'about_page'} )