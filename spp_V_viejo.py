# -*- coding: utf-8 -*-
#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1COMPROBAR, wxID_FRAME1ENTRADA, wxID_FRAME1PANEL1,
 wxID_FRAME1PANEL2, wxID_FRAME1SALIDA, wxID_FRAME1SALIR,
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2,
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(615, 369), size=wx.Size(239, 301),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame1')
        self.SetClientSize(wx.Size(231, 274))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(200, 128),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(252, 217, 177))

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2', parent=self,
              pos=wx.Point(16, 160), size=wx.Size(200, 100),
              style=wx.TAB_TRAVERSAL)
        self.panel2.SetBackgroundColour(wx.Colour(210, 255, 234))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Introduzca aqu\xed una palabra o secuencia de caracteres al darle a comprobar el programa dir\xe1 si se puede pronunciar en espa\xf1ol.',
              name='staticText1', parent=self.panel1, pos=wx.Point(19, 8),
              size=wx.Size(159, 56), style=0)

        self.entrada = wx.TextCtrl(id=wxID_FRAME1ENTRADA, name=u'entrada',
              parent=self.panel1, pos=wx.Point(50, 70), size=wx.Size(100, 21),
              style=0, value=u'')
        self.entrada.Bind(wx.EVT_TEXT_ENTER, self.OnEntradaTextEnter,
              id=wxID_FRAME1ENTRADA)

        self.comprobar = wx.Button(id=wxID_FRAME1COMPROBAR, label=u'Comprobar',
              name=u'comprobar', parent=self.panel1, pos=wx.Point(63, 97),
              size=wx.Size(75, 23), style=0)
        self.comprobar.Bind(wx.EVT_BUTTON, self.OnComprobarButton,
              id=wxID_FRAME1COMPROBAR)

        self.salida = wx.TextCtrl(id=wxID_FRAME1SALIDA, name=u'salida',
              parent=self.panel2, pos=wx.Point(49, 31), size=wx.Size(100, 21),
              style=0, value=u'')

        self.salir = wx.Button(id=wxID_FRAME1SALIR, label=u'Salir',
              name=u'salir', parent=self.panel2, pos=wx.Point(62, 56),
              size=wx.Size(75, 23), style=0)
        self.salir.Bind(wx.EVT_BUTTON, self.OnSalirButton, id=wxID_FRAME1SALIR)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Respuesta:', name='staticText2', parent=self.panel2,
              pos=wx.Point(72, 16), size=wx.Size(55, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)


    def OnComprobarButton(self, event):

        #...........................LISTAS......................................
        #Lista de las vocales, mayúsculas, minúsculas, acentuadas y dieresis.
        vocal= ['A', 'E', 'I', 'O', 'U', u'Á', u'É', u'Í', u'Ó', u'Ú', 'a', 'e',
        'i', 'o', 'u', u'á', u'é',  u'í', u'ó', u'ú', u'ü', 'Y', 'y']
        #Lista consonantes solo vocales o dobles. Ojo con la segunda doblada.
        con_doble=['L', 'l', 'R', 'r']
        #Lista consonantes solo con vocales.
        con_vocal=['J', 'j', 'M', 'm', 'N', 'n', 's', 'v', 'x', 'z']
        #Lista consonantes solo R.
        con_R= ['D', 'd', 'T', 't']
        #Lista consonantes R o L.
        con_RL=['B', 'b', 'F', 'f', 'G', 'g', 'P', 'p']
        #Lista posibilidades con la R.
        pr= ['ra', 're', 'ri', 'ro', 'ru', u'rá', u'ré', u'rí', u'ró', u'rú',
        'Ra', 'Re', 'Ri', 'Ro', 'Ru', u'Rá', u'Ré', u'Rí', u'Ró', u'Rú']
        #Lsta posibilidades con la L.
        pl= ['la', 'le', 'li', 'lo', 'lu', u'lá', u'lé', u'lí', u'ló', u'lú',
        'La', 'Le', 'Li', 'Lo', 'Lu', u'Lá', u'Lé', u'Lí', u'Ló', u'Lú']
        #letra Q.
        q= ['Q', 'q']
        #Lista letra tras Q.
        pq= ['ue', u'ué', 'ui', u'uí']
        #Letra C
        c= ['C', 'c']
        #Lista letras tras C.
        pc= ['ha', 'he', 'hi', 'ho', 'hu', u'há', u'hé', u'hí', u'hó', u'hú']
        #Letra H
        h= ['H', 'h']
        #Caso de NST
        #Letra Ñ
        spain= [u'Ñ', u'ñ']
        #.........................FIN LISTAS....................................

        pal= self.entrada.GetValue()    #Palabra a comprobar.
        sal= True                       #Por defecto es pronunciable.
        nx= 0                           #Primera letra de la palabra.

        #........................Bucle principal................................
        while (sal == True and nx != 0):
            for n in range(nx, len(pal)):
                #Si la palabra es de una sola letra.
                if len(pal) == 1:
                    if pal in vocal:
                        pass
                    else:
                        sal= False
                #Consonante doble.
                if pal[n] in con_doble:
                    if pal[n-1] in vocal:       #Vocal delante.
                        pass
                    if pal[n+1] in vocal:       #Vocal detras.
                        pass
                    if pal[n+1] == palabra[n]:  #Hay una repetida.
                        if palabra[n+2] in vocal:
                            nx =+ 2
                        else:
                            sal= False
                #Consonante solo con vocal.
                if pal[n] in con_vocal:
                    if pal[n-1] in vocal:       #Vocal delante.
                        pass
                    if pal[n+1] in vocal:       #Vocal detras.
                        pass
                    else:
                        if pal[n+2] in vocal:
                            nx =+ 3
                        else:
                            sal= False
                #Consonante con R.
                if pal[n] in con_R:
                    if pal[n-1] in vocal:       #Vocal delante.
                        pass
                    if pal[n+1] in vocal:       #Vocal detras.
                        pass
                    if pal[n+1:n+2] in pr:      #Consonante con R y vocal.
                        nx =+ 3
                    else:
                        sal= False
                #Consonante con RL.
                if pal[n] in con_RL:
                    if pal[n-1] in vocal:       #Vocal delante.
                        pass
                    if pal[n+1] in vocal:       #Vocal detras.
                        pass
                    if pal[n+1:n+2] in pr:
                        nx =+ 3
                        pass
                    if pal[n+1:n+2] in pl:
                        nx =+ 3
                        pass
                    else:
                        sal= False
                if pal[n] in q:                 #Letra CU (Q).
                    if pal[n+1:n+2] in pq:
                        nx =+ 3
                    else:
                        sal= False
                if pal[n] in c:                 #Letra CE.(C).
                    if pal[n-1] in vocal:       #Vocal delante.
                        pass
                    if pal[n+1] in vocal:       #Vocal detras.
                        pass
                    if pal[n+1:n+2] in pc:      #Sonido CHE (CH).
                        nx =+ 3
                    else:
                        sal= False
                if pal[n] in h:                 #Letra HACHE.(H).
                    if pal[n-1] in vocal:       #Vocal delante.
                        pass
                    if pal[n+1] in vocal:       #Vocal detras.
                        pass
                    if pal[n-1] in c:
                        if pal[n+1] in vocal:
                            pass
                        else:
                            sal= False


        #Salida de la respuesta.
        if sal == False:
            self.salida.SetValue('Impronunciable')
        if sal == True:
            self.salida.SetValue('Pronunciable')


    def OnSalirButton(self, event):
        self.Close()

    def OnEntradaTextEnter(self, event):
        event.Skip()
