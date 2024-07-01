from .adjectives import ADJECTIVES
from .animals import ANIMALS
from .architecture import ARCHITECTURE
from .astronomy import ASTRONOMY
from .biology import BIOLOGY
from .chemistry import CHEMISTRY
from .computer_science import COMPUTER_SCIENCE
from .countries import COUNTRIES
from .food import FOOD
from .geography import GEOGRAPHY
from .history import HISTORY
from .math import MATH
from .medicine import MEDICINE
from .microbiology import MICROBIOLOGY
from .molecular_biology import MOLECULAR_BIOLOGY
from .music import MUSIC
from .physics import PHYSICS
from .plants import PLANTS
from .scientists import SCIENTISTS
from .sports import SPORTS
from .misc import MISC

categories = {
    'animals': [ANIMALS],
    'architecture': [ARCHITECTURE],
    'astronomy': [ASTRONOMY],
    'biology': [
        BIOLOGY,
        MICROBIOLOGY,
        MOLECULAR_BIOLOGY,
    ],
    'chemistry': [CHEMISTRY],
    'countries': [COUNTRIES],
    'computer_science': [COMPUTER_SCIENCE],
    'food': [FOOD],
    'geography': [GEOGRAPHY],
    'history': [HISTORY],
    'math': [MATH],
    'medicine': [MEDICINE],
    'microbiology': [MICROBIOLOGY],
    'misc': [MISC],
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
}