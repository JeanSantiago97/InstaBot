from core.instacore import *

core = Instagram_Core()
elements = ElementsCore()


class Login:

    # Função de Logar
    def logar(self, login, senha):

        core.get_input(elements.login_input, login)
        core.get_input(elements.senha_input, senha)
        core.get_element(elements.button).click()

        if core.visibility(elements.msg_erro):
            print("Login Invalido")
            return False

        if core.visibility(elements.msg_saveinfos_notnow):
            core.get_element(elements.msg_saveinfos_notnow).click()
            print("Salvar Informações OFF")

        if core.visibility(elements.msg_notifications_notnow):
            core.get_element(elements.msg_notifications_notnow).click()
            print("Notificação OFF")

        if core.visibility(elements.barra):
            print("Login Valido")
            return True

        else:
            print("Falha ao fazer o login")
            return False

    def logar_manual(self):
        if core.visibility(elements.barra):
            print("Login Valido")
            return True
        else:
            print("Tentativa de Login Manual inválida")
