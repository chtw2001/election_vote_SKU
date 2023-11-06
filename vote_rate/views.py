from django.shortcuts import render
from vote_rate.models import Candidate
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from vote_rate.serializers import CandidateSerializer
from rest_framework.generics import get_object_or_404

def test(request, name):
    candidate = Candidate.objects.get(name=name)
    return HttpResponse(candidate.name)

@api_view(['GET'])
def CandidateAPI(request, name):
    candidate = get_object_or_404(Candidate, name=name)
    serializer = CandidateSerializer(candidate)
    
    return Response(serializer.data, status=status.HTTP_200_OK)