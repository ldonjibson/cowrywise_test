import uuid
from django.db import models
  
class UUIDTABLE(models.Model):
	uuid_id = models.UUIDField()
	created_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.uuid

	class Meta:
		ordering = ['-created_at']