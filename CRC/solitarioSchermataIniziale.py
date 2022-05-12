# solitario schermata iniziale

import wx
import webbrowser

class Schermata(wx.Frame):

    def __init__(self):
        super().__init__(None, title="Schermata iniziale solitario")

        panel = wx.Panel(self)
        panel.SetBackgroundColour("green")
        vbox = wx.BoxSizer(wx.VERTICAL)
        
        hbox11 = wx.BoxSizer(wx.HORIZONTAL)
        st11 = wx.StaticText(panel, label="")
        hbox11.Add(st11, proportion = 0 , flag = wx.ALL, border = 5)
        vbox.Add(hbox11,proportion = 0 , flag = wx.ALL | wx.EXPAND, border = 5)
        
#----------------------------------------------------------------------------------

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label="Inserisci il nome del giocatore ->")
        self.tc1 = wx.TextCtrl(panel)
        hbox1.Add(st1, proportion = 0 , flag = wx.ALL, border = 5)
        hbox1.Add(self.tc1, proportion = 1, flag = wx.ALL, border = 5)
        vbox.Add(hbox1,proportion = 0 , flag = wx.ALL | wx.EXPAND, border = 5)
        
#------------------------------------------------------------------------------------
        
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        st2 = wx.StaticText(panel, label="Le regole del solitario ->")
        hbox2.Add(st2, proportion = 0 , flag = wx.ALL, border = 5)
        self.pulsante = wx.Button(panel, label="Regolamento")
        self.pulsante.Bind(wx.EVT_BUTTON, self.Regolamento)
        hbox2.Add(self.pulsante, proportion = 0, flag = wx.ALL, border = 5)
        vbox.Add(hbox2,proportion = 0 , flag = wx.ALL | wx.ALIGN_CENTER , border = 5)
        
#----------------------------------------------------------------------
        
        hbox4 = wx.BoxSizer(wx.HORIZONTAL)
        self.pulsanteOk = wx.Button(panel, label="Inizia a giocare")
        hbox4.Add(self.pulsanteOk, proportion = 0, flag = wx.ALL, border = 5)
        vbox.Add(hbox4, proportion = 0, flag = wx.ALL | wx.ALIGN_CENTER, border = 5)

        panel.SetSizer(vbox)
        self.Centre()
    
    def Regolamento(self,evt):
        webbrowser.open("http://www.solitariconlecarte.it/solitariodinapoleone.html")
        return

# ----------------------------------------
if __name__ == "__main__":
    app = wx.App()
    window = Schermata()
    window.Show()
    app.MainLoop()