class CreateCourses < ActiveRecord::Migration[5.0]
  def change
    create_table :courses do |t|
      t.string :title
      t.string :cid
      t.string :terms
      t.string :instructors
      t.string :credits
      t.text :overview

      t.timestamps
    end
  end
end
