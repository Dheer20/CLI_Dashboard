from rich.panel import Panel
from rich.console import Group
from rich.live import Live
from time import strftime
from rich.layout import Layout
from rich.align import Align
from widgets.quote import get_random_quote
from widgets.weather import get_weather
from widgets.system_stats import get_system_stats

def build_dashboard():

    layout = Layout()

    layout.split_column(
        Layout(name="upper",ratio=2),
        Layout(name="lower",ratio=1)
    )

    layout["upper"].split_row(
        Layout(name="weather"),
        Layout(name="system_stats")
    )
    
    weather_text = get_weather()

    system_stats,battery_stats = get_system_stats()
    cpu_text = f"{system_stats}\n🕒 Time         : {strftime('%H:%M:%S')}\n"

    layout["weather"].update(
        Panel(Align.center(weather_text,vertical="middle"), title="☁️   Weather", border_style="cyan", expand=True)
    )
    layout["system_stats"].update(
        Panel(
            Align.center(Group(
                cpu_text,
                battery_stats),vertical="middle"),
                title="⚙️  System Stats",
                border_style="green",
                expand=True),
    )
    layout["lower"].update(
        Panel(Align.center(get_random_quote(),vertical="middle"), title="💬 Quote of the Day", border_style="magenta", expand=True)
    )

    return layout

if __name__ == "__main__":
    with Live(build_dashboard(), refresh_per_second=1) as live:
        while True:
            live.update(build_dashboard())