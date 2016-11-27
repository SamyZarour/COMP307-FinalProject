class Course < ApplicationRecord
	has_many :comments, dependent: :destroy

	validates :title, presence: true, length: { maximum: 50 }
	validates :faculty, presence: true
	validates :crn, presence: true
end
