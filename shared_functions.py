# shared_functions.py
import global_storage
def color_expression(start_color, end_color, lifetime):
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    return f"x=0;y=0;z=0;cr=({r1}+({r2}-{r1})*(t/{lifetime}))/255.0;cg=({g1}+({g2}-{g1})*(t/{lifetime}))/255.0;cb=({b1}+({b2}-{b1})*(t/{lifetime}))/255.0"

def add_firework_command(tick, x, y, z, lifetime, color_expr):
    command = f'particleex rgbatickparameter minecraft:end_rod {round(x, 4)} {round(y, 4)} {round(z, 4)} 0.0 0.0 0.0 0.0 1.0 "{color_expr}" 0.1 1 {int(lifetime)}'
    global_storage.add_command(tick, command)

def add_spark_command(tick, x, y, z, vx, vy, vz, lifetime):
    command = f'particleex normal minecraft:end_rod {round(x, 4)} {round(y, 4)} {round(z, 4)} 1.0 1.0 1.0 1.0 {round(vx, 4)} {round(vy, 4)} {round(vz, 4)} 0 0 0 1 {int(lifetime)}'
    global_storage.add_command(tick, command)

def add_thick_spark_command(tick, x, y, z, vx, vy, vz, lifetime, range_x, range_y, range_z, particle_count):
    command = f'particleex normal minecraft:end_rod {round(x, 4)} {round(y, 4)} {round(z, 4)} 1.0 1.0 1.0 1.0 {round(vx, 4)} {round(vy, 4)} {round(vz, 4)} {round(range_x, 4)} {round(range_y, 4)} {round(range_z, 4)} {particle_count} {int(lifetime)}'
    global_storage.add_command(tick, command)