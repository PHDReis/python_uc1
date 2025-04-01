d1 = {"a":1, "b":2}
d3 = {"a":1, "b":2}
d2 = {"b":3, "c":4}

print(f"\n\tOs dicionários originais são: ")
print(f"\n\tD1: {d1}")
print(f"\n\tD2: {d2}\n")

d1.update(d2)
d2.update(d1)

print(f"\n\tOs dicionários atualizados são: ")
print(f"\n\tD1: {d1}")
print(f"\n\tD2: {d2}\n")