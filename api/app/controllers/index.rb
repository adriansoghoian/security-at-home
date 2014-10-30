require 'gcm'

get "/" do
	return "hello world!! You may need to upgrade your home network security ;)" 
end

post "/register" do
	regid = Regid.create(regid: params["Reg Id"])
end

post "/notify" do 
	gcm = GCM.new(ENV['GOOGLE'])
	registration_ids = [Regid.all.last.regid]
	options = {data: {title: "YOUR WIFI SUCKS!!"}}
	gcm.send(registration_ids, options)
end

get "/regids" do 
	erb :regids
end

