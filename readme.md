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
* Crew Page
  * Affiliations
  * Fame/Rank/Founded Info/Public Statement
  * Reputation
  * Politics
  * Booty Shares
  * Ship Restocking
  * Active Mates
  * Members/Member Ranks
## Usage
#### Download
```sh
git clone https://github.com/DirtyCajunRice/python-YowebAPI.git
cd python-YowebAPI
python3
```
#### Starting an Instance
```py
from yoweb import base

OCEAN_NAME = 'Obsidian'
PIRATE_NAME = 'Cajun'
CREW_ID = 5000435

OCEAN = base.Ocean(OCEAN_NAME)
PIRATE = OCEAN.getpirate(PIRATE_NAME)
CREW = OCEAN.getcrew(CREW_ID)
```
#### Usage Examples
```py
# Example 1: Get a pirate's piracy skill in carpentry:
>>> CAJUN.skills.piracy.carpentry.ocean_wide
'Renowned'
>>> CAJUN.skills.piracy.carpentry.archipelago
'Master'
>>> CAJUN.skills.piracy.carpentry.experience
'Solid'

# Example 2: Get a pirate's flag information
>>> pirate.affiliations.flag.name
'Consider it Sunk'
>>> pirate.affiliations.flag.rank
'Lord'

# Example 3: Get a crew's current active mates count
>>> CREW.active_mates.jobbing_pirate
5
>>> CREW.active_mates.officer
67

# Example 4: Get a crew's current captain and info
>>> CREW.crew_members.Captain
[<Pirate:Scar>]
>>> Crew.crew_members.Captain[0].name
'Scar'
```