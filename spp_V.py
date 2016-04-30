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

        pal= self.entrada.GetValue()
        #Lista de las vocales, las acentuadas y la u con dieresis.
        v= ['A','E','I','O','U',u'Á',u'É',u'Í',u'Ó',u'Ú',u'a', u'e', u'i', u'o', u'u', u'á',
            u'é', u'í', u'ó', u'ú', u'ü', 'y']
        #Lista posibilidades con la R
        pr= ['ra', 're', 'ri', 'ro', 'ru', u'rá', u'ré', u'rí',u'ró', u'rú']
        #Lsta posibilidades con la L
        pl= ['la', 'le', 'li', 'lo', 'lu', 'lá', 'lé', 'lí', 'ló', 'lú']
        #Lista letra tras Q
        q= ['ue',  'ué', 'ui', u'uí']


        #Minima espresión pronunciable
        def voc (pal):
            """Comprueba que hay vocales"""
            #Determina si pal tiene alguna vocal.
            #Devuelve True en caso de que tenga alguna y False si no hay vocal.
            sal= False
            for i in v:

                if i in pal:
                    sal= True
                    break
                break
            return sal


        def con (pal):
            """Comprueba las consonantes"""

            p= -1    #Para acceder a las compañeras de sílaba.

            for x in pal:
                p =+1
                if x not in v:  #Si no es vocal..
                    if pal[p-1:p] in v: #Lleva una vocal delante.
                        sa= True
                    if pal[p+1] in v:   #Lleva una vocal detrás
                        sa= True
                    if pal[p+1:p+3] in pr:  #Lleva R
                        sa= True
                    if pal[p+1:p+3] in pl:  #Lleva L
                        sa= True
            return sa




##                if x in cr: #Algunas consonantes no admiten L...creo
##                    if pal[p-1:p] in v:
##                        sa= True
##                    if pal[p+1] in v:
##                        sa= True
##                    if pal[p+1:p+3] in pr:
##                        sa= True
##                if x == 'q':
##                    if pal [p+1:p+3] in q:
##                        sa= True
##                if x == 'h':
##                    if pal[p+1] in v:
##                        sa= True
##                    if pal[p-1] in v:
##                        sa= True
##                    if pal[p-1] == 'c':
##                        if pal[p+1] in v:
##                            sa= True



        def pro(pal):
            voc(pal)
            if sal== True:
                con(pal)
                if sa:
                    self.salida.SetValue('Pronunciable')
            else:
                self.salida.SetValue('Impronunciable')

        pro(pal)


    def OnSalirButton(self, event):
        self.Close()

    def OnEntradaTextEnter(self, event):
        event.Skip()
