#!/usr/bin/env python

"""Makes distance and torsion restraints files of user-specified type

Functions
---------
incorporate :: merge first dict into second dict w/out duplicates

make_restraints ::
	choose which types of restraints you want to generate.

	Options include secondary structure restraints (requires a 
	single letter sequence of 'H', 'E', and 'C' from PSIPRED
	or RaptorX prediction), original_pdb restraints (requires an
	original pdb file to draw restraints from), or contact map
	restraints. Mark option variables true/false.

	Function also optionally takes strings for the name of the
	distance and torsion restraints files

"""

from generators import *

__all__ = ["incorporate", "make_restraints"]

def incorporate(part, main_dict):
	for k in part:
		if main_dict[k] == None: main_dict[k] = part[k]
		elif (part[k][upper] <= main_dict[k][upper]) and (part[k][lower] >= main_dict[k][lower]): #if tighter bound, replace
			main_dict[k] = part[k]

	return main_dict


def make_restraints(secondary_structure=False, contact_map=False, original_pdb=False, hydrogen_bond_distances=False, xu_ml=False, struc_seq="", orig_pdbfile="", linear_pdbfile="", dist_file="distance_restraints", tor_file="torsion_restraints"):
	dist_rst = dict();
	tor_rst = dict();

	#TODO - get Fasta

	if (original_pdb):
		if (orig_pdbfile == "") or (linear_pdbfile == ""):
			exit("Error: Needs name of original and linear pdb files to generate restraints!")
		o_dist, o_tor = make_pdb_rst(orig_pdbfile=orig_pdbfile, linear_pdbfile=linear_pdbfile) #can optionally specify restraint ranges and forces here
                dist_rst = incorporate(o_dist, dist_rst)
                tor_rst = incorporate(o_tor, tor_rst)

	if (secondary_structure):
		s_dist, s_tor = make_sec_struc_rst(seq, struc_seq)
		dist_rst = incorporate(s_dist, dist_rst)
		tor_rst = incorporate(s_tor, tor_rst)

	if (contact_map):
                c_dist, c_tor = make_contact_rst()
                dist_rst = incorporate(c_dist, dist_rst)
                tor_rst = incorporate(c_tor, tor_rst)

	if (hydrogen_bond_distances or xu_ml):
		print("Not yet available. The main ExaFold program does take these restraints if you have them, but we cannot currently generate them on our own.")


	d = open(dist_file, "w+")
	for k in dist_rst:
		d.write() #TODO

	d.close()

	t = open(tor_file, "w+")
	for k in tor_rst:
        	t.write() #TODO

	t.close()

