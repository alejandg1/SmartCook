import subprocess
subprocess.run(['python', '-m', 'venv', 'venv'])
subprocess.run(['source', './venv/bin/activate'])
subprocess.run(['pip', 'install', '-r', 'dependencias.txt'])
