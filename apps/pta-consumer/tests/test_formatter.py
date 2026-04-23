from pta_shared.utils.jenkins import JenkinsBuild

from pta_consumer.formatter import format_greeting


def test_format_greeting():
    build = JenkinsBuild(id="xyz")
    assert format_greeting(build) == "Hello from pta-consumer! id='xyz'"
