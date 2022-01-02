from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from core.browser import Browser
from random import random
import time


class ElementsCore:
    # Elementos da página de Login
    button = 'section._9eogI.E3X2T main.SCxLW.o64aR:nth-child(2) div.qF0y9.Igw0E.rBNOH.YBx95.ybXk5.vwCYk.MGky5.i0EQd div.rgFsT div.gr27e:nth-child(1) div.EPjEi form.HmktE div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.kEKum div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB:nth-child(3) > button.sqdOP.L3NKy.y3zKF'
    login_input = 'section._9eogI.E3X2T main.SCxLW.o64aR:nth-child(2) div.qF0y9.Igw0E.rBNOH.YBx95.ybXk5.vwCYk.MGky5.i0EQd div.rgFsT div.gr27e:nth-child(1) div.EPjEi form.HmktE div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.kEKum div.-MzZI:nth-child(1) div._9GP1n label.f0n8F > input._2hvTZ.pexuQ.zyHYP'
    senha_input = 'section._9eogI.E3X2T main.SCxLW.o64aR:nth-child(2) div.qF0y9.Igw0E.rBNOH.YBx95.ybXk5.vwCYk.MGky5.i0EQd div.rgFsT div.gr27e:nth-child(1) div.EPjEi form.HmktE div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.kEKum div.-MzZI:nth-child(2) div._9GP1n label.f0n8F > input._2hvTZ.pexuQ.zyHYP'
    barra = 'body:nth-child(2) div:nth-child(1) section._9eogI.E3X2T:nth-child(2) > nav.NXc7H.jLuN9:nth-child(3)'
    msg_erro = '#slfErrorAlert'
    profilepic = "section._9eogI.E3X2T:nth-child(2) nav.NXc7H.jLuN9:nth-child(3) div._8MQSO.Cx7Bp div._lz6s div.MWDvN div.ctQZg.KtFt3 div.J5g42 div.XrOey:nth-child(6) span._2dbep.qNELH:nth-child(2) > img._6q-tv"
    profilename = "section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) section._1SP8R.C3uDN.j9XKR:nth-child(1) div.COOzN.MnWb5.YT6rB div.m0NAq.xrWdL div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.ItkAi div.qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm div.qF0y9.Igw0E.IwRSH.YBx95.vwCYk:nth-child(2) div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.DhRcB:nth-child(2) div._7UhW9.xLCgt.MMzan._0PwGv.fDxYl div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk.n4cjz > div._7UhW9.xLCgt.MMzan._0PwGv.fDxYl"
    followers = "section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr header.zw3Ow section.wW3k- ul.k9GMp li.Y8-fY:nth-child(2) a.-nal3 > span.g47SY"
    following = "section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr header.zw3Ow section.wW3k- ul.k9GMp li.Y8-fY:nth-child(3) a.-nal3 > span.g47SY"

    msg_saveinfos_notnow = "section._9eogI.E3X2T main.SCxLW.o64aR:nth-child(2) div.qF0y9.Igw0E.rBNOH.YBx95.vwCYk div.pV7Qt.DPiy6.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.qhGB0.ZUqME div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.aGBdT div.cmbtv > button.sqdOP.yWX7d.y3zKF"
    msg_notifications_notnow = "div.RnEpo.Yx5HN:nth-child(21) div.pbNvD.fPMEg div._1XyCr div.piCib div.mt3GC > button.aOOlW.HoLwm:nth-child(2)"

    # Elementos do Menu de Navegação
    btn_explorer = "section._9eogI.E3X2T nav.NXc7H.jLuN9:nth-child(3) div._8MQSO.Cx7Bp div._lz6s div.MWDvN div.ctQZg.KtFt3 div.J5g42 div.XrOey:nth-child(4) > a:nth-child(1)"
    btn_perfil_opcoes = "section._9eogI.E3X2T:nth-child(2) nav.NXc7H.jLuN9:nth-child(3) div._8MQSO.Cx7Bp div._lz6s div.MWDvN div.ctQZg.KtFt3 div.J5g42 div.XrOey:nth-child(6) > div.wWGrn"
    btn_perfil = "section._9eogI.E3X2T:nth-child(2) nav.NXc7H.jLuN9:nth-child(3) div._8MQSO.Cx7Bp div._lz6s div.MWDvN div.ctQZg.KtFt3 div.J5g42 div.XrOey:nth-child(6) div.poA5q div.uo5MA._2ciX.tWgj8.XWrBI div._01UL2 a.-qQT3:nth-child(1) div.qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm.XfCBB.HVWg4.La5L3.ZUqME div.qF0y9.Igw0E.IwRSH.YBx95.vwCYk:nth-child(2) div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm > div._7UhW9.xLCgt.MMzan.KV-D4.fDxYl"

    # Elementos de Postagens
    post = "_9AhH0"
    postcs = "section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr div._2z6nI article.ySN3v div.Nnq7C.weEfm:nth-child(1) div.v1Nh3.kIKUG._bz0w:nth-child(1) a:nth-child(1) div.eLAPa > div._9AhH0"
    btn_like = "fr66n"
    follow = "div._2dDPU.QPGbb.CkGkG:nth-child(22) div._32yJO div.PdwC2.fXiEu article.M9sTE.L_LMM.JyscU.ePUX4 div.qF0y9.Igw0E.IwRSH.YBx95.ybXk5._4EzTm div.HP0qD div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk div.NvNrm div.UE9AK div.qF0y9.Igw0E.rBNOH.CcYR1.ybXk5._4EzTm header.Ppjfr div.o-MQd.z8cbW div.PQo_0.RqtMr div.bY2yH > button.sqdOP.yWX7d.y3zKF"
    btn_next = "div._2dDPU.QPGbb.CkGkG:nth-child(19) div.EfHg9 div.Z2Inc div.JPgJ_ div.l8mY4.feth3 > button.wpO6b"
    input_comentario = "div._2dDPU.QPGbb.CkGkG:nth-child(20) div._32yJO div.PdwC2.fXiEu article.M9sTE.L_LMM.JyscU.Tgarh.ePUX4 div.qF0y9.Igw0E.IwRSH.YBx95.ybXk5._4EzTm div.HP0qD div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk div.NvNrm div.eo2As section.sH9wk._JgwE div.RxpZH form.X7cDz > textarea.Ypffh:nth-child(3)"
    input_comentario_class = "Ypffh"
    input_comentario_class_visible = "Ypffh focus-visible"
    btn_publi_perfil = "div._2dDPU.QPGbb.CkGkG:nth-child(20) div._32yJO div.PdwC2.fXiEu article.M9sTE.L_LMM.JyscU.Tgarh.ePUX4 div.qF0y9.Igw0E.IwRSH.YBx95.ybXk5._4EzTm div.HP0qD div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk div.NvNrm div.eo2As section.sH9wk._JgwE div.RxpZH form.X7cDz > button.sqdOP.yWX7d.y3zKF:nth-child(4)"
    btn_publi_explorer = "div._2dDPU.QPGbb.CkGkG:nth-child(22) div._32yJO div.PdwC2.fXiEu article.M9sTE.L_LMM.JyscU.ePUX4 div.qF0y9.Igw0E.IwRSH.YBx95.ybXk5._4EzTm div.HP0qD div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk div.NvNrm div.eo2As section.sH9wk._JgwE div.RxpZH form.X7cDz > button.sqdOP.yWX7d.y3zKF:nth-child(4)"
    btn_publi_class = "sqdOP yWX7d    y3zKF     "

    # Página de Perfil
    nomeperfil = "section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) div.v9tJq.AAaSh.VfzDr header.zw3Ow section.wW3k- div.XBGH5 > h2._7UhW9.fKFbl.yUEEX.KV-D4.fDxYl"

    # Feed
    nomePessoal = "section._9eogI.E3X2T:nth-child(2) main.SCxLW.o64aR:nth-child(2) section._1SP8R.C3uDN.j9XKR:nth-child(1) div.COOzN.MnWb5.YT6rB div.m0NAq.xrWdL div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.ItkAi div.qF0y9.Igw0E.rBNOH.eGOV_.ybXk5._4EzTm div.qF0y9.Igw0E.IwRSH.YBx95.vwCYk:nth-child(2) div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.DhRcB:nth-child(2) div._7UhW9.xLCgt.MMzan._0PwGv.fDxYl div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk.n4cjz > div._7UhW9.xLCgt.MMzan._0PwGv.fDxYl"


# Classe responsável por abrigar os comandos do Selenium pré configurados
class Instagram_Core(Browser):
    ignore_list = (TimeoutException, ElementNotVisibleException, ElementClickInterceptedException)

    # Acessa página principal
    def access_mainpage(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

    # Pega elemento por CSS_SELECTOR
    def get_element(self, locator):
        WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    # Pega elemento por Classe
    def get_element_class(self, locator):
        try:
            WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(
                ec.presence_of_element_located((By.CLASS_NAME, locator)))
            return self.driver.find_element(By.CLASS_NAME, locator)
        except TimeoutException:
            print("Elemento não encontrado")

    # Pega elementos por Classe
    def get_elements_class(self, locator):
        try:
            WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(
                ec.presence_of_element_located((By.CLASS_NAME, locator)))
            return self.driver.find_elements(By.CLASS_NAME, locator)
        except TimeoutException:
            print("Elemento não encontrado")

    # Pega elemento Input e envia dados
    def get_input(self, locator, element):
        input = self.get_element(locator)
        input.send_keys(Keys.CONTROL, 'a')
        for i in element:
            t = random()
            print(t)
            time.sleep(t)
            input.send_keys(i)

    # Pega elemento Input por Classe e envia os dados
    def get_input_class(self, locator, element):
        input = self.get_element_class(locator)
        input.send_keys(Keys.CONTROL, 'a')
        for i in element:
            t = random()
            print(t)
            time.sleep(t)
            input.send_keys(i)

    # Determina se o elemento está na tela
    def visibility(self, locator):
        try:
            wait = WebDriverWait(self.driver, timeout=10, poll_frequency=1, ignored_exceptions=self.ignore_list)
            return wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))

        except TimeoutException:
            return False

    # Pega o texto do elemento especificado
    def get_text(self, locator):
        WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        return self.driver.find_element(By.CSS_SELECTOR, locator).text

    # Aperta ESC
    def key_escape(self):
        ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()
