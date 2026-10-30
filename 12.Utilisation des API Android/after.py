
from kivy.app import App
from kivy.uix.label import Label
from plyer import notification


class AndroidApp(App):
    def build(self):
        try:
            notification.notify(
                title="Some title",
                message="Some message text"
            )
        except Exception as e:
            print(f"Erreur de notification : {e}")

        return Label(text="Test des notifications Plyer")


if __name__ == "__main__":
    AndroidApp().run()

