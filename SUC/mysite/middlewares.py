from django.shortcuts import HttpResponse,render


class UnderConstructuionMiddleware:
    def __init__(self, get_response):
        self.get_respponse = get_response

    def __call__(self, re):
        print("Call From Middleware Before view")
        response = render(re , 'mysite/site.html')
        print("Call From Middleware after view")
        return response