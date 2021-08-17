#Podemos criar exceções personalizadas caso o proprio python não levante a mesma.

class IncefaloError(Exception):
    pass

def teste():
    raise IncefaloError('Incefalo Ignorante!!')

try:
    teste()
except IncefaloError as error:
    print(error)