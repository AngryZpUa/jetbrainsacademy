iris = {}


def add_iris(id_n, species, petal_length, petal_width, **kwargs):
    id_n_value = {'species': species, 'petal_length': petal_length, 'petal_width': petal_width}
    for key, value in kwargs.items():
        id_n_value[key] = value
    iris[id_n] = id_n_value
