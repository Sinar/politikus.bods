# ============================================================================
# DEXTERITY ROBOT TESTS
# ============================================================================
#
# Run this robot test stand-alone:
#
#  $ bin/test -s politikus.bods -t test_ownership_control_statement.robot --all
#
# Run this robot test with robot server (which is faster):
#
# 1) Start robot server:
#
# $ bin/robot-server --reload-path src politikus.bods.testing.POLITIKUS_BODS_ACCEPTANCE_TESTING
#
# 2) Run robot tests:
#
# $ bin/robot /src/politikus/bods/tests/robot/test_ownership_control_statement.robot
#
# See the http://docs.plone.org for further details (search for robot
# framework).
#
# ============================================================================

*** Settings *****************************************************************

Resource  plone/app/robotframework/selenium.robot
Resource  plone/app/robotframework/keywords.robot

Library  Remote  ${PLONE_URL}/RobotRemote

Test Setup  Open test browser
Test Teardown  Close all browsers


*** Test Cases ***************************************************************

Scenario: As a site administrator I can add a Ownership Control Statement
  Given a logged-in site administrator
    and an add Ownership Control Statement form
   When I type 'My Ownership Control Statement' into the title field
    and I submit the form
   Then a Ownership Control Statement with the title 'My Ownership Control Statement' has been created

Scenario: As a site administrator I can view a Ownership Control Statement
  Given a logged-in site administrator
    and a Ownership Control Statement 'My Ownership Control Statement'
   When I go to the Ownership Control Statement view
   Then I can see the Ownership Control Statement title 'My Ownership Control Statement'


*** Keywords *****************************************************************

# --- Given ------------------------------------------------------------------

a logged-in site administrator
  Enable autologin as  Site Administrator

an add Ownership Control Statement form
  Go To  ${PLONE_URL}/++add++Ownership Control Statement

a Ownership Control Statement 'My Ownership Control Statement'
  Create content  type=Ownership Control Statement  id=my-ownership_control_statement  title=My Ownership Control Statement

# --- WHEN -------------------------------------------------------------------

I type '${title}' into the title field
  Input Text  name=form.widgets.IBasic.title  ${title}

I submit the form
  Click Button  Save

I go to the Ownership Control Statement view
  Go To  ${PLONE_URL}/my-ownership_control_statement
  Wait until page contains  Site Map


# --- THEN -------------------------------------------------------------------

a Ownership Control Statement with the title '${title}' has been created
  Wait until page contains  Site Map
  Page should contain  ${title}
  Page should contain  Item created

I can see the Ownership Control Statement title '${title}'
  Wait until page contains  Site Map
  Page should contain  ${title}
