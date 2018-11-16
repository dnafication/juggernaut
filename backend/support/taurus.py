from bzt import cli
import logging
import traceback


def main():
    """
    This function is used as entrypoint by setuptools
    """
    parser = cli.get_option_parser()

    parsed_options, parsed_configs = parser.parse_args()

    print("--------------", parsed_options, parsed_configs)

    parsed_configs = ['simple-test.yml']

    executor = cli.CLI(parsed_options)

    try:
        code = executor.perform(parsed_configs)
    except BaseException as exc_top:
        logging.error("%s: %s", type(exc_top).__name__, exc_top)
        logging.debug("Exception: %s", traceback.format_exc())
        code = 1

    exit(code)


if __name__ == "__main__":
    main()
