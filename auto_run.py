import logging
import logging.config

if __name__ == '__main__':
    # Ignore logs from other files and libs
    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': True,
    })
    # Create new logger
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler("./output.txt"),
            logging.StreamHandler()
        ]
    )

    logging.info("Ran App!")
