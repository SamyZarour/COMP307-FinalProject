# app/controllers/sessions_controller.rb
require 'json'
require 'net/http'

class SessionsController < ApplicationController

  def new
  end

  def create
    user = User.find_by_email(params[:email])
    # If the user exists AND the password entered is correct.
    if user && user.authenticate(params[:password])
      # Save the user id inside the browser cookie. This is how we keep the user 
      # logged in when they navigate around our website.
      session[:user_id] = user.id
      data = {"username" => params[:email], "password" => params[:password]}

			uri = URI.parse("http://localhost:3000")
			header = {'Content-Type': 'text/json'}
			data = {
      	username: params[:email],
        password: params[:password]
      }

			# Create the HTTP objects
			http = Net::HTTP.new(uri.host, uri.port)
			request = Net::HTTP::Post.new(uri.request_uri, header)
			request.body = data.to_json

			# Send the request
			res = http.request(request)	

      File.open(Rails.root.join('public', 'user_details', "user-#{user.id.to_s}.json"), "w") do |f|
        f.write(res.body)

      end
      redirect_to '/'
    else
    # If user's login doesn't work, send them back to the login form.
      redirect_to '/login'
    end
  end

  def destroy
    session[:user_id] = nil
    redirect_to '/'
  end
  
end
