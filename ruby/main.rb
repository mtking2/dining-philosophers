require 'awesome_print'
require_relative 'philosopher'
require_relative 'chopstick'

$g_lock = Mutex.new

chopsticks = Array.new 5 { |e| e = Chopstick.new }
philosophers = []

names = [
  'Aristotle'.red,
  'Confucius'.yellow,
  'Descartes'.green,
  'Kant'.blue,
  'Plato'.purple
]

puts "Philosophers: #{names.join(', ')}\n"
puts "Dinner is served! (Ctl-C to end)\n\n"

names.each_with_index do |ph, i|
  phil = Philosopher.new(
    name: ph,
    left_chopstick: chopsticks[i],
    right_chopstick: chopsticks[(i + 1) % names.size]
  )
  philosophers.push phil
end

trap 'SIGINT' do
  puts "Dinner is over! Waiting for everyone to finish up..."
  philosophers.each(&:stop)
end

philosophers.each(&:join)
