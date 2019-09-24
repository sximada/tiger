import json

from rest_framework.views import APIView 
from rest_framework.response import Response


class PingPoingAPIView(APIView):
    def get(self, request):
        return Response(data="OK")


class BalanceAPIView(APIView):
    def get(self, request):
        return Response(data={
	    "labels": ['January', 'February', 'March', 'April', 'May', 'June', 'July'],
	    "datasets": [{
		"label": 'LALEL A',
		"data": [1,2,3,4,5,6,7]
	    }, {
		"label": 'LABEL B',
		"data": [-1,-2,-3,-4,-5,-6,-7]
	    }]
        })


