from solution import build_response


def test_defaults():
    assert build_response() == {"status": 200, "ok": True, "message": "OK", "data": {}}


def test_created_and_not_found():
    r = build_response({"id": 1}, 201)
    assert r["message"] == "Created" and r["ok"] is True and r["data"] == {"id": 1}
    r2 = build_response(status=404)
    assert r2["ok"] is False and r2["message"] == "Not Found"


def test_custom_message():
    assert build_response(status=500, message="boom")["message"] == "boom"


def test_no_shared_default_dict():
    r1 = build_response()
    r1["data"]["x"] = 1
    assert build_response()["data"] == {}
