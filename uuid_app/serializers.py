from django.core.serializers.json import Serializer as CoreSerializer
from django.utils.encoding import smart_text

class Serializer(CoreSerializer):
    def get_dump_object(self, obj):
		
        self._current['id'] = smart_text(obj._get_pk_val(), strings_only=True)
        return self._current