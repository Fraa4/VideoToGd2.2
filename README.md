# VideoToGd2.2
A program that converts videos from [Geometrize](https://www.geometrize.co.uk/) to [Geometry Dash](https://en.wikipedia.org/wiki/Geometry_Dash). Only available on [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows).

# Categories

- [Requirements](#requirements)
- [How to use](#how-to-use)
- [Import methods](#import-methods)
- [Credits](#credits)

# Requirements
- [GDShare](https://geode-sdk.org/mods/hjfod.gdshare/) and [WSLiveEditor](https://geode-sdk.org/mods/iandyhd3.wsliveeditor/), which both of them are available on the [Geode](https://geode-sdk.org) modloader
- 4GB patch (not required but **highly** recommended)
- Atleast 1GB of free space in disk

# How to use
- Download the program from [Releases](https://github.com/Fraa4/VideoToGd2.2/releases)
- Open VideoToGd.exe
- Select a video (mp4, avi or gif)
- Select import method (check the [Import methods](#import-methods) category to see the import methods)
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

Your antivirus could detect this program as a virus. This is because the program is using a batch command to run the Geometrize function. If the program has any problem, try
disabling your antivirus before contacting me.

The script can take a very long time to run. If you decide that you want to stop the generation, you can close the Command Prompt window and then run the "quick import.py" script to just import the frames it has generated or instead you can change settings and just run the .EXE file again. Once you stop the program, it's not resumable, it has to start over.

Sometimes the file can freeze at the last frame. If it's staying there for longer than usual, you can stop the app. If it's finished but it's not showing, check for a static camera trigger in the editor if you're using WSLiveEditor. If the camera trigger is there, it means the program has finished.

# Import methods

## GMD import
This method uses the [GDShare](https://geode-sdk.org/mods/hjfod.gdshare/) mod created by HJfod, which is available on the [Geode](https://geode-sdk.org) modloader. Simply start the .EXE file and at the end of the script when the window closes, you will see a "level.gmd" file in the "Files" folder. Open Geometry Dash and go to the Create tab, then click the GDShare button and select that file. Now a level should appear on top of your created levels.

## WSLiveEditor
This method uses the [WSLiveEditor](https://geode-sdk.org/mods/iandyhd3.wsliveeditor/) mod created by IAndyHD3, which is available on the [Geode](https://geode-sdk.org) modloader. Install it and create a new level, then while Geometry Dash is running in the background, start the script.
You should see objects appearing in the level, wait for it to finish.
It's recommended that you use an empty level for this, the groups are not customizable and the object position is fixed.

**NOTE:** You need to stay in the editor in order to make the script work.

# Credits

- Program made by Fra4 (fra4 on Discord)
- GUI made by Hacoc (.nasos. on Discord)
