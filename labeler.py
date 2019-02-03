import cv2
import os
import matplotlib.pyplot as plt


class Labeler(object):
	def __init__(self, *args):
		self.basedir = os.path.abspath(os.path.dirname(__file__))
		print("starting.")
		self.fileName = args[0]
		self.target = args[1]
		self.filesCreated = []
		self.labeledFrames = []

	def readFile(self):
		print(self.basedir)
		d = self.basedir.split('/')
		base = '/'.join(d[:-1])
		vidcap = cv2.VideoCapture(base+'/video/'+self.fileName)
		success,image = vidcap.read()
		count = 0
		success = True
		while success:
		  success,image = vidcap.read()
		  fileWritePath = self.target+"/"+self.fileName+"_frame%d.jpg" % count
		  cv2.imwrite(fileWritePath, image)     # save frame as JPEG file
		  self.filesCreated.append(fileWritePath)
		  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
		      break
		  count += 1

	def viewAndMarkFrame(self, frame):

		im = cv2.imread(frame)
		im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)

		plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
		plt.show()
		print("What state did you see? (hit-area, travel)")
		print("if hit-area, just type 'hit-area' then press enter.")
		v = input()
		# Change frame name 
		writePath = v+"_"+frame
		self.labeledFrames.append(writePath)

	def viewFrames(self):
		for frame in self.filesCreated:
			self.viewAndMarkFrame(frame)


	def writeLabeledFrames(self):
		d = self.basedir.split('/')
		base = '/'.join(d[:-1]) + "/" +self.fileName+'_labels.txt'
		with open(base, 'w+') as _file:
			for label in self.labeledFrames:
				_file.write(label+'\n')



# targetVideo = 'out.mp4' # CHANGE ME
# framesDest = 'frames'
# s = Labeler(targetVideo, framesDest)
# s.readFile()
# s.viewFrames()
# s.writeLabeledFrames()

