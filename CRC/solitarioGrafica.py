# solitario

import wx

class Solitario(wx.Frame):
    def __init__(self):
        super().__init__(None, title = "Gioco del Tris")

        
        panel = wx.Panel(self)
        grid = wx.GridSizer(rows = 6, cols = 10, vgap = 5, hgap = 5)
        font = wx.Font(50,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        panel.SetBackgroundColour("green")
        self.lista=[]
        
        c0 = wx.StaticText(panel, label="")
        c1 = wx.StaticText(panel, label="1")
        c2 = wx.StaticText(panel, label="2")
        c3 = wx.StaticText(panel, label="3")
        c4 = wx.StaticText(panel, label="4")
        c5 = wx.StaticText(panel, label="5")
        c6 = wx.StaticText(panel, label="6")
        c7 = wx.StaticText(panel, label="7")
        c8 = wx.StaticText(panel, label="8")
        c9 = wx.StaticText(panel, label="9")
        grid.Add(c0,proportion = 0, flag = wx.ALL, border = 0)

        grid.Add(c1,proportion = 0, flag = wx.ALL, border = 0)
        grid.Add(c2,proportion = 0, flag = wx.ALL, border = 0)
        grid.Add(c3,proportion = 0, flag = wx.ALL, border = 0)
        grid.Add(c4,proportion = 0, flag = wx.ALL, border = 0)
        grid.Add(c5,proportion = 0, flag = wx.ALL, border = 0)
        grid.Add(c6,proportion = 0, flag = wx.ALL, border = 0)
        grid.Add(c7,proportion = 0, flag = wx.ALL, border = 0)
        grid.Add(c8,proportion = 0, flag = wx.ALL, border = 0)
        grid.Add(c9,proportion = 0, flag = wx.ALL, border = 0)


        
        spade = wx.StaticText(panel, label="spade")
        grid.Add(spade,proportion = 0, flag = wx.ALL, border = 0)
 
        for n in range(1,10):
            bmp = wx.Bitmap("../carte/Retro1.jpg")
            bmp.SetSize((100,180))
            nome = wx.BitmapButton(panel, bitmap = bmp, id = n, size = (2000,800))
            grid.Add(nome, proportion = 1, flag = wx.EXPAND)

            self.lista.append(nome)
        

         
        bastoni = wx.StaticText(panel, label="bastoni")
        grid.Add(bastoni,proportion = 0, flag = wx.ALL, border = 0)
 
        for n in range(1,10):
            bmp = wx.Bitmap("../carte/Retro1.jpg")
            bmp.SetSize((100,180))
            nome = wx.BitmapButton(panel, bitmap = bmp, id = n, size = (2000,800))
            grid.Add(nome, proportion = 1, flag = wx.EXPAND)

            self.lista.append(nome)
        
      
        
        coppe = wx.StaticText(panel, label="coppe")
        grid.Add(coppe,proportion = 0, flag = wx.ALL, border = 0)
 
        for n in range(1,10):
            bmp = wx.Bitmap("../carte/Retro1.jpg")
            bmp.SetSize((100,180))
            nome = wx.BitmapButton(panel, bitmap = bmp, id = n, size = (2000,800))
            grid.Add(nome, proportion = 1, flag = wx.EXPAND)

            self.lista.append(nome)
            
        denari = wx.StaticText(panel, label="denari")
        grid.Add(denari,proportion = 0, flag = wx.ALL, border = 0)
 
        for n in range(1,10):
            bmp = wx.Bitmap("../carte/Retro1.jpg")
            bmp.SetSize((100,180))
            nome = wx.BitmapButton(panel, bitmap = bmp, id = n, size = (2000,800))
            grid.Add(nome, proportion = 1, flag = wx.EXPAND)

            self.lista.append(nome)
            
        vuoto = wx.StaticText(panel, label="")
        vuoto2 = wx.StaticText(panel, label="")
        vuoto3 = wx.StaticText(panel, label="")
        
        grid.Add(vuoto, proportion = 1, flag = wx.EXPAND)
        grid.Add(vuoto2, proportion = 1, flag = wx.EXPAND)
        grid.Add(vuoto3, proportion = 1, flag = wx.EXPAND)

        
               
        for n in range(4):
            bmp = wx.Bitmap("../carte/Retro1.jpg")
            bmp.SetSize((100,180))
            nome = wx.BitmapButton(panel, bitmap = bmp, id = n, size = (2000,800))
            grid.Add(nome, proportion = 1, flag = wx.EXPAND)
            self.lista.append(nome)
        
        self.SetMinSize( (1000,800) )
        self.SetMaxSize( (1000,800) )
        panel.SetSizer(grid)
        self.Centre()
        
    def Chiudi (self,evt):
            return
        
        
if __name__ == "__main__" :
    app = wx.App()
    window = Solitario()
    window.Show()
    app.MainLoop()
        











