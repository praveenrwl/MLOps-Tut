# lst = [1,2,3]
# my_str = "mlops playlist"
# my_int = 195

# # print(type(lst))
# a = 'x'
# b = 'y'

# print(a+b)


from oops_proj import chatbot

# Static method
user1 = chatbot()
print(user1.id)

chatbot.set_id(10)
user2 = chatbot()
print(user2.id)

# user2 = chatbot()
# print(user2.id)

# user3 = chatbot()
# print(user3.id)

# Encapsulation
# user1 = chatbot()
# print(user1.name)
# print(user1._chatbot__name)



# Getter and Setter
# print(user1.get_name())
# user1.set_name('Agent Ace')
# print(user1.get_name())

# Function VS Method Below
# user1 = chatbot()
# lst = [1,2,3,4]

# a1 = len(lst)
# print(a1)

# user1 = chatbot()
# user1.send_msg()

