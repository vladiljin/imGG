import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout

class BoxLayoutMain(BoxLayout):
    pass
    #def __init__(self, **kwargs):
        #super(BoxLayoutMain, self).__init__(**kwargs)
        # Construct the path to the image file
        #self.image_path = os.path.join("data", "image.png")



class OverlayLayout(RelativeLayout):
    pass

class MyApp(App):
    def build(self):
        return BoxLayoutMain()

if __name__ == "__main__":
    MyApp().run()
