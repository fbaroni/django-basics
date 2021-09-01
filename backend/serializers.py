from django.core.serializers.json import DjangoJSONEncoder
from backend.models import Post

class PostSerializer(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Post):
            return str(obj)
        return super().default(obj)