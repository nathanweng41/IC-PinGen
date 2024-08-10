
from Pingroup import * 
from pathlib import Path
import pandas as pd

def main():

    """ How to Use

    Virtuoso INPUT:
    (origin_x, origin_y, width, height, busname, buswidth, layer, w, s, edge, orient, extension, stop, direction)
    Innovus INPUT:
    Same as Virtuoso's INPUT but remove the direction at the end
    
    When generating the OUTPUT, specify whether it is an Virtuoso or Innovus OUTPUT
    [object_name].genOutput([fileHandle], "innovus"/"virtuoso")

    """
    #mp = pin_generator.mam_pins()
    current_file_name = Path(__file__).stem
    out_fn = "C:/Users/natha/GitHub/IC-PinGen/output/"+current_file_name+"_out.txt"

    out_fh = open(out_fn,'w')
    df = pd.read_csv('SigNames.csv')
    #inout pins 
    topList = ["VSS","CLK1_PAD","CLK2_PAD","AVDD","VNEG0P6","VNEG","VNEG_erase","VIN_LDO1","VIN_LDO2","VDD_PRG_BL_S_SW","VDD_PRG_BL_S"]
    i = 0
    group = PinGroup(1)
    for signal in topList:
        group.add(BasePins(41.66667+i*41.66667,0,500,300,signal,1,"OI",2,10,"top","l_r",10,1,"inputOutput"))
        i+=1

    i=0
    rightList=["ADC_OUT","ADC_OUT","ADC_OUT","ADC_OUT","ADC_OUT","ADC_OUT","ADC_OUT","ADC_OUT","INPUT1","INPUT2"]
    for signal in rightList:
        if signal == "ADC_OUT":
            group.add((BasePins(0,27.27273+i*27.27273,500,300,signal,1,"JA",2,10,"right","b_t",5,50,"inputOutput")))
            i+=1
        else:
            group.add(BasePins(0,27.27273+i*27.27273,500,300,signal,1,"JA",2,10,"right","b_t",5,1,"inputOutput"))
            i+=1

    i=0
    leftList = ["DVDD","macro_aout","macro_dout"]
    for signal in leftList:
        group.add(BasePins(0,75+i*75,500,300,signal,1,"JA",2,10,"left","b_t",10,1,"inputOutput"))
        i+=1

    i=0
    bottomList = ["Ibias1u","AVDD2","VREF","VB_DELAY","VREAD","CTT_body","V1P1","VDD1p8","VDD_TIA2","VDD_TIA1","VDD_erase_BL_S","VDD_prg","VDD_prg_BL_US"]
    for signal in bottomList:
        group.add(BasePins(35.71429+i*35.71429,0,500,300,signal,1,"OI",2,10,"bottom","l_r",10,1,"inputOutput"))
        i+=1

    #output pins
    i=0
    outputList = ["ADC_TO_DIG","CLK_DIG_ROOT"]
    for signal in outputList:
        if signal == "ADC_TO_DIG":
            group.add(BasePins(0,100+i*100,500,300,signal,16,"C2",.044,.2,"left","b_t",5,17,"output"))
            i+=1
        else:
            group.add(BasePins(0,100+i*100,500,300,signal,1,"C2",.044,.2,"left","b_t",5,1,"output"))
            i+=1
    i=0
    #input pins
    #WL pin
    group.add(BasePins(490,0,500,300,"WL",2048,"C1",0.044,0.046,"top","r_l",5,5000,"input"))
    #leafclkpin on c1:
    group.add(BasePins(250,0,500,300,"LEAF_CLK_IN",1,"C1",0.044,0.046,"bottom","l_r",5,1,"input"))
    #all other bottom input pins
    signal_names = df['Signal Name'].values
    widths = df['Width'].values
    x_start = 10
    for signal,width in zip(signal_names,widths):
        if width==1:
            group.add(BasePins(x_start,0,500,300,signal,width,"C3",0.044,0.2,"bottom","l_r",5,1,"input"))
            x_start += 5
        else:
             group.add(BasePins(x_start,0,500,300,signal,width,"C3",0.044,0.2,"bottom","l_r",5,width+1,"input"))
             x_start = x_start + 5 + (width*.244)
    #endGroup = PinGroup(0.832)
    #endGroup.add(pin2)
    #endGroup.duplicateGroup(41)
    #print(group.itemList)
 
    #group.newGroup(36.712)
    #group.duplicateGroup(6)
    #group.add(endGroup)
    
    group.genOutput(out_fh,"virtuoso")


    #Block.addPins(pin2)
    out_fh.close()

if __name__ == '__main__':
    main()