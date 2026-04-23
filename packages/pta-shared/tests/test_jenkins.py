from pta_shared.utils.jenkins import JenkinsBuild, get_build


def test_get_build_returns_model():
    build = get_build("abc")
    assert isinstance(build, JenkinsBuild)
    assert build.id == "abc"
