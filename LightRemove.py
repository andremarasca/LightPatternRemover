from os import listdir
from os.path import isfile, join
import os as osfnc

#%% Descobrir o nome de todas as imagens da base

# Para isso é necessário descobrir o diretório atual
# Em seguida apontar a pasta da base de imagens
# Descobrir o nome de todos os arquivos da pasta
# Filtrar apenas aqueles que são imagens e adicionar
# Na lista de imagens

# Descobrir o diretório atual
mypath = osfnc.getcwd()
# apontar a pasta que as minhas imagens estão
dirEntrada = mypath + '\\Entrada'
dirSaida = mypath + '\\Saida'
# Criar uma lista de imagens
soimagens = []
# Iterar cada um dos arquivos dentro de mypath
for f in listdir(dirEntrada):
    #Calcular o diretório completo do arquivo
    aa = join(dirEntrada, f)
    # verificar se é um arquivo ou não
    if isfile(aa):
        # Se for arquivo verificar se é .png
        if f.endswith(".png") or f.endswith(".jpg"):
            # Se for .png ou .jpg então adiciona na lista de imagens
            soimagens.append(f)

#%%
import numpy as np
import cv2

for u, nome_das_imagens in enumerate(soimagens):

    #%% Carrega imagem e transforma para cinza

    img = cv2.imread(join(dirEntrada, nome_das_imagens))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    #%% Criar uma imagem borrada

    img2 = img[:]
    kernel = np.ones((5,5),np.float32)/25
    for i in range(5):
        img2 = cv2.filter2D(img2,-1,kernel)

    #%% converter imagens para inteiro de 32 bits

    img = img.astype(np.int32)
    img2 = img2.astype(np.int32)

    #%% subtrai imagem borrada da original

    img = img - img2

    #%% Reescala imagem

    media = np.mean(img)
    desvio = np.std(img)

    img = 128 + (128/3)* (img - media) / desvio
    img[img < 0] = 0
    img[img > 255] = 255

    #%% Salvar saida

    img = img.astype(np.uint8)
    cv2.imwrite(join(dirSaida, nome_das_imagens), img)



