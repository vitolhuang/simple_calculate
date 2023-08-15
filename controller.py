class Control:
    def __init__(self, model, view):
        self.view = view
        self.mod = model

        for Button in self.view.Buttons:
            Button.clicked.connect(lambda *args, btn=Button: self.ChangeData(btn.text()))

        for OpButton in self.view.OpButtons:
            OpButton.clicked.connect(lambda *args, btn=OpButton: self.ChangeData(btn.text()))

    def ChangeData(self, number):
        self.mod.operate(number)
        self.view.UpdateLabel(self.mod.GetValue())
