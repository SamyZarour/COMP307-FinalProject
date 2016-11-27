class CreateCourses < ActiveRecord::Migration[5.0]
  def change
    create_table :courses do |t|
      t.string :title
      t.string :faculty
      t.integer :crn

      t.timestamps
    end
  end
end
