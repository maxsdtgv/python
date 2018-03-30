from test2_window_unit.test2_window_unit import MyFrame1, App


# ------------ Event handlers



if __name__ == "__main__":
    app = App(False)
    frame = MyFrame1(None)
    app.MainLoop()