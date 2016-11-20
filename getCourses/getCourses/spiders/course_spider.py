import scrapy


class QuotesSpider(scrapy.Spider):

    name = "courses"

    def start_requests(self):
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

        # # Loop through all pages while there is a next button
        # next_page = response.xpath("//a[@title='Go to next page']/@href").extract_first()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)

        print '\n\n'
        self.log('Saved file %s' % filename)

    def extractCourse(self, response):
        print response.url
        print '\n'
