'''
Script to create dictionaries that contain diagnostic snps used to identify hammerhead species
Last updated: 8/14/17
A. Barker
'''

import csv
import numpy as np
import pickle

# Dictionary for Great vs Scalloped/Carolina

# get contig names to create list for Key names
with open('SLM1.ScallCar_Great.fixed.formatted.txt') as f:
    reader = csv.reader(f, delimiter = '\t')
    contig_keyList_Great_ScallCar = next(reader)
# Load great vs scalloped/carolina allele data. Note: scalloped/carolina first in file
alleles_Great_ScaCar = np.loadtxt('SLM1.ScallCar_Great.fixed.formatted.txt', skiprows=1)

species_names_great_scacar = ['scalloped/carolina', 'great']

# Create dictioanry
contig_allele_species_Great_ScallCar = {}

# Add alleles to dictionary
for k in range(0, len(contig_keyList_Great_ScallCar)):
    allele_list = []
    contig = contig_keyList_Great_ScallCar[k]
    contig_allele_species_Great_ScallCar[contig] = {}
    for n in range(0, 2):
        allele_list.append(alleles_Great_ScaCar[n, k])
    for n in range(0, 2):
        allele = float(allele_list[n])
        s = species_names_great_scacar[n]
        contig_allele_species_Great_ScallCar[contig][allele] = s

# test
print(contig_allele_species_Great_ScallCar['dDocent_Contig_4_49'][120])

# pickle dictionary for use in other scripts
pickle.dump(contig_allele_species_Great_ScallCar, open('Great_ScallCar_dict.pickle', 'wb'))

#######################################

# Create dictionary for Scalloped vs Carolina

# get contig names to create list for Key names
with open('SLM1.ScallCar.fixed.formatted.txt') as f:
    reader = csv.reader(f, delimiter = '\t')
    contig_keyList_ScallCar = next(reader)
# Load great vs scalloped/carolina allele data. Note: carolina first in file
alleles_ScaCar = np.loadtxt('SLM1.ScallCar.fixed.formatted.txt', skiprows=1)

species_names_scacar = ['carolina', 'scalloped']

# Create dictioanry
contig_allele_species_ScallCar = {}

# Add alleles to dictionary
for k in range(0, len(contig_keyList_ScallCar)):
    allele_list = []
    contig = contig_keyList_ScallCar[k]
    contig_allele_species_ScallCar[contig] = {}
    for n in range(0, 2):
        allele_list.append(alleles_ScaCar[n, k])
    for n in range(0, 2):
        allele = float(allele_list[n])
        s = species_names_scacar[n]
        contig_allele_species_ScallCar[contig][allele] = s
# test
print(contig_allele_species_ScallCar['dDocent_Contig_14_37'][130])

pickle.dump(contig_allele_species_ScallCar, open('Scall_Car_dict.pickle', 'wb'))