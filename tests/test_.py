import pytest

import namer


def test_stats():
	stats = namer.stats()
	assert len(stats) == len(namer.data.categories) + 1


def test_list_categories():
	assert len(namer.list_categories()) == len(namer.data.categories)


@pytest.mark.parametrize('category,suffix_length,separator,style',[
    ('', 0, '-', 'lowercase'),
    ('microbiology', 2, '_', 'uppercase'),
    ('microbiology', 4, ' ', 'title'),
    ([], 0, '-', 'lowercase'),
    (['microbiology', 'physics'], 0, '-', 'lowercase'),
])
def test_generate(category, suffix_length, separator, style):
	name_str = namer.generate(category, suffix_length, separator, style)
	name_lst = name_str.split(separator)
	words_count = 3 if suffix_length else 2
	assert len(name_lst) == words_count
	assert all([len(word) for word in name_lst])
	if suffix_length:
		assert len(name_lst[2]) == suffix_length
