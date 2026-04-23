from fp_studio import namer


def test_hemlo_actually():
    assert namer.hemlo_actually("pepe") == "hemlo pepe"
