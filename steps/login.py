from interface.GUI_Menu import *
from core.instacore import *

'''from interface.GUI import GUICore
GUI = GUICore()'''

core = Instagram_Core()
iMenu = GUI_Menu()


class Elements:
    button = 'section._9eogI.E3X2T main.SCxLW.o64aR:nth-child(2) div.qF0y9.Igw0E.rBNOH.YBx95.ybXk5.vwCYk.MGky5.i0EQd div.rgFsT div.gr27e:nth-child(1) div.EPjEi form.HmktE div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.kEKum div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB:nth-child(3) > button.sqdOP.L3NKy.y3zKF'
    login_input = 'section._9eogI.E3X2T main.SCxLW.o64aR:nth-child(2) div.qF0y9.Igw0E.rBNOH.YBx95.ybXk5.vwCYk.MGky5.i0EQd div.rgFsT div.gr27e:nth-child(1) div.EPjEi form.HmktE div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.kEKum div.-MzZI:nth-child(1) div._9GP1n label.f0n8F > input._2hvTZ.pexuQ.zyHYP'
    senha_input = 'section._9eogI.E3X2T main.SCxLW.o64aR:nth-child(2) div.qF0y9.Igw0E.rBNOH.YBx95.ybXk5.vwCYk.MGky5.i0EQd div.rgFsT div.gr27e:nth-child(1) div.EPjEi form.HmktE div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.kEKum div.-MzZI:nth-child(2) div._9GP1n label.f0n8F > input._2hvTZ.pexuQ.zyHYP'
    barra = 'body:nth-child(2) div:nth-child(1) section._9eogI.E3X2T:nth-child(2) > nav.NXc7H.jLuN9:nth-child(3)'
    msg_erro = '#slfErrorAlert'
    profilepic = "section._9eogI.E3X2T:nth-child(2) nav.NXc7H.jLuN9:nth-child(3) div._8MQSO.Cx7Bp div._lz6s div.MWDvN div.ctQZg.KtFt3 div.J5g42 div.XrOey:nth-child(6) span._2dbep.qNELH:nth-child(2) > img._6q-tv"
    profilename = "section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) section._1SP8R.C3uDN.j9XKR:nth-child(1) div.COOzN.MnWb5.YT6rB div.m0NAq.xrWdL div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.ItkAi div.qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm div.qF0y9.Igw0E.IwRSH.YBx95.vwCYk:nth-child(2) div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.DhRcB:nth-child(2) div._7UhW9.xLCgt.MMzan._0PwGv.fDxYl div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk.n4cjz > div._7UhW9.xLCgt.MMzan._0PwGv.fDxYl"
    followers = "section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr header.zw3Ow section.wW3k- ul.k9GMp li.Y8-fY:nth-child(2) a.-nal3 > span.g47SY"
    following = "section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr header.zw3Ow section.wW3k- ul.k9GMp li.Y8-fY:nth-child(3) a.-nal3 > span.g47SY"


class Login():

    def logar(self, login, senha):

        core.get_input(Elements.login_input, login)
        core.get_input(Elements.senha_input, senha)
        core.get_element(Elements.button).click()

        if core.login_visibility(Elements.msg_erro):
            print("Login Invalido")
            return False

        elif core.login_visibility(Elements.barra):
            print("Login Valido")
            return True

        else:
            print("Falha ao fazer o login")
            return False

    def logar_manual(self):
        if core.login_visibility(Elements.barra):
            print("Login Valido")
            return True
        else:
            print("Tentativa de Login Manual inválida")
