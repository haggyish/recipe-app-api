from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''Test creating a new user with an email is successful'''
        email = 'test@londondev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email, password =password
        )
        self.assertEquals(user.email, email)
        self.assertTrue(user.check_password(password))


        #second part of the user domain name for email addresses is
        #case-insensitive.  That means that the case of the last part so
        #that's the domain like @londonappdev.com is not case-sensitive so
        #we don't want that to be case sensitive when the users login to the
        #system.  Because of this what we're going to do is we're going to
        #make that part all lowercase every time a new user registers.  So
        #let's go ahead and add this feature to our create user function.
        #Alright so we're going to load up our tests here for our test models.
        #And below the tests that we created in the last video we're gonna
        #add def test_new_user_email_normalized add the self argument here


    def test_new_user_email_normalized(self):
            '''test that the email for a new user is normalized'''

        # Alright and below this let's
        #create an email variable and let's say test@londonappdev.com all
        #uppercase for the domain part and below this
            email = 'test@LONDONAPPDEV.COM'
        #
        #  let's create our user
        #so user = get_user_model
        #.objects.create_user
        #then the email and we're just gonna add a random string for the
        #password and since we have already tested the password we don't
        #need to test the password again so this is basically just a throwaway
        #string that's going to be assigned as the password

            user = get_user_model().objects.create_user(email,'test123')
        #
        #
        #  and then below
        #let's type self.assertEqual(user.email, is equal to email.lower so
        #this is just the string function with Python that makes the string
        #lower case.

            self.assertEqual(user.email,email.lower())
        #


        #Next we're going to add validation to ensure that an email field
        #has actually been provided when the create user function is called.
        #So let's open up our tests.  test_models.py and below this we're
        #going to add a new test def test new user invalid email add the
        #self argument

    def test_new_user_invalid_email(self):
    # and then let's write a description here test creating
    #user with no email raises error.
        '''if invalid email raises error when creating user via email'''
    #
    #
    #  Okay so what we want is we want
    #to make sure that if we call the create user function and we don't
    #pass an email address so if we just pass a blank string or we just
    #pass a non value then we want to make sure we raise a value error
    #that says the email address was not provided.
    #  Okay so what we'll
    #do is we'll use the with self.assertRaises and then in the brackets
    #of the assertRaises we type ValueError

    # and what this does is anything that
    #we run in here should raise the value error.  And if it doesn't
    #raise a value error then this test will fail.

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')
    #  Okay so what we're
    #gonna do is we're gonna type get_user_model().objects.create_user


       #Now that we have our create user function finished there's
        #just one more #function that we need to add to our user
        #model manager and that is the create #super user function.
        #Create super user is a function used by the Django CLI
        #when #we're creating new users using the command line.  #So
        #we want to make sure #it's included in our custom user model
        #so that we can take advantage of the #Django management
        #command for creating a super user.  #Alright so let's add
        #this #function to our user model.  #We're going to start
        #as always by adding a test to #test models.py #The test is
        #going to be to test that a super user is created #when we
        #call create super user and that it is assigned #the is staff
        #and the is super user settings.  #So let's type #user or
        #first let's type #our function #def test_create_new_superuser
        #and give it the doc string #test creating a new super user.

    def test_create_new_superuser(self):
        '''test creating a new superuser'''
        #Below this let's create our user with #user = get_user_model
        #.objects.create_superuser #and let's pass in an email
        #address we don't need to worry about saving the email
        #address as a variable #we'll just type test@londonappdev.com
        #and below this we'll just type a #password test123 and
        user= get_user_model().objects.create_superuser('test@londonddeve.com', 'test123')

        #then let's do an assertion here so let's say #a self.assertTrue
        #user.is_superuser #and self.assertTrue #user.is_staff #You
        #may be wondering where the is_superuser field is on our
        #user model #because we didn't add it here but it is included
        #as part of the #PermissionsMixin.
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

         #Okay so now let's save
        #this and go back to our terminal #and lets run our tests.
        #And you can see that the tests fail because the create
        #super #user doesn't exist so let's go ahead and implement
        #this feature and make this #test pass.  #So head over to
        #models.py below the create user.
        #







