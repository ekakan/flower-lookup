# Importing the linked list
from linked_list import Node, LinkedList

# Importing the flower definitions
from blossom_lib import flower_definitions

# A basic HashMap
# define the HashMap class
class HashMap:
  # constructor that takes a parameter size.
  def __init__(self, size):
    #Save size into self.array_size
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]

  # the hash method
  def hash(self, key):
    new_encode = key.encode()
    return sum(new_encode)

  # the compress method
  def compress(self, hash_code):
    return hash_code % self.array_size

  # the assign method
  def assign(self, key, value):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)

    payload = Node([key, value])
    list_at_array = self.array[array_index]

    for list in list_at_array:
      if list[0] == key:
        list[1] == value

    list_at_array.insert(payload)   ## May need to come change

  # the retrieve method
  def retrieve(self, key):
    hash_code = self.hash(key)
    array_index = self.compress(hash_code)
    list_at_index = self.array[array_index]

    for item in list_at_index:
      if key == item[0]:
        return item[1]

      else:
        return None

blossom = HashMap(len(flower_definitions))
for flower in flower_definitions:
  blossom.assign(flower[0], flower[1])

### Testing the HashMap
val = input('Enter a flower: ')
val_1 = val.lower()
if blossom.retrieve(val_1) != None:
  print('{0} means {1}'.format(val, blossom.retrieve(val_1)))
else:
  print('{0} not in dictionary'.format(val))
