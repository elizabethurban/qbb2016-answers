copy files to virtual env called lab_week_8

we have count files for data and bed files for primers

hifive 5c-complete express -h
usage: hifive 5c-complete express [-h] [--re RE] [--genome GENOME]
                                  (-B BAM BAM | -C COUNT) [-f MININT]
                                  [-m MINDIST] [-x MAXDIST] [-r REGIONS] [-q]
                                  (-P PREFIX | -o OUTPUT OUTPUT OUTPUT)
                                  [-e EXPITER] [-d] [-w {cis,trans,all}] [-k]
                                  [-z]
                                  bed
                                  
enrichment is the count divided by the e and the log of that value. 
gives a matrix of fragments - for each fragment, somewhere along the chromosome we have ctcf peaks 
that are in the ctcf file- we want to know if we can identify which fragments have at least
once ctcf, and given the fragments that have ctcf sites, what is its strongest interaction partner?
meaning what is the most enriched itneraction. 

matrix comes out of the .heat file- find which positions the ctcfs line up with- then you can eliminate all the 
positions that dont have ctcf. look at other bins that have highest value then....

hifive 5c-heatmap 5C.fcp Out_fragment_bin0.heat -i Out_fragment_bin0.png -b 0 -d fragment

