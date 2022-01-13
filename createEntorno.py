import platform



sistema = platform.system()

if(sistema == 'Linux'):
    comando = "python3 -m venv entorn\nsource entorno/bin/activate\npython -m pip install -r requeriments.txt\npip freeze --local"
    print(comando)
else:
    pass