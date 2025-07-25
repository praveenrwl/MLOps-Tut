class chatbot:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.login = False
        self.menu()

    def menu(self):
        user_input = input('''Welcome to Chatbot !! How would you like to proceed?
        1. Press 1 to SignUp!!
        2. Press 2 to SignIn
        3. Press 3 to write a post
        4. Press 4 to message a friend
        5. Press any other key to exit
                           
        Type number >> ''')

        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.send_msg()
        else:
            exit()
         
# obj = chatbot()

    def signup(self):
        email = input('Enter your email here: ')
        password2 = input('Enter your password here: ')
        self.username = email
        self.password = password2
        print('You have Signed Up Successfully')
        self.menu()

    def signin(self):
        # if self.username == '' and self.password == '':
        if self.signup == False:
            print("Please Signup by Pressing 1 in Main Menu")
        else:
            uname = input('Enter your email here: ')
            password3 = input('Enter your password here: ')
            if self.username == uname and  self.password == password3:
                print('You have signed in successfully')
                self.loggedin = True
            else:
                print('Invalid username or password')

            print('\n')
            self.menu()

    # Method
    def my_post(self):
        if self.loggedin == True:
            txt = input('Enter your message here: ')
            print(f'Your following content is posted -> {txt} ')
        else:
            print("You need to sign in first")

    def send_msg(self):
        if self.loggedin == True:
            txt = input('Enter your message here: ')
            name = input('Whom do you want to message: ')
            print(f'Your following message is sent to {name} -> {txt} ')
        else:
            print("You need to sign in first")

# Object
obj = chatbot()