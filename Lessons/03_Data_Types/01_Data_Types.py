# 1.  Numeric Types

# Integer
x = 10
print("Integer:", x, "Type:", type(x))

# Float
y = 3.14
print("Float:", y, "Type:", type(y))

# Complex
z = 2 + 3j
print("Complex:", z, "Type:", type(z))
print("Real part:", z.real, "Imaginary part:", z.imag)


# 2. Text Type

# String
name = "Krishna"
print("String:", name, "Type:", type(name))

# Access characters
print("First character:", name[0])
print("Uppercase:", name.upper())


# 3. Boolean Type

is_happy = True
is_sad = False
print("Boolean True:", is_happy, "Type:", type(is_happy))
print("Boolean False:", is_sad, "Type:", type(is_sad))


# 4. None Type

nothing = None
print("None value:", nothing, "Type:", type(nothing))




# 5. Bytes & Memory Types 

# Bytes (immutable)
b = b"hello"
print("Bytes:", b, "Type:", type(b))

# Bytearray (mutable)
ba = bytearray(b"hi")
ba[0] = 72  # H in ASCII
print("Bytearray:", ba, "Type:", type(ba))

# Memoryview (view of bytes)
mv = memoryview(b"hello")
print("Memoryview:", mv, "Type:", type(mv))
print("First byte in memoryview:", mv[0])  # 104 (ASCII for 'h')
