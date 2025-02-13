# -*- coding: utf-8 -*-
"""projetando sistema de assistencia virtual do zero.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dnfc6IhBePxGwK-kJCJE0_eapxUQLhhU
"""

!pip install pyttsx3 SpeechRecognition  wikipedia googlemaps
!pip install pipwin
!pipwin install pyaudio

 #biblioteca necessárias

!pip install gTTS

from gtts import gTTS
from IPython.display import Audio

# Função para converter texto em fala
def text_to_speech(text):
    tts = gTTS(text=text, lang='pt')
    tts.save("output.mp3")

    # Reproduzir o áudio gerado
    return Audio("output.mp3", autoplay=True)

# Testando
text_to_speech("Olá, estou funcionando muito bem obrigada! volte sempre!")

"""# Conversão de arquivos para formato WAV
Usar as próximas células para arquivos de áudio que não estão em formato wav.

"""

!apt-get install ffmpeg
!pip install pydub

from pydub import AudioSegment

# Carregar o arquivo m4a
audio = AudioSegment.from_file("/content/11 de fev. 14.18_.m4a")

# Converter para wav e salvar
audio.export("/content/audio_convertido.wav", format="wav")

"""# A partir daqui já voltamos aos métodos de conversão"""

import speech_recognition as sr

recognizer = sr.Recognizer()
audio_file = "/content/audio_convertido.wav"

with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language="pt-BR")
    print(f"Você disse: {text}")
except sr.UnknownValueError:
    print("Não consegui entender o áudio")
except sr.RequestError:
    print("Erro ao se conectar ao serviço de reconhecimento de fala")

import wikipedia
from gtts import gTTS
import IPython.display as ipd

# Configuração da língua para português
wikipedia.set_lang("pt")

def text_to_speech(text):
    # Converte texto em fala e reproduz automaticamente
    tts = gTTS(text=text, lang="pt")
    tts.save("fala.mp3")
    return ipd.Audio("fala.mp3", autoplay=True)

def search_wikipedia(query):
    # Pesquisar na Wikipédia e ler o resumo
    try:
        result = wikipedia.summary(query, sentences=2)
        print(result)  # Exibe o resumo no console
        ipd.display(text_to_speech(result))
    except wikipedia.exceptions.DisambiguationError:
        ipd.display(text_to_speech("Desculpe, houve uma ambiguidade na pesquisa. Tente ser mais específico."))
    except wikipedia.exceptions.HTTPTimeoutError:
        ipd.display(text_to_speech("Houve um erro na conexão com a Wikipédia."))

# Teste
search_wikipedia("Darwin Nunez")

import webbrowser

def open_youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    print(f"🔗 Clique no link para abrir o YouTube: {search_url}")
    webbrowser.open(search_url, new=2)

# Teste
open_youtube("Python programação")

"""# Instalando geopy para busca de locais"""

!pip install geopy requests

!pip install geopy requests
from geopy.geocoders import Nominatim
import requests

def find_pharmacy(location):
    # Geocodificação para obter latitude e longitude da localização
    geolocator = Nominatim(user_agent="pharmacy_locator")
    location = geolocator.geocode(location)

    if location:
        lat = location.latitude
        lon = location.longitude
        print(f"Localização encontrada: {location.address} ({lat}, {lon})")

        # Consulta à Overpass API para buscar farmácias nas proximidades
        overpass_url = f"http://overpass-api.de/api/interpreter?data=[out:json];(node['amenity'='pharmacy'](around:5000,{lat},{lon}););out;"
        response = requests.get(overpass_url)
        pharmacy_data = response.json()

        if pharmacy_data['elements']:
            pharmacy = pharmacy_data['elements'][0]  # Pega a primeira farmácia encontrada
            pharmacy_name = pharmacy.get('tags', {}).get('name', 'Farmácia desconhecida')
            pharmacy_address = f"Lat: {pharmacy['lat']}, Lon: {pharmacy['lon']}"
            print(f"A farmácia mais próxima é {pharmacy_name} localizada em {pharmacy_address}")
        else:
            print("Não encontrei nenhuma farmácia nas proximidades.")
    else:
        print("Não foi possível encontrar a localização fornecida.")

# Testando a função com um endereço ou nome de lugar
find_pharmacy("Belém - Pará")

"""# Integrando tudo"""

# Instalar dependências necessárias
!pip install gTTS pydub geopy requests wikipedia

# Importando as bibliotecas necessárias
import wikipedia
import webbrowser
from gtts import gTTS
from IPython.display import Audio
import speech_recognition as sr
from geopy.geocoders import Nominatim
import requests
from pydub import AudioSegment

# Função para converter texto em fala
def text_to_speech(text):
    tts = gTTS(text=text, lang='pt')
    tts.save("output.mp3")
    return Audio("output.mp3", autoplay=True)

# Função para reconhecer áudio e converter em texto (para microfone ou arquivo de áudio)
def speech_to_text(audio_file=None):
    recognizer = sr.Recognizer()

    if audio_file:  # Caso esteja usando um arquivo de áudio
        try:
            with sr.AudioFile(audio_file) as source:
                print("Carregando áudio...")
                audio = recognizer.record(source)
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Não consegui entender o áudio.")
            return ""
        except sr.RequestError:
            print("Erro ao se conectar ao serviço de reconhecimento de fala.")
            return ""

    else:  # Caso esteja usando o microfone
        with sr.Microphone() as source:
            print("Aguardando comando de voz...")
            audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Não consegui entender o áudio.")
            return ""
        except sr.RequestError:
            print("Erro ao se conectar ao serviço de reconhecimento de fala.")
            return ""

# Função para pesquisar no Wikipedia
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        print(result)  # Exibe o resumo no console
        text_to_speech(result)
    except wikipedia.exceptions.DisambiguationError:
        text_to_speech("Desculpe, houve uma ambiguidade na pesquisa. Tente ser mais específico.")
    except wikipedia.exceptions.HTTPTimeoutError:
        text_to_speech("Houve um erro na conexão com a Wikipédia.")

# Função para abrir o YouTube
def open_youtube(query):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    print(f"🔗 Clique no link para abrir o YouTube: {search_url}")
    webbrowser.open(search_url, new=2)
    text_to_speech(f"Abrindo YouTube para {query}")

# Função para encontrar farmácias próximas
def find_pharmacy(location):
    geolocator = Nominatim(user_agent="pharmacy_locator")
    location = geolocator.geocode(location)

    if location:
        lat = location.latitude
        lon = location.longitude
        print(f"Localização encontrada: {location.address} ({lat}, {lon})")

        # Consulta à Overpass API para buscar farmácias nas proximidades
        overpass_url = f"http://overpass-api.de/api/interpreter?data=[out:json];(node['amenity'='pharmacy'](around:5000,{lat},{lon}););out;"
        response = requests.get(overpass_url)
        pharmacy_data = response.json()

        if pharmacy_data['elements']:
            pharmacy = pharmacy_data['elements'][0]
            pharmacy_name = pharmacy.get('tags', {}).get('name', 'Farmácia desconhecida')
            pharmacy_address = f"Lat: {pharmacy['lat']}, Lon: {pharmacy['lon']}"
            print(f"A farmácia mais próxima é {pharmacy_name} localizada em {pharmacy_address}")
            text_to_speech(f"A farmácia mais próxima é {pharmacy_name} localizada em {pharmacy_address}")
        else:
            print("Não encontrei nenhuma farmácia nas proximidades.")
            text_to_speech("Não encontrei nenhuma farmácia nas proximidades.")
    else:
        print("Não foi possível encontrar a localização fornecida.")
        text_to_speech("Não foi possível encontrar a localização fornecida.")

# Função principal para ouvir e executar os comandos de voz
def main():
    text_to_speech("Assistente ativado. Como posso ajudar?")
    while True:
        print("Aguardando comando de voz...")
        command = speech_to_text()  # Usando o microfone por padrão

        if 'pesquisar' in command:
            text_to_speech("Por favor, diga o que deseja pesquisar na Wikipedia.")
            query = speech_to_text()  # Obtém o termo de pesquisa do usuário
            search_wikipedia(query)

        elif 'youtube' in command:
            text_to_speech("Por favor, diga o que deseja buscar no YouTube.")
            query = speech_to_text()  # Obtém o termo para busca no YouTube
            open_youtube(query)

        elif 'farmácia' in command:
            text_to_speech("Por favor, diga sua localização para encontrar farmácias nas proximidades.")
            location = speech_to_text()  # Obtém a localização do usuário
            find_pharmacy(location)

        elif 'sair' in command:
            text_to_speech("Até logo!")
            print("Saindo...")
            break  # Sai do loop e encerra o assistente

        else:
            text_to_speech("Desculpe, não entendi o comando. Tente novamente.")

# Executar o assistente
main()

