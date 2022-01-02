import tkinter as tk
from tkinter import *
from tkinter import font as tkfont
from PIL import ImageTk
from PIL import Image

from steps.login import *
from steps.likepost import *
from steps.autofollow import *
from steps.autocomments import *

core = Instagram_Core()
Login = Login()
likefeed = LikeFeed()
autofollow = AutoFollow()
autocomments = AutoComments()


# Configuração da troca de interface
class GUICore(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.title("Instabot by JSANTIAGO")
        self.iconbitmap(r"..\resources\icon.ico")

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
        frame = self.frames[page_name]
        frame.tkraise()

    def geo_frame(self, valor):
        self.geometry(valor)


# Pagina de Login
class PageLogin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Funções
        def login_auto(element1, element2):
            if Login.logar(element1.get(), element2.get()):
                controller.show_frame("PageMenu")

        def login_manual():
            if Login.logar_manual():
                controller.show_frame("PageMenu")

        # Acessando site do Instagram pelo Selenium
        core.access_mainpage()

        # Declaração
        self.controller = controller

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
            r"..\resources\Logo.png").resize(
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

        btn_login = tk.Button(self, text="ENTRAR",
                            command=lambda: login_auto(login, senha))
        btn_login.pack(padx=10, pady=10, anchor=CENTER)

        btn_login_manual = tk.Button(self, text="LOGIN MANUAL",
                            command=lambda: login_manual())
        btn_login_manual.pack(padx=10, pady=10, anchor=CENTER)


class PageMenu(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Definição
        self.controller = controller
        controller.geo_frame("300x350")

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
        txt_bemvindo = tk.Label(frame_bemvindo, text=f"MENU", font=controller.title_font)
        txt_bemvindo.pack(anchor=N)

        btn_likeposts = tk.Button(frame_menu, text="LikePosts",
                                  command=lambda: likefeed.run_like())
        btn_likeposts.grid(row=0, column=0, padx=10, pady=10)

        btn_autofollow = tk.Button(frame_menu, text="AutoFollow",
                                   command=lambda: autofollow.run_follow())
        btn_autofollow.grid(row=1, column=0, padx=10, pady=10)

        btn_autocomments = tk.Button(frame_menu, text="AutoComments",
                                     command=lambda: autocomments.run_comments())
        btn_autocomments.grid(row=2, column=0, padx=10, pady=10)


if __name__ == "__main__":
    app = GUICore()
    app.mainloop()
