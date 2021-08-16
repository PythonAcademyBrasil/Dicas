import gtts
import pyttsx3
from playsound import playsound

# Escolha entre 'online' ou 'offline'
MODO = 'online'
TEXTO = """
Olá! Seja muito bem vindo à Dica de Conversão de Texto da Python Academy!
Utilizamos a biblioteca gtts (Google Text to Speech) para esse objetivo.
Não se esqueça que nossas Dicas estão disponíveis no Github da Python Academy,
é só acessar github.com/PythonAcademyBrasil/Dicas. Te vejo lá!
"""

if __name__ == '__main__':
    # Utiliza o Google para realizar a tradução (requer conexão com Internet)
    if MODO == 'online':
        tts = gtts.gTTS(TEXTO, lang='pt-br')

        # Salva o arquivo de áudio
        tts.save("audio.mp3")

        # Toca o arquivo de áudio
        playsound("audio.mp3")

    # Utiliza as vozes disponíveis no Sistema Operacional
    elif MODO == 'offline':
        # Cria a Engine para processamento offline de acordo com as vozes
        # disponíveis em seu Sistema Operacional
        engine = pyttsx3.init()

        # > Descomente as 3 linhas abaixo para checar as "Voices" disponíveis
        # voices = engine.getProperty("voices")
        # for voice in voices:
        #     print(voice.name)

        # 'brazil' é uma voz disponível no meu Sistema Operacional
        engine.setProperty("voice", 'brazil')

        # Configura o que deve ser dito
        engine.say(TEXTO)

        # Toca o áudio
        engine.runAndWait()

