# Bad-Apple-Signs
Bad Apple in Minecraft with signs using sprites

## Note: this has currently only been tested to work on linux.

- To use this first download BadApple.mp4, ImageExtract.py, and SignGenerator.py.
- Execute ImageExtract.py in the same directory as BadApple.mp4 and it should create a directory called "data" with each individual frame from the video.
- Extract signs.zip and place it into the datapacks directory of the world you want to use it in.
- Execute SignGenerator.py and give the paths to the functions section of the datapack directory (the one in your world's folder) as well as the path to the directory containing the frames (this should be the full path of the /data directory that we previously generated)
- Give the xyz coordinates you want the the signs to be generated at
- List what frames you want turned into signs
- This will generate each frame as a separate .mcfunction file (there's probably a better way to do this but it's what I came up with at 4am)

## Important: this is badly coded so if you try to load all 6573 frames into the datapack it will likely freeze/crash your game. I found loading 2000 at a time was enough to get a decent (although slow) fps

This is mainly a proof of concept project for fun, probably not going to expand

But if I do:
- custom 4:3 sizes
- error correction for file already exists
- background
- optimization(!!)
