import pyttsx3

def speak(rate, volume, voice_index, text) -> None:
    """
    Синтезирует речь из текста с заданной скоростью, громкостью и голосом.
    """
    engine = pyttsx3.init()                    
    engine.setProperty('rate', rate)                         
    engine.setProperty('volume', volume)       
    voices = engine.getProperty('voices')     
    engine.setProperty('voice', voices[voice_index].id) 
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    speak(150, 1.0, 0, "Hello! I am your text-to-speech assistant.")
    speak(170, 0.4, 1, "I can read out any text you provide.")
