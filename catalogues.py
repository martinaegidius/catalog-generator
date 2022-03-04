from fpdf import FPDF 
import fpdf
import os #for dirs
import glob #for path-handling

class PDF(FPDF):
    def lines(self,xstart,ystart,xend,yend):
        self.set_line_width(1.0)
        self.line(xstart,ystart,xend,yend) #(x1,y1,x2,y2) origin and end-points
    def rectborder(self):
        self.set_fill_color(65,66,65) #printzlau-grey
        self.rect(5.0,5.0,200.0,287.0,'F')
        self.set_fill_color(255,255,255)
        self.rect(8.0,8.0,194.0,282.0,'F') #fill inner rectangle with paper-white
    def addImage(self,locX,locY,name):
        self.set_xy(locX,locY)
        self.image(name,w=85) #automaticYScaling
        

def loadAllImages(path):
    images = []
    for img in glob.glob(os.path.join(path,'*.jpg')):
        images.append(img)
    return images
        

path = os.path.dirname(os.path.abspath(__file__))
dataDir = os.path.join(path,'fake_folder/') #overfolder containing every operation-type
opDir = os.path.join(dataDir,'op1/') #operation specifier
filename = 'skrt3.pdf'
outputPath = os.path.join(opDir,filename)



pdf_w = 210 #in mm (standard A4 format) 
pdf_h = 297 
pdf = PDF(unit='mm') #object initialization 
pdf.add_page()
pdf.lines(0,pdf_h/2,210,pdf_h/2)
pdf.rectborder()

#image module 
images = loadAllImages(opDir)#load all images in dir

for i in range(len(images)//2):
    #for j in range(2): #number of images on page
    if (i%2==0): #generate new page every time 4 images have been plotted
        pdf.add_page()
        pdf.rectborder()
        
    pdf.addImage(15,(i*(297/2)+30),images[i])
    pdf.addImage(85+25,(i*(297/2)+30),images[i+1])
        
    
#addImage(10,30


pdf.output(outputPath,'F')