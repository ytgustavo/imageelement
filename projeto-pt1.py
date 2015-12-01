# -*- coding: UTF-8 -*-
'''
Created on 21/11/2015

@author: ytallo
'''

#!!!:alterar

imagemDeEntrada = "boneco.png"


import sys
import math

#-----instalar essas bibliotecas----
import numpy as np
from matplotlib import pyplot as plt
import cv2
#----------------------------------

PI = 3.141592653589793 #!!!



#-----1ª Etapa: Converter em Tons de Cinza-----
def converteImagemEmTonsDeCinza(image):
    
    # grayscale
    scale = (0.299, 0.587, 0.114)
    # get image dimensions
    width = image.shape[1] #openCV
    height = image.shape[0]#openCV
    # convert pixels
    for x in range(0, height):
        for y in range(0, width):
            value = (scale[0] * image.item(x, y, 0)) + (scale[1] * image.item(x, y, 1)) + (scale[2] * image.item(x, y, 2))
            for pI in range(0, 3):
                image.itemset((x, y, pI), value)

#---fim---- de converteImagemEmTonsDeCinza



def applyLaplacianOperator(image):
    # operators
    lX = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    lY = [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
    # get image dimensions
    width = image.shape[1]
    height = image.shape[0]
    # create a blank image to draw edges
    blankImage = np.zeros((height, width, 3), np.uint8)
    # apply filters
    for x in range(1, height-1):
        for y in range(1, width-1):
            pixelX = [0, 0, 0]
            pixelY = [0, 0, 0]
            # evaluate x, y
            for sX in range(0, 3):
                for sY in range(0, 3):
                    for pI in range(0, 3):
                        pixelX[pI] += (lX[sX][sY] * image.item(x+(sX-1), y+(sY-1), pI))
                        pixelY[pI] += (lY[sX][sY] * image.item(x+(sX-1), y+(sY-1), pI))
            for pI in range(0, 3):
                # calculate the gradient magnitude
                mag = math.hypot(pixelX[pI], pixelY[pI])
                # draw edges
                blankImage.itemset((x, y, pI), mag)
    return blankImage
                
def applySobelOperator(image):
    # sobel operators
    sobelX = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobelY = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    # get image dimensions
    width = image.shape[1]
    height = image.shape[0]
    # create a blank image to draw edges
    blankImage = np.zeros((height, width, 3), np.uint8)
    # apply filters
    for x in range(1, height-1):
        for y in range(1, width-1):
            pixelX = [0, 0, 0]
            pixelY = [0, 0, 0]
            # evaluate x, y
            for sX in range(0, 3):
                for sY in range(0, 3):
                    for pI in range(0, 3):
                        pixelX[pI] += (sobelX[sX][sY] * image.item(x+(sX-1), y+(sY-1), pI))
                        pixelY[pI] += (sobelY[sX][sY] * image.item(x+(sX-1), y+(sY-1), pI))
            for pI in range(0, 3):
                # calculate the gradient magnitude
                mag = math.hypot(pixelX[pI], pixelY[pI])
                # draw edges
                blankImage.itemset((x, y, pI), mag)
    return blankImage





#---------------main-------------------
#carregando a imagem...
imagemCarregada = cv2.imread(imagemDeEntrada)
cv2.imshow("Imagem Original", imagemCarregada )#exibe a imagem em uma janela



#carregando e exibindo a imagem em tons de cinza
imagemEmTonsDeCinza = cv2.imread(imagemDeEntrada)

converteImagemEmTonsDeCinza(imagemEmTonsDeCinza)
cv2.imshow("Imagem Pós Conversão em Tons de Cinza", imagemEmTonsDeCinza )

filtroImage = applySobelOperator(imagemEmTonsDeCinza)
#filtroImage = applyLaplacianOperator(imagemEmTonsDeCinza)
cv2.imshow("Suavizada", filtroImage )



#salvando a imagem
#cv2.imwrite("novaLampada.png", fatiaImagem)

#fim
cv2.waitKey(0) #esperando alguma tecla ser apertada para finalizar

#-------------------'main'-------------------




