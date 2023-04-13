# loanCalculator_test.py

# assert expression
## if true nothing happens
## if false raises AssertionError

# create virtual environment and activate
# pip install pytest
# pip install pytest-cov

# run tests with python -m pytest -s
# compare -s and -v when running the tests
# run coverage tests with python -m pytest --cov
import builtins
import pytest
from unittest.mock import patch
from pytest import approx
from oop_loan_pmt import *


########## Unit Tests ##########
def test_setting_initial_amount():
    """
    GIVEN a user enters their loan details
    WHEN the loan object's calculateDiscountFactor function is called
    THEN the discount factor is accurately calculated
    """
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    
    assert (loan.loanAmount == 100000)
    assert (loan.annualRate == 0.06)
    assert (loan.numberOfPmts == 360)
    assert (loan.periodicIntRate == 0.005)
    assert (loan.discountFactor == 0.0)
    assert (loan.loanPmt == 0)


# Tests Discount Factor 
def test_calculateDiscountFactor():
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    loan.calculateDiscountFactor()
    
    assert (loan.discountFactor == approx(166.79, rel=1e-3))    

def test_getDiscountFactor():
    
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    
    assert (loan.getDiscountFactor() == loan.discountFactor) 


# Tests Loan Pmt 
def test_calculateLoanPmt():
    """
    GIVEN a user enters their loan details
    WHEN the loan object's calculateLoanPmt function is called
    THEN the loan payment is accurately calculated
    """
    loan = Loan(loanAmount=100000, numberYears=30, annualRate=0.06)
    loan.calculateLoanPmt()
    
    assert (loan.loanPmt == approx(599.55, rel=1e-3))

def test_getLoanPmt():
    loan = Loan(100000, 30, 0.06)
    
    assert (loan.getLoanPmt() == loan.loanPmt)


######### Functional Tests ##########

# Test collectLoanDetails() function
def test_collectLoanDetails():
    with patch.object(builtins, 'input', side_effect=['100000', '30', '0.06']):
        loan = collectLoanDetails()
        assert loan.loanAmount == 100000.0
        assert loan.numberOfPmts == 360
        assert loan.annualRate == 0.06

# Test main() function
def test_main(capsys):
    with patch.object(builtins, 'input', side_effect=['100000', '30', '0.06']):
        main()
        captured = capsys.readouterr()
        assert captured.out == "Your monthly payment is: $599.55\n"