import argparse
import glob
import os
import pandas as pd
import cv2
from vaODV import vaODV
from saliency_estimate import generate_saliencymap

SOUND_TYPE = ['none', 'mono', 'ambix']

def run(args):
    # height and width of a given ODV
    input_shape = list( map(int, str(args.resolution).split('x')) )
    input_shape.append(3)


    for st in SOUND_TYPE:
        va_odv = vaODV(
            odv_folder=args.odv,
            user_dataset=args.input,
            modality=st,
            odv_shape=input_shape
        )
        

        for odv_count, odv in enumerate(va_odv.odv_list):
            odv_name = odv.split('/')[-2]
            va_odv.display_status(odv_count, odv_name)
            fixation_maps = va_odv.generate_fixations(odv_name)
            
            if args.saliency == True:

                generate_saliencymap(
                    fixation_maps = fixation_maps,
                    output_folder = os.path.join(st, odv_name),
                    segment_no = odv_count
                )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", 
                        "-i", 
                        type=str,
                        required=True,
                        help="Input dataset_public folder location")
    parser.add_argument("--odv", 
                        "-o", 
                        type=str,
                        required=True,
                        help="Input ODV folder location")                        
    parser.add_argument("--resolution", 
                        "-r", 
                        type=str,
                        required=True,
                        help="Resolution size of each ODV, Height x Width")
    parser.add_argument("--saliency", 
                        "-s", 
                        type=bool,
                        required=False,
                        help="Resolution size of each ODV, Height x Width")                        
    args = parser.parse_args()
    run(args)