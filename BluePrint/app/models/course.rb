class Course < ApplicationRecord
	
	extend FriendlyId
	friendly_id :name, use: :slugged
	
	has_many :comments, dependent: :destroy

	validates :title, presence: true, length: { maximum: 50 }
	validates :cid, presence: true
	validates :terms, presence: true
	validates :instructors, presence: true
	validates :credits, presence: true
	validates :overview, presence: true
end
