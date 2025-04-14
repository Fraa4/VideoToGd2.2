# VideoToGd2.2
A program that converts videos from [Geometrize](https://www.geometrize.co.uk/) to [Geometry Dash](https://en.wikipedia.org/wiki/Geometry_Dash). Only available on [Windows](https://en.wikipedia.org/wiki/Microsoft_Windows).

# Categories

- [Requirements](#requirements)
- [How to use](#how-to-use)
- [Import methods](#import-methods)
- [Credits](#credits)
- [Most common errors](#most-common-errors)

# Requirements
- [GDShare](https://geode-sdk.org/mods/hjfod.gdshare/) or [WSLiveEditor](https://geode-sdk.org/mods/iandyhd3.wsliveeditor/), which both of them are available on the [Geode](https://geode-sdk.org) modloader
- 4GB patch (not required but **highly** recommended)
- Atleast 1GB of free space in disk

# How to use
- Download the program from [Releases](https://github.com/Fraa4/VideoToGd2.2/releases)
- Extract the folder
- Move the video you want to convert (mp4, avi or gif) in the folder and copy the name of it
- Open "geometrize to gd.exe"
- Paste in the "File name" the name of the file.
- Customize the other settings.
- Check "Use WSLiveEditor" if you want to use the mod, make sure you have it enabled on GD and open a level **editor** before starting the program, otherwise gdshare will be used and at the end a level.gmd file will pop up on the folder
- Click "Generate Animation"
- Wait till the window quit by itself, if you stop it early it will not work.
- Then if you used WSLiveEditor it's already done, if you used gdshare import the level.gmd file in gd.

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
It's recommended that you use an empty level for this, the groups are not customizable and the object position is fixed, you can then copy-paste the animation into another level later.

**NOTE:** You need to stay in the editor in order to make the script work.

# Most common errors

## 1: Video not found:
If the progress bar shows that it is at 0/total it probably means that the program couldn't find the video, make sure you included the right extension and put the video in the same folder as the .exe or the .py.
If it shows that it stopped after some frames maybe there's a corrupted frame or the video simply finished.
In both cases you need to stop the program, fix the issue (maybe download the video again or lower the frames rendered) and run it again.

## 2: Error comunicating with the Editor
Make sure the WSLiveEditor mod is installed and at the latest version, then make sure to open the level editor before starting the program.
If this doesn't fix it check for antiviruses or anything that could block the connection.

# Credits

- Program made by Fra4 (fra4 on Discord)
- GUI made by Hacoc (.nasos. on Discord)
