# global_storage.py
commands_by_tick = {}
max_tick = 0
g = 9.8
def update_max_tick(tick):
    global max_tick
    if tick > max_tick:
        max_tick = tick

def add_command(tick, command):
    update_max_tick(tick)
    if tick not in commands_by_tick:
        commands_by_tick[tick] = []
    commands_by_tick[tick].append(command)
