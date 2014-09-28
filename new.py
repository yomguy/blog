#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Guillaume Pellerin <yomguy@parisson.com>

# TimeSide is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# TimeSide is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.


import os, sys, datetime
from collections import OrderedDict
from django.template.defaultfilters import slugify


class PelicanBlogEntry(object):
	""" a raw Pelican blog entry writer """

	def __init__(self):
		self.metadata = ['Title', 'Date', 'Category', 'Tags', 'Author']
		self.dict = OrderedDict()

	def query(self):
		for data in self.metadata:
			if data == 'Date':
				self.dict[data] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
			else:
				self.dict[data] = raw_input(data + ': ')

		self.text = raw_input('Text:\n')
		self.dict['Slug'] = slugify(self.dict['Title'])
		self.dict['Summary'] = self.text[:64] + '...'

	def write(self):
		self.file = open('content' + os.sep + self.dict['Slug'] + '.md', 'w')
		for key in self.dict.keys():
			self.file.write(key + ': ' + self.dict[key] + '\n')
		self.file.write('\n' + self.text)
		self.file.close()

	def run(self):
		self.query()
		self.write()


if __name__ == '__main__':
	b = PelicanBlogEntry()
	b.run()
