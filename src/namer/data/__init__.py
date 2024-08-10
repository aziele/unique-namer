from .adjectives import ADJECTIVES
from .animals import ANIMALS
from .architecture import ARCHITECTURE
from .art import ART
from .astronomy import ASTRONOMY
from .biology import BIOLOGY
from .chemistry import CHEMISTRY
from .computer_science import COMPUTER_SCIENCE
from .countries import COUNTRIES
from .economy import ECONOMY
from .food import FOOD
from .geography import GEOGRAPHY
from .general import GENERAL
from .history import HISTORY
from .literature import LITERATURE
from .math import MATH
from .medicine import MEDICINE
from .microbiology import MICROBIOLOGY
from .molecular_biology import MOLECULAR_BIOLOGY
from .music import MUSIC
from .physics import PHYSICS
from .plants import PLANTS
from .scientists import SCIENTISTS
from .sports import SPORTS
from .technology import TECHNOLOGY

categories = {
    'animals': [ANIMALS],
    'architecture': [ARCHITECTURE],
    'art': [ART],
    'astronomy': [ASTRONOMY],
    'biology': [
        BIOLOGY,
        MICROBIOLOGY,
        MOLECULAR_BIOLOGY,
    ],
    'chemistry': [CHEMISTRY],
    'countries': [COUNTRIES],
    'computer_science': [COMPUTER_SCIENCE],
    'economy': [ECONOMY],
    'food': [FOOD],
    'geography': [GEOGRAPHY],
    'general': [GENERAL],
    'history': [HISTORY],
    'literature': [LITERATURE],
    'math': [MATH],
    'medicine': [MEDICINE],
    'microbiology': [MICROBIOLOGY],
    'molecular_biology': [MOLECULAR_BIOLOGY],
    'music': [MUSIC],
    'physics': [PHYSICS],
    'plants': [PLANTS],
    'science': [
        ASTRONOMY,
        CHEMISTRY,
        MICROBIOLOGY,
        MOLECULAR_BIOLOGY,
        PHYSICS,
    ],
    'scientists': [SCIENTISTS],
    'sports': [SPORTS],
    'technology': [TECHNOLOGY],
}