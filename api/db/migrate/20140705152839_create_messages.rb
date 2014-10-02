class CreateMessages < ActiveRecord::Migration
  def change
  	create_table :messages do |t|
  		t.text :content
  		t.belongs_to :user
  		t.belongs_to :game

  		t.timestamps
  	end
  end
end
