#!/usr/bin/env python
import glob
import os


def find(pattern, path):
    return (y for y in glob.glob(os.path.join(path, pattern)


def findrec(pattern, path):
    return (y for x in os.walk(path) for y in glob.glob(os.path.join(x[0], pattern)))
