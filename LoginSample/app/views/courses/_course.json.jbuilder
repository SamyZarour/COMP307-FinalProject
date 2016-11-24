json.extract! course, :id, :title, :faculty, :crn, :created_at, :updated_at
json.url course_url(course, format: :json)