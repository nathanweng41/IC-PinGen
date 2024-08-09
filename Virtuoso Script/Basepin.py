class BasePins: 
    #basepin for virtuoso
    def __init__(self,origin_x,origin_y,width,height,busname,buswidth,layer,w,s,edge,orient,extension,stop,direction=None) -> None:
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.width = width
        self.height = height

        #Virtuoso BasePin
        if(direction is not None):
            self.layers  = ["M1","M2","C1","C2","C3","C4","C5","OI","JA"]
            self.direction = direction
        #Innovus BasePin
        else:
            self.layers = ["1","2","3","4","5","6","7"]
            self.direction = None

        self.min_w   = [0.040,0.040,0.044,0.044,0.044,0.044,0.044,0,0]
        self.min_s   = [0.040,0.040,0.046,0.046,0.046,0.046,0.046,0,0]
        self.busname = busname
        self.buswidth = buswidth
        self.layer = layer
        self.w = w
        self.s = s
        self.edge = edge
        self.orient = orient
        self.extension = extension
        self.stop = stop

    def duplicateWithOffset(self,iter_offset,spacing):
        if (self.orient == 'l_r' or self.orient == 'r_l'):
            directionFactor = 1 if self.orient == "l_r" else -1 
            new_x = self.origin_x + iter_offset * spacing * directionFactor
            return BasePins(new_x,self.origin_y,self.width,self.height,self.busname,self.buswidth,self.layer,self.w,self.s,self.edge,self.orient,self.extension,self.stop,self.direction)
        elif (self.orient == 'b_t' or self.orient == 't_b'):
            directionFactor = 1 if self.orient == 'b_t' else -1
            new_y = self.origin_y + iter_offset * spacing * directionFactor
            return BasePins(self.origin_x,new_y,self.width,self.height,self.busname,self.buswidth,self.layer,self.w,self.s,self.edge,self.orient,self.extension,self.stop,self.direction)

    def setOriginX(self, x_origin):
        self.origin_x = x_origin

    def setOriginY(self, y_origin):
        self.origin_y = y_origin

    def setWidth(self, width):
        self.width = width

    def setHeight(self, height):
        self.origin_y = height
    
    def getOriginX(self):
        return self.origin_x
    
    def getOriginY(self):
        return self.origin_y
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height

    def isVirtuoso(self):
        if(self.direction is not None):
            return True
        else:
            return False