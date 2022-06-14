#pip install google_trans_new
from googletrans import Translator
translator = Translator()
texto = input("digite a frase a ser identificada: ")


while (texto!="0"):
    translate_text = translator.detect(texto)
    print(translate_text)
    texto = input("digite a frase a ser identificada ou digite 0 para finalizar: ")
else:
     print("Finalizado com sucesso")


