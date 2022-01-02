import time
from core.instacore import *
import linecache
from random import randint

core = Instagram_Core()
core_elements = ElementsCore()


# Função de dar likes no explorer do instagram
class AutoComments():

    def run_comments(self):
        if not core.visibility(core_elements.nomeperfil):
            core.get_element(core_elements.btn_explorer).click()

        for btn in core.get_elements_class(core_elements.post):
            print("Cliquei na postagem")
            btn.click()
            time.sleep(0.7)

            comentario = linecache.getline(r"..\resources\comments", randint(1, 43))

            core.get_element_class(core_elements.input_comentario_class).click()
            print("cliquei no comentário!")
            core.get_input_class(core_elements.input_comentario_class, comentario)
            print(f"Comentei: {comentario}")
            core.key_escape()
            print("Apertei ESC")
