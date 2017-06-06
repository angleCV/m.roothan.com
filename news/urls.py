from django.conf.urls import url
from . import views
app_name = 'news'
urlpatterns = [
    url(r"^$", views.index, name="主页"),
    # 2ji_page
    url(r'^safeHot/$', views.safeHot, name='安全热点'),
    url(r'^ManagementPolicy/$', views.ManagementPolicy, name="管理政策"),
    url(r'^SouthernSecurityPerspective/$', views.SouthernSecurityPerspective, name="南方安全视角"),
    url(r'^SafeLaw/$', views.SafeLaw, name="安全法制"),
    url(r'^TalentDevolopment/$', views.TalentDevolopment, name="人才培养"),
    url(r'^AdvancedTechnology/$', views.AdvancedTechnology, name="前沿技术"),
    url(r'^FunScience/$', views.FunScience, name="趣味科普"),
    url(r'^ThemeActivity/$', views.ThemeActivity, name="主题活动"),
    url(r'^HotTopics/$', views.HotTopics, name="热点专题"),
    url(r'^NetSafeLaw/$', views.NetSafeLaw, name="网络安全法"),
    url(r'^PersonInfoProtect/$', views.PersonInfoProtect, name="公民个人信息保护"),
    url(r'^NSAarsenal/$', views.NSAarsenal, name="NSA武器库"),

    # detail
    url(r'^detail/(?P<pk>[0-9]+)/$', views.detail, name='详情页'),
]

