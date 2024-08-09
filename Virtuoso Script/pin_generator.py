import sys

class mam_pins:
    N_R=256
    N_C=256
    HYB_TYPE="4-4"
    F=0.104
    #mam_x = 750
    #mam_y = 750

    layers  = ["M1","M2","C1","C2","C3","C4","C5"]
    layers_inv  = ["1","2","3","4","5","6","7"]
    min_w   = [0.040,0.040,0.044,0.044,0.044,0.044,0.044]
    min_s   = [0.040,0.040,0.046,0.046,0.046,0.046,0.046]

    def __init__(self,origin_x,origin_y,mam_x=750,mam_y=750) -> None:
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.mam_x = mam_x
        self.mam_y = mam_y

    #Setters and Getters

    def setOriginX(self, x_origin):
        self.origin_x = x_origin

    def setOriginY(self, y_origin):
        self.origin_y = y_origin
    
    def getOriginX(self):
        return self.origin_x
    
    def getOriginY(self):
        return self.origin_y
    
    def getMamX(self):
        return self.mam_x
    
    def getMamY(self):
        return self.mam_y

    #OUTPUT: bus name, #ofPin, x coord, y coord, layer, edge, I/O,width,extension
    #INPUT: file name, bus name, I/O, # of pins, layer, width, spacing, edge, orient(toptobottom...),extension, IGNORE base_index
    def gen_pin(self, fh, busname,direction, buswidth, layer, w, s, edge, orient, extension,base_index):
        
        lay = self.layers.index(layer)
        if(w<self.min_w[lay] or s<self.min_s[lay]):
            sys.exit("Violates layer rules")
        y = [0]*buswidth
        x = [0]*buswidth
        for i in range(buswidth):
            if(edge=="bottom"):
                lbor="R90"
                y[i]=self.origin_y
                if(orient=="l_r"):
                    x[i]=self.origin_x+i*(w+s)
                else:
                    x[i]=self.mam_x+self.origin_x-i*(w+s)

            if(edge=="top"):
                lbor="R90"
                y[i]=self.mam_y+self.origin_y
                if(orient=="l_r"):
                    x[i]=self.origin_x+i*(w+s)
                else:
                    x[i]=self.mam_x+self.origin_x-i*(w+s)

            if(edge=="left"):
                lbor="R0"
                x[i]=self.origin_x
                if(orient=="t_b"):
                    y[i]=self.mam_y+self.origin_y-i*(w+s)
                else:
                    y[i]=self.origin_y+i*(w+s)

            if(edge=="right"):
                lbor="R0"
                x[i]=self.mam_x+self.origin_x
                if(orient=="t_b"):
                    y[i]=self.mam_y+self.origin_y-i*(w+s)
                else:
                    y[i]=self.origin_y+i*(w+s)
            if(buswidth==1):
                print (busname+" "+"{:.3f}".format(x[i])+" {:.3f}".format(y[i])+" "+layer+" "+edge+" "+direction+" {:.3f}".format(w)+" {:.3f}".format(extension))
                print (busname+" "+"{:.3f}".format(x[i])+" {:.3f}".format(y[i])+" "+layer+" "+edge+" "+direction+" {:.3f}".format(w)+" {:.3f}".format(extension),file=fh)
            else:
                print (busname+"<"+str(i+base_index)+"> "+"{:.3f}".format(x[i])+" {:.3f}".format(y[i])+" "+layer+" "+edge+" "+direction+" {:.3f}".format(w)+" {:.3f}".format(extension))
                print (busname+"<"+str(i+base_index)+"> "+"{:.3f}".format(x[i])+" {:.3f}".format(y[i])+" "+layer+" "+edge+" "+direction+" {:.3f}".format(w)+" {:.3f}".format(extension),file=fh)

#create this class to duplicate once you have a template class with defined origin values and size
class duplicateMam_pins:
    def __init__(self,numBlocks, spacing, fh) -> None:
        self.numBlocks = numBlocks
        self.spacing = spacing
        self.fh = fh
        #dictionary to keep track of busnames
        self.index_tracker = {}

    #set how many repetitions
    def setnumBlocks(self,numBlocks):
        self.numBlocks = numBlocks
    
    def setSpacing(self,spacing):
        self.spacing = spacing

    #generate block horizontally
    def gen_block_horizontal(self,pinTemplate,busname,direction,buswidth,layer,w,s,edge,orient,extension):
        base_index = self.index_tracker.get(busname,0)
        for i in range(self.numBlocks):
            origin_x = pinTemplate.getOriginX() + i * (self.spacing)
            origin_y = pinTemplate.getOriginY()
            newBlock = mam_pins(origin_x, origin_y, pinTemplate.getMamX(), pinTemplate.getMamY())
            newBlock.gen_pin(self.fh,busname,direction,buswidth,layer,w,s,edge,orient,extension,base_index)
            base_index+=buswidth
        self.index_tracker[busname] = base_index

    #generate block vertically
    def gen_block_vertical(self,pinTemplate,busname,direction,buswidth,layer,w,s,edge,orient,extension):
        base_index = self.index_tracker.get(busname,0) 
        for i in range(self.numBlocks):
            origin_x = pinTemplate.getOriginX()
            origin_y = pinTemplate.getOriginY() + i * (self.spacing)
            newBlock = mam_pins(origin_x, origin_y, pinTemplate.getMamX(), pinTemplate.getMamY())
            newBlock.gen_pin(self.fh,busname,direction,buswidth,layer,w,s,edge,orient,extension,base_index)
            base_index+=buswidth
        self.index_tracker[busname] = base_index