#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, json

courses_in = {}
courses_out = {}
majors_in = {}
majors_out = {}

with open('courses.json') as outfile:
	courses_in = json.load(outfile)

with open('courses.txt', 'w') as outfile:
	i = 1
	for c in courses_in:
		outfile.write("%d\t%s\t%s\t%s\t%s\t%s\t%s\n" % 
			(
				i,
				c["title"].encode('ascii', 'ignore'),
				c["cid"].encode('ascii', 'ignore'),
				c["terms"].encode('ascii', 'ignore'),
				c["instructors"].encode('ascii', 'ignore'),
				c["credits"],
				c["overview"].encode('ascii', 'ignore')
			)
		)
		i+=1

# with open('courses.json') as outfile:
# 	courses_in = json.load(outfile)

# with open('majors.json') as outfile:
# 	majors_in = json.load(outfile)

# for course in courses_in:
# 	if course["subj"] not in courses_out : courses_out[course["subj"]] = []
# 	courses_out[course["subj"]].append(course)

# for major in majors_in:
# 	if major["major"] not in majors_out : majors_out[major["major"]] = []
# 	majors_out[major["major"]].append(major["course"])

# with open('courses_formated.json', 'w') as outfile:
# 	json.dump(courses_out, outfile)

# with open('majors_formated.json', 'w') as outfile:
# 	json.dump(majors_out, outfile)

