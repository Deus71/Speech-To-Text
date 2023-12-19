import tkinter as tk
import speech_recognition as sr
from googletrans import Translator, LANGUAGES

def translate_text(text, lang):
    try:
        return translator.translate(text, dest=lang).text
    except Exception as e:
        print(f"Błąd podczas tłumaczenia: {e}")
        return ""

def listen():
    with sr.Microphone() as source:
        try:
            audio_data = recognizer.listen(source, phrase_time_limit=5)
            text = recognizer.recognize_google(audio_data, language='pl-PL')
            text_display.insert(tk.END, f"Oryginał: {text}\n")

            # Tłumaczenie tekstu
            for lang in ['en', 'fr', 'es']:
                translated_text = translate_text(text, lang)
                text_display.insert(tk.END, f"{LANGUAGES[lang].capitalize()}: {translated_text}\n")
        except sr.UnknownValueError:
            text_display.insert(tk.END, "Nie zrozumiałem\n")
        except sr.RequestError as e:
            text_display.insert(tk.END, f"Błąd serwisu; {e}\n")
        window.after(100, listen)

recognizer = sr.Recognizer()
translator = Translator()

window = tk.Tk()
window.title("Rozpoznawanie i tłumaczenie mowy")

text_display = tk.Text(window, height=20, width=50)
text_display.pack()

window.after(100, listen)
window.mainloop()
