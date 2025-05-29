class KnowledgeBase:
    def __init__(self):
        self.topics = {
            "viajes en el tiempo": "Los viajes en el tiempo son un concepto teórico de la física y la ciencia ficción. Según la teoría de la relatividad de Einstein, es posible viajar en el tiempo a través de la dilatación temporal y los agujeros de gusano.",
            "vampiros": "Los vampiros son criaturas legendarias que se alimentan de la sangre de los vivos. En la ficción, suelen ser inmortales, sensibles a la luz del sol y pueden transformarse en murciélagos.",
            "hombres lobo": "Los hombres lobo son seres mitológicos que pueden transformarse en lobos o criaturas híbridas bajo la luna llena. En muchas historias, su transformación es provocada por una maldición o una mordida de otro hombre lobo.",
            "información científica": "La ciencia abarca múltiples campos como la física, la química y la biología. Por ejemplo, la mecánica cuántica estudia las partículas subatómicas y sus comportamientos extraños.",
            "cómo programar juegos": "Para programar videojuegos, puedes usar motores como Unity (C#) o Unreal Engine (C++). También existen bibliotecas como Pygame para Python. Aprender sobre física de juegos, inteligencia artificial y gráficos es esencial."
        }

    def get_info(self, topic):
        return self.topics.get(topic.lower(), "Lo siento, no tengo información sobre ese tema.")


def main():
    knowledge = KnowledgeBase()
    print("Bienvenido al asistente de conocimiento. Puedes preguntar sobre viajes en el tiempo, vampiros, hombres lobo, ciencia y programación de juegos.")
    
    while True:
        question = input("¿Sobre qué quieres información? (Escribe 'salir' para terminar): ")
        if question.lower() == "salir":
            print("Gracias por usar el asistente. ¡Hasta luego!")
            break
        
        answer = knowledge.get_info(question)
        print(answer)


if __name__ == "__main__":
    main()
