import json
import uuid

from rentomatic.serializers import room_json_serializer as ser
from rentomatic.domain import room as r


def test_serialize_domain_room():
    code = uuid.uuid4()
    room = r.Room(code, size=200, price=10, longitude=-0.099, latitude=51.4234)
    expected_json = """
        {{
        "code": "{}",
        "size": 200,
        "price": 10,
        "longitude": -0.099,
        "latitude": 51.4234
        }}
    """.format(code)
    json_room = json.dumps(room, cls=ser.RoomJsonEncoder)
    assert json.loads(json_room) == json.loads(expected_json)
