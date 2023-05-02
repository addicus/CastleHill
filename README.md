# InterviewProject
Technical interview for hudl

# To install
install python
pip install behave
pip install selenium
make sure chromedriver is in the root of project or in path 


# to run 
python -m behave features\login.feature -D BROWSER=Chrome (other features are not fully working and are there for examples) 

# Credential note 
Login tests will fail without valid credentials 

Enter credentials into setup.cfg and the login smoketest feature file shown below :

Scenario Outline: multiple login smoketests
      Given User is on login screen
      When user logs in with "<user>" and "<password>"
      Then user should <result>
      Examples: Credentials
                  | user           | password       | result               |
                  | entervaliduser | entervalidpass | be authenticated     |
                  | user2          | pwd2           | not be authenticated |# Credentials 
                note  

# Description 
Small suite of tests using behave to automate authentication

# Additional Notes

## Functioning Login feature scenarios
      User authenticates 
            (uses valid credentials from setup.cfg)
      User submits blank authentication form: 
            checks for correct error message when submitting blank form
      User fails authentication: 
            checks for correct error message when incorrect credentials are supplied
      User logs in with organization: 
            not implemented as I was not supplied with an organizational login, but left the feature file here.
      User is not registered with an organization: 
            checks for correct error when attempting to log in through an organization with an account that is not registered to one. 
      Multiple login smoketests: 
            This feature file is used to smoke test username and password lists when extensive testing is needed. username and password is supplied through the feature file, as well as the expected result.
      
      I also started to flesh out several other features, and completed one for a profile update. This was a useful excersise because I soon realized my initial login test was a bit fragile. Most of these are not implemented but I left the feature files in place to show what i would move on to. 

## Not implemented
      I would have liked to implement tests on password reset emails but this seemed a bit out of scope and inefficient using selenium alone. Likewise signing up seemed out of scope as well so I did not create those cases. 
      Likewise I noticed there are custom data-qaid selectors, I would probably refactor to use those wherever possible instead of using messy xpath or css selectors
      


                  
                  
                  
