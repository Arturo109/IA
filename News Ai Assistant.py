import requests
import json
import tkinter as tk
from tkinter import scrolledtext

def get_latest_news():
    url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=6f916868de07b79f7422e1f906fda226"
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        return [f"{article['title']} - {article['source']['name']}\n{article['url']}\n" for article in news_data["articles"]]
    else:
        return ["Error al obtener noticias"]

    # Ejemplo de uso
for news in get_latest_news():
    print(news)

def get_latest_movies(): 
    api_key = "6f916868de07b79f7422e1f906fda226"
    base_url = "https://api.themoviedb.org/3"
    movie_base_url = "https://www.themoviedb.org/movie"
    
    endpoints = {
        "latest": f"{base_url}/movie/now_playing?api_key={api_key}",
        "dc": f"{base_url}/search/movie?api_key={api_key}&query=DC",
        "marvel": f"{base_url}/search/movie?api_key={api_key}&query=Marvel",
        "dune": f"{base_url}/search/movie?api_key={api_key}&query=Dune",
        "ladybug": f"{base_url}/search/movie?api_key={api_key}&query=Miraculous Ladybug"
    }
    
    results = []
    
    for category, url in endpoints.items():
        response = requests.get(url)
        if response.status_code == 200:
            movie_data = response.json()
            results.extend([
                f"{movie['title']} - Estreno: {movie['release_date']} - Link: {movie_base_url}/{movie['id']}"
                for movie in movie_data.get("results", [])[:5]
            ])
        else:
            results.append(f"Error al obtener películas de {category}")
    
    return results


def get_latest_tv_shows(): 
    api_key = "6f916868de07b79f7422e1f906fda226"
    base_url = "https://api.themoviedb.org/3"
    tv_base_url = "https://www.themoviedb.org/tv"
    
    endpoints = {
        "latest": f"{base_url}/tv/on_the_air?api_key={api_key}",
        "dc": f"{base_url}/search/tv?api_key={api_key}&query=DC",
        "marvel": f"{base_url}/search/tv?api_key={api_key}&query=Marvel",
        "dune": f"{base_url}/search/tv?api_key={api_key}&query=Dune: La Profecía",
        "ladybug": f"{base_url}/search/tv?api_key={api_key}&query=Miraculous Ladybug"
    }
    
    results = []
    
    for category, url in endpoints.items():
        response = requests.get(url)
        if response.status_code == 200:
            tv_data = response.json()
            results.extend([
                f"{show['name']} - Estreno: {show['first_air_date']} - Link: {tv_base_url}/{show['id']}"
                for show in tv_data.get("results", [])[:5]
            ])
        else:
            results.append(f"Error al obtener series de {category}")
    
    return results


def get_horoscope(sign):
    url = f"https://aztro.sameerkumar.website/?sign={sign}&day=today"
    response = requests.post(url)
    if response.status_code == 200:
        horoscope_data = response.json()
        return horoscope_data["description"]
    else:
        return "Error al obtener horóscopo"

def analyze_symptoms(symptoms):
    known_illnesses = {
        "fiebre, tos, fatiga": "Posible gripe o COVID-19",
        "dolor de cabeza, mareo": "Posible migraña o presión baja",
        "picazón, estornudos": "Posible alergia"
    }
    return known_illnesses.get(symptoms.lower(), "Síntomas no reconocidos, consulta con un médico")

def update_news():
    news_text.config(state=tk.NORMAL)
    news_text.delete(1.0, tk.END)
    news_text.insert(tk.END, "\n".join(get_latest_news()))
    news_text.config(state=tk.DISABLED)

def update_movies():
    movie_text.config(state=tk.NORMAL)
    movie_text.delete(1.0, tk.END)
    movie_text.insert(tk.END, "\n".join(get_latest_movies()))
    movie_text.config(state=tk.DISABLED)

def update_tv():
    tv_text.config(state=tk.NORMAL)
    tv_text.delete(1.0, tk.END)
    tv_text.insert(tk.END, "\n".join(get_latest_tv_shows()))
    tv_text.config(state=tk.DISABLED)

def check_health():
    symptoms = symptom_entry.get()
    result = analyze_symptoms(symptoms)
    health_result.config(text=result)

def show_horoscope():
    sign = horoscope_entry.get()
    result = get_horoscope(sign)
    horoscope_result.config(text=result)

# Interfaz gráfica
root = tk.Tk()
root.title("IA de Noticias, Salud y Calculadora")

news_label = tk.Label(root, text="Últimas Noticias")
news_label.pack()
news_text = scrolledtext.ScrolledText(root, height=10, width=80, state=tk.DISABLED)
news_text.pack()
news_button = tk.Button(root, text="Actualizar Noticias", command=update_news)
news_button.pack()

movie_label = tk.Label(root, text="Últimas Películas")
movie_label.pack()
movie_text = scrolledtext.ScrolledText(root, height=10, width=80, state=tk.DISABLED)
movie_text.pack()
movie_button = tk.Button(root, text="Actualizar Películas", command=update_movies)
movie_button.pack()

tv_label = tk.Label(root, text="Últimas Series")
tv_label.pack()
tv_text = scrolledtext.ScrolledText(root, height=10, width=80, state=tk.DISABLED)
tv_text.pack()
tv_button = tk.Button(root, text="Actualizar Series", command=update_tv)
tv_button.pack()

health_label = tk.Label(root, text="Ingrese sus síntomas:")
health_label.pack()
symptom_entry = tk.Entry(root, width=50)
symptom_entry.pack()
health_button = tk.Button(root, text="Analizar Salud", command=check_health)
health_button.pack()
health_result = tk.Label(root, text="")
health_result.pack()

horoscope_label = tk.Label(root, text="Ingrese su signo zodiacal:")
horoscope_label.pack()
horoscope_entry = tk.Entry(root, width=20)
horoscope_entry.pack()
horoscope_button = tk.Button(root, text="Obtener Horóscopo", command=show_horoscope)
horoscope_button.pack()
horoscope_result = tk.Label(root, text="")
horoscope_result.pack()
root.mainloop()
