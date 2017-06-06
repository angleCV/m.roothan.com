from django.http import HttpResponseRedirect

from minicms.settings import MOBILE_USERAGENTS, MB_FLAG



class MobileTemplate(object):

    """
    If a mobile user agent is detected, inspect the default args for the view
    func, and if a template name is found assume it is the template arg and
    attempt to load a mobile template based on the original template name.
    """

    def process_view(self, request, view_func, view_args, view_kwargs):
        global MOBILE_USERAGENTS
        if any(ua for ua in MOBILE_USERAGENTS if ua in
                request.META["HTTP_USER_AGENT"]) or \
                        request.META["PROCESSOR_IDENTIFIER"] in \
                        ["Intel64 Family 6 Model 58 Stepping 9, GenuineIntel"]:
            return view_func(request, *view_args, **view_kwargs)
        else:
            return HttpResponseRedirect("http://roothan.com")




import sys
from django.views.debug import technical_500_response
from django.conf import settings


class UserBasedExceptionMiddleware(object):
    def process_exception(self, request, exception):
        if request.user.is_superuser or request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS:
            return technical_500_response(request, *sys.exc_info())

'''
    def process_view(self, request, view_func, view_args, view_kwargs):
        if any(ua for ua in MOBILE_USERAGENTS if ua in
                request.META["HTTP_USER_AGENT"]):
            return view_func(request, *view_args, **view_kwargs) ## 手机端不做处理——3g.roothan.com
        else:
            return HttpResponseRedirect("http://roothan.com") ## PC访问的话重定向
'''

