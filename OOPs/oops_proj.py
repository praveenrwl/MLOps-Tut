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
            pass
        elif user_input == '4':
            pass
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


obj = chatbot()