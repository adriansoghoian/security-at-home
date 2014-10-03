get "/" do
  return 'hello world, you fuckers!'
end

post "/register" do
	Regid.create(regid: "test")
end

get "/regids" do 
	erb :regids
end