class Notification < ActiveRecord::Base
	require 'httparty'

	def initialize(regid) ## Hits post request, creates a new notification object. 
		@regid = regid
		@url = 'https://android.googleapis.com/gcm/send'
		@api_key = ENV['GOOGLE']
	end

	def notify
		HTTParty.post('https://android.googleapis.com/gcm/send', :query => { "data" => {"title" => "Test Title", "message" => "Test message"}, "registration_ids" => ["APA91bFDuc9x7y-E4aOYJSY5OjJh40MVJ0mZVtgdc4-iCSQ_dHbf9fIDU8GHdBMn96CTT7mBwJefo8znkthvVB8P8g2_w_lcq5LQ3VB0x2NHZXndwVNrk4Badjy2U0O4MUNZndqX7XiRkkkF0C1k84jaFyHYSgfRiOXr9O9RxmNep6fnNrtT0ik"] },
			:headers => { 'Content-Type' => 'application/json', 'Authorization' => ENV['GOOGLE']})
	end

end