from asyncio.log import logger
from etl_anime import etl
from anime_scraper import extract
import logging
logging.basicConfig(level=logging.INFO)


def main():
    logger.info("Iniciando..")
    extract()
    logger.info("Scraper end")
    etl()
    logger.info("ETL realizando con exito")




if __name__ == "__main__":
    main()

