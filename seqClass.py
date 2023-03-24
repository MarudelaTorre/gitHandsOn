#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser
#The argparse module makes it easy to write user-friendly command-line interfaces 

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

#The argparse module also automatically generates help and usage messages.
#The module will also issue errors when users give the program invalid arguments.

args = parser.parse_args()

#Defining the characteristics of each type of sequence (DNA or RNA), even if they are write in uppercase or lowercase
#Instructions say what to print in each case (if the sequence is DNA, RNA or neither).
args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

#Defining the conditions to search motifs in a sequence and what to print in case of found them (or not)
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
