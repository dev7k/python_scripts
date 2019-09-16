import os
from subprocess import Popen, PIPE


def run_command(command):
    print('Executing command: *** {0} ***'.format(command))
    process = Popen(command, shell=True, stdout=PIPE)
    process.wait()
    if (process.returncode != 0):
        raise SystemExit('Error during execution: *** {0} ***'.format(command))


# MY_APP_DIR = 'C:\\TOOLS\\MY_APP'
# SCRIPTS_PATH = 'C:\\SHARE\\SCRIPTS'

# command_setup = os.path.join(MY_APP_DIR, 'bin', 'app.exe'), '--config', 'setScriptDirs', SCRIPTS_PATH
# run_command(command_setup)

command_display = 'echo message'
run_command(command_display)
