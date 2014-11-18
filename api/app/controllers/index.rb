require 'gcm'
require 'json'

before do
  headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, DELETE, OPTIONS'
  headers['Access-Control-Allow-Origin'] = 'http://localhost:4567'
  headers['Access-Control-Allow-Headers'] = 'accept, authorization, origin'
  headers['Access-Control-Allow-Credentials'] = 'true'
end

get "/" do
	erb :index_age
end

post "/register" do
	@user = User.create(regid: params["Reg Id"])
	@notification = Notification.create(message: "Welcome! You've successfuly registered.")
	@user.notifications << @notification
	@user.notify(@notification)
end

post "/refresh" do
	p params
end

get "/regids" do 
	erb :regids
end

get "/testjson" do 
	yo = {"test" => [ {"obj1" => 1}, {"obj2" => 2} ]}
	sup = yo.to_json
	return sup
end

post "/testjson" do 
	p params
	return "hello I'm sending data to you!"
end
