import json

from django.utils.encoding import force_str
from django.utils.functional import Promise


class LazyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Promise):
            return force_str(obj)
        return super(LazyEncoder, self).default(obj)


def json_dumps(data):
    return json.dumps(data, cls=LazyEncoder)
