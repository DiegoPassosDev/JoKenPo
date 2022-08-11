import random
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Cores---------
cor0 = '#FFFFFF'  # Branco
cor1 = '#333333'  # Preto
cor2 = '#fcc058'  # Laranja
cor3 = '#fff873'  # Amarelo
cor4 = '#34eb3b'  # Verde
cor5 = '#e85151'  # Vermelho
fundo = '#3b3b3b'

# Criando Janela
janela = Tk()
janela.title('JOKENPO')
janela.geometry('260x280')
janela.configure(bg=fundo)

# Dividindo a janela
parteCima = Frame(janela, width=260, height=100, bg=cor1, relief='raised')
parteCima.grid(row=0, column=0, sticky=NW)

parteBaixo = Frame(janela, width=260, height=180, bg=cor0, relief='flat')
parteBaixo.grid(row=1, column=0, sticky=NW)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

# Parte de Cima
jogador = Label(parteCima, text='Jogador', height=1, anchor='center', font='Ivy 10 bold', bg=cor1, fg=cor0)
jogador.place(x=45, y=70)
jogadorLinha = Label(parteCima, text='', height=10, anchor='center', font='Ivy 10 bold', bg=cor0, fg=cor0)
jogadorLinha.place(x=0, y=0)
jogadorPontos = Label(parteCima, text='00', height=1, anchor='center', font='Ivy 30 bold', bg=cor1, fg=cor0)
jogadorPontos.place(x=50, y=20)

xPlacar = Label(parteCima, text='x', height=1, anchor='center', font='Ivy 30 bold', bg=cor1, fg=cor0)
xPlacar.place(x=120, y=20)

computadorPontos = Label(parteCima, text='00', height=1, anchor='center', font='Ivy 30 bold', bg=cor1, fg=cor0)
computadorPontos.place(x=170, y=20)
computador = Label(parteCima, text='COM', height=1, anchor='center', font='Ivy 10 bold', bg=cor1, fg=cor0)
computador.place(x=175, y=70)
computadorLinha = Label(parteCima, text='', height=10, anchor='center', font='Ivy 10 bold', bg=cor0, fg=cor0)
computadorLinha.place(x=255, y=0)

empateLinha = Label(parteCima, text='', width=255, anchor='center', font='Ivy 1 bold', bg=cor0, fg=cor0)
empateLinha.place(x=0, y=95)

escolhaJogador = Label(parteBaixo, width=40, image='', compound=CENTER, bg=cor0, fg=cor0, font='Ivy, 10 bold',
                       anchor=CENTER, relief=FLAT)
escolhaJogador.place(x=50, y=0)

escolhaComputador = Label(parteBaixo, width=40, image='', compound=CENTER, bg=cor0, fg=cor0, font='Ivy, 10 bold',
                          anchor=CENTER, relief=FLAT)
escolhaComputador.place(x=168, y=0)

# Criando imagens da disputa
pedraJogador = Image.open('Imagens/pedra_jogador.png')
pedraJogador = pedraJogador.resize((40, 40))
pedraJogador = ImageTk.PhotoImage(pedraJogador)

papelJogador = Image.open('Imagens/papel_jogador.png')
papelJogador = papelJogador.resize((40, 40))
papelJogador = ImageTk.PhotoImage(papelJogador)

tesouraJogador = Image.open('Imagens/tesoura_jogador.png')
tesouraJogador = tesouraJogador.resize((40, 40))
tesouraJogador = ImageTk.PhotoImage(tesouraJogador)

xPlacarBaixo = Label(parteBaixo, text='x', height=1, anchor='center', font='Ivy 20 bold', bg=cor0, fg=cor0)
xPlacarBaixo.place(x=123, y=0)

pedraPC = Image.open('Imagens/pedra_computador.png')
pedraPC = pedraPC.resize((40, 40))
pedraPC = ImageTk.PhotoImage(pedraPC)

papelPc = Image.open('Imagens/papel_computador.png')
papelPc = papelPc.resize((40, 40))
papelPc = ImageTk.PhotoImage(papelPc)

tesouraPc = Image.open('Imagens/tesoura_computador.png')
tesouraPc = tesouraPc.resize((40, 40))
tesouraPc = ImageTk.PhotoImage(tesouraPc)

# Criando Variáveis Globais
global player
global maquina
global partidas
global pontosJogador
global pontosComputador
pontosJogador = 0
pontosComputador = 0
partidas = 5


# Lógica do Jogo
def jogar(fig):
    global partidas
    global pontosJogador
    global pontosComputador

    if partidas > 0:
        opc = ['Pedra', 'Papel', 'Tesoura']
        maquina = random.choice(opc)
        player = fig
        xPlacarBaixo['fg'] = cor1
        # Gerando a tela de disputa
        if fig == 'Pedra':
            escolhaJogador['image'] = pedraJogador
        elif fig == 'Papel':
            escolhaJogador['image'] = papelJogador
        else:
            escolhaJogador['image'] = tesouraJogador

        if maquina == 'Pedra':
            escolhaComputador['image'] = pedraPC
        elif maquina == 'Papel':
            escolhaComputador['image'] = papelPc
        else:
            escolhaComputador['image'] = tesouraPc
        # Analisando os empates
        if player == maquina:
            computadorLinha['bg'] = cor0
            jogadorLinha['bg'] = cor0
            empateLinha['bg'] = cor3
        # Analisando vitória do jogador
        elif player == 'Pedra' and maquina == 'Tesoura' or player == 'Tesoura' and maquina == 'Papel' or \
                player == 'Papel' and maquina == 'Pedra':
            empateLinha['bg'] = cor0
            computadorLinha['bg'] = cor5
            jogadorLinha['bg'] = cor4
            pontosJogador += 10
        # Analisando vitória do Computador
        else:
            empateLinha['bg'] = cor0
            computadorLinha['bg'] = cor4
            jogadorLinha['bg'] = cor5
            pontosComputador += 10
        # Gerando a pontuação
        jogadorPontos['text'] = pontosJogador
        computadorPontos['text'] = pontosComputador
        if pontosJogador == 0 and pontosComputador == 0:
            jogadorPontos['text'] = '00'
            computadorPontos['text'] = '00'
        elif pontosJogador > 0 and pontosComputador == 0:
            computadorPontos['text'] = '00'
        elif pontosComputador > 0 and pontosJogador == 0:
            jogadorPontos['text'] = '00'
        partidas -= 1
    else:
        fim_jogo()


# Iniciar Jogo
def inicio_jogo():
    global pedra
    global papel
    global tesoura
    global btnPedra
    global btnPapel
    global btnTesoura
    # Apagando o botão Jogar
    btnOk.destroy()

    pedra = Image.open('Imagens/pedra.png')
    pedra = pedra.resize((50, 50))
    pedra = ImageTk.PhotoImage(pedra)
    btnPedra = Button(parteBaixo, command=lambda: jogar('Pedra'), width=50, image=pedra, compound=CENTER, bg=cor0,
                      fg=cor0, font='Ivy, 10 bold', anchor=CENTER, relief=FLAT)
    btnPedra.place(x=20, y=80)

    papel = Image.open('Imagens/papel.png')
    papel = papel.resize((50, 50))
    papel = ImageTk.PhotoImage(papel)
    btnPapel = Button(parteBaixo, command=lambda: jogar('Papel'), width=50, image=papel, compound=CENTER, bg=cor0,
                      fg=cor0, font='Ivy, 10 bold', anchor=CENTER, relief=FLAT)
    btnPapel.place(x=100, y=80)

    tesoura = Image.open('Imagens/tesoura.png')
    tesoura = tesoura.resize((50, 50))
    tesoura = ImageTk.PhotoImage(tesoura)
    btnTesoura = Button(parteBaixo, command=lambda: jogar('Tesoura'), width=50, image=tesoura, compound=CENTER, bg=cor0,
                        fg=cor0, font='Ivy, 10 bold', anchor=CENTER, relief=FLAT)
    btnTesoura.place(x=185, y=80)


# Fim do Jogo
def fim_jogo():
    global partidas
    global pontosJogador
    global pontosComputador
    # Reiniciando os pontos e as partidas
    pontosJogador = pontosComputador = 0
    partidas = 5
    # Apagando os botões pedra, papel e tesoura
    btnPedra.destroy()
    btnPapel.destroy()
    btnTesoura.destroy()
    # Definindo a partida
    ptoJogador = int(jogadorPontos['text'])
    ptoComputador = int(computadorPontos['text'])

    if ptoJogador > ptoComputador:
        resultado = Label(parteBaixo, text='Parabéns, você venceu!!', height=1, anchor='center', font='Ivy 12 bold',
                          bg=cor0, fg=cor4)
        resultado.place(x=36, y=80)
    elif ptoComputador > ptoJogador:
        resultado = Label(parteBaixo, text='Infelizmente você perdeu!!', height=1, anchor='center', font='Ivy 12 bold',
                          bg=cor0, fg=cor5)
        resultado.place(x=30, y=80)
    else:
        resultado = Label(parteBaixo, text='Deu Empate!!', height=1, anchor='center', font='Ivy 12 bold',
                          bg=cor0, fg=cor3)
        resultado.place(x=76, y=80)

    def jogar_novamente():
        jogadorLinha['bg'] = cor0
        computadorLinha['bg'] = cor0
        empateLinha['bg'] = cor0
        jogadorPontos['text'] = '00'
        computadorPontos['text'] = '00'
        resultado.destroy()
        escolhaComputador['image'] = ''
        escolhaJogador['image'] = ''
        xPlacarBaixo['fg'] = cor0

        btnJogarNovamente.destroy()
        inicio_jogo()

    btnJogarNovamente = Button(parteBaixo, command=jogar_novamente, width=30, text='NOVA PARTIDA', bg=fundo, fg=cor0,
                               font='Ivy, 10 bold', anchor=CENTER, relief=RAISED, overrelief=RIDGE)
    btnJogarNovamente.place(x=5, y=150)


# Parte de Baixo
btnOk = Button(parteBaixo, command=inicio_jogo, width=30, text='JOGAR', bg=fundo, fg=cor0, font='Ivy, 10 bold',
               anchor=CENTER, relief=RAISED, overrelief=RIDGE)
btnOk.place(x=5, y=150)

janela.mainloop()
