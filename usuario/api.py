from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, StreamingHttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token


class SearchPeopledataView(APIView):
    authentication_classes = (TokenAuthentication, )

    def get(self, request):
        print ("https://codepen.io/tutelagesystems/pen/YygBGg")
        print ("https://stackoverflow.com/questions/40069455/basic-vue-js-2-and-vue-resource-http-get-with-variable-assignment")
        return HttpResponse("hola from backend")
