from pyglet.text import Label

class Hud:
    def __init__(self, simulation_round, batch):
        self.round_label = Label(f"Round: {simulation_round}", x=20, y=520, color=(0,0,0,255), batch=batch)
        self.population_label = Label(x=120, y=520, color=(0,0,0,255), batch=batch)
        self. speed_label = Label(x=280, y=520, color=(0,0,0,255), batch=batch)

    def update(self, alive, population, speed):
        self.population_label.text = f"Population: {alive}/{population}"
        self.speed_label.text = f"Speed: {speed:.2f}"