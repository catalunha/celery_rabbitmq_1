from tasks import hello

a = hello("Word")
print(a)
a = hello.delay("teste2")
print(a)
