#Generator function
def generator(n=0, maximus=10):
    while True:
        yield n
        n += 1
        
        if n >= maximus:
            return

gen = generator()
for n in gen:
    print(n)
print()
    
#Com yield from podemos pegar a continuacao de outro iterator
def gen1():
    yield 1
    yield 2
    yield 3
    

def gen2():
    yield from gen1()
    yield 4
    yield 5
    
genes = gen2()
for c in genes:
    print(c)
