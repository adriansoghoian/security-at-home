class CreatePlayers < ActiveRecord::Migration
  def change
    create_table :players do |t|
      t.belongs_to :user
      t.belongs_to :game
      t.string :playertype

      t.timestamps
    end
  end
end
