from pta_shared.utils.jenkins import JenkinsBuild


def format_greeting(build: JenkinsBuild) -> str:
    return f"Hello from pta-consumer! id={build.id!r}"

