 ActiveRecord::Schema.define(version: 20161130224920) do
  
 
create_table "comments", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
  t.string   "commenter"
  t.text     "body",       limit: 65535
  t.integer  "course_id"
@@ -21,21 +21,21 @@
  t.index ["course_id"], name: "index_comments_on_course_id", using: :btree
end
  
 
create_table "courses", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
  t.string   "title"
  t.string   "faculty"
  t.integer  "crn"
  t.datetime "created_at", null: false
  t.datetime "updated_at", null: false
end
  

create_table "majors", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
  t.string   "name"
  t.datetime "created_at", null: false
  t.datetime "updated_at", null: false
end
  

create_table "users", force: :cascade, options: "ENGINE=InnoDB DEFAULT CHARSET=utf8" do |t|
  t.string   "username"
  t.string   "email"
  t.string   "password_digest"