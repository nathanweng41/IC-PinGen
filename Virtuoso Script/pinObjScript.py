
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

    """
    #mp = pin_generator.mam_pins()
    current_file_name = Path(__file__).stem
    out_fn = "C:/Virtuoso Script/output/"+current_file_name+"_out.txt"

    out_fh = open(out_fn,'w')
    pinCLK_PAD = BasePins(0,66,100,100,"CLK_PAD",1,"3",0.044,0.046,"left","b_t",0.5,1)
    pinLEAF_CLK_IN = BasePins(0,33,100,100,"LEAF_CLK_IN",1,"3",0.044,0.046,"left","b_t",0.5,1)

    pinMamSrcSel = BasePins(10,0,100,100,"ctrl_mam_adc1_clk_src_sel",2,"2",0.044,0.046,"bottom","l_r",0.5,10)
    pinMamPw = BasePins(12,0,100,100,"ctrl_mam_adc1_clk_pw",8,"2",0.044,0.046,"bottom","l_r",0.5,5)
    pinMamSel = BasePins(14,0,100,100,"ctrl_mam_adc1_clk_sel",1,"2",0.044,0.046,"bottom","l_r",0.5,1)
    pinLeafEn = BasePins(16,0,100,100,"ctrl_leaf_clk_dly_en",1,"2",0.044,0.046,"bottom","l_r",0.5,1)
    pinLeafDel = BasePins(18,0,100,100,"ctrl_leaf_clk_del",8,"2",0.044,0.046,"bottom","l_r",0.5,9)
    pinLeafByepass = BasePins(20,0,100,100,"ctrl_leaf_clk_dly_byepass",1,"2",0.044,0.046,"bottom","l_r",0.5,1)
    pin2MamSrcSel = BasePins(22,0,100,100,"ctrl_mam_adc2_clk_src_sel",2,"2",0.044,0.046,"bottom","l_r",0.5,5)
    pin2MamPw = BasePins(24,0,100,100,"ctrl_mam_adc2_clk_pw",8,"2",0.044,0.046,"bottom","l_r",0.5,10)
    pin2MamSel = BasePins(26,0,100,100,"ctrl_mam_adc2_clk_sel",1,"2",0.044,0.046,"bottom","l_r",0.5,1)
    pinMirrSrcSel = BasePins(28,0,100,100,"ctrl_mam_mirr_clk_src_sel",2,"2",0.044,0.046,"bottom","l_r",0.5,3)
    pinMirrPw = BasePins(30,0,100,100,"ctrl_mam_mirr_clk_pw",8,"2",0.044,0.046,"bottom","l_r",0.5,9)
    pinMirrSel = BasePins(32,0,100,100,"ctrl_mam_mirr_clk_sel",1,"2",0.044,0.046,"bottom","l_r",0.5,1)


    pinMonitor = BasePins(90,0,100,100,"MONITOR_OFF_CHIP",1,"2",0.044,0.046,"bottom","l_r",0.5,1)
    pinMonitorSel = BasePins(88,0,100,100,"ctrl_mam_adc2_clk_sel",4,"2",0.044,0.046,"bottom","l_r",0.5,5)

    pinDigEn= BasePins(10,0,100,100,"ctrl_dig_clk_en",1,"2",0.044,0.046,"top","l_r",0.5,1)
    pinDigDel = BasePins(12,0,100,100,"ctrl_clk_dig_del",8,"2",0.044,0.046,"top","l_r",0.5,9)
    pinDigByepass = BasePins(14,0,100,100,"ctrl_dig_clk_dly_byepass",1,"2",0.044,0.046,"top","l_r",0.5,1)

    pinADC1Clk = BasePins(0,25,100,100,"ADC1_CLK",1,"3",0.044,0.046,"right","b_t",0.5,1)
    pinADC2Clk = BasePins(0,50,100,100,"ADC2_CLK",1,"3",0.044,0.046,"right","b_t",0.5,1)
    pinMirrClk = BasePins(0,75,100,100,"MIRR_CLK",1,"3",0.044,0.046,"right","b_t",0.5,1)
    group = PinGroup(10)
    group.add(pinCLK_PAD)
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