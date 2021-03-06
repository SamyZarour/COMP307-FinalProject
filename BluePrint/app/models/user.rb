class User < ApplicationRecord
	attr_accessor :major
	has_secure_password

	EMAIL_REGEX = /\A[A-Z0-9._%+-]+@mail.mcgill+\.[A-Z]{2,4}\z/i
	validates :username, :presence => true, :uniqueness => true, :length => { :in => 3..20 }
	validates :email, :presence => true, :uniqueness => true, :format => EMAIL_REGEX
	validates :password, :confirmation => true #password_confirmation attr
	validates_length_of :password, :in => 6..20, :on => :create
end
