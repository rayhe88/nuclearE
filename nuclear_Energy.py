#!/usr/bin/env python
# -*- coding: utf-8 -*-
from iodata import *
import numpy as np
import sys


def nuclearEnergy(namefile):
    mol = load_one(namefile)


    if(len(mol.atnums) != len(mol.atcoords)):
        raise Exception(" The size of atcoords and atnums is different")

    totalAtoms = len(mol.atnums)
    energy = 0.
    for i in range(totalAtoms):
        for j in range(i+1, totalAtoms):
            dist = np.linalg.norm(mol.atcoords[i] - mol.atcoords[j])
            energy += mol.atnums[i] * mol.atnums[j] / dist

    return energy


if __name__ == "__main__":
    if(len(sys.argv) == 2):
        for i, arg in enumerate(sys.argv):
            if(i == 1):
                nucenergy = nuclearEnergy(arg)
                print(f" Energy = {nucenergy}")
