import os, json

courses_in = {}
courses_out = {}
majors_in = {}
majors_out = {}

with open('courses.json') as outfile:
	courses_in = json.load(outfile)

with open('majors.json') as outfile:
	majors_in = json.load(outfile)

for course in courses_in:
	if course["subj"] not in courses_out : courses_out[course["subj"]] = []
	courses_out[course["subj"]].append(course)

for major in majors_in:
	if major["major"] not in majors_out : majors_out[major["major"]] = []
	majors_out[major["major"]].append(major["course"])

with open('courses_formated.json', 'w') as outfile:
	json.dump(courses_out, outfile)

with open('majors_formated.json', 'w') as outfile:
	json.dump(majors_out, outfile)

