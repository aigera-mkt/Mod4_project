from main import MoviesLibrary

def test_is_empty():
    library = MoviesLibrary(['Ужасы', 'Комедия', 'Романтика'])
    #assert [''] == library.recommend('')

    assert [] == library.recommend('Комедия')


