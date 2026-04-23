from pta_shared.utils import jenkins


def ojoj():
    return jenkins.JenkinsBuild(id="ojoj")


def hemlo_actually(name: str) -> str:
    return f"hemlo {name}"
