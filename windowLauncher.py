try:
    import wx
except ImportError:
    raise ImportError,"The wxPython module is required to run this program"

import maingame
import player
import characters
import roles

class simpleapp_wx(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

        self.entry = wx.TextCtrl(self,-1,value=u"Enter name here.")
        sizer.Add(self.entry,(0,0),(1,1),wx.EXPAND)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnPressEnter, self.entry)

        button = wx.Button(self,-1,label="Click me !")
        sizer.Add(button, (0,1))
        self.Bind(wx.EVT_BUTTON, self.OnButtonClick, button)


        self.label = wx.StaticText(self,-1,label=u'Hello !')
        self.label.SetBackgroundColour(wx.BLUE)
        self.label.SetForegroundColour(wx.WHITE)
        sizer.Add( self.label, (1,0),(1,2), wx.EXPAND )

        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1,self.GetSize().y,-1,self.GetSize().y );
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)
        self.Show(True)
        self.battle = None

    def OnButtonClick(self,event):
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)

        if self.battle == None :
            self.label.SetLabel("Starting game")

            p1Name = str(self.entry.GetValue())
            p2Name = "Demon"

            self.p1 = player.Player(p1Name, roles.GrandWizard)
            self.p2 = player.Player(p2Name, roles.DarkLord)

            self.p1.addCardToDeck(characters.Paladin())
            self.p2.addCardToDeck(characters.Goblin())

            self.battle = self.p1.startBattle(self.p2)
        else :
            print("sdfsdf")

            if self.p1.holdsCards() and self.p2.holdsCards():
                self.battle.turns.runTurns()
            else :
                self.label.SetLabel("Game Over")



    def OnPressEnter(self,event):
        self.label.SetLabel( self.entry.GetValue() + " (You pressed ENTER)" )
        self.entry.SetFocus()
        self.entry.SetSelection(-1,-1)

if __name__ == "__main__":
    app = wx.App()
    frame = simpleapp_wx(None,-1,'my application')
    app.MainLoop()
