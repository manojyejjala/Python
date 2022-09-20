x=5
print(int(x))
x="hello world"
print(str(x))
x=20.5
print(float(x))
x=complex(1j)
print(complex(x))
x=["apple", "banana", "cherry"]
print(list(x))
x=("apple", "banana", "cherry")
print(tuple(x))
x=range(6)
print(x)
x={"name":"John","age":36}
print(dict(x))
x={"apple","banana","cherry"}
print(set(x))
x=frozenset({"apple","banana","cherry"})
print(frozenset(x))
x=True
print(bool(x))
x=b"hello"
print(bytes(x))
x=memoryview(bytes(5))
print(memoryview(x))
x=None
print(NoneType(x))