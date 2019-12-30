import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Por algum motivo não foi possível abrir o site "http://www.pudim.com.br"')
else:
    print('O site está funcionando normalmente!')
