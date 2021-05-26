from django.db.models.fields import UUIDField
from django.shortcuts import render
import uuid, json
from uuid_app.models import UUIDTABLE
from django.http import JsonResponse
from django.core import serializers
from django.core.serializers import BUILTIN_SERIALIZERS

BUILTIN_SERIALIZERS['json'] = 'uuid_app.serializers'

def main(request):
	return JsonResponse({"status": "success", "payload": "welcome!"}, status=200)

def generate_uuid(request):
	gen = UUIDTABLE.objects.create(uuid_id=uuid.uuid4())
	queryset = UUIDTABLE.objects.all()
	data = serializers.serialize('json', queryset)
	return JsonResponse({"status": "success", "payload": json.loads(data)}, status=201)