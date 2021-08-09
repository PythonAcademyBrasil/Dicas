import speech_recognition as sr

if __name__ == '__main__':
    try:
        # Instancia a classe Recognizer
        r = sr.Recognizer()

        # Lê o arquivo de áudio
        with sr.AudioFile("./audio.wav") as fonte:
            audio = r.record(fonte)

        # Utiliza o Google Speech Recognition para fazer a conversão
        # Utiliza a chave de API padrão do próprio Speech Recognition
        # Para utilizar uma chave própria (recomendada), acesse a documentação
        texto = r.recognize_google(audio, language='pt-br')
        print(f'Google Speech Recognition acha que você disse: \n"{texto}"')

    except sr.UnknownValueError:
        print('Google Speech Recognition não entendeu seu áudio')

    except sr.RequestError as e:
        print(f'Não foi possível se conectar à API da Google. Erro: {str(e)}')
