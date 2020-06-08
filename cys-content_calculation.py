#!/usr/bin/python3
# -*- coding: utf-8 -*-

import Bio
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

list_of_protein_cyscontent = []

def sortSecond(val):
    return val[1]

SHORT_MEDIUM_BOUNDARY = 100
MEDIUM_LONG_BOUNDARY = 400

how_many_short = 0
how_many_medium = 0
how_many_long = 0

#for seq_record in SeqIO.parse("test.fasta", "fasta"):
for seq_record in SeqIO.parse("uniprot-organism__Homo+sapiens_+reviewed_yes.fasta", "fasta"):
    seq_string = str(seq_record.seq)
    #print(seq_string)
    analysis_result = ProteinAnalysis(seq_string)
    percent = analysis_result.get_amino_acids_percent()
    #print(seq_record.id, round(percent['C']*100, 4))
    protein_size = len(seq_record)
    list_of_protein_cyscontent.append([seq_record.id, percent['C'], protein_size])
    if protein_size < SHORT_MEDIUM_BOUNDARY:
        how_many_short += 1
    elif protein_size < MEDIUM_LONG_BOUNDARY:
        how_many_medium += 1
    else:
        how_many_long += 1

list_of_protein_cyscontent.sort(key = sortSecond, reverse = True)

number_of_proteins = len(list_of_protein_cyscontent)
header = 'List of all reviewed human proteins ({0}), sorted according to cystein content:\n'.format(number_of_proteins)

short_numbering = 1
medium_numbering = 1
long_numbering = 1

short_protein_list = 'SHORT PROTEINS:\nno length top% %cysteine id\n'
medium_protein_list = 'MEDIUM PROTEINS:\nno length top% %cysteine id\n'
long_protein_list = 'LONG PROTEINS:\nno length top% %cysteine id\n'

for item in list_of_protein_cyscontent:
    if item[2] < SHORT_MEDIUM_BOUNDARY:
        text = str(short_numbering) + ' ' + str(item[2]) + ' (' + str(round(short_numbering*100/how_many_short, 2)) + '%) ' + str(round(item[1]*100,2)) + ' ' + item[0] + '\n'
        short_protein_list += text
        short_numbering += 1
    elif item[2] < MEDIUM_LONG_BOUNDARY:
        text = str(medium_numbering) + ' ' + str(item[2]) + ' (' + str(round(medium_numbering*100/how_many_medium, 2)) + '%) ' + str(round(item[1]*100,2)) + ' ' + item[0] + '\n'
        medium_protein_list += text
        medium_numbering += 1
    else:
        text = str(long_numbering) + ' ' + str(item[2]) + ' (' + str(round(long_numbering*100/how_many_long, 2)) + '%) ' + str(round(item[1]*100,2)) + ' ' + item[0] + '\n'
        long_protein_list += text
        long_numbering += 1

try:
    with open('results.txt', "w") as file:
        file.write(header)
        file.write(short_protein_list)
        file.write(medium_protein_list)
        file.write(long_protein_list)
        file.close()
except Exception as ex:
    print("Could not write list to file. Error: " + str(ex))
