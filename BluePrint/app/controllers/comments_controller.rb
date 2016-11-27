class CommentsController < ApplicationController
	def create

		# Get Article comment is attached to

		@course = Course.find(params[:course_id])

		# Create and save comment

		@comment = @course.comments.create(comment_params)

		# Go to the course this comment is associated with

		redirect_to course_path(@course)

	end

	private
		def comment_params
	  		params.require(:comment).permit(:commenter, :body)
	  	end
end
