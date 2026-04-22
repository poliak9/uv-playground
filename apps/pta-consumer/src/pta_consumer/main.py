from pta_shared.utils import jenkins

from pta_consumer.formatter import format_greeting


def main():
    build = jenkins.get_build("hemlo")
    print(format_greeting(build))


if __name__ == "__main__":
    main()

