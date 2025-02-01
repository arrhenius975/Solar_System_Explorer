import webbrowser
from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table
import pyfiglet
from .planet_data import PlanetData

console = Console()

class UIHandler:
    def __init__(self):
        self.planet_data = PlanetData()

    def display_banner(self):
        banner = pyfiglet.figlet_format("Solar System Explorer")
        console.print(Panel.fit(
            f"[bold yellow]{banner}[/bold yellow]",
            title="Welcome to Solar System Explorer",
            subtitle="Explore the Wonders of Our Solar System"
        ))

    def display_planet_menu(self) -> str:
        planets = self.planet_data.list_planets()
        
        console.print("\n[bold cyan]Available Planets:[/bold cyan]")
        for i, planet in enumerate(planets, 1):
            console.print(f"[yellow]{i}.[/yellow] {planet}")
        console.print(f"[yellow]9.[/yellow] Exit")
        
        while True:
            choice = Prompt.ask(
                "\nEnter the name of the planet you want to explore",
                choices=planets + ["9"],
                show_choices=False
            )
            if choice == "9":
                console.print("\n[green]Thank you for exploring the Solar System![/green]")
                exit(0)
            if choice in planets:
                return choice
            console.print("[red]Invalid planet name. Please try again.[/red]")

    def display_action_menu(self) -> str:
        console.print("\n[bold cyan]Available Actions:[/bold cyan]")
        console.print("[yellow]1.[/yellow] View Detailed Planet Information")
        console.print("[yellow]2.[/yellow] Explore Planet in NASA 3D Viewer")
        console.print("[yellow]3.[/yellow] Return to Planet Selection")

        return Prompt.ask(
            "\nChoose an action",
            choices=["1", "2", "3"],
            show_choices=False
        )

    def open_nasa_viewer(self, planet_name: str) -> None:
        url = self.planet_data.get_nasa_url(planet_name)
        if url:
            console.print(f"\n[green]Opening NASA 3D viewer for {planet_name}...[/green]")
            webbrowser.open(url)
        else:
            console.print(f"\n[red]NASA 3D viewer URL not found for {planet_name}[/red]")

    def run(self):
        while True:
            console.clear()
            self.display_banner()
            
            planet_name = self.display_planet_menu()
            
            while True:
                action = self.display_action_menu()
                
                if action == "1":
                    console.clear()
                    self.display_banner()
                    self.planet_data.display_planet_info(planet_name)
                    input("\nPress Enter to continue...")
                
                elif action == "2":
                    self.open_nasa_viewer(planet_name)
                    input("\nPress Enter to continue...")
                
                elif action == "3":
                    break
                
