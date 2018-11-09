import ctypes as C
import numpy as np
math = C.CDLL('./myLib.so')

math.add_int.restype = C.c_int
math.add_int.argtypes = [C.c_int, C.c_int]
print("suma esperada 40")
print(math.add_int(22, 18))

math.add_float.restype = C.c_float
math.add_float.argtypes = [C.c_float, C.c_float]
print("suma esperada 40.0")
print(math.add_float(22.0,18.0))

veintidosI = C.c_int(22)
diciochoI = C.c_int(18)
resultadoI = C.c_int()
math.add_int_ref(C.byref(veintidosI),C.byref(diciochoI),C.byref(resultadoI))
print("suma esperada 40")
print(resultadoI.value)

veintidosF = C.c_float(22.0)
diciochoF = C.c_float(18.0)
resultadoF = C.c_float()
math.add_float_ref(C.byref(veintidosF),C.byref(diciochoF),C.byref(resultadoF))
print("suma esperada 40.0")
print(resultadoF.value)

intPointer = C.POINTER(C.c_int)
in1 = np.array([1, 2, 3], dtype=C.c_int)
in2 = np.array([3, 2, 1], dtype=C.c_int) 
intOut = np.zeros(3, dtype=np.int32)
math.add_int_array(in1.ctypes.data_as(intPointer), in2.ctypes.data_as(intPointer), intOut.ctypes.data_as(intPointer), C.c_int(3))
print("suma esperada [4,4,4]")
print(intOut)

math.dot_product.restype = C.c_float
floatPointer = C.POINTER(C.c_float)
fl1 = np.array([1.0, 1.7, 3.3], dtype=C.c_float)
fl2 = np.array([3.3, 2.0, 1.0], dtype=C.c_float)
floatOut = math.dot_product(fl1.ctypes.data_as(floatPointer), fl2.ctypes.data_as(floatPointer), C.c_int(3))
print("suma esperada 10.0")
print(floatOut)
