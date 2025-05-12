import os

roms_dir = 'roms'
output_file = '/var/www/html/nes.html'

roms = []
for root, _, files in os.walk(roms_dir):
    for f in files:
        if f.lower().endswith('.nes'):
            full_path = os.path.join(root, f)
            # Получаем путь относительно самой папки roms
            relative_path = os.path.relpath(full_path, start=roms_dir)
            roms.append(relative_path.replace('\\', '/'))  # на случай Windows-путей

roms.sort()

with open(output_file, 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html><html><head><meta charset="utf-8"><title>NES ROMs</title></head><body>')
    f.write('<h1>NES ROMs</h1><ul>')
    for rom in roms:
        label = os.path.basename(rom)
        f.write(f'<li><a href="/?core=nestopia&rom={rom}">{label}</a></li>')
    f.write('</ul></body></html>')
