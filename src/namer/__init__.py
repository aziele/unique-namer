"""Generate unique, human-readable, and memorable names or identifiers"""

from dataclasses import dataclass
import random
from typing import Dict, NamedTuple, Union, List

from . import data

__version__ = '1.6.1'


SUFFIX_ALPHABET = '0123456789abcdefghijklmnopqrstuvwxyz'

def _generate(
        category: Union[str, List[str]] = 'general',
        suffix_length: int = 0,
        separator: str = '-',
        style: str = 'lowercase'
) -> List[str]:
    """
    Generate a random name composed of an adjective and a noun from a specified
    or randomly chosen category, with an optional random suffix.

    Args:
        category (Union[str, List[str]]): 
            The category or list of categories to choose the noun from.
        suffix_length (int): 
            The length of the optional random suffix.
        separator (str): 
            The separator between the adjective, noun, and suffix.  
        style (str):
            The style to apply to the generated name ('lowercase', 'uppercase', 
            'title').

    Returns:
        List[str]: A list containing the adjective, noun, and optional suffix.

    Raises:
        ValueError: If the specified category does not exist.
    """
    adjective = random.choice(data.ADJECTIVES)
    
    # Determine the category name
    if not category:
        category_name = 'general'
    elif category == '__all__':
        category_name = random.choice(list(data.categories.keys()))
    elif isinstance(category, list):
        category_name = random.choice(category)
    else:
        category_name = category

    if category_name not in data.categories:
        raise ValueError(f'Category {category_name} does not exist.')

    # Pick a random noun from the chosen category
    noun_list = random.choice(data.categories[category_name])
    noun = random.choice(noun_list)

    # Create a list with the adjective and noun
    name_parts = [adjective, noun]

    # Add a random suffix if specified
    if suffix_length:
        suffix = ''.join(random.choices(SUFFIX_ALPHABET, k=suffix_length))
        name_parts.append(suffix)

    # Apply style transformation if specified
    if style == 'uppercase':
        name_parts = [part.upper() for part in name_parts]
    elif style == 'title':
        name_parts = [part.capitalize() for part in name_parts]

    return name_parts, separator


def generate(*args, **kwargs) -> str:
    """
    Wrapper for the `_generate` function to return the string name.

    Returns:
        str: The generated name.
    """
    name_parts, separator = _generate(*args, **kwargs)
    return separator.join(name_parts)


def list_categories() -> List[str]:
    """Returns a sorted list of all available categories."""
    return sorted(data.categories.keys())


@dataclass
class Stat:
    noun_count: int
    example_name: str
    name_combinations: int
    id_combinations: int

def stats(suffix_length: int = 4) -> Dict[str, Stat]:
    """
    Generate statistics for each category:
    - Number of nouns
    - Example name
    - Number of possible name combinations
    - Number of possible ID combinations

    Returns:
        Dict[str, Stat]: A dictionary where keys are category names
        and values are instances of the Stat named tuple containing
        the calculated statistics.
    """
    adjective_count = len(data.ADJECTIVES)

    # Count total nouns from all categories
    all_nouns = set()
    for subcategories in data.categories.values():
        for subcategory in subcategories:
            all_nouns.update(subcategory)
    stats = {'__all__': len(all_nouns)}

    # Count nouns in each category
    for category, subcategories in data.categories.items():
        stats[category] = sum(len(nouns) for nouns in subcategories)

    # Generate example name and number of combinations for each category
    for category in stats:
        noun_count = stats[category]
        name_combinations = adjective_count * noun_count
        id_combinations = name_combinations * (len(SUFFIX_ALPHABET) ** suffix_length)
        example_name = generate(category=category)
        stats[category] = Stat(
            noun_count=noun_count,
            example_name=example_name,
            name_combinations=name_combinations,
            id_combinations=id_combinations,
        )
    
    return stats