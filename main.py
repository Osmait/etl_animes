from etl_anime import etl
from anime_scraper import extract


def main():
    print("Iniciando..")
    extract()
    print("Scraper end")
    etl()
    print("ETL realizando con exito")




if __name__ == "__main__":
    main()

