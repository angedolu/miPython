# -*- coding: utf-8 -*-
"""Este programa determina si una palabra se puede pronunciar."""

#Lista de las vocales, las acentuadas y la u con diéresis.
v= ['A','E','I','O','U','Á','É','Í','Ó','Ú','a', 'e', 'i', 'o', 'u', 'á',
    'é', 'í', 'ó', 'ú', 'ü', 'y']
#Lista posibilidades con la R
pr= ['ra','re','ri','ro','ru','rá','ré','rí','ró','rú']
#Lsta posibilidades con la L
pl= ['la','le','li','lo','lu','lá','lé','lí','ló','lú']
#Lista letra tras Q
q= ['ue', 'ué', 'ui', 'uí']

p= 0


#Minima espresión pronunciable
def voc (pal):
    """Una palabra sin vocales ni Y, no se puede pronunciar"""
    #Determina si pal tiene alguna vocal.
    #Devuelve True en caso de que tenga alguna y False si no hay vocal.
    spp= False
    for i in v:
        if i in pal:
            spp= True
            break
    return spp

def con (pal):
    """Comprueba si las consonantes de una palabra se pueden pronunciar"""
    #p se necesita para acceder a la letra de delante y a las de detrás.
    p= -1
    spp= False
    for x in pal:
        p =+1
        if x in crl:
            if pal[p-1:p] in v:
                spp= True
            if pal[p+1] in v:
                spp= True
            if pal[p+1:p+3] in pr:
                spp= True
            if pal[p+1:p+3] in pl:
                spp= True
        if x in cr:
            if pal[p-1:p] in v:
                spp= True
            if pal[p+1] in v:
                spp= True
            if pal[p+1:p+3] in pr:
                spp= True
        if x == 'q':
            if pal [p+1:p+3] in q:
                spp= True
        if x == 'h':
            if pal[p+1] in v:
                spp= True
            if pal[p-1] in v:
                spp= True
            if pal[p-1] == 'c':
                if pal[p+1] in v:
                    spp= True


    return spp


def pro(palabra):
    if voc(palabra) == True:
        if con(palabra) == True:
            return True
    return False
