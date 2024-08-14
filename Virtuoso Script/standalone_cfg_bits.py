
from Pingroup import * 
from pathlib import Path
import pandas as pd
import xlrd

def main():

    """ ------------------------ How to Use ------------------------

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

    #SET THESE VALUES:
    width = 500
    height = 300
    
    current_file_name = Path(__file__).stem
    out_fn = "C:/Users/natha/GitHub/IC-PinGen/output/"+current_file_name+"_out.txt"

    out_fh = open(out_fn,'w')
    df = pd.read_excel('bits.xlsx',header=None)

    #setting second row as header
    df.columns = df.iloc[1]
    df = df.drop(1).reset_index(drop=True)

    #drop empty rows and columns
    df = df.dropna(axis=1, how='all')
    df = df.dropna(how='all')
    print(df.head())
    #converting side to lowercase
    df['Side'] = df['Side'].str.lower()

    #renaming some stuff for simplicity
    df = df.rename(columns={'Bus direction: l_,r, r_l, t_b, b_t': 'busdirection'})
    df = df.rename(columns={"Location of first pin (bit '0')": 'origin'})
    #looping and grouping... 500x300
    group = PinGroup(10)
    
    for index,row in df.iterrows():
        if(pd.isna(row['Signal Name']) or pd.isna(row['Width']) or pd.isna(row['origin']) or pd.isna(row['busdirection']) or
            pd.isna(row['Side']) or pd.isna(row['Layer']) or pd.isna(row['PinWidth']) or pd.isna(row['Spacing']) or
            pd.isna(row['PinLogical_Direction']) or pd.isna(row['Pin Extension'])):
           continue
        if(row['Side'] == "left"):
            x_origin = 0
            y_origin = row['origin']
        if(row['Side'] == "right"):
            x_origin = width
            y_origin = row['origin']
        if(row['Side'] == "bottom"):
            x_origin = row['origin']
            y_origin = 0
        if(row['Side'] == "top"):
            x_origin = row['origin']
            y_origin = height
        if(row['Width'] == 1):
            pinStop = 1
        else:
            pinStop = row['Width']
        pin = BasePins(x_origin,y_origin,width,height,row['Signal Name'],row['Width'],row['Layer'],row['PinWidth'],row['Spacing'],row['Side'],row['busdirection'],row['Pin Extension'],pinStop,row['PinLogical_Direction'])
        group.add(pin)
    group.genOutput(out_fh,"virtuoso")

    #Block.addPins(pin2)
    out_fh.close()

if __name__ == '__main__':
    main()