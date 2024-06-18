# VideoToGd2.2
A program that converts videos from Geometrize to Geometry Dash. Only available on Windows.

# Categories

- Requirements
- How to use
- Import methods
- Credits

# Requirements
- [GDShare](https://geode-sdk.org/mods/hjfod.gdshare/) and [WSLiveEditor](https://geode-sdk.org/mods/iandyhd3.wsliveeditor/), which both of them are available on the [Geode](https://geode-sdk.org) modloader
- 4GB patch (not required but recommended)
- Atleast 1GB of free space in disk

# How to use
- Download the program from [Releases](https://github.com/Fraa4/VideoToGd2.2/releases)
- Open VideoToGd.exe
- Select a video (mp4, avi or gif)
- Select import method
- Write numbers of shapes per frame
- Select the shapes (they will be used in the frame)
- Write numbers of frames
- Write numbers of FPS (Frames Per Second)
- Write numbers of frame skip (frame skip in actual video, if video is 60 FPS you can put 30 FPS and 2 frame skip to make it play at the same speed)
- Select the resolution (if you put more than 100, the quality will practically not change, but the import speed will be slower)
- Write numbers of shapes per refresh
- Write numbers of mutations (the higher the number, the more the shapes will change)
- Write number of scale (do not go above 5)
- Click next

Sometimes the file can freeze at the last frame, if it's staying there for longer then usual you can stop the app, it's finished but it's not showing, one method to see if it's finised is that if you're using WSLiveEditor you should see a static camera trigger, if it's there the program has finished.

# Import methods

## GMD import
This method uses [GDShare](https://geode-sdk.org/mods/hjfod.gdshare/). Simply start the .EXE file and at the end of the script when the window closes, you will see a "level.gmd" file in the "Files" folder, open Geometry Dash and go to the Create tab, then click the GDShare button and select that file, now a level should have appeared in the top of your created levels.

## WSLiveEditor
This method uses the [WSLiveEditor](https://geode-sdk.org/mods/iandyhd3.wsliveeditor/) mod created by IAndyHD3, which is available in the [Geode](https://geode-sdk.org) modloader. install it and create a new level, then while Geometry Dash is running in the background, start the script.
You should start seeing objects appearing in the level, wait for it to finish.
It's recommended that you use an empty level for this, the groups are not customizable and the object position is fixed.

**NOTE:** You need to stay in the editor in order to make the script work.

# Credits

- Program made by Fra4 (fra4 on Discord)
- GUI made by Hacoc (.nasos. on Discord)
