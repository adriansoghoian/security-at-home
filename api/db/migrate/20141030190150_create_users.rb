class CreateUsers < ActiveRecord::Migration
  def change
  	create_table :users do |t|
  		t.string :regid
  		t.string :username
  		t.string :password
  		t.string :password_confirmation

  		t.timestamps
  	end
  end
end
