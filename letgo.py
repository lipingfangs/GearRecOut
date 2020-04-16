import os
import sys
yourinfiledir = sys.argv[1]
yourmcrdir = sys.argv[2]
youroutputnamedir = sys.argv[3]
youroutputname = sys.argv[4]
selection = ""
selection  = sys.argv[5]

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
    
