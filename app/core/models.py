from django.db import models
#  we're going to import the abstract base
#   9 user the base user manager and the permissions mixin.  These are
#  10 all things that are required to extend the Django user model whilst
#  11 making use of some of the features that come with the django user
#  12 model out of the box.  Alright so let's type from
#  13 django.contrib.auth.models import AbstractBaseUser comma base user
#  14 manager comma a and then I'm gonna break a new line here using the
#  15 backslash because I'd like to keep my lines short and easy to read
#  16 and finally we 're going to import the PermissionsMixin.

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin

#  Okay so
#  19 now that we've imported these we can create our user manager class.
#  20 The manager class is a class that provides the helper functions for
#  21 creating a user or creating a super user.  So let's type class
#  22 UserManager and let's extend the base user manager so we're going
#  23 to pull in all of the features that come with the base user manager
#  24 but we're going to override a couple of the functions to handle our
#  25 email address instead of the username that expects.

class UserManager(BaseUserManager):

# Okay so below
# this lets create function def_create user the first argument is
# self the second argument is the email address third argument is
# password but we'll put equals none in case you want to create a
# user that is not active that doesn't have a password and then next
# we will do two asterixis and type extra underscore fields For those
# that don't know this last bit here basically says take any of the
# extra functions that are passed in when you call the create user
# and pass them into extra fields so that we can then just add any
# additional fields that we create without user model.  It's not
# required but it just makes our function a little more flexible
# because every time we add new fields to our user it means we don't
# have to add them in here we can just add them ad hoc as we add them
# to our model.

    def create_user(self, email, password=None, **extra_fields):
        '''Creates and saves a new user'''
        #we do is just at the top here so between the user.self.model and
        #the doc string here we're going to type if not email raise value
        #error and we'll just type a message because this message will
        #sometimes get printed to the screen for the user we'll type "users
        #must have an email address" okay let's save that and let's run our
        #tests again and you can see that the test passes.
        if not email:
            raise ValueError("Users must have an email on creation")

        #the way that the manager works, is that you can
        #get the model that it manages by doing self.model
        # can access the model that the manager is for by just typing self.model so this is
        # effectively the same as creating a new user model and assigning it to the user
        # variable.

        # So lets do user = self.model email equals email and then extra
        # fields.  So this is going to unwind the extra fields into here so
        # it's going to pass the email first and then it's going to pass
        # anything extra that we add.  And the way that the management commands
        # work is you can access the model that the manager is for by just
        # typing self.model so this is effectively the same as creating a new
        # user model and assigning it to the user variable.

        #all we need to do for this is wrap this email here with the normalized
        #email function.  So let's type self.normalize email and make sure
        #we put the brackets around the email and normalize email is a helper
        #function that comes with the base user manager so I'll link to the
        #docs in the resources of this video.
        #
        user = self.model(email=self.normalize_email(email), **extra_fields)

        #         Alright below this we are going to set
        # the password.
        # You can't set the password in this call because the password has to
        # be encrypted it's very important that the password is not stored in clear text
        # and the way you do that is you use the set password helper function that comes
        # with the Django base user or the abstract base user.
        # Alright so we're
        # going to set the password to the password that's passed in here and then
        #and

        user.set_password(password)
        # then next we're going to save the user so we're going to
        # type user.save and we're gonna say using=self.db this bit is just
        # required for supporting multiple databases which we're not gonna
        # worry about in this course but it's good practice to keep it in
        # there anyway

        user.save(using=self._db)

        # And then finally we're going to return the user.  So
        # return user okay so this function when you call create user it
        # creates a new user model it sets the password and it saves the model
        # and then it returns the user model that it has just created.

        return user


#-------------SuperUser========
       #Because we're only
        #really going #to be using the create super user with the
        #command-line we don't need to worry #about the extra fields.
        #So let's create a doc string that says creates and saves
        #a #new super user.
    def create_superuser(self, email,password):
        '''Creates and saves a superuser'''
        #  #And below this let's create our user
        #with an email and password that we're provided,
        #using the function we just defined above.
        user=self.create_user(email,password)
        #
        #
         #So at
        #this #point we have a user the same as the user that is
        #created here now all we need to #do is set user.is_staff =
        #True #and below that we set user.is_superuser #= True

        user.is_superuser = True
        user.is_staff = True
                # #and
        #then because we modified the user we need to save it #just
        #type user.save #using=self._db #and then finally we #return
        #the user.
        user.save(using=self._db)
        return user

        #
        #
        #
        # #Okay now we can save this file head back to our
        #terminal run #our test again and this time the test should
        #pass.  #Okay so now we can see that #we have ran four tests
        #and they all came back okay now we can commit our changes
        #to our git project.  #Before we do that let's just add the
        #flake command so #flake8 and what this will do is it will
        #run linting on our project and #let's just make sure that
        #we don't have any linting failures here.  #Okay you can
        #see we have one failure because we haven't populated our
        #admin.py #yet so this... it doesn't like that this is an
        #un-used #import so I'm just going to add a #a hash to the
        #front here just to basically #disable this line I'm gonna
        #save that and we're gonna be populating this later #so let's
        #not delete it just yet.  #Now let's run the test and the
        #flake again #and everything should come back okay #yep we
        #got a green arrow here no bad output #so now let's just
        #type git add . to add all the files to git and then git
        #commit - a #and let's type the commit message added custom
        #user model #okay now #we can push this up to github and
        #Travis should be triggered and should run our #tests and
        #it will email us if there is any failures with that project.





    # Okay
    # so now we have the manager class let's go ahead and create our
    # model.  So you create the model by just typing class User with a
    # capital U and we're going to extend from the abstract base user and
    # the permissions mixin.Just type AbstractBaseUser and PermissionsMixin.
    # and what this does is it basically gives us all the features that
    # come out of the box with the Django user model but we can then build
    # on top of them and customize it to support our email address.

class User(AbstractBaseUser, PermissionsMixin):
    '''this is a custom user model that supports using email instead of username.'''

    # Alright and now we define the fields of our database model so the
    # first one is going to be email = models.EmailField and with the
    # email field you need to provide a max length = 255 and we want it
    # to be unique so you can only create one user with one email and the
    # models here is the import that's added by default with the create
    # app command so it should be already at the top of your file.
    #it is: from django.db import models

    email = models.EmailField(max_length=255, unique=True)
    # Next we're gonna add a name = models models.CharField just a standard
    # character field with a max length of 255
    name = models.CharField(max_length=255)
    #Next we're gonna add is
    # active = models.BooleanField default=True and this is just to
    # determine if the user in the system is active or not so it allows
    # us to deactivate users that we require.
    is_active = models.BooleanField(default=True)

    # Next we're going to type
    # is_staff = models.BooleanField default = false so users are going
    # to be active the default for active is true so when they create
    # their active but they're not staff so if you want to create staff
    # user you're gonna have to use a special command that we're gonna
    # create in a future video.

    is_staff = models.BooleanField(default=False)

            #Okay so now let's come down let's leave
            #a space here just to separate this next bit because we're going to
            #assign the user manager to the objects attribute.  objects equals
            #user manager and make sure you remember the brackets here at the
            #end so it creates a new user manager for our object.

    objects = UserManager()


    #And then
    #finally we're going to add the USERNAME_FIELD = email so by default
    #the user name field is username and we've customizing that to email
    #so we can use an email address.  Alright now let's save that that's
    #all we need to do for our models.py file

    USERNAME_FIELD = 'email'

    #next we can move on to our
    #settings.py and we can customize our user model in there.



        # So now let's save this and
        #let's open up our terminal and let's run our test again.  Okay now
        #you can see that the test is passed so we have successfully added
        #the normalized email feature.

