# label-video
Framework to process video &amp; output labeled frames for model consumption. Configurable, and requires human.
ffmpeg -i test.mov out.mp4 can be useful


# PREP
1. place all video files in video folder. be sure they are .mp4
2. go to run.py and change target videos, but keep destinationFrames alone.


Create the a folder, lets call if myFolder: 

Go to your terminal and pwd should show ***/***/myfolder. 
there, ```mkdir video``` and store all videos in this 
finally, ``` git clone https://github.com/rocco-haro/label-video.git ``` 

myFolder structure should look like:
	myFolder - label-video
			 - video 

# dependencies
1. ```pip3 install opencv-python```
2. ```pip3 install matplotlib```

# run 
``` python3 run.py ```

# todo 
write script to read all video files in video folder, and then loop through those file 
names in the run.py script


