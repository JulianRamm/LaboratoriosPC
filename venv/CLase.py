import numpy as np
import struct as st
file = open("archivo.txt", "w")
file.write("Esta \nes \nuna \nlinea")
file = open("archivo.txt", "r")
linea = file.readline()
while linea:
    print(linea)
    linea = file.readline()
var1 = np.random.randint(1, 100, 100)
print(var1)
file = open("archivo.txt", "wb")
var2 = st.pack("B"*int(len(var1)), *var1)
file.write(var2)
file = open("archivo.txt", "rb")
var2 = file.read()
var3 = st.unpack("B"*int(len(var2)/1), var2) #Se divide entre el número de bytes del formato
file.close()
print(var3)