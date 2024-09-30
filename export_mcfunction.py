# export_mcfunction.py
import os
import global_storage

def export_mcfunction(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for tick in range(global_storage.max_tick + 1):
        filename = os.path.join(output_dir, f'{tick}.mcfunction')
        f = open(filename, 'w')
        for cmd in global_storage.commands_by_tick[tick]:
            f.write(f'{cmd}\n')
