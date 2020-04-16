import argparse
def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-R', '--skipped_columns', action='store',
                        type=str,
                        default="n",
                        help='if you want to remove your recombination region')
    parser.add_argument('-i', '--inflie', action='store',
                        type=str,
                        default="n",
                        help='if you want to remove your recombination region')
    parser.add_argument('-m', '--mcrdir', action='store',
                        type=str,
                        default="n",
                        help='if you want to remove your recombination region')
    parser.add_argument('-o', '--outdir', action='store',
                        type=str,
                        default="data",
                        help='if you want to remove your recombination region')
    parser.add_argument('-f', '--outfilename', action='store',
                        type=str,
                        default="data",
                        help='if you want to remove your recombination region')
    return parser.parse_args()

if __name__ == "__main__":
    options = get_options()

    import os
    import sys
    yourinfiledir = options.inflie
    yourmcrdir =options.mcrdir
    youroutputnamedir = options.outdir
    youroutputname = options.outfilename
    selection = ""
    selection  = options.skippe_dcolumns

    os.system("chmod 777 fastGEAR")

    command0 = "mkdir data"
    os.system(command0)

    command00 = "mv " + yourinfiledir + " data"
    os.systtem(command00)
    command1 = "mkdir "+ youroutputnamedir
    command2 = "bash run_fastGEAR.sh "+ yourmcrdir +" "+"data/"+yourinfiledir +" " + youroutputnamedir+"/"+ youroutputname+ " ./fG_input_specs.txt"
    os.system(command1)
    os.system(command2)


    if selection == "ance":
        command3 = "python ./recombinant2out.py " + "data/"+yourinfiledir + " "+ youroutputnamedir+"/output/recombinations_ancestral.txt  " + youroutputnamedir+"/"+ youroutputname+"_anceout"
        os.system(command3)
    if selection == "recent":
        command3 = "python ./recombinant2out.py " + "data/"+yourinfiledir + " "+ youroutputnamedir+"/output/recombinations_recent.txt  " + youroutputnamedir+"/"+ youroutputname+"_recout"
        os.system(command3)

    if selection == "both":
        command3 = "python ./recombinant2out.py " + "data/"+yourinfiledir + " "+ youroutputnamedir+"/output/recombinations_recent.txt  " + youroutputnamedir+"/"+ youroutputname+"_recout"
        command4 = "python ./recombinant2out.py " + youroutputnamedir+"/"+ youroutputname+"_recout" + " "+ youroutputnamedir+"/output/recombinations_ancestral.txt  " + youroutputnamedir+"/"+ youroutputname+"_bothout"

        os.system(command3)
        print(command3)
        os.system(command4)
        print(command4)

