require 'json'

class UsersController < ApplicationController

  attr_accessor :major

  def new
  	@user = User.new
  end

  def create
    @user = User.new(user_params)

    if @user.save
      session[:user_id] = @user.id
      flash[:notice] = "You signed up successfully, you can now sign in!"
      flash[:color]= "valid"
      redirect_to "/logout"
    else
    	flash[:notice] = "Form is invalid please try again"
  		flash[:color]= "invalid"
      redirect_to "/signup"
    end

  end

  def update
    @user = current_user
    User.all.each do |u|
      puts u.username
      debugger(u.major)
    end
    if current_user.update_column(:major, params[:user][:major])
      redirect_to "/profile"
    else
      redirect_to "/"
    end
  end

private

  def user_params
    params.require(:user).permit(:username, :email, :password, :password_confirmation, :major)
  end

  def major_params
    params.require(:user).permit(:major)
  end

end
