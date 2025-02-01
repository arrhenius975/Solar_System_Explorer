from rich.console import Console
from src.ui_handler import UIHandler

console = Console()

def main():
    try:
        ui = UIHandler()
        ui.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]Program terminated by user.[/yellow]")
    except Exception as e:
        console.print(f"\n[red]An unexpected error occurred: {str(e)}[/red]")
    finally:
        console.print("\n[green]Thank you for using Solar System Explorer![/green]")

if __name__ == "__main__":
    main()
