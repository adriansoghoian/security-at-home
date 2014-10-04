require 'gcm'

get "/" do
  gcm = GCM.new(ENV['GOOGLE'])
	registration_ids = ["APA91bFDuc9x7y-E4aOYJSY5OjJh40MVJ0mZVtgdc4-iCSQ_dHbf9fIDU8GHdBMn96CTT7mBwJefo8znkthvVB8P8g2_w_lcq5LQ3VB0x2NHZXndwVNrk4Badjy2U0O4MUNZndqX7XiRkkkF0C1k84jaFyHYSgfRiOXr9O9RxmNep6fnNrtT0ik"]
	options = {data: {title: "YOUR WIFI SUCKS!!"}}
	response = gcm.send(registration_ids, options)
	p response
	return "hello world, you weak-wified fuckers!!" 
end

post "/register" do
	regid = Regid.create(regid: params["Reg Id"])
	gcm = GCM.new(ENV['GOOGLE'])
	registration_ids = [regid]
	options = {data: {title: "YOUR WIFI SUCKS!!"}}
	gcm.send(registration_ids, options)
end

get "/regids" do 
	erb :regids
end

