import scrapy, re, os, json, sys
from scrapy.http import HtmlResponse

class CoursesSpider(scrapy.Spider):

    # courses_json = {}
    # majors_json = {}

    name = "courses"

    def start_requests(self):


        urls = [
            'http://www.mcgill.ca/study/2016-2017/courses/search/',
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

        # Write local dictionaries into json file

        # with open('courses.json', 'w') as outfile:
        #     json.dump(self.courses_json, outfile)

        # with open('majors.json', 'w') as outfile:
        #     json.dump(self.majors_json, outfile)

    def parse(self, response):
        courses = response.xpath("//h4[@class='field-content']/a/@href")

        # Visit each course on the current page
        for course in courses:
            course_page = response.urljoin(course.extract())
            yield scrapy.Request(course_page, callback=self.extractCourse)

        # Loop through all pages while there is a next button
        next_page = response.xpath("//a[@title='Go to next page']/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    def extractCourse(self, response):
        item = {}
        # Get course name
        item["subj"], item["code"] = response.url.split("/")[-1].split("-")
        item["cid"] = "%s %s" % (item["subj"], item["code"])
        item['title'] = (((response.xpath('//div[@id="inner-container"]/h1/text()').extract_first()).strip( '\n' )[17:-17]).rstrip(' ')).encode('utf-8')
        try:
            item['credits'] = (re.search(r'.*?\((\d)', response.xpath('//div[@id="inner-container"]/h1/text()').extract_first().strip( '\n' )).group(1)).encode('utf-8')
        except:
            item['credits'] = 0
        item['overview'] = (response.xpath('//div[@class="content"]/p/text()').extract_first().strip( '\n ' )).encode('utf-8')
        item['terms']  = (re.search(r'.*?\: (.*)', response.xpath('//p[@class="catalog-terms"]/text()').extract_first()).group(1).strip()).encode('utf-8')
        item['instructors'] = (re.search(r'.*?\: (.*)', response.xpath('//p[@class="catalog-instructors"]/text()').extract_first()).group(1).strip()).encode('utf-8')
        item['preqs'] = map(lambda x: x.encode('utf-8'), response.xpath('//ul[@class="catalog-notes"]/li/p[contains(., \'Prerequisite\')]/a/text()').extract())
        item['creqs'] = map(lambda x: x.encode('utf-8'), response.xpath('//ul[@class="catalog-notes"]/li/p[contains(., \'Corequisite\')]/a/text()').extract())

        # return course to make json file through terminal
        
        if sys.argv[3] == "courses.json" : yield item

        # Writing courses into local hashmap
        # 
        # if item["subj"] not in self.courses_json: self.courses_json[item["subj"]] = []
        # else : self.courses_json[item["subj"]].append(item)
        
        # return major to make json file through terminal
        
        elif sys.argv[3] == "majors.json" : 
            majors = response.xpath("//div[@class='field-content']/a/text()").extract()
            for major in majors:
                if ' or ' in major:
                    ms = major.split(' or ')
                    for m in ms:
                        yield {'major': m.encode('utf-8'), 'course': item["cid"]}
                else : yield {'major': major.encode('utf-8'), 'course': item["cid"]}

        # Writing majors into local hashmap
        # 
        # for major in majors:
        #     if 'or' in major:
        #         ms = major.split(' or ')
        #         for m in ms:
        #             if m not in self.majors_json: self.majors_json[m] = []
        #             else : self.majors_json[m].append(item["cid"])
        #     else :
        #         if major not in self.majors_json: self.majors_json[major] = []
        #         else : self.majors_json[major].append(item["cid"])



        # Parsing Prereqs

        # catalogNotes = response.xpath("//ul[@class='catalog-notes']/li/p")
        # # print catalogNotes.extract_first()
        # for note in catalogNotes:
        #     if 'Prerequisite' in note.extract():
        #         print "\n%s :\n" % course_name
        #         # self.parsePrereqs(str(note.extract()))
        #         print '\n'

    def parsePrereqs(self, prereqs):

        result = []
        i = 0

        for a in prereqs.split('and'):
            result.append([])
            for o in a.split('or'):
                hrefFinder = re.compile(r"href=\"[A-Za-z0-9_/-]+\">([A-Za-z0-9_ ]+)<")
                for c in hrefFinder.findall(o):
                    result[-1].append(c)
            i += 1

        with open(self.filename, 'a') as f:
            f.write("%s\n%s\n\n" % (prereqs, str(result)))
