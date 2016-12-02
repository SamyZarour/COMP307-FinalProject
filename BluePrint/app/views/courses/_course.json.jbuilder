json.extract! course, :id, :title, :cid, :terms, :instructors, :credits, :overview, :created_at, :updated_at
json.url course_url(course, format: :json)