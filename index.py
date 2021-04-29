# importar bibliotecas para o projeto
from tkinter import *
from tkinter import messagebox
from tkinter import ttk # biblioteca para atualizar gráficos
import DataBaser # importa o arquivo do banco de dados

# criar janela

jan = Tk()
jan.title("Dog Track - Login")
jan.geometry("600x300")
jan.configure(bg="white") # bg = background
jan.resizable(width=False, height=False)
jan.attributes("-alpha", 0.9) 
jan.iconbitmap(default="images/dog-track.ico")

# ---Inserindo imagens---
logo = PhotoImage(file="images/logo.png") # carregar imagem com photoimage, o tkinter só aceita png

# ---Widgets---
LeftFrame = Frame(jan, width=200, height=300, bg="midnightblue", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="snow3", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="midnightblue")
LogoLabel.place(x=50, y=100)

UserLabel = Label(RightFrame, text="Usuário: ", font=("Arial", 15), bg="snow3", fg="black")
UserLabel.place(x=20, y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=100, y=107)

PassLabel = Label(RightFrame, text="Senha: ", font=("Arial", 15), bg="snow3", fg="black")
PassLabel.place(x=20, y=140)

PassEntry = ttk.Entry(RightFrame, width=30, show="⚽")
PassEntry.place(x=100, y=147)

# função para alterar layout da tela ao clicar no botão registrar
def Register():
    # removendo widgets do login
    LoginButton.place(x=9000)
    RegisterButton.place(x=9000)

    # inserindo widgets de cadastro
    NameLabel = Label(RightFrame, text="Nome: ", font=("Arial", 15), bg="snow3", fg="black")
    NameLabel.place(x=20, y=15)
    NameEntry = ttk.Entry(RightFrame, width=40)
    NameEntry.place(x=100, y=21)

    MailLabel = Label(RightFrame, text="E-mail: ", font=("Arial", 15), bg="snow3", fg="black")
    MailLabel.place(x=20, y=55)
    MailEntry = ttk.Entry(RightFrame, width=40)
    MailEntry.place(x=100, y=62)

    #função para voltar para a tela de início
    def BackToLogin():
        # removendo widgets do cadastro
        NameLabel.place(x=9000)
        MailLabel.place(x=9000)
        NameEntry.place(x=9000)
        MailEntry.place(x=9000)
        AddUserButton.place(x=9000)
        BackButton.place(x=9000)
        LoginButton.place(x=137, y=205)
        RegisterButton.place(x=137, y=235)
        
    
    def RegisterToDataBase():
        # pegando entrada das variáveis
        Name = NameEntry.get()
        Mail = MailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        # verifica se os dados estão todos preenchidos
        if (Name == "" or Mail == "" or User == "" or Pass == ""):
            messagebox.showerror(title="Dados vazios", message="Preencha todos os campos!")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(name, mail, user, pass) VALUES (?, ?, ?, ?)
            """, (Name, Mail, User, Pass)) #coloca variáveis dentro dos parentêses
            DataBaser.conn.commit()
            messagebox.showinfo(title="Aviso", message="Cadastro feito com sucesso!")

    # botões da tela registrar
    AddUserButton = ttk.Button(RightFrame, text="Cadastrar", width=15, command=RegisterToDataBase)
    AddUserButton.place(x=137, y=205)

    BackButton = ttk.Button(RightFrame, text="Voltar ao início", width=15, command=BackToLogin)
    BackButton.place(x=137, y=235)


# ---Botões---

# função para o login
def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE user = ? AND pass = ?
    ;
    """, (User, Pass))

    # verifica login
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if (User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Sucesso", message="Login feito com sucesso!")
            root.attributes("-alpha", 0.3)
            print("Login feito com sucesso.")
        else:
            pass
    except:
        messagebox.showerror(title="Login Erro", message="Usuário ou senha incorretos.")
        print("Erro no login.")


LoginButton = ttk.Button(RightFrame, text="Entrar", width=15, command=Login)
LoginButton.place(x=137, y=205)

RegisterButton = ttk.Button(RightFrame, text="Registrar", width=15, command=Register)
RegisterButton.place(x=137, y=235)



#não esquecer mainloop para abrir a janela
jan.mainloop()