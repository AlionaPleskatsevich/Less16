import uuid

VALID_USERS = [{
    "name": "Aliona",
    "email": f"{uuid.uuid4().hex[:8]}@mail.com"
}, {
    "name": "Alla",
    "email": f"{uuid.uuid4().hex[:8]}@mail.com"
}
]


INVALID_USERS = [{
    "name": "",
    "email": f"{uuid.uuid4().hex[:8]}@mail.com"
}, {
    "name": "",
    "email": f"{uuid.uuid4().hex[:8]}@mail.com"
}]
