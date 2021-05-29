# Global variables
global users_list
class Users:
    '''

    Class that generates new instances of users

    '''
   user_list = [] # Empty user list

   def __init__(self,user_name,password): 

       '''

       __init__ method that helps us define properties for our users.

       '''

       self.user_name = user_name
       self.password = password

      def save_user(self):

          '''
          save_user method saves user objects into user_list

          ''' 

          Users.user-list.append(self)

          def delete_user(self):

              '''
              delete_user method deletes a saved user from the user_list

              '''
              

          