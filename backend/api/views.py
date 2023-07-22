from django.http import JsonResponse


def api_home (request, *args,**kwargs):
    body=request.body

    print(body)
    return JsonResponse( {"message":" hi there, this is your django api response"})
