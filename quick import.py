from colorsys import rgb_to_hsv as rgbhsv
from base64 import urlsafe_b64encode
from gzip import compress
from subprocess import run as cmd
from cv2 import imread, imwrite, resize, VideoCapture
from moviepy.editor import VideoFileClip
import os
with open("var.txt","a") as v:
    v.write("1,1268,2,100,3,100,36,1,51,"+str(599+2)+",63,0;")
with open("var.txt","r") as v:
    lvlstr=compress(v.read().encode())
lvlstr=urlsafe_b64encode(lvlstr)
strin="<d><k>kCEK</k><i>4</i><k>k18</k><i>43</i><k>k36</k><i>26</i><k>k85</k><i>48</i><k>k86</k><i>13</i><k>k87</k><i>908714</i><k>k88</k><s>99</s><k>k89</k><t/><k>k23</k><i>1</i><k>k19</k><i>99</i><k>k71</k><i>99</i><k>k90</k><i>99</i><k>k20</k><i>99</i><k>k2</k><s>ImageToGd</s><k>k4</k><s>"
strlast="</s><k>k5</k><s>Fra4</s><k>k95</k><i>1694</i><k>k101</k><s>0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0</s><k>k13</k><t/><k>k21</k><i>2</i><k>k16</k><i>1</i><k>k80</k><i>4013</i><k>k81</k><i>22811</i><k>k42</k><i>98711088</i><k>k45</k><i>76743</i><k>k50</k><i>39</i><k>k47</k><t/><k>k48</k><i>2271</i><k>k66</k><i>9</i><k>kI1</k><r>-2398.72</r><k>kI2</k><r>74.8316</r><k>kI3</k><r>0.1</r><k>kI5</k><i>9</i><k>kI6</k><d><k>0</k><s>0</s><k>1</k><s>0</s><k>2</k><s>2</s><k>3</k><s>0</s><k>4</k><s>0</s><k>5</k><s>0</s><k>6</k><s>0</s><k>7</k><s>0</s><k>8</k><s>0</s><k>9</k><s>0</s><k>10</k><s>6</s><k>11</k><s>0</s><k>12</k><s>0</s><k>13</k><s>0</s></d></d>"
final=strin+lvlstr.decode()+strlast
with open("level.gmd","wb") as fn:
    fn.write(final.encode())
    print("Done")