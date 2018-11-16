from bzt.cli import CLI
import logging
import traceback

class Options:
    "creating an arbitrary class for the bzt options"
    def __init__(self, *args, **kwargs):
        self.__dict__.update(kwargs)


def main(configs):
    """
    starting point
    """

    options = Options() # command line arguments which are usually passed to `bzt`
    
    # hard defaults below
    options.log = None 
    options.option = None
    options.quiet = None
    options.verbose = None
    options.no_system_configs = None
    options.aliases = []

    # configs = [] # list which contains bzt config files 

    executor = CLI(options)

    try:
        code = executor.perform(configs)
    except BaseException as exc_top:
        logging.error("%s: %s", type(exc_top).__name__, exc_top)
        logging.debug("Exception: %s", traceback.format_exc())
        code = 1

    exit(code)


if __name__ == "__main__":
    configs = ['path/to/config'] # list which contains bzt config files
    main(configs)
