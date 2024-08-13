
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
    out_fn = "output/"+current_file_name+"_out.txt"
    group = PinGroup(-49.393)
    out_fh = open(out_fn,'w')
    core_x = (49.393)*2
    offset = 49.393+10
    #mirr2
    mirr_2_AMP_EN = BasePins(0.022+offset,0,core_x,10,"mirr_2_AMP_EN",1,"3",0.044,0.046,"top","l_r",2,3)
    group.add(mirr_2_AMP_EN)
    mirr_2_AMP_ENB = BasePins(.126+offset,0,core_x,10,"mirr_2_AMP_ENB",1,"3",0.044,0.046,"top","l_r",2,3)
    group.add(mirr_2_AMP_ENB)
    mirr_2_AMP_BYEPASSB = BasePins(0.639+offset,0,core_x,10,"mirr_2_AMP_BYEPASSB",1,"3",0.044,0.046,"top","l_r",2,3)
    group.add(mirr_2_AMP_BYEPASSB)
    mirr_2_AMP_BYEPASS = BasePins(0.729+offset,0,core_x,10,"mirr_2_AMP_BYEPASS",1,"3",0.044,0.046,"top","l_r",2,3)
    group.add(mirr_2_AMP_BYEPASS)
    mirr_2_rb = BasePins(1.43+offset,0,core_x,10,"mirr_2_rb",2,"3",0.044,0.476,"top","l_r",2,10)
    group.add(mirr_2_rb)
    mirr_2_r = BasePins(1.534+offset,0,core_x,10,"mirr_2_r",2,"3",0.044,0.476,"top","l_r",2,10)
    group.add(mirr_2_r)
#
#    #mirr1
    mirr_1_rb = BasePins(5.111+offset,0,core_x,10,"mirr_1_rb",2,"3",0.044,0.476,"top","r_l",2,10)
    group.add(mirr_1_rb)
    mirr_1_r = BasePins(5.215+offset,0,core_x,10,"mirr_1_r",2,"3",0.044,0.476,"top","r_l",2,10)
    group.add(mirr_1_r)
    mirr_1_AMP_BYEPASS = BasePins(5.889+offset,0,core_x,10,"mirr_1_AMP_BYEPASS",1,"3",0.044,0.046,"top","l_r",2,3)
    group.add(mirr_1_AMP_BYEPASS)
    mirr_1_AMP_BYEPASSB = BasePins(5.979+offset,0,core_x,10,"mirr_1_AMP_BYEPASSB",1,"3",0.044,0.046,"top","l_r",2,3)
    group.add(mirr_1_AMP_BYEPASSB)
    mirr_1_AMP_EN = BasePins(6.069+offset,0,core_x,10,"mirr_1_AMP_EN",1,"3",0.044,0.046,"top","l_r",2,3)
    group.add(mirr_1_AMP_EN)
    mirr_1_AMP_ENB = BasePins(6.159+offset,0,core_x,10,"mirr_1_AMP_ENB",1,"3",0.044,0.046,"top","l_r",2,3)
    group.add(mirr_1_AMP_ENB)
#
#    #mirr0
    mirr_0_AMP_EN = BasePins(37.474+offset,0,core_x,10,"mirr_0_AMP_EN",4,"3",0.044,8.625,"top","r_l",2,10)
    group.add(mirr_0_AMP_EN)
    mirr_0_AMP_ENB = BasePins(37.564+offset,0,core_x,10,"mirr_0_AMP_ENB",4,"3",0.044,8.625,"top","r_l",2,10)
    group.add(mirr_0_AMP_ENB)
    mirr_0_AMP_BYEPASS = BasePins(37.654+offset,0,core_x,10,"mirr_0_AMP_BYEPASS",4,"3",0.044,8.625,"top","r_l",2,10)
    group.add(mirr_0_AMP_BYEPASS)
    mirr_0_AMP_BYEPASSB = BasePins(37.744+offset,0,core_x,10,"mirr_0_AMP_BYEPASSB",4,"3",0.044,8.625,"top","r_l",2,8)
    group.add(mirr_0_AMP_BYEPASSB)
    mirr_0_l = BasePins(15.571+offset,0,core_x,10,"mirr_0_l",3,"5",0.044,0.046,"top","l_r",2,10)
    group.add(mirr_0_l)
    mirr_0_lb = BasePins(15.841+offset,0,core_x,10,"mirr_0_lb",3,"5",0.044,0.046,"top","l_r",2,10)
    group.add(mirr_0_lb)
#
    mirr_0_rGroup = PinGroup(-8.669)
    mirr_0_r = BasePins(42.118+offset,0,core_x,10,"mirr_0_r",3,"5",0.044,0.046,"top","l_r",2,24)
    mirr_0_rGroup.add(mirr_0_r)
    mirr_0_rGroup.duplicateGroup(4)
    group.add(mirr_0_rGroup)
#
    mirr_0_rbGroup = PinGroup(-8.669)
    mirr_0_rb = BasePins(42.388+offset,0,core_x,10,"mirr_0_rb",3,"5",0.044,0.046,"top","l_r",2,24)
    mirr_0_rbGroup.add(mirr_0_rb)
    mirr_0_rbGroup.duplicateGroup(4)
    group.add(mirr_0_rbGroup)
#
    group.duplicateGroup(2)
#
    group.newGroup()
#    #--------------------------------- DO NOT DUPLICATE EVERYTHING UNDER HERE! -------------------------------------------------
#    #Extras that don't align and with the analog block (placed on the right):
#
    mirr_0_ENB_OUT = BasePins(11,0,core_x,10,"mirr_0_ENB_OUT",8,"5",0.044,0.046,"bottom","l_r",2,10)
    group.add(mirr_0_ENB_OUT)
#
    mirr_0_EN_OUT = BasePins(13,0,core_x,10,"mirr_0_EN_OUT",8,"5",0.044,0.046,"bottom","l_r",2,10)
    group.add(mirr_0_EN_OUT)
#
#    #bottom pins
#
    EXECUTE_EN = BasePins(15,0,core_x,10,"EXECUTE_EN",1,"3",0.044,0.046,"bottom","l_r",2,1)
    group.add(EXECUTE_EN)

    ADC_DONE = BasePins(17,0,core_x,10,"ADC_DONE",1,"3",0.044,0.046,"bottom","l_r",2,1)
    group.add(ADC_DONE)

    CLK = BasePins(19,0,core_x,10,"CLK",1,"3",0.044,0.046,"bottom","l_r",2,1)
    group.add(CLK)

    COLUMN_EN = BasePins(21,0,core_x,10,"COLUMN_EN",2,"3",0.044,10,"bottom","l_r",2,10)
    group.add(COLUMN_EN)

    OVERRIDE_CTRL = BasePins(23,0,core_x,10,"OVERRIDE_CTRL",2,"3",0.044,10,"bottom","l_r",2,10)
    group.add(OVERRIDE_CTRL)

    OVERRIDE_EN = BasePins(25,0,core_x,10,"OVERRIDE_EN",2,"3",0.044,10,"bottom","l_r",2,10)
    group.add(OVERRIDE_EN)

    #bottom pins
    in_mirr_0_IOUT_EN = BasePins(27,0.83,core_x,10,"in_mirr_0_IOUT_EN",8,"5",0.044,0.046,"bottom","l_r",2,10)
    group.add(in_mirr_0_IOUT_EN)

    in_mirr_0_SLICE_AMP_EN = BasePins(29,1.67,core_x,10,"in_mirr_0_SLICE_AMP_EN",8,"5",0.044,0.046,"bottom","l_r",2,10)
    group.add(in_mirr_0_SLICE_AMP_EN)

    in_mirr_0_SLICE_BYEPASS = BasePins(31,2.50,core_x,10,"in_mirr_0_SLICE_BYEPASS",8,"5",0.044,0.046,"bottom","l_r",2,10)
    group.add(in_mirr_0_SLICE_BYEPASS)

    in_mirr_0_l = BasePins(33,3.3267,core_x,10,"in_mirr_0_l",6,"5",0.044,0.046,"bottom","l_r",2,10)
    group.add(in_mirr_0_l)

    in_mirr_0_r = BasePins(38,4.157,core_x,10,"in_mirr_0_r",24,"5",0.044,0.046,"bottom","l_r",2,25)
    group.add(in_mirr_0_r)

    in_mirr_1_r = BasePins(43,6.5,core_x,10,"in_mirr_1_r",4,"5",0.044,0.046,"bottom","l_r",2,25)
    group.add(in_mirr_1_r)

    in_mirr_1_AMP_BYEPASS = BasePins(45,7.057,core_x,10,"in_mirr_1_AMP_BYEPASS",2,"5",0.044,0.046,"bottom","l_r",2,25)
    group.add(in_mirr_1_AMP_BYEPASS)

    in_mirr_1_AMP_EN = BasePins(47,7.887,core_x,10,"in_mirr_1_AMP_EN",2,"5",0.044,0.046,"bottom","l_r",2,25)
    group.add(in_mirr_1_AMP_EN)

    in_mirr_2_r = BasePins(51,8.717,core_x,10,"in_mirr_2_r",4,"5",0.044,0.046,"bottom","l_r",2,25)
    group.add(in_mirr_2_r)

    in_mirr_2_AMP_EN = BasePins(53,9.547,core_x,10,"in_mirr_2_AMP_EN",2,"5",0.044,0.046,"bottom","l_r",2,25)
    group.add(in_mirr_2_AMP_EN)

    in_mirr_2_AMP_BYEPASS = BasePins(55,9.70,core_x,10,"in_mirr_2_AMP_BYEPASS",2,"5",0.044,0.046,"bottom","l_r",2,25)
    group.add(in_mirr_2_AMP_BYEPASS)














    #group = PinGroup()
#    group.duplicateGroup(2)

    #endGroup = PinGroup(0.832)
    #endGroup.add(pin2)
    #endGroup.duplicateGroup(41)
    print(group.itemList)

    group.genOutput(out_fh,"innovus")


    #Block.addPins(pin2)
    out_fh.close()

if __name__ == '__main__':
    main()