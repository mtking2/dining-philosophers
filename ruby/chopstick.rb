class Chopstick < Mutex
  attr_reader :id

  def initialize
    @id = [*('a'..'z'), *('0'..'9')].sample(7).join
  end
end