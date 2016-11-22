import scrapy, re, os
from scrapy.http import HtmlResponse


class QuotesSpider(scrapy.Spider):

    name = "courses"
    filename = "courses.html"

    def start_requests(self):
        try:
            os.remove(self.filename)
        except OSError:
            pass

        urls = [
            'http://www.mcgill.ca/study/2016-2017/courses/search/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'courses.html'
        courses = response.xpath("//h4[@class='field-content']/a/@href")
        print '\n\n'

        # Visit each course on the current page
        for course in courses:
            course_page = response.urljoin(course.extract())
            yield scrapy.Request(course_page, callback=self.extractCourse)

        # Loop through all pages while there is a next button
        next_page = response.xpath("//a[@title='Go to next page']/@href").extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

        print '\n\n'
        self.log('Saved file %s' % filename)

    def extractCourse(self, response):

        # Get course name
        course_name = response.url.split("/")[-1]

        catalogNotes = response.xpath("//ul[@class='catalog-notes']/li/p")
        # print catalogNotes.extract_first()
        for note in catalogNotes:
            if 'Prerequisite' in note.extract():
                print "\n%s :\n" % course_name
                self.parsePrereqs(str(note.extract()))
                print '\n'

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
