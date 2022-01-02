from core.instacore import *

core = Instagram_Core()
core_elements = ElementsCore()


# Função para seguir pessoas do explorar
class AutoFollow():

    # Iniciar função de seguir automáticamente.
    def run_follow(self):
        core.get_element(ElementsCore.btn_explorer).click()
        for btn in core.get_elements_class(core_elements.post):
            print("Cliquei na postagem")
            btn.click()
            time.sleep(1)

            if core.get_text(core_elements.follow) == "Seguir" or "Follow":
                print("Cliquei no seguir")
                core.get_element(core_elements.follow).click()
                core.key_escape()
            else:
                print("Você já segue esta pessoa")
