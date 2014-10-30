class CreateVulnerabilities < ActiveRecord::Migration
  def change
  	create_table :vulnerabilities do |t|
  		t.references :user
  		t.references :device
  		t.string :type
  		t.string :description
  		t.string :url

  		t.timestamps
  	end
  end
end
