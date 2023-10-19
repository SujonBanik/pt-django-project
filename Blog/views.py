from django.http import HttpResponse
from django.shortcuts import render

blog_post = [
    {
        'title' : 'ভালো শুরুর পরও বাংলাদেশ ২৫৬',
        'content' : 'ঊরুর চোটের কারণে ম্যাচটা খেলছেন না সাকিব আল হাসান। তাতে বিশ্বকাপের মঞ্চে বাংলাদেশ দলকে নেতৃত্ব দেওয়ার সুযোগ আসে নাজমুল হোসেনের। পুনের ব্যাটিং স্বর্গে টস ভাগ্য গেছে তাঁর পক্ষেই। কিন্তু আগে ব্যাটিংয়ের সিদ্ধান্ত নেওয়া বাংলাদেশ মহারাষ্ট্র ক্রিকেট অ্যাসোসিয়েশন স্টেডিয়ামের ব্যাটিং কন্ডিশনের সুবিধা কতটা কাজে লাগাতে পারল, সে প্রশ্ন থেকেই যায়।',
        'auther' : 'sujon',
        'post_create_date': 'রয়টার্স'



    }
]

def home(request):
    return render(request, 'blog/home.html', {'blog_post':blog_post})
    # return HttpResponse("Hello")

def about(request):
    return render(request, 'blog/about.html', {'title':'about_page'} )