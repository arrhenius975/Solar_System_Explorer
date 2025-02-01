import json
from pathlib import Path
from typing import Dict, Any, Optional
from rich.console import Console
from rich.table import Table
import os

console = Console()

class PlanetData:
    def __init__(self, data_file: str = None):
        if data_file is None:
            current_dir = Path(__file__).parent.parent
            data_file = current_dir / "data" / "planets.json"
        self.data_file = Path(data_file)
        self._data: Dict[str, Any] = {}
        self.load_data()
    
    def load_data(self) -> None:
        """Load planet data"""
        try:
            if not self.data_file.exists():
                console.print(f"[red]Error: Could not find planet data file at {self.data_file}[/red]")
                self._data = {}
                return

            with open(self.data_file, 'r', encoding='utf-8') as f:
                self._data = json.load(f)
                console.print(f"[green]Successfully loaded planet data from {self.data_file}[/green]")
        except json.JSONDecodeError as e:
            console.print(f"[red]Error: Invalid JSON format in {self.data_file}[/red]")
            console.print(f"[red]Details: {str(e)}[/red]")
            self._data = {}
        except Exception as e:
            console.print(f"[red]Error loading planet data: {str(e)}[/red]")
            self._data = {}

    def get_planet_info(self, planet_name: str) -> Optional[Dict[str, Any]]:
        return self._data.get(planet_name)

    def list_planets(self) -> list:
        return list(self._data.keys())

    def display_planet_info(self, planet_name: str) -> None:
        planet_data = self.get_planet_info(planet_name)
        if not planet_data:
            console.print(f"[red]Planet '{planet_name}' not found.[/red]")
            return

        # Create info table
        table = Table(title=f"[bold cyan]{planet_name} - Detailed Information[/bold cyan]")
        table.add_column("Property", style="green")
        table.add_column("Value", style="yellow")

        for key, value in planet_data.items():
            if key not in ['interesting_facts', 'nasa_3d_url']:
                if isinstance(value, (str, int, float)):
                    table.add_row(key.replace('_', ' ').title(), str(value))

        console.print(table)

        # Display interesting facts
        if 'interesting_facts' in planet_data:
            console.print("\n[bold cyan]Interesting Facts:[/bold cyan]")
            for fact in planet_data['interesting_facts']:
                console.print(f"[yellow]• {fact}[/yellow]")

    def get_nasa_url(self, planet_name: str) -> Optional[str]:
        planet_data = self.get_planet_info(planet_name)
        return planet_data.get('nasa_3d_url') if planet_data else None
