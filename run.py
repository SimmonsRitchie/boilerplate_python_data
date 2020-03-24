import logging
from datetime import datetime
from definitions import DIR_DATA
from logs.config.logging import logs_config
from modules.helper.misc import delete_dir_contents

def main():

    # init logging
    scrape_start_time = datetime.now()
    logs_config()
    logging.info(f'Begin program run: {scrape_start_time}')

    # create or clean up PDF download dir
    if DIR_DATA.is_dir():
        # delete files from previous run
        delete_dir_contents(DIR_DATA)
    else:
        DIR_DATA.mkdir()




if __name__ == '__main__':
    main()