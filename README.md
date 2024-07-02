# unique-namer

![PyPI - Version](https://img.shields.io/pypi/v/unique-namer?&color=blue)

A Python package and command-line utility to generate unique, human-readable, and memorable names (e.g., `talented-toucan`, `naughty-watermelon`) and identifiers (e.g., `broken-radio-7ab4g`) across various categories such as science, animals, biology, etc.

### Features

* Over 16 million unique names
* Nearly infinite unique identifiers
* Ideal for naming temporary directories, user session IDs, gamer tags, project names, process names, submitted jobs, and more.

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
8. [License](#8-license)

## 1. Categories

Categories enable customization of generated names to align with the specific topic or theme of the project.

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
            <td>7043</td>
            <td><code>awful-deadline</code></td>
            <td>16,720,082</td>
            <td>10<sup>13</sup></td>
        </tr>
        <tr>
            <td>:chipmunk:</td>
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
            <td>604</td>
            <td><code>shiny-centriole</code></td>
            <td>1,433,896</td>
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
            <td>280</td>
            <td><code>funny-malware</code></td>
            <td>664,720</td>
            <td>10<sup>12</sup></td>
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
            <td>186</td>
            <td><code>enjoyed-tsunami</code></td>
            <td>441,564</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:european_castle:</td>
            <td>history</td>
            <td>162</td>
            <td><code>cool-epoch</code></td>
            <td>384,588</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:triangular_ruler:</td>
            <td>math</td>
            <td>158</td>
            <td><code>peachy-prime</code></td>
            <td>375,092</td>
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
            <td>103</td>
            <td><code>crazy-bacteria</code></td>
            <td>244,522</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:gun:</td>
            <td>misc</td>
            <td>2823</td>
            <td><code>curvy-flight</code></td>
            <td>6,701,802</td>
            <td>10<sup>13</sup></td>
        </tr>
        <tr>
            <td>:microscope:</td>
            <td>molecular_biology</td>
            <td>118</td>
            <td><code>retired-oligonucleotide</code></td>
            <td>280,132</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:musical_note:</td>
            <td>music</td>
            <td>202</td>
            <td><code>solid-contrabassoon</code></td>
            <td>479,548</td>
            <td>10<sup>11</sup></td>
        </tr>
        <tr>
            <td>:atom:</td>
            <td>physics</td>
            <td>145</td>
            <td><code>terrible-pressure</code></td>
            <td>344,230</td>
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
            <td>:books:</td>
            <td>science</td>
            <td>745</td>
            <td><code>golden-hertz</code></td>
            <td>1,768,630</td>
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

#### `category` - str or list, default is an empty string

By default, `generate` randomly selects one category to pick a noun from. Categories are selected with equal probability, regardless of the number of nouns they contain. You can specify one or more categories to restrict the selection. 

```python
import namer

name = namer.generate(category='astronomy')
print(name)   # Example: 'crazy-supernova'                 

name = namer.generate(category=['physics', 'molecular_biology'])
print(name)   # Example: 'pink-bacteria'
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
# ['animals', 'architecture', 'astronomy', 'biology', 
# 'chemistry', 'computer_science', 'countries', 'food',
# 'geography', 'history', 'math', 'medicine, 'misc', 
# 'microbiology', 'molecular_biology', 'music', 'physcics', 
# 'plants', 'science', 'scientists', 'sports']
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
Category           Nouns  Example                 Name_combs  ID_combs (4-char suffix)
__all__             7043  fertile-mazurka         16,720,082  3e+13
animals              461  understood-anglerfish    1,094,414  2e+12
architecture         134  zenzeroth-burjalarab       318,116  5e+11
astronomy            124  lavish-magnetosphere       294,376  5e+11
biology              604  makeshift-endonuclease   1,433,896  2e+12
chemistry            255  rancid-sodium              605,370  1e+12
countries            182  brown-elsalvador           432,068  7e+11
computer_science     280  abandoned-token            664,720  1e+12
food                 217  uninterested-parmesan      515,158  9e+11
geography            186  espressivo-taiga           441,564  7e+11
history              162  tiresome-valhalla          384,588  6e+11
math                 158  brutal-geometry            375,092  6e+11
medicine             706  vocal-gastroenterology   1,676,044  3e+12
microbiology         103  formidable-koch            244,522  4e+11
misc                2823  male-possibility         6,701,802  1e+13
molecular_biology    118  jumbled-centriole          280,132  5e+11
music                202  visiting-mp3               479,548  8e+11
physics              145  developing-meter           344,230  6e+11
plants               178  fermented-grain            422,572  7e+11
science              745  patient-receptor         1,768,630  3e+12
scientists           101  electoral-ramanujan        239,774  4e+11
sports               191  neighbouring-tag           453,434  8e+11
```

## 6.2. Generating names

The `generate` command creates a list of names or IDs based on specified parameters.

### Example 1: Generating 5 names

```bash
namer generate 5
```

Output:

```
basic-mortise
focused-berry
uncommon-broth
decisive-dentil
kingly-afforestation
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

The package adheres to Semantic Versioning with the format `MAJOR.MINOR.PATCH`:

* **MAJOR version** is incremented for significant codebase changes, such as new features or major reorganizations.
* **MINOR version** is incremented for category-related updates, like adding or modifying categories.
* **PATCH version** is incremented for bug fixes, improvements, or vocabulary expansions without category changes.

## 8. License

[MIT License](https://choosealicense.com/licenses/mit/)