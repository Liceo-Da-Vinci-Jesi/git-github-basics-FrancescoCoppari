# solitario

import wx
import random
import solitarioSchermataIniziale as ssi
import solitarioGrafica as sg

class GiocoSolitario:
    
    def __init__ (self):
        self.iniziale = ssi.Schermata() #crea come attributo la finestra schermata
        self.iniziale.Show()
        self.iniziale.pulsanteOk.Bind(wx.EVT_BUTTON, self.iniziaPartita)
        self.mazzo = self.creaMazzo()
        self.mischiaMazzo()
        print(self.mazzo)
        return
    
    def iniziaPartita (self,evt):
        nomeUtente = self.iniziale.tc1.GetValue()
        if nomeUtente != "":
            self.nomeUtente = self.iniziale.tc1.GetValue()
            self.iniziale.Hide()
            self.tabellone = sg.Solitario()
            self.tabellone.Show()
            self.creaManoGiocatore()
        return
    
    def creaMazzo (self):
        mazzo = []
        for seme in ("Denari", "Bastoni", "Coppe", "Spadi"):
            for numero in range (1,11):
                mazzo.append(seme + str(numero))
        return mazzo
    
    def mischiaMazzo (self):
        return random.shuffle(self.mazzo)
    
    def creaManoGiocatore (self):
        self.manoGiocatore = []
        self.manoGiocatore.append(self.mazzo[-1])
        self.manoGiocatore.append(self.mazzo[-2])
        self.manoGiocatore.append(self.mazzo[-3])
        self.manoGiocatore.append(self.mazzo[-4])
        self.mazzo.remove(self.mazzo[-1])
        self.mazzo.remove(self.mazzo[-2])
        self.mazzo.remove(self.mazzo[-3])
        self.mazzo.remove(self.mazzo[-4])
        bmp = wx.Bitmap("../carte/"+self.manoGiocatore[0]+".jpg")
        bmp.SetSize((100,180))
        self.tabellone.lista[-4].SetBitmap(bmp)
        return
        


    

if __name__ == "__main__" :
    app = wx.App()
    window = GiocoSolitario()
    app.MainLoop()
        