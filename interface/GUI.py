import tkinter as tk
from tkinter import *
from tkinter import font as tkfont  # python 3
from PIL import ImageTk
from PIL import Image

from steps.login import *
from interface.GUI_Menu import *

core = Instagram_Core()
Login = Login()
Menu = GUI_Menu()

#Configuração da troca de interface
class GUICore(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (PageLogin, PageMenu):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("PageLogin")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

    def geo_frame(self, valor):
        self.geometry(valor)

#Pagina de Login
class PageLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Acessando site do Instagram pelo Selenium
        core.access_mainpage()

        # Declaração
        self.controller = controller

        '''controller.geo_frame("300x300")'''

        # Containers
        frame_Logo = tk.Frame(self)
        frame_Logo.configure(padx=5)
        frame_Logo.configure(pady=5)
        frame_Logo.pack(padx=5)

        frame_Login = tk.Frame(self)
        frame_Login.configure(padx=5)
        frame_Login.configure(pady=5)
        frame_Login.pack(padx=5)

        # Elementos
        self.Img_Instabot = ImageTk.PhotoImage(Image.open(
            r"C:\Users\jean_\OneDrive\Estudos e Curriculos\QA e Python\Projetos Python\InstaBot\img\Logo.png").resize(
            (150, 150), Image.ANTIALIAS))
        logo = Label(frame_Logo, image=self.Img_Instabot)
        logo.pack(anchor=N)

        bemvindo = Label(frame_Logo, text="INSTAGRAM BOT")
        bemvindo.pack(anchor=CENTER)
        credito = Label(frame_Logo, text="By JSantiago")
        credito.pack(anchor=CENTER)

        txtLogin = Label(frame_Login, text="LOGIN ")
        txtLogin.grid(row=0, column=0)
        login = Entry(frame_Login)
        login.grid(row=0, column=1)

        txtSenha = Label(frame_Login, text="SENHA")
        txtSenha.grid(row=1, column=0)
        senha = Entry(frame_Login, show="*")
        senha.grid(row=1, column=1)

        button1 = tk.Button(self, text="ENTRAR",
                            command=lambda: login_auto(login, senha))
        button1.pack(padx=10, pady=10, anchor=CENTER)

        # BOTÃO DE LOGIN MANUAL
        button2 = tk.Button(self, text="LOGIN MANUAL",
                            command=lambda: login_manual())
        button2.pack(padx=10, pady=10, anchor=CENTER)

        def login_auto(element1, element2):
            if Login.logar(element1.get(), element2.get()):
                controller.show_frame("PageMenu")

        def login_manual():
            if Login.logar_manual():
                controller.show_frame("PageMenu")



class PageMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Definição
        self.controller = controller
        '''controller.geo_frame("300x300")'''

        # Frames
        frame_bemvindo = tk.Frame(self)
        frame_bemvindo.configure(padx=5)
        frame_bemvindo.pack(padx=5)

        frame_statusbar = tk.Frame(self)
        frame_statusbar.configure(padx=5, pady=5)
        frame_statusbar.pack(padx=5)

        frame_menu = tk.Frame(self)
        frame_menu.configure(padx=5)
        frame_menu.configure(pady=5)
        frame_menu.pack(padx=5)

        # Elements
        txt_bemvindo = tk.Label(frame_bemvindo, text=f"Bem vindo, Fulano", font=controller.title_font)
        txt_bemvindo.pack(anchor=N)

        seguidores = tk.Label(frame_statusbar, text=f"Seguidores: #")
        seguidores.pack(side='left', padx=10, pady=10)

        seguindo = tk.Label(frame_statusbar, text=f"Seguindo: #")
        seguindo.pack(side='right', padx=10, pady=10)

        btn_LikePosts = tk.Button(frame_menu, text="LikePosts",
                                  command=lambda: likefeed.run_like())
        btn_LikePosts.grid(row=0, column=0, padx=10, pady=10)

        btn_AutoFollow = tk.Button(frame_menu, text="AutoFollow",
                                   command=lambda: controller.show_frame("PageLogin"))
        btn_AutoFollow.grid(row=0, column=1, padx=10, pady=10)

        btn_AutoComments = tk.Button(frame_menu, text="AutoComments",
                                     command=lambda: controller.show_frame("PageLogin"))
        btn_AutoComments.grid(row=1, column=0, padx=10, pady=10)

        btn_SelfCommentsLike = tk.Button(frame_menu, text="SelfCommentsLike",
                                         command=lambda: controller.show_frame("PageLogin"))
        btn_SelfCommentsLike.grid(row=1, column=1, padx=10, pady=10)


if __name__ == "__main__":
    app = GUICore()
    app.mainloop()
