# -*- coding: utf-8 -*-
#Boa:App:BoaApp

import wx

import spp_V_viejo

modules ={u'spp_V_viejo': [1, 'Main frame of Application', u'spp_V_viejo.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = spp_V_viejo.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
