from rich import print
from rich.panel import Panel as p

class Panels:

    def __init__(self, text: str, title: str, padding: (int,int), subtitle: str = "", border: str = "") -> None:
        self._text = text
        self._title = title
        self._border = border
        self._subtitle = subtitle
        self._padding = padding
        self._panel = None

    def create_panel(self):
        self._panel = p(self._text, title = self._title,subtitle=self._subtitle, border_style = self._border, padding = self._padding, expand = False)

    def display_panel(self):
        print(self._panel)

    def clear_panel(self):
        print("\033c", end="")

    def clear_and_display_panel(self):
        print("\033c", end="")
        print(self._panel)

    def update_panel_text(self, text: str):
        self._panel.renderable = text

    def update_panel_title(self, title: str):
        self._panel.title = title

    def update_panel_subtitle(self, subtitle: str):
        self._panel.subtitle = subtitle

    def update_panel_color(self, color: str):
        self._panel.border_style = color

    def destroy_panel(self):
        self._panel = None


if __name__ == "__main__":
    p_test = Panels(f"Hello [red]w[/red]o[green]r[/green][yellow]l[/yellow][blue]d[/blue]!", "Test Panel", (1,3), "Made by Lytzeer", "red")
    p_test.create_panel()
    p_test.clear_panel()
    p_test.display_panel()