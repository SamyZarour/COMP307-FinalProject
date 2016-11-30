class UsersController < ApplicationController

  attr_accessor :major

  def new
  	@user = User.new
  end

  def create
    @user = User.new(user_params)

    if @user.save
      session[:user_id] = @user.id
      flash[:notice] = "You signed up successfully"
      flash[:color]= "valid"
      redirect_to "/"
    else
    	flash[:notice] = "Form is invalid"
  		flash[:color]= "invalid"
      render "new"
    end

  end

private

  def user_params
    params.require(:user).permit(:username, :email, :password, :password_confirmation)
  end
end