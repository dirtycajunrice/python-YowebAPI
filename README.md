# Python-YowebAPI

## Overview
Unofficial Python bindings for the
[Yoweb Browser](https://yppedia.puzzlepirates.com/Yoweb).
My goal is to match all capabilities of the existing browser. A few of
the features I currently support are:

* Pirate Page
  * Affiliations
  * Piracy/Carousing/Crafting Skills
  * Reputation
  * Familiars
  * Hearties

## Usage
#### Download
```sh
git clone https://github.com/DirtyCajunRice/python-YowebAPI.git
cd python-YowebAPI
python3
```
#### Starting an Insance
```py
from yoweb import base

OCEAN_NAME = 'Obsidian'
PIRATE_NAME = 'Cajun'

OCEAN = base.Ocean(OCEAN_NAME)
CAJUN = OCEAN.getpirate(PIRATE_NAME)
```
#### Usage Examples
```py
# Example 1: Get a pirates piracy skill in carpentry:
>>> CAJUN.skills.piracy.carpentry.ocean_wide
'Renowned'
>>> CAJUN.skills.piracy.carpentry.archipelago
'Master'
>>> CAJUN.skills.piracy.carpentry.experience
'Solid'

# Example 2: Get a pirates flag information
>>> pirate.affiliations.flag.name
'Consider it Sunk'
>>> pirate.affiliations.flag.rank
'Lord'
```