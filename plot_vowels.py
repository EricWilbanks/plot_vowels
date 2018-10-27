#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import argparse


def process_csv(path,avg):
	"""
	Read in a .csv file from `path` which contains columns "f1","f2","f3","phone"
	Return a parsed pandas DataTable object
	"""	
	data = pd.read_csv(path)
	# user chose to average measurements for phones
	if avg is True:
		data = data.groupby('phone').mean().reset_index()
		print(data)
	return data


def plot_vowels(data):
	"""
	Take in a parsed DataTable object with f1, f2, and phone columns and create a vowel plot.
	"""
	# determine ranges for axes
	f1_min = min(data['f1'])
	f1_max = max(data['f1'])
	f1_ave = data['f1'].mean()

	f2_min = min(data['f2'])
	f2_max = max(data['f2'])
	f2_ave = data['f2'].mean()

	x_range = f2_max-f2_min
	x_min = f2_min - (float(x_range)/10)
	x_max = f2_max + (float(x_range)/10)

	y_range = f1_max-f1_min
	y_min = f1_min - (float(y_range)/10)
	y_max = f1_max + (float(y_range)/10)

	# make figure
	fig, ax = plt.subplots()
	fig.suptitle('Vowel Plot', fontsize=14, fontweight='bold')
	
	# set axes
	ax.set_xlabel('f2 (hz)')
	ax.set_ylabel('f1 (hz)')
	ax.set_xlim([x_min,x_max])
	ax.set_ylim([y_min,y_max])
	plt.gca().invert_xaxis()
	plt.gca().invert_yaxis()

	# plot data
	for iter, row in data.iterrows():
		ax.annotate(row['phone'], (row['f2'], row['f1']))
	plt.show()

	return


#####

if __name__ == "__main__":
	# process arguments
	parser = argparse.ArgumentParser(description='Command line arguments to plot vowels')
	parser.add_argument('-c', '--csv', help = 'path to input .csv')
	parser.add_argument('-a', '--avg', action = 'store_true', help = 'plot mean values for each phone, rather than the default behavior of plotting all points')
	args = parser.parse_args()

	# read in data
	data = process_csv(args.csv,args.avg)
	plot_vowels(data)
	
