# Testing must allow reusability of test; it must be traceable and efficient
"""
TYPES OF TESTING:
Unit or Component Testing: Test that is carried out on a specific program before been integrated with other units of the code base.

Integration: Here, all the units are integrated and testing is done.

System Testing: tests all the software you tested against the set requirements and expectations to ensure completeness. This includes measurements of the location of deployed components such as reliability, performance, security and load balancing. It also measures operability in the working environment such as the platform and the operating system. This is the most important stage handled by team of testers. It's also the most critical stage as the shipping of software to the stakeholders and end user happened after this phase.

Acceptance Testing: When the product arrives at this stage, it's generally considered to be ready for deployment. It's expected to be bug free and meet the set standards. The stakeholders and the select few end users are involved in acceptance testing.

Also, there are different ways to categorize the different test types. We have the White Box Test and the Black Box Test
White Box Test - Here, the tester has knowledge of the code design and functionalities.
Black Box Test - it functions with no knowledge of the code design and functionalities and the tester has no idea about the internal implementation

Furthermore, we can categorize different tests as functional, non functional, and maintenance tests
Functional tests are based on the business requirements stated. They determine if the features and functionalities are in line with the expectations.
Non functional tests are more complex to define and involve metrics such as overall performance and quality of the product.
Maintenance tests occur when the system and its operational environment is corrected, changed or extended


TEST AUTOMATION PACKAGES
In programming, the test chosen for automation are the ones with -high repeatability and volume - predictable environment and data -determinant outcomes
Some examples of test automation packages are - PyTest, -Robot, -Selenium
"""
import pytest
import nCrnPrfunctions


def test_factorial():
    assert nCrnPrfunctions.factorial(5) == 120


def test_combination():
    assert nCrnPrfunctions.combination(5, 2) == 10


def test_permutation():
    assert nCrnPrfunctions.permutation(5, 2) == 20
