import requests
from bs4 import BeautifulSoup

def obtener_noticias():
    url = "https://news.google.com/rss"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "xml")
        noticias = soup.find_all("item", limit=5)
        
        print("\n===========================")
        print("       DIARIO DIGITAL")
        print("===========================\n")
        
        for i, noticia in enumerate(noticias, 1):
            titulo = noticia.title.text
            link = noticia.link.text
            fecha = noticia.pubDate.text
            
            print(f"{i}. {titulo}")
            print(f"   Fecha: {fecha}")
            print(f"   Leer más: {link}\n")
    else:
        print("No se pudo obtener las noticias. Inténtalo más tarde.")

if __name__ == "__main__":
    obtener_noticias()
