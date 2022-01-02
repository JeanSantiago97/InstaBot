from core.instacore import *

core = Instagram_Core()
core_elements = ElementsCore()


# Função de dar likes no explorer e em perfil específico
class LikeFeed():

    # Iniciar função de dar Like automáticamente.
    def run_like(self):
        if not core.visibility(core_elements.nomeperfil):
            core.get_element(core_elements.btn_explorer).click()
        for post in core.get_elements_class(core_elements.post):
            print("Cliquei na postagem")
            post.click()
            time.sleep(0.7)
            print("Cliquei no like")
            core.get_element_class(core_elements.btn_like).click()
            core.key_escape()
