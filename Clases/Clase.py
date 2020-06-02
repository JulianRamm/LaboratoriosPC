import numpy as np
import struct as st
import matplotlib.pyplot as plt
# file = open("archivo.txt", "w")
# file.write("Esta \nes \nuna \nlinea")
# file = open("archivo.txt", "r")
# linea = file.readline()
# while linea:
#     print(linea)
#     linea = file.readline()
# var1 = np.random.rand(100)
# print(var1)
# file = open("archivo.txt", "wb")
# var2 = st.pack("f"*int(len(var1)), *var1)
# file.write(var2)
file = open("averagebin1 (1).bin", "rb")
var2 = file.read()
var3 = st.unpack("f"*int(len(var2)/4), var2) #Se divide entre el número de bytes del formato
print(len(var3))
print(var3[2], var3[21], var3[43])
# plt.figure()
# plt.plot(var3)
# plt.show()
file.close()

# file = open("FileBinInt16.bin", "wb")
# var1 = np.random.randint(-10, 10, 1000)
# print(var1)
# var2 = st.pack("h"*int(len(var1)), *var1)
# file.write(var2)
# file = open("FileBinInt16.bin", "rb")
# var2 = file.read()
# var3 = st.unpack("h"*int(len(var2)/2), var2)
# print(var3)
# file.close()


