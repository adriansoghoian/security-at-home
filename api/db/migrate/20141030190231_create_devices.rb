class CreateDevices < ActiveRecord::Migration
  def change
  	create_table :devices do |t|
  		t.references :user
  		t.string :form_factor
  		t.string :type
  		t.string :software

  		t.timestamps
  	end
  end
end
