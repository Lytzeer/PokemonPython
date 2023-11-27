from rich import print
from rich.progress_bar import ProgressBar

class Healthbar:
    def __init__(self,name,maxHealth,Health) -> None:
        self._name = name
        self._maxHealth = maxHealth
        self._Health = Health
        self._progress_bar = None

    def update_health(self,health):
        self._Health = health
        self._progress_bar.update(health)

    def update_name(self, name):
        self._name = name

    def create_healthbar(self):
        self._progress_bar=ProgressBar(self._maxHealth, self._Health,40, style="white", complete_style="red", finished_style="red",)

    def display_healthbar(self):
        print(f"[green]{self._name}[/green]")
        print(self._progress_bar)
        print(f" {self._Health}/{self._maxHealth}")

    def clear_healthbar(self):
        print("\033c", end="")

    def clear_and_display_healthbar(self):
        print("\033c", end="")
        self.display_healthbar()

    def destroy_healthbar(self):
        self._progress_bar = None

if __name__ == "__main__":
    h_test = Healthbar("Test", 100, 100)
    h_test.create_healthbar()
    h_test.display_healthbar()
    h_test.clear_healthbar()
    h_test.update_health(50)
    h_test.display_healthbar()