# unique-namer

![PyPI - Version](https://img.shields.io/pypi/v/unique-namer?label=version&color=blue)

![cover](images/cover.png)

A Python package and command-line utility to generate unique and memorable names (e.g., `talented-toucan`, `naughty-watermelon`) and IDs (e.g., `broken-radio-7ab4g`). These names/IDs are ideal for naming temporary directories, user session IDs, gamer tags, project names, process names, or submitted jobs.

The generated names cover a wide range of thematic categories, including science, animals, or history, often with a humorous twist. While creating unique-namer, I was inspired by the creative names used by Docker for its containers and Nextflow for its processes.

### Features

* Over 19 million unique names
* Nearly infinite unique identifiers
* 20+ categories
* Customizable names and categories

## Table of contents

1. [Categories](#1-categories)
2. [Requirements](#2-requirements)
3. [Installation](#3-installation)
4. [Using Without Installation](#4-using-without-installation)
5. [Usage](#5-usage)
      1. [Generating Names](#51-generating-names)
      2. [Customizing Names](#52-customizing-names)
      3. [Getting Category List](#53-getting-category-list)
      4. [Adding Custom Categories](#54-adding-custom-categories)
6. [Command-line Utility](#6-command-line-utility)
      1. [Getting Statistics](#61-getting-statistics)
      2. [Generating Names](#62-generating-names)
7. [Versioning](#7-versioning)
8. [Tests](#8-tests)
9. [License](#9-license)

## 1. Categories

Categories allow you to customize generated names to fit the specific topic or theme of your project. The default category, `general`, includes widely recognized nouns and excludes more specialized or uncommon terms.

<table>
    <thead>
        <tr>
            <th rowspan="2">-</th>
            <th rowspan="2">Category</th>
            <th rowspan="2">Nouns count</th>
            <th rowspan="2">Example name</th>
            <th colspan="2">Possible combinations</th>
        </tr>
        <tr>
            <th>Names</th>
            <th>IDs (suffix 4)</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td></td>
            <td>__all__</td>
            <td>8,082</td>
            <td><code>awful-deadline</code></td>
            <td>19,186,668</td>
            <td>10<sup>13</sup></td>
        </tr>
        <tr>
            <td>:frog:</td>
            <td>animals</td>
            <td>461</td>
            <td><code>tan-octopus</code></td>
            <td>1,094,414</td>
            <td>10<sup>12</sup></td>
        </tr>
        <tr>
            <td>:department_store:</td>
            <td>architecture</td>
            <td>134</td>
            <td><code>blowing-facade</code></td>
            <td>318,116</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:telescope:</td>
            <td>astronomy</td>
            <td>124</td>
            <td><code>ruthless-meteoroid</code></td>
            <td>294,376</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:four_leaf_clover:</td>
            <td>biology</td>
            <td>730</td>
            <td><code>shiny-centriole</code></td>
            <td>1,733,020</td>
            <td>10<sup>12</sup></td>
        </tr>
        <tr>
            <td>:test_tube:</td>
            <td>chemistry</td>
            <td>255</td>
            <td><code>junior-peroxide</code></td>
            <td>605,370</td>
            <td>10<sup>12</sup></td>
        </tr>
        <tr>
            <td>:us:</td>
            <td>countries</td>
            <td>182</td>
            <td><code>satisfying-tanzania</code></td>
            <td>432,068</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:computer:</td>
            <td>computer_science</td>
            <td>333</td>
            <td><code>funny-malware</code></td>
            <td>790,542</td>
            <td>10<sup>12</sup></td>
        </tr>
        <tr>
            <td>:moneybag:</td>
            <td>economy</td>
            <td>175</td>
            <td><code>flowery-income</code></td>
            <td>415,450</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:hamburger:</td>
            <td>food</td>
            <td>217</td>
            <td><code>pretty-waffle</code></td>
            <td>515,158</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:earth_americas:</td>
            <td>geography</td>
            <td>185</td>
            <td><code>enjoyed-tsunami</code></td>
            <td>439,190</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:star:</td>
            <td><b>general</b></td>
            <td>5,476</td>
            <td><code>curvy-flight</code></td>
            <td>13,000,024</td>
            <td>10<sup>13</sup></td>
        </tr>
        <tr>
            <td>:european_castle:</td>
            <td>history</td>
            <td>156</td>
            <td><code>cool-epoch</code></td>
            <td>370,344</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:books:</td>
            <td>literature</td>
            <td>587</td>
            <td><code>winning-limerick</code></td>
            <td>1,393,538</td>
            <td>10<sup>12</sup></td>
        </tr>
        <tr>
            <td>:triangular_ruler:</td>
            <td>math</td>
            <td>157</td>
            <td><code>peachy-prime</code></td>
            <td>372,718</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:hospital:</td>
            <td>medicine</td>
            <td>706</td>
            <td><code>curly-diarrhea</code></td>
            <td>1,676,044</td>
            <td>10<sup>12</sup></td>
        </tr>
        <tr>
            <td>:bug:</td>
            <td>microbiology</td>
            <td>130</td>
            <td><code>crazy-bacteria</code></td>
            <td>308,620</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:microscope:</td>
            <td>molecular_biology</td>
            <td>220</td>
            <td><code>retired-oligonucleotide</code></td>
            <td>522,280</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:musical_note:</td>
            <td>music</td>
            <td>203</td>
            <td><code>solid-contrabassoon</code></td>
            <td>481,922</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:atom:</td>
            <td>physics</td>
            <td>147</td>
            <td><code>terrible-pressure</code></td>
            <td>348,978</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:sunflower:</td>
            <td>plants</td>
            <td>178</td>
            <td><code>anonymous-cactus</code></td>
            <td>422,572</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:electron:</td>
            <td>science</td>
            <td>876</td>
            <td><code>golden-hertz</code></td>
            <td>2,079,624</td>
            <td>10<sup>12</sup></td>
        </tr>
        <tr>
            <td>:technologist:</td>
            <td>scientists</td>
            <td>101</td>
            <td><code>gifted-newton</code></td>
            <td>239,774</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:basketball:</td>
            <td>sports</td>
            <td>191</td>
            <td><code>intergalactic-olympics</code></td>
            <td>453,434</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:satellite:</td>
            <td>technology</td>
            <td>228</td>
            <td><code>awesome-python</code></td>
            <td>541,272</td>
            <td>10<sup>11</sup></td>
        </tr>
    </tbody>
</table>

## 2. Requirements

* Python version 3.6 or higher
* No external dependencies are required

## 3. Installation

Install `unique-namer` from [PyPI](https://pypi.org/project/unique-namer/):

```bash
pip install unique-namer
```

Alternatively, you can install the latest version directly from GitHub:

```bash
pip install "git+https://github.com/aziele/unique-namer.git"
```

## 4. Using without installation

If you prefer to use `unique-namer` without installation, you can clone or download the repository:

```bash
git clone https://github.com/aziele/unique-namer.git
cd unique-namer/src/
```

You can import `namer` in Python:

```python
python
>>> import namer
>>> namer.__doc__
'Generate unique, human-readable, and memorable names or identifiers'
```

You can also use `unique-namer` as a command-line tool:

```bash
python -m namer
```

## 5. Usage

### 5.1. Generating names

The `generate` function returns a string with a randomly generated name consisting of an adjective and a noun.

```python
import namer

name = namer.generate()
print(name)   # Example: 'blushy-cyclist'
```

#### `category` - str or list, default is `general`

The `generate` function selects nouns from the `general` category by default. If category is provided as a list of categories, the function randomly chooses one category from the list to generate a noun. Each category is chosen with equal probability, regardless of the number of nouns it contains.

```python
import namer

name = namer.generate(category='astronomy')
print(name)   # Example: 'crazy-supernova'                 

name = namer.generate(category=['physics', 'biology'])
print(name)   # Example: 'pink-bacteria'
```

To use all available categories, set the `category` argument to `__all__`.

```python
import namer

name = namer.generate(category='__all__')
print(name)   # Example: 'lonely-momentum'

```

#### `suffix_length` - int, default is `0`

Adds a random suffix of the specified length to the generated name to create a unique identifier. The suffix consists of alphanumeric characters (`0-9a-z`).

```python
import namer

name = namer.generate(category='history', suffix_length=3)
print(name)   # Example: 'annoying-cleopatra-9a1'
```

#### `separator` - str, default is `'-'`

Specifies the separator to use between the adjective, noun, and suffix in the generated name.

```python
import namer

name = namer.generate(category='sports', separator='_')
print(name)   # Example: 'savage_judo'
```

#### `style` - str, one of `title`, `lowercase`, `uppercase`

Specifies the text case format of the generated name.

```python
import namer

name = namer.generate(suffix_length=5, style='uppercase')
print(name)   # Example: 'DAMAGED-ELECTRON-J20ZX'

name = namer.generate(separator=' ', style='title')
print(name)   # Example: 'Lazy Unicorn'
```

### 5.2. Customizing names

To tailor the generated names to your specific project needs, such as adding a date or project name, use the `_generate` function. This function returns a Python list of name components and a separator. You can modify the list and then format it into a string.

Here's an example:

```python
import namer

# Generate name components
name_components, separator = _generate(category='food', suffix_length=3)
print(name_components)   # Example: ['macho', 'pizza', '7dx']

# Create custom generate function
def my_generate(*args, **kwargs):
    name_components, separator = namer_generate(*args, **kwargs)
    name_components.insert(0, '2024')
    return separator.join(name_components)

name = my_generate(category='food', suffix_length=3)
print(name)         # Example: 2024-macho-pizza-7dx
```

### 5.3. Getting category list

You can retrieve the list of available categories using the `list_categories` function.

```python
import namer

print(namer.list_categories())
# ['animals', 'architecture', ..., 'sports']
```

### 5.4. Adding custom categories

To generate names or IDs tailored to your project, you can add custom categories. Extend the `namer.data.categories` dictionary with lists of words representing your custom category.

```python
import namer

# Create two subcategories.
my_dogs = ['charlie', 'bella', 'biga']
my_cats = ['tommy', 'lucy']

# Add a custom category named 'my_pets' containing both dogs and cats
namer.data.categories['my_pets'] = [my_dogs, my_cats]

# Generate a name from the 'my_pets' category
name = namer.generate(category='pets')
print(name)   # Example: 'thankful-tommy'
```


## 6. Command-line utility

The tool is available as a command-line utility.

```bash
namer -h
```

or 

```bash
python -m namer -h
```

### 6.1. Getting statistics

The `stats` command prints a table with name/ID statitics for each category.

```bash
namer stats
```

Output:

```
Category           Nouns  Example                Name_combs  ID_combs (4-char suffix)
__all__             8082  young-phages           19,186,668  3e+13
animals              461  absurd-cuckoo           1,094,414  2e+12
architecture         134  mutual-loggia             318,116  5e+11
astronomy            124  grumpy-telescope          294,376  5e+11
biology              730  immature-commensalism   1,733,020  3e+12
chemistry            255  becoming-osmosis          605,370  1e+12
countries            182  quintessential-gambia     432,068  7e+11
computer_science     333  ruling-proxy              790,542  1e+12
economy              175  enjoyed-savings           415,450  7e+11
food                 217  amicable-pretzel          515,158  9e+11
geography            185  key-antarctic             439,190  7e+11
general             5476  regal-acappella        13,000,024  2e+13
history              156  minimal-tribe             370,344  6e+11
literature           587  prime-sestet            1,393,538  2e+12
math                 157  bustling-settheory        372,718  6e+11
medicine             706  phobic-lumbago          1,676,044  3e+12
microbiology         130  squeamish-virologists     308,620  5e+11
molecular_biology    220  merciless-betasheet       522,280  9e+11
music                203  prepared-chorus           481,922  8e+11
physics              147  likely-ohm                348,978  6e+11
plants               178  wide-gladiolus            422,572  7e+11
science              876  xenacious-ion           2,079,624  3e+12
scientists           101  sour-lamarck              239,774  4e+11
sports               191  concave-crew              453,434  8e+11
technology           228  zygotic-circuits          541,272  9e+11
```

## 6.2. Generating names

The `generate` command creates a list of names or IDs based on specified parameters.

### Example 1: Generating 5 names

```bash
namer generate 5
```

Output:

```
telling-adrenaline
infinite-gonad
close-span
bloody-blow
puffy-biology
```

### Example 2: Generating 10 IDs with custom parameters

To generate 10 IDs from the `physics` and `biology` categories, with a random suffix of `3` characters, using `_` as a separator, and converting name style to title, use

```bash
namer generate 10 --category physics --category biology --suffix_length 3 -- \
separator _ --style title
```

Output:

```
Visiting_Haploid_Eep
Eventual_Refraction_Cnr
Snugly_Monod_Sim
Cruel_Codon_46p
Relieved_Decibel_Cn5
Underground_Bug_7wf
Super_Acre_30r
Guttural_Farad_E1w
Lead_Stalk_Fi4
Formidable_Field_621
```

## 7. Versioning

The package follows Semantic Versioning with the format `MAJOR.MINOR.PATCH`:

* **MAJOR version**: significant changes (e.g., new features, major code reorganizations).
* **MINOR version**: category-related updates (e.g., adding/moving categories).
* **PATCH version**: bug fixes or vocabulary expansions without changing the list of categories.

## 8. Tests

To ensure that unique-namer works as expected, you can run tests using pytest.

```
pytest tests
```

## 9. License

[MIT License](https://choosealicense.com/licenses/mit/)