# basic_fireworks.py
import math
import random
import global_storage
import shared_functions
from global_storage import g

def basic_single_layer_firework(tick, x, y, z, start_color, end_color, speed, horizontal_angle_step, vertical_angle_step, duration, lifetime):
    t_step = 1.0 / 20  # 一秒20个tick
    initial_tick = tick  # 存储起始tick

    horizontal_angles = int(360 / horizontal_angle_step)
    vertical_angles = int(180 / vertical_angle_step)

    for i in range(horizontal_angles):
        for j in range(vertical_angles):
            # 随机生成水平和垂直角度偏移
            horizontal_angle_offset = random.uniform(-horizontal_angle_step / 2, horizontal_angle_step / 2)
            vertical_angle_offset = random.uniform(-vertical_angle_step / 2, vertical_angle_step / 2)

            # 计算粒子的初始方向
            horizontal_angle = (i * horizontal_angle_step + horizontal_angle_offset) % 360
            vertical_angle = (j * vertical_angle_step + vertical_angle_offset) % 180 - 90
            rad_horizontal = math.radians(horizontal_angle)
            rad_vertical = math.radians(vertical_angle)
            speed_ = speed + random.uniform(-speed / 12, speed / 12)
            vx0 = speed_ * math.cos(rad_vertical) * math.cos(rad_horizontal)
            vy0 = speed_ * math.sin(rad_vertical)
            vz0 = speed_ * math.cos(rad_vertical) * math.sin(rad_horizontal)

            t = 0
            n_tick = initial_tick  # 使用 n_tick 并重置为初始 tick
            while t <= duration:
                # 计算水平方向的位移
                k = 1.2  # 空气阻力系数
                m0 = 1.0  # 粒子质量
                vx = vx0 * math.exp(-k * t / m0)
                vz = vz0 * math.exp(-k * t / m0)
                x_ = x + (vx0 * m0 / k) * (1 - math.exp(-k * t / m0))
                z_ = z + (vz0 * m0 / k) * (1 - math.exp(-k * t / m0))

                # 计算垂直方向的位移
                y_ = y - (m0 * g * t / k) + (vy0 + (m0 * g / k)) * (m0 / k) * (1 - math.exp(-k * t / m0))

                # 计算颜色表达式
                color_expr = shared_functions.color_expression(start_color, end_color, lifetime)

                # 添加粒子指令
                shared_functions.add_firework_command(n_tick, round(x_, 4), round(y_, 4), round(z_, 4), lifetime * 20, color_expr)

                t += t_step
                n_tick += 1  # 增加n_tick

def calculate_inner_angle_steps(outer_horizontal_angle_step, outer_vertical_angle_step, inner_speed, outer_speed):
    # 内外层的半径比例
    radius_ratio = outer_speed / inner_speed

    # 根据半径比例调整内层的角度步长，使内层粒子的密度接近外层的密度
    inner_horizontal_angle_step = outer_horizontal_angle_step * radius_ratio
    inner_vertical_angle_step = outer_vertical_angle_step * radius_ratio

    return inner_horizontal_angle_step, inner_vertical_angle_step

def basic_double_layer_firework(tick, x, y, z, inner_start_color, inner_end_color, outer_start_color, outer_end_color, inner_speed, outer_speed, outer_horizontal_angle_step, outer_vertical_angle_step, duration, lifetime):
    # 计算内层的角度步长
    inner_horizontal_angle_step, inner_vertical_angle_step = calculate_inner_angle_steps(outer_horizontal_angle_step, outer_vertical_angle_step, inner_speed, outer_speed)

    # 生成内层烟花
    basic_single_layer_firework(tick, x, y, z, inner_start_color, inner_end_color, inner_speed, inner_horizontal_angle_step, inner_vertical_angle_step, duration, lifetime)
    # 生成外层烟花
    basic_single_layer_firework(tick, x, y, z, outer_start_color, outer_end_color, outer_speed, outer_horizontal_angle_step, outer_vertical_angle_step, duration, lifetime)

def rotate_vector(vx, vy, vz, rad_horizontal, rad_vertical):
    # 绕水平轴旋转
    cos_h = math.cos(rad_horizontal)
    sin_h = math.sin(rad_horizontal)
    x_ = vx * cos_h + vz * sin_h
    z_ = -vx * sin_h + vz * cos_h
    vx, vz = x_, z_

    # 绕垂直轴旋转
    cos_v = math.cos(rad_vertical)
    sin_v = math.sin(rad_vertical)
    y_ = vy * cos_v - vz * sin_v
    z_ = vy * sin_v + vz * cos_v
    vy, vz = y_, z_

    return vx, vy, vz

def directional_firework(tick, x, y, z, start_color, end_color, speed, direction_horizontal_angle, direction_vertical_angle, spread_angle, track_count, duration, lifetime):
    t_step = 1.0 / 20  # 一秒20个tick
    initial_tick = tick  # 存储起始tick

    for i in range(track_count):
        # 在spread_angle范围内添加随机偏移
        random_horizontal_angle = random.uniform(-spread_angle / 2, spread_angle / 2)
        random_vertical_angle = random.uniform(-spread_angle / 2, spread_angle / 2)
        
        total_horizontal_angle = direction_horizontal_angle + random_horizontal_angle
        total_vertical_angle = direction_vertical_angle + random_vertical_angle

        # 转换为弧度
        rad_horizontal = math.radians(total_horizontal_angle)
        rad_vertical = math.radians(total_vertical_angle)

        # 初始速度向量
        vx0 = speed * math.cos(rad_vertical) * math.cos(rad_horizontal)
        vy0 = speed * math.sin(rad_vertical)
        vz0 = speed * math.cos(rad_vertical) * math.sin(rad_horizontal)

        #print(f"vx0={vx0}, vy0={vy0}, vz0={vz0}")

        t = 0
        n_tick = initial_tick  # 使用 n_tick 并重置为初始 tick
        while t <= duration:
            # 计算水平方向的位移
            k = 1.2  # 空气阻力系数
            m0 = 2.0  # 粒子质量
            vx = vx0 * math.exp(-k * t / m0)
            vz = vz0 * math.exp(-k * t / m0)
            x_ = x + (vx0 * m0 / k) * (1 - math.exp(-k * t / m0))
            z_ = z + (vz0 * m0 / k) * (1 - math.exp(-k * t / m0))

            # 计算垂直方向的位移
            g = 9.8  # 重力加速度
            y_ = y - (m0 * g * t / k) + (vy0 + (m0 * g / k)) * (m0 / k) * (1 - math.exp(-k * t / m0))

            # 计算颜色表达式
            color_expr = shared_functions.color_expression(start_color, end_color, lifetime)

            # 添加粒子指令
            shared_functions.add_firework_command(n_tick, round(x_, 4), round(y_, 4), round(z_, 4), lifetime * 20, color_expr)

            t += t_step
            n_tick += 1  # 增加n_tick

def clustered_firework(tick, x, y, z, start_color, end_color, speed, horizontal_angle_step, vertical_angle_step, track_count, spread_angle, duration, lifetime):
    horizontal_angles = int(360 / horizontal_angle_step)
    vertical_angles = int(180 / vertical_angle_step)
    for i in range(horizontal_angles):
        for j in range(vertical_angles):
            # 随机生成水平和垂直角度偏移
            horizontal_angle_offset = random.uniform(-horizontal_angle_step / 4, horizontal_angle_step / 4)
            vertical_angle_offset = random.uniform(-vertical_angle_step / 4, vertical_angle_step / 4)
            horizontal_angle = (i * horizontal_angle_step + horizontal_angle_offset) % 360
            vertical_angle = (j * vertical_angle_step + vertical_angle_offset) % 180 - 90
            #print(f"{horizontal_angle}, {vertical_angle}")
            directional_firework(tick, x, y, z, start_color, end_color, speed, horizontal_angle, vertical_angle, spread_angle, track_count, duration, lifetime)