from core.instacore import *

core = Instagram_Core()

class Elements:
    Feed = 'section._9eogI.E3X2T nav.NXc7H.jLuN9:nth-child(3) div._8MQSO.Cx7Bp div._lz6s div.MWDvN div.ctQZg.KtFt3 div.J5g42 div.XrOey:nth-child(1) > div:nth-child(1)'
    btn_explorer = 'section._9eogI.E3X2T nav.NXc7H.jLuN9:nth-child(3) div._8MQSO.Cx7Bp div._lz6s div.MWDvN div.ctQZg.KtFt3 div.J5g42 div.XrOey:nth-child(4) > a:nth-child(1)'
    postpri = 'H-KQe'
    '''postsec = 'pKKVh' '''
    btn_like = 'div._2dDPU.QPGbb.CkGkG:nth-child(22) div._32yJO div.PdwC2.fXiEu article.M9sTE.L_LMM.JyscU.ePUX4 div.qF0y9.Igw0E.IwRSH.YBx95.ybXk5._4EzTm div.HP0qD div.qF0y9.Igw0E.IwRSH.eGOV_.vwCYk div.NvNrm div.eo2As section.ltpMr.Slqrh span.fr66n > button.wpO6b'
    mainexplorer = 'body:nth-child(2) div:nth-child(1) section._9eogI.E3X2T > main.SCxLW.o64aR:nth-child(2)'

# Função de dar likes no explorer do instagram
class LikeFeed():

    def run_like(self):
        core.get_element(Elements.btn_explorer).click()
        for btn in core.get_elements_class(Elements.postpri):
            btn.click()
            core.get_element(Elements.btn_like).click()
            core.key_escape()