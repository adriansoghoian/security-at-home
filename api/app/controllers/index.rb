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
	regid = params["Reg Id"]
	@user = User.find_by_regid(regid)
	## Create a notification object based on vulnerabilities
	## @user.notifications << @notification 
	## @user.notify(@notification) 
end

get "/regids" do 
	erb :regids
end

