from django.shortcuts import render

from .models import *
from .utils import set_page2, set_cates, set_sliders, set_home_infos


def index(request):
    return render(request, "index_base.html", {
        "cates": set_cates(),
        "sliders": set_sliders(),
        "postss": set_home_infos(),
    })


def detail(request, pk):
    gaim = Article.objects.get(id=str(pk))
    cate = gaim.categary
    others_all = Article.objects.filter(categary=cate)
    return render(request, "detail.html", {
        "gaim": gaim,
        "other_posts": others_all[:5],
        # need url and category;
        "cate": cate,
    })


def meta_page_def(request, num):
    return render(request, "page_detail.html", {
        "posts": set_page2(num)[0],
        "cate": set_page2(num)[1],
        "sliders": set_sliders(),
        "cates": set_cates(),
    })

'''
def make_funcs(request, num):
    def set_page():
        return meta_page_def(request, num)
    return set_page
safeHot, ManagementPolicy, SouthernSecurityPerspective, SafeLaw, TalentDevolopment, AdvancedTechnology,FunScience, ThemeActivity, HotTopics, NetSafeLaw,  PersonInfoProtect, NSAarsenal = tuple([make_funcs(request="111", num=i+1) for i in range(12)])
'''


def safeHot(request):
    return meta_page_def(request, 1)

def ManagementPolicy(request):
    return meta_page_def(request, 2)

def SouthernSecurityPerspective(request):
    return meta_page_def(request, 3)

def SafeLaw(request):
    return meta_page_def(request, 4)

def TalentDevolopment(request):
    return meta_page_def(request, 5)

def AdvancedTechnology(request):
    return meta_page_def(request, 6)

def FunScience(request):
    return meta_page_def(request, 7)

def ThemeActivity(request):
    return meta_page_def(request, 8)

def HotTopics(request):
    return meta_page_def(request, 9)

def NetSafeLaw(request):
    return meta_page_def(request, 10)

def PersonInfoProtect(request):
    return meta_page_def(request, 11)

def NSAarsenal(request):
    return meta_page_def(request, 12)
