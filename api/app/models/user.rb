class User < ActiveRecord::Base
  has_many :devices
  has_many :vulnerabilities
  has_many :notifications

end
