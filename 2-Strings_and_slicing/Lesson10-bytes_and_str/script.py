from typing import Any

a = b"h\x65llo"

print(f"{type(a)=}")
print(f"{list(a)=}")
print(f"{a=}")

print("------------")

a = "a\u0300 propos"
print(f"{type(a)=}")
print(f"{list(a)=}")
print(f"{a=}")

print("------------")

def to_str(b: Any):
    if isinstance(b, bytes):
        return b.decode("utf-8")
    return b

print(repr(to_str(b"foo")))
print(b"foo")
print(repr(to_str("bar")))

print("------------")

def to_bytes(s: Any):
    if isinstance(s, str):
        return s.encode("utf-8")
    return s

print(repr(to_bytes(b"foo")))
print(repr(to_bytes("bar")))

print(b"one" + b"two")
print("one" + "two")

# print(b"one" + "two")  # TypeError
# print("one" + b"two")  # TypeError


print(f"{b"red" > b"blue"=}")
print(f"{'red' > 'blue'=}")

# print(b"red" > "blue")  # TypeError
# print("red" > b"blue")  # TypeError

print("------------")
# print(f"{b"blue" < "red"=}")

print(f"{b"foo" == "foo"=}")

# to read / write from binary files use rb / wb mode !!!
# and to be 100% sure about encoding use encoding="utf-8" in text mode using encoding parameter
import locale

print(f"Locale: {locale.getpreferredencoding()=}")