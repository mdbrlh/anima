# AnimA ARPG .char editor

POC to edit .char files of the Android and PC game AnimA in offline mode.

## How to use:

Connect your android, go to Android\data\com.ExiliumGames.Anima\files\Local
You can see your character file, *character_name.char*
Copy your file (make a backup before) in this folder and open a python3 (min 3.8) repl

Example:

```
import anima
c = anima.load_file('charname.char')
c.set_gold(1_000_000)
c.set_strength(1000.0)
anima.save_file(c, 'charname.char')
```

Open anima.py for more set functions (spells points, oboli, ...)

Copy the generated file to Android\data\com.ExiliumGames.Anima\files\Local and launch the AnimA app

## Note

This is ugly, coded with the ass, ... I do this one night so take it like this and good game/luck ;p

