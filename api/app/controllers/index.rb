require 'gcm'

get "/" do
	return "hello world!! You may need to upgrade your home network security ;)" 
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

