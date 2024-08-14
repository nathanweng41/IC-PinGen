
from Pingroup import * 
from pathlib import Path

def main():

    """ How to Use

    Virtuoso INPUT:
    (origin_x, origin_y, width, height, busname, buswidth, layer, w, s, edge, orient, extension, stop, direction)
    Innovus INPUT:
    Same as Virtuoso's INPUT but remove the direction at the end
    
    When generating the OUTPUT, specify whether it is an Virtuoso or Innovus OUTPUT
    [object_name].genOutput([fileHandle], "innovus"/"virtuoso")

    orient:
    r_l --> pin start at the origin_x and decrement based on w and s
    l_r --> pin start at origin_x and increment based on w and s
    t_b --> pin start at origin_y and decrement based on w and s
    b_t --> pin start at origin_y and increment based on w and s
    """
    #mp = pin_generator.mam_pins()
    current_file_name = Path(__file__).stem
    out_fn = "C:/Virtuoso Script/output/"+current_file_name+"_out.txt"

    out_fh = open(out_fn,'w')

    #inputPins (TOP)
    pinCLK1_PAD = BasePins(11,0,60,20,"CLK1_PAD",1,"5",0.044,0.046,"top","l_r",0.5,1)
    pinCLK2_PAD = BasePins(13,66,60,20,"CLK2_PAD",1,"5",0.044,0.046,"top","l_r",0.5,1)
    pinLEAF_CLK_IN = BasePins(15,33,60,20,"LEAF_CLK_IN",1,"5",0.044,0.046,"top","b_t",0.5,1)
    pinMamSrcSel = BasePins(17,0,60,20,"ctrl_mam_adc1_clk_src_sel",2,"5",0.044,0.046,"top","l_r",0.5,10)
    pinMamPw = BasePins(19,0,60,20,"ctrl_mam_adc1_clk_pw",8,"5",0.044,0.046,"top","l_r",0.5,10)
    pinMamSel = BasePins(21,0,60,100,"ctrl_mam_adc1_clk_sel",1,"5",0.044,0.046,"top","l_r",0.5,1)
    pinLeafEn = BasePins(23,0,60,100,"ctrl_leaf_clk_dly_en",1,"5",0.044,0.046,"top","l_r",0.5,1)
    pinLeafDel = BasePins(25,0,60,100,"ctrl_leaf_clk_del",8,"5",0.044,0.046,"top","l_r",0.5,9)
    pinLeafByepass = BasePins(27,0,60,100,"ctrl_leaf_clk_dly_byepass",1,"5",0.044,0.046,"top","l_r",0.5,1)
    pin2MamSrcSel = BasePins(29,0,60,100,"ctrl_mam_adc2_clk_src_sel",2,"5",0.044,0.046,"top","l_r",0.5,5)
    pin2MamPw = BasePins(31,0,60,100,"ctrl_mam_adc2_clk_pw",8,"5",0.044,0.046,"top","l_r",0.5,10)
    pin2MamSel = BasePins(33,0,60,100,"ctrl_mam_adc2_clk_sel",1,"5",0.044,0.046,"top","l_r",0.5,1)
    pinMirrSrcSel = BasePins(35,0,60,100,"ctrl_mam_mirr_clk_src_sel",2,"5",0.044,0.046,"top","l_r",0.5,3)
    pinMirrPw = BasePins(37,0,60,100,"ctrl_mam_mirr_clk_pw",8,"5",0.044,0.046,"top","l_r",0.5,9)
    pinMirrSel = BasePins(39,0,60,100,"ctrl_mam_mirr_clk_sel",1,"5",0.044,0.046,"top","l_r",0.5,1)
    pinctrlMonitor = BasePins(41,0,60,100,"ctrl_mam_timing_monitor_sel",4,"5",0.044,0.046,"top","l_r",0.5,5)
    pinMonitorSel = BasePins(43,0,60,100,"ctrl_mam_adc2_clk_sel",4,"5",0.044,0.046,"top","l_r",0.5,5)
    
    pinDigEn= BasePins(45,0,60,100,"ctrl_dig_clk_en",1,"5",0.044,0.046,"top","l_r",0.5,1)
    pinDigDel = BasePins(47,0,60,100,"ctrl_clk_dig_del",8,"5",0.044,0.046,"top","l_r",0.5,9)
    pinDigByepass = BasePins(49,0,60,100,"ctrl_dig_clk_dly_byepass",1,"5",0.044,0.046,"top","l_r",0.5,1)
    pinDigSel = BasePins(51,0,60,100,"ctrl_mam_dig_clk_src_sel",1,"5",0.044,0.046,"top","l_r",0.5,1)
    #output pins (bottom)
    pinADC1Clk = BasePins(20,0,60,20,"ADC1_CLK",1,"5",0.044,0.046,"bottom","l_r",0.5,1)
    pinADC2Clk = BasePins(30,0,60,20,"ADC2_CLK",1,"5",0.044,0.046,"bottom","l_r",0.5,1)
    pinMirrClk = BasePins(40,0,60,20,"MIRR_CLK",1,"5",0.044,0.046,"bottom","l_r",0.5,1)
    pinClkDig = BasePins(50,0,60,20,"CLK_DIG",1,"5",0.044,0.046,"bottom","l_r",0.5,1)
    pinMonitor = BasePins(60,0,60,20,"MONITOR_OFF_CHIP",1,"5",0.044,0.046,"bottom","l_r",0.5,1)
    group = PinGroup(10)
    group.add(pinCLK1_PAD)
    group.add(pinCLK2_PAD)
    group.add(pinctrlMonitor)
    group.add(pinLEAF_CLK_IN)
    group.add(pinMamSrcSel)
    group.add(pinMamPw)
    group.add(pinMamSel)
    group.add(pinLeafEn)
    group.add(pinLeafDel)
    group.add(pinLeafByepass)
    group.add(pin2MamSrcSel)
    group.add(pin2MamPw)
    group.add(pin2MamSel)
    group.add(pinMirrSrcSel)
    group.add(pinMonitor)
    group.add(pinMirrSel)
    group.add(pinMirrPw)
    group.add(pinMonitorSel)
    group.add(pinDigEn)
    group.add(pinDigDel)
    group.add(pinDigByepass)
    group.add(pinADC1Clk)
    group.add(pinADC2Clk)
    group.add(pinMirrClk)
    group.add(pinClkDig)
    group.add(pinDigSel)

    #endGroup = PinGroup(0.832)
    #endGroup.add(pin2)
    #endGroup.duplicateGroup(41)
    #print(group.itemList)
 
    #group.newGroup(36.712)
    #group.duplicateGroup(6)
    #group.add(endGroup)
    
    group.genOutput(out_fh,"innovus")


    #Block.addPins(pin2)
    out_fh.close()

if __name__ == '__main__':
    main()