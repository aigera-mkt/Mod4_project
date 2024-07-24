from main import MoviesLibrary
def test_is_one():
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])
    library.add_movie('Ужасы','Крик')

    assert ['Крик'] == library.recommend('Ужасы')


def test_is_many():
    library=MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])

    library.add_movie('Комедия','Свадебный переполох')
    library.add_movie('Комедия','Бриллиантовая рука')
    library.add_movie('Ужасы','Пила')


    assert['Свадебный переполох','Бриллиантовая рука']==library.recommend('Комедия')

def test_is_not_thisGenre():
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])
    library.add_movie('Ужасы','Крик2')

    assert ['Крик2'] != library.recommend('Комедия')



