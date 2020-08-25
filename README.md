Trying out Redis as a way to get remote signatures more easily. It's an alternative to using action arguments, `force_ask`, and such.

These tests are a bit outdated, but they can be the foundation of more extensive tests:

1:
1. User signs on computer
1. Sends to both cosigners by email
1. Both sign on computer

2:
1. User signs on phone and finishes on phone.
1. Sends to both cosigners by text
1. Both sign on phone

3:
1. User says they’ll sign on phone
1. User changes their mind before opening the site
1. User signs on the computer
1. Sends to both cosigners by email
1. Cosigner 1 signs on computer
1. Cosigner 2 signs on phone

4:
1. User says they’ll sign on phone
1. User goes to first page of site on phone
1. User changes their mind
1. User signs on a different phone
1. User finishes on computer
1. User texts both cosigners
1. Cosigner 1 says they’re not willing.
1. Cosigner 1 visits the site again on computer and signs on computer.
1. Cosigner 2 whatever

5:
1. User says they’ll sign on phone
1. gets to signature on phone
1. user changes their mind
1. user signs on computer
1. Tries to sign on phone, but instead taken to… not sure. ‘Finish on phone?’ question?
1. User emails both cosigners
1. Cosigner 1 says they’re not willing
1. Cosigner 1 visits the site again on phone and signs on phone
1. Cosigner 2 whatever

6:
1. User says they’ll sign on phone
1. User signs on phone
1.  User changes their mind and is taken to the page to send link to cosigners (because already have signature)
1. User emails both cosigners
1. Cosigner 1 starts on computer
1. Cosigner 1 switches to phone
1. Cosigner 1 signs on phone
1. Cosigner 1 changes mind and tries to sign on computer
1. Cosigner 1 taken to final page instead
1. Cosigner 2 whatever

7:
1. User says they’ll sign on phone, signs on phone, but tries to change their mind and is taken to the ‘done’ page (because they’ve already signed)
1. Cosigners do whatever

8:
1. User says to sign on phone
1. User signs and moves on to emails
1. User tries to continue on computer and… what happens?
1. Cosigners do whatever