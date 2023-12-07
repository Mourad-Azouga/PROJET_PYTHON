from header import *


class SalleScreen(Screen):
    def __init__(self, **kwargs):
        super(SalleScreen, self).__init__(**kwargs)

        amphi_layout = BoxLayout(orientation='vertical')
        amphi_layout.add_widget(Label(text="Amphi Window"))
        amphi_layout.add_widget(Button(text="Close", on_press=self.dismiss))
        self.add_widget(amphi_layout)

    def dismiss(self, instance):
        self.manager.current = 'main'
