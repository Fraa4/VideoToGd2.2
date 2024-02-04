from colorsys import rgb_to_hsv as rgbhsv
from subprocess import run as cmd
from cv2 import imwrite, resize, VideoCapture
from moviepy.editor import VideoFileClip
import websockets
import asyncio
from json import dumps
import os
from gzip import compress
from base64 import urlsafe_b64encode

#Add
def Add(obj):
    if(Method==True):
        asyncio.get_event_loop().run_until_complete(AsAdd(obj))
    else:
        with open("var.txt","a") as f:
            f.write(obj)
            

async def AsAdd(obj):
    uri = "ws://127.0.0.1:1313"

    async with websockets.connect(uri) as websocket:
        # Send a message to the WebSocket server
        message = {
            "action": "ADD",
            "objects": obj
        }
        message_json = dumps(message)
        await websocket.send(message_json)




#Clean
    WIDTH=1
def Clean():
    for file in os.listdir('output'):
        file_path = os.path.join("output", file)
        os.remove(file_path)
    for file in os.listdir('output2'):
        file_path = os.path.join("output2", file)
        os.remove(file_path)
    for file in os.listdir('Files'):
        file_path = os.path.join("Files", file)
        os.remove(file_path)
    os.remove("var.txt")
#getConfig
with open("config.txt") as c:
    config=c.read()
config=config.split("\n")
fileN=config[0][config[0].find("<")+1:config[0].find(">")]
NShapes=config[1][config[1].find("<")+1:config[1].find(">")]
Shapes=config[2][config[2].find("<")+1:config[2].find(">")]
SKIP=int(config[3][config[3].find("<")+1:config[3].find(">")])
FPS=int(config[4][config[4].find("<")+1:config[4].find(">")])
FRAMES=int(config[5][config[5].find("<")+1:config[5].find(">")])
RES=int(config[6][config[6].find("<")+1:config[6].find(">")])
SpG=config[7][config[7].find("<")+1:config[7].find(">")]
Mutations=config[8][config[8].find("<")+1:config[8].find(">")]
SCALE=int(config[9][config[9].find("<")+1:config[9].find(">")])
Method=bool(int(config[10][config[10].find("<")+1:config[10].find(">")]))
print(Method)
with open("var.txt","w") as flie:
    flie.write("kS38,1_0_2_0_3_0_11_255_12_255_13_255_4_-1_6_1000_7_1_15_1_18_0_8_1|1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1001_7_1_15_1_18_0_8_1|1_0_2_102_3_255_11_255_12_255_13_255_4_-1_6_1009_7_1_15_1_18_0_8_1|1_255_2_255_3_255_11_255_12_255_13_255_4_-1_6_1002_5_1_7_1_15_1_18_0_8_1|1_40_2_125_3_255_11_255_12_255_13_255_4_-1_6_1013_7_1_15_1_18_0_8_1|1_40_2_125_3_255_11_255_12_255_13_255_4_-1_6_1014_7_1_15_1_18_0_8_1|1_125_2_0_3_255_11_255_12_255_13_255_4_-1_6_1005_5_1_7_1_15_1_18_0_8_1|1_0_2_255_3_255_11_255_12_255_13_255_4_-1_6_1006_5_1_7_1_15_1_18_0_8_1|1_23_2_25_3_121_11_255_12_255_13_255_4_-1_6_1_5_1_7_0.6_15_1_18_0_8_1|1_0_2_255_3_255_11_255_12_255_13_255_4_-1_6_2_5_0_7_0.5_15_1_18_0_8_1|1_255_2_255_3_255_11_255_12_255_13_255_4_-1_6_1004_7_1_15_1_18_0_8_1|,kA13,0,kA15,0,kA16,0,kA14,,kA6,0,kA7,0,kA25,0,kA17,0,kA18,0,kS39,0,kA2,0,kA3,0,kA8,0,kA4,0,kA9,0,kA10,0,kA22,0,kA23,0,kA24,0,kA27,1,kA40,1,kA41,1,kA42,1,kA28,0,kA29,0,kA31,1,kA32,1,kA36,0,kA43,0,kA44,0,kA45,1,kA33,1,kA34,1,kA35,0,kA37,1,kA38,1,kA39,1,kA19,0,kA26,0,kA20,0,kA21,0,kA11,0;")
with open("level.gmd", "w") as f:
    f.write("")

rfr=1/FPS
factor=float(RES/100)
print("Objects estimate: "+str(float(NShapes)*float(FRAMES)))
fileOut="file.json"
bl=False
if(fileN[len(fileN)-3:len(fileN)]=="gif"):
    bl=True

#getImages
def getImages(bl):
    if(bl):
        clip = VideoFileClip(fileN)
        clip.write_videofile("Files/video.mp4")
        capture = VideoCapture('Files/video.mp4')
    else:
        capture = VideoCapture(fileN)
    frameNr = 0
    fs=1
    

    for z in range(0,FRAMES*(SKIP)):
        
        success, frame = capture.read()
    
        if success:
            global WIDTH
            WIDTH=frame.shape[1]/(frame.shape[0]/RES)
            frame=resize(frame,(int(WIDTH),RES))
            imwrite(f'output/frame_{frameNr}.jpg', frame)
    
        else:
            break
        print("Created Frame: "+str(frameNr+1)+"/"+str(float(FRAMES)*float(SKIP)))
        frameNr = frameNr+1
        


        fs=int((frameNr*SKIP)+1)
        
    return frameNr
    capture.release()

frames=getImages(bl)/(SKIP)
print(frames)
lvlstr=""
for sFrame in range(0,int(frames)):
    id=sFrame+1
    print("Converting frame"+str(sFrame))
    cmd('geometrize -i output/frame_'+str(sFrame*SKIP)+'.jpg -o output2/'+str(sFrame)+'.json -s '+NShapes+' -t "'+Shapes+'" -m '+Mutations+' -c '+SpG)

    with open("output2/"+str(sFrame)+".json") as file:
        f=file.read()
    f=f.split("\n")
    
    for a in range(1,len(f)-1):
        d=f[a]
        #create Data[]
        indtype=d.find('e":')+3
        indtype2=d[indtype:len(d)].find(',')
        typ=d[indtype:indtype2+indtype]
        ind1=d.find('data":')
        data=d[ind1+7:len(d)]
        ind2=data.find("]")
        data=data[0:ind2]
        #create Color[]
        ind1=d.find('color":')
        color=d[ind1+8:len(d)]
        ind2=color.find("]")
        color=color[0:ind2]

        #Convert Data to GD
        instr="1,3802,2,"
        data=data.split(",")
        obj=""
        xPos=str(float(data[0])/factor*SCALE+4800)
        yPos=str(((2000-(float(data[1])/factor*SCALE)))+(600*(id-1)))
        match int(typ):
            case 32:
                obj=instr+xPos+",3,"+yPos+",57,"+str(int(sFrame)+2)+",21,2,128,"+str(float(data[2])/(factor)*4*SCALE/30)+",129,"+str(float(data[2])/(factor)*4*SCALE/30)+",41,1,43,"

            case 8:
                obj=instr+xPos+",3,"+yPos+",57,"+str(int(sFrame)+2)+",21,2,128,"+str(float(data[2])/(factor)*4*SCALE/30)+",129,"+str(float(data[3])/(factor)*4*SCALE/30)+",41,1,43,"
            case 1:
                xPos=(float(data[0])/(factor)+float(data[2])/(factor))/2
                yPos=(float(data[1])/(factor)+float(data[3])/(factor))/2
                xScale=float(data[0])/(factor)-float(data[2])/(factor)
                yScale=float(data[1])/(factor)-float(data[3])/(factor)
                obj="1,211,2,"+str(xPos*SCALE+4800)+",3,"+str((2000-(yPos*SCALE))+(600*(id-1)))+",57,"+str(int(sFrame)+2)+",21,2,128,"+str(float(xScale*SCALE/30))+",129,"+str(float(yScale*SCALE/30))+",41,1,43,"
            case 16:
                    obj=instr+xPos+",3,"+yPos+",57,"+str(int(sFrame)+2)+",6,"+str(data[4])+",21,2,128,"+str(float(data[2])/(factor)*4*SCALE/30)+",129,"+str(float(data[3])/(factor)*4*SCALE/30)+",41,1,43,"
                #Convert Color to GD
        color=color.split(",")
        (r, g, b) = (float(color[0])/255, float(color[1])/255, float(color[2])/255)
        (h, s, v) = rgbhsv(r, g, b)
        h=h*360-180
        value=str(h)+"a"+str(s)+"a"+str(v)+"a0a0;"
        obj=obj+value
        Add(obj)
        



    Add("1,1268,2,"+str(300+(id*30))+",3,1335,57,"+str(frames+1+id)+",62,1,87,1,36,1,51,"+str(frames+2+id)+",63,"+str(rfr)+";")

    if(id!=1):
        Add("1,901,2,"+str(300+(id*30))+",3,225,57,"+str(frames+id)+",62,1,87,1,36,1,51,"+str(id+1)+",28,0,29,"+str(-(id-1)*600)+",10,0,30,0,85,2,544,1;")
        Add("1,901,2,"+str(300+(id*30))+",3,255,57,"+str(frames+id)+",62,1,87,1,36,1,51,"+str(id)+",28,0,29,"+str(-900)+",10,0,30,0,85,2,544,1;")
    

xPos=float(WIDTH/2)*SCALE/factor+4800
yPos=((2000-(float(RES/2)*SCALE/factor)))
Add("1,1268,2,100,3,100,36,1,51,"+str(frames+2)+",63,0;1,3802,2,"+str(xPos)+",3,"+str(yPos)+",57,1;")
Add("1,899,2,-15,3,195,155,1,36,1,7,0,8,255,9,255,10,0,35,1,23,2;")
Add("1,1914,2,-15,3,165,155,1,36,1,85,2,71,1,213,1;")

if (Method!=True):
    with open("var.txt","r") as v:
        lvlstr=compress(v.read().encode())
    lvlstr=urlsafe_b64encode(lvlstr)
    strin="<d><k>kCEK</k><i>4</i><k>k18</k><i>43</i><k>k36</k><i>26</i><k>k85</k><i>48</i><k>k86</k><i>13</i><k>k87</k><i>908714</i><k>k88</k><s>99</s><k>k89</k><t/><k>k23</k><i>1</i><k>k19</k><i>99</i><k>k71</k><i>99</i><k>k90</k><i>99</i><k>k20</k><i>99</i><k>k2</k><s>ImageToGd</s><k>k4</k><s>"
    strlast="</s><k>k5</k><s>Fra4</s><k>k95</k><i>1694</i><k>k101</k><s>0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0</s><k>k13</k><t/><k>k21</k><i>2</i><k>k16</k><i>1</i><k>k80</k><i>4013</i><k>k81</k><i>22811</i><k>k42</k><i>98711088</i><k>k45</k><i>76743</i><k>k50</k><i>39</i><k>k47</k><t/><k>k48</k><i>2271</i><k>k66</k><i>9</i><k>kI1</k><r>-2398.72</r><k>kI2</k><r>74.8316</r><k>kI3</k><r>0.1</r><k>kI5</k><i>9</i><k>kI6</k><d><k>0</k><s>0</s><k>1</k><s>0</s><k>2</k><s>2</s><k>3</k><s>0</s><k>4</k><s>0</s><k>5</k><s>0</s><k>6</k><s>0</s><k>7</k><s>0</s><k>8</k><s>0</s><k>9</k><s>0</s><k>10</k><s>6</s><k>11</k><s>0</s><k>12</k><s>0</s><k>13</k><s>0</s></d></d>"
    final=strin+lvlstr.decode()+strlast
    with open("level.gmd","a") as fn:
        fn.write(final)
    print("Done")

Clean()
