class CommentsController < ApplicationController
	def create

		# Get Article comment is attached to

		@course = Course.friendly.find(params[:course_id])

		# Create and save comment

		@comment = @course.comments.create(comment_params)

		# Go to the course this comment is associated with

		redirect_to course_path(@course)

	end

	private
		def comment_params
	  		params.require(:comment).permit(:body).merge(commenter: current_user.username)
	  	end
end
