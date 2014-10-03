class CreateNotifications < ActiveRecord::Migration
  def change
  	create_table :notifications do |t|
			t.string :regid
			t.string :url
			t.string :api_key

			t.timestamps
  	end
  end
end
