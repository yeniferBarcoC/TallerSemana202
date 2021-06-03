""" Taller 2.2 Espacios de Color #
    Yenifer Barco Castrillón
    Mayo 15-2021 """

# Definición de Funciones (Dividir)

#======================================================================
#          E S P A C I O    P R E _ _ C O N F I G U R A D O
# =====================================================================
def convertir_yiq_a_rva(y,i,q):
  """ 
  Parameters
  ----------
  y,i,q:float
     valores del espacio de color YIQ
  Returns
  -------
  r,v,a:float
     valores del espacio de color RVA    
  """ 
  r = y+0.955*i+0.618*q
  v = y-0.271*i-0.645*q
  a = y-1.11*i+1.7*q

  return r,v,a
#-------------------------------------------
def convertir_yiq_a_ycbcr(y,i,q): 
  """ 
  Parameters
  ----------
  y,i,q:float
     valores del espacio de color YIQ
  Returns
  -------
  y,cb,cr:float
     valores del espacio de color YCbCr
  """ 
  #Se hace aqui la conversión intermedia
  r = y+0.955*i+0.618*q
  v = y-0.271*i-0.645*q
  a = y-1.11*i+1.7*q 
  
  #Se hace aqui la conversión que se pide
  y = 0.299*r+0.587*v+0.114*a
  cb = 0.1687*r-0.3313*v-0.5*a
  cr = 0.5*r-0.418*v+0.0813*a

  return y,cb,cr
#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================
def convertir_rva_a_yiq(r,v,a):
  """
  Parameters
  ---------------
  r,v,a:float
     valores del espacio de color RVA
  Returns
  ---------------
  y,i,q
     valores del espacio de color YIQ
  """

  y=0.299*r+0.587*v+0.114*a
  i=0.596*r-0.275*v-0.321*a
  q=0.212*r-0.528*v+0.311*a

  return y,i,q
#-------------------------------------------
def convertir_rva_a_ycbcr(r,v,a):
  """ 
    Parameters
    ----------
    r,v,a:float
     valores del espacio de color RVA
    Returns
     -------
    y,cb,cr:float
     valores del espacio de color YCbCr
  """ 

  y=0.299*r+0.587*v+0.114*a
  cb=0.1687*r-0.3313*v-0.5*a
  cr=0.5*r-0.418*v+0.0813*a

  return y,cb,cr
#-------------------------------------------
def convertir_ycbcr_a_yiq(y,cb,cr):
  """ 
    Parameters
    ----------
    y,cb,cr:float
     valores del espacio de color YCbCr
    Returns
     -------
    y,i,q:float
     valores del espacio de color YIQ
  """
  #Conversion intermedia
  r=1*y+0*cb+1.402*cr
  v=1*y+0.344*cb-0.714*cr
  a=1*y+1.772*cb+0*cr

  #Conversion a YIQ
  y=0.299*r+0.587*v+0.114*a
  i=0.596*r-0.275*v-0.321*a
  q=0.212*r-0.528*v+0.311*a

  return y,i,q 

def convertir_ycbcr_a_rva(y,cb,cr):
  """ 
    Parameters
    ----------
    y,cb,cr:float
     valores del espacio de color YCbCr
    Returns
     -------
    r,v,a:float
     valores del espacio de color RVA
  """
  r=1*y+0*cb+1.402*cr
  v=1*y+0.344*cb-0.714*cr
  a=1*y+1.772*cb+0*cr

  return r,v,a 


#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================

#lectura espacio de color RVA 
r = float(input("Digite el valor de r:"))
v = float(input("Digite el valor de v:"))
a = float(input("Digite el valor de a:"))


#lectura espacio de color YIQ 
y = float(input("\nDigite el valor de Y:"))
i = float(input("Digite el valor de I:"))
q = float(input("Digite el valor de Q:"))

#lectura espacio de color YCbCr 
y = float(input("\nDigite el valor de Y:"))
cb = float(input("Digite el valor de Cb:"))
cr = float(input("Digite el valor de Cr:"))


#Llamado/invocación de funciones

"""Se utilizan otras variables para guardar lo que retorna la funciòn
para no cambiar el valor de las entradas por teclado"""

#YIQ a RVA
rt,vt,at= convertir_yiq_a_rva(y,i,q)
print("\nla conversión de yiq a rva es","r=",rt,"v=",vt,"a=",at)

#YIQ a YCbCr
yt,cbt,crt=convertir_yiq_a_ycbcr(y,i,q)
print("la conversión de yiq a yCbCr es","y=",yt,"Cb=",cbt,"Cr=",crt)

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# =====================================================================

#RVA a YIQ
yp,ip,qp = convertir_rva_a_yiq(r,v,a)
print("la conversión de rva a yiq es","y=",yp,"i=",ip,"q=",qp)

#RVA a YCbCr
yl,cbl,crl = convertir_rva_a_ycbcr(r,v,a)
print("la conversión de rva a yCbCr es","y=",yl,"Cb=",cbl,"Cr=",crl)

#YCbCr a YIQ
yn,inn,qn = convertir_ycbcr_a_yiq(y,cb,cr)
print("la conversión de yCbCr a yiq es","y=",yn,"i=",inn,"q=",qn)

#YCbCr a rva
rm,vm,am = convertir_ycbcr_a_rva(y,cb,cr)
print("la conversión de yCbCr a rva es","r=",rm,"v=",vm,"a=",am)