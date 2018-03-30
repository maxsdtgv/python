# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jul 27 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gSizer1 = wx.GridSizer(0, 2, 0, 0)

        self.m_checkBox1 = wx.CheckBox(self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer1.Add(self.m_checkBox1, 0, wx.ALL, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.Show()


# ------------ Event handlers



if __name__ == "__main__":
    app = wx.App(False)
    frame = MyFrame1()
    app.MainLoop()