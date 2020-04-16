# GearRecOut
This pipeline aims to provide a tool for shielded the recombination region base the HMM and bayes analysis of FastGear(Mostowy, R. et al. Efficient inference of recent and ancestral recombination
within bacterial populations. Mol. Biol. Evol. 34, 1167–1182 (2017).)
#useage:

#python letgo.py -i <.fasta after mafft or other similar software> -m <your mcr dir> -o <your output dir> -f <your output name>  -R <wheather shielded the recombination region(ance/recent/both)>
ance :sheild the ancestral recombinations region
recent: sheild the recent recombinations region
both : sheild all of the recombinations region

#example
python letgo.py -i alignment-rec.fa -m /usr/local/MATLAB/MATLAB_Runtime/v901/ -o mydata -f dataname -R both
