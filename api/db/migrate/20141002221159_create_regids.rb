class CreateRegids < ActiveRecord::Migration
  def change
  	create_table :regids do |t|
  		t.string :regid

  		t.timestamps
  	end
  end
end
