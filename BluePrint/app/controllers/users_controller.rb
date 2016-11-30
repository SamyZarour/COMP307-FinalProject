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