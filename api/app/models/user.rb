class User < ActiveRecord::Base
  has_many :devices
  has_many :vulnerabilities
  has_many :notifications

  def notify(notification)
  	gcm = GCM.new(ENV['GOOGLE'])
  	registration_id = [self.regid]
  	message = {data: {title: notification.message}}
  	gcm.send(registration_ids, options)
  end

  def refresh
	## Create a notification object based on vulnerabilities
  end

end
