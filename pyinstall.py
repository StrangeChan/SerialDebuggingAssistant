import  os
# if __name__ == '__main__':
#     from PyInstaller.__main__ import run
#     opts=['main.py','-c','--icon=1.ico']
#     run(opts)

from PyInstaller.__main__ import run
if __name__ == '__main__':
    opts = ['-F', '-w','-d',
            '--paths=C:\\Users\\StrangeChen\\AppData\\Local\\Programs\\Python\\Python35\\Lib\site-packages\\PyQt5\\Qt\\bin',
            '--paths=C:\\Users\\StrangeChen\\AppData\\Local\\Programs\\Python\\Python35\\Lib\site-packages\\PyQt5\\Qt\\plugins',
            '--paths=E:\\myCode\\Python\\SerialDebuggingAssistant',
            '--paths=C:\\Windows\\SysWOW64\\downlevel',
            'main.py','--icon','1.ico', '--noupx', '--clean'
            ]
    run(opts)
