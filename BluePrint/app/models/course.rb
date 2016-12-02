class Course < ApplicationRecord
	has_many :comments, dependent: :destroy

	extend FriendlyId
	friendly_id :cid, use: :slugged

	validates :title, presence: true, length: { maximum: 50 }
	validates :cid, presence: true
	validates :terms, presence: true
	validates :instructors, presence: true
	validates :credits, presence: true
	validates :overview, presence: true
end
