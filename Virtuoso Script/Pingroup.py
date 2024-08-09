import sys

indexTracker = {}

from Basepin import *
    
def flattenGroup(group,depth=0):
    items = []
    for item in group.itemList:
        if isinstance(item, BasePins):
            items.append((item,depth))
        elif isinstance(item, PinGroup):
            items.extend(flattenGroup(item,depth+1))
    return items

def inv_io_header(fh):
    print("(globals",file=fh)
    print("\tversion = 3",file=fh)
    print("\tio_order = default",file=fh)
    print(" )",file=fh)
    print("(iopin",file=fh)

    print("(globals")
    print("\tversion = 3")
    print("\tio_order = default")
    print(" )")
    print("(iopin")

class PinGroup:
    def __init__(self,spacing,itemList=None):
        self.spacing = spacing
        if (itemList == None):
            self.itemList = []
        else:
            self.itemList = itemList
        # implement in the future maybe? self.basePinsList = []
        #listof pins...
        # .
    def setSpacing(self,spacing):
        self.spacing = spacing

    def add(self,element):
        if isinstance(element,(PinGroup,BasePins)):
            self.itemList.append(element)
        else:
           raise TypeError("Only BasePin or PinGroup objects can be added to the group")
        
    def newGroup(self,newSpacing=None):
        if newSpacing == None:
            newSpacing = self.spacing
        else:
            newSpacing = newSpacing
        newGroup = PinGroup(newSpacing,self.itemList.copy())
        self.itemList = [newGroup]
        self.spacing = newSpacing

    def getAllBasePins(self):
        collectedPins = []
        for item in self.itemList:
            if isinstance(item, BasePins):
                collectedPins.append(item)
            elif isinstance(item,PinGroup):
                collectedPins.extend(item.getAllBasePins())
        return collectedPins
    
    def duplicateGroup(self,iterations):
        flat_list = flattenGroup(self)
        for i in range(1,iterations):
            #offset = i * self.spacing
            new_group = PinGroup(self.spacing)
            for pin,depth in flat_list:
                new_pin = pin.duplicateWithOffset(i,self.spacing)
                new_group.add(new_pin)
            self.itemList.append(new_group)

    def genOutput(self,fh,isVirtuoso):
        pins = self.getAllBasePins()
        if(isVirtuoso == "innovus"):
            inv_io_header(fh)
            right_list = []
            left_list = []
            top_list = []
            bottom_list = []
            for pin in pins:
                if(pin.edge == "right"):
                    right_list.append(pin)
                elif(pin.edge == "left"):
                    left_list.append(pin)
                elif(pin.edge == "top"):
                    top_list.append(pin)
                elif(pin.edge == "bottom"):
                    bottom_list.append(pin)
                else:
                    raise TypeError("invalid edge on an innovus pin")
            self.processPinInnovus(fh,"right",right_list)
            self.processPinInnovus(fh,"left",left_list)
            self.processPinInnovus(fh,"top",top_list)
            self.processPinInnovus(fh,"bottom",bottom_list)
            fh.write(")")
        elif(isVirtuoso == "virtuoso"):
            for pin in pins:
                self.processPin(fh,pin)
        else:
            raise TypeError("Invalid software for processing")
        
    def processPin(self,fh,pin): 
        base_index = indexTracker.get(pin.busname,0)
        lay = pin.layers.index(pin.layer)
        if(pin.w<pin.min_w[lay] or pin.s<pin.min_s[lay]):
            sys.exit("Violates layer rules")
        y = [0]*pin.buswidth
        x = [0]*pin.buswidth
        for i in range(pin.buswidth):
            if((base_index+i) < pin.stop):
                if(pin.edge=="bottom" or pin.edge == "top"):
                    lbor="R90"
                    fixed_dimension = pin.origin_y if pin.edge == "bottom" else pin.height + pin.origin_y
                    variable_dimension = pin.origin_x

                    offset = i * (pin.w+pin.s)

                    if(pin.orient=="r_l"):
                        offset = offset * -1
                    
                    x[i],y[i] = (variable_dimension + offset, fixed_dimension)

                elif (pin.edge == "left" or pin.edge == "right"):
                    lbor = "R0"
                    fixed_dimension = pin.origin_x if pin.edge == "left" else pin.width + pin.origin_x
                    variable_dimension = pin.origin_y

                    offset = i * (pin.w+pin.s)
                    if pin.orient == "b_t":
                        offset = offset * -1
                    
                    x[i],y[i] = (fixed_dimension, variable_dimension + offset)
                if(pin.buswidth==1 and pin.stop == 1):
                    print(pin.busname+" "+"{:.3f}".format(x[i])+" {:.3f}".format(y[i])+" "+pin.layer+" "+pin.edge+" "+pin.direction+" {:.3f}".format(pin.w)+" {:.3f}".format(pin.extension))
                    print(pin.busname+" "+"{:.3f}".format(x[i])+" {:.3f}".format(y[i])+" "+pin.layer+" "+pin.edge+" "+pin.direction+" {:.3f}".format(pin.w)+" {:.3f}".format(pin.extension),file=fh)
            
                else:
                    print(pin.busname+"<"+str(base_index+i)+"> "+"{:.3f}".format(x[i])+" {:.3f}".format(y[i])+" "+pin.layer+" "+pin.edge+" "+pin.direction+" {:.3f}".format(pin.w)+" {:.3f}".format(pin.extension))
                    print(pin.busname+"<"+str(base_index+i)+"> "+"{:.3f}".format(x[i])+" {:.3f}".format(y[i])+" "+pin.layer+" "+pin.edge+" "+pin.direction+" {:.3f}".format(pin.w)+" {:.3f}".format(pin.extension),file=fh)
        base_index += pin.buswidth
        #print(f"baseIndex={base_index}" )
        indexTracker[pin.busname] = base_index

    def processPinInnovus(self,fh,side,pins):
        if(len(pins) == 0):
            return 
        else:
            fh.write(f"\t({side}\n")
        for pin in pins:
            base_index = indexTracker.get(pin.busname,0)
            lay = pin.layers.index(pin.layer)
            if pin.w < pin.min_w[lay] or pin.s < pin.min_s[lay]:
                print(f"Pin {pin.busname} violates layer rules: width= {pin.w}, minwidth = {pin.min_w[lay]},spacing ={pin.s},minspacing = {pin.min_s[lay]}")
                sys.exit("Violates layer rules")
            offset = [0] * pin.buswidth
            for i in range(pin.buswidth):
                if((base_index+i) < pin.stop):
                    if pin.edge == "bottom" or pin.edge == "top":
                        if pin.orient == "l_r": 
                            offset[i] = pin.origin_x + i * (pin.w + pin.s)  
                        else: 
                            offset[i] = pin.origin_x + pin.width - i * (pin.w + pin.s)
                    else:
                        if pin.orient == "b_t": 
                            offset[i] = pin.origin_y + i * (pin.w + pin.s) 
                        else: 
                            offset[i] = pin.origin_y + pin.height - i * (pin.w + pin.s)

                    pin_name = f"{pin.busname}[{i+base_index}]" if pin.buswidth > 1 or pin.stop != 1 else pin.busname
                    #pin_output = f"\t\t(pin name=\"{pin_name}\" )"
                    print ("\t\t(pin name=\""+f"{pin_name}"+"\" offset="+"{:.3f}".format(offset[i])+" layer="+pin.layer+" width={:.3f}".format(pin.w)+" depth={:.3f}".format(pin.extension)+" place_status=placed)")
                    print ("\t\t(pin name=\""+f"{pin_name}"+"\" offset="+"{:.3f}".format(offset[i])+" layer="+pin.layer+" width={:.3f}".format(pin.w)+" depth={:.3f}".format(pin.extension)+" place_status=placed)",file=fh) 
            base_index += pin.buswidth
            indexTracker[pin.busname] = base_index
        fh.write("\t)\n")