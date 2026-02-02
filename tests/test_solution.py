## Student Name:
## Student ID: 

"""
Public test suite for the meeting slot suggestion exercise.

Students can run these tests locally to check basic correctness of their implementation.
The hidden test suite used for grading contains additional edge cases and will not be
available to students.
"""
from solution import is_allocation_feasible
import pytest


def test_basic_feasible_single_resource():
    # Basic Feasible Single-Resource
    # Constraint: total demand <= capacity
    # Reason: check basic functional requirement
    resources = {'cpu': 10}
    requests = [{'cpu': 3}, {'cpu': 4}, {'cpu': 3}]
    assert is_allocation_feasible(resources, requests) is True

def test_multi_resource_infeasible_one_overloaded():
    # Multi-Resource Infeasible (one overload)
    # Constraint: one resource exceeds capacity
    # Reason: check detection of per-resource infeasibility
    resources = {'cpu': 8, 'mem': 30}
    requests = [{'cpu': 2, 'mem': 8}, {'cpu': 3, 'mem': 10}, {'cpu': 3, 'mem': 14}]
    assert is_allocation_feasible(resources, requests) is False

def test_missing_resource_in_availability():
    # Missing Resource in Requests
    # Constraint: request references unavailable resource
    # Reason: allocation must be infeasible
    resources = {'cpu': 10}
    requests = [{'cpu': 2}, {'gpu': 1}]
    assert is_allocation_feasible(resources, requests) is False

def test_non_dict_request_raises():
    # Non-Dict Request Raises Error
    # Constraint: structural validation
    # Reason: request must be a dict
    resources = {'cpu': 5}
    requests = [{'cpu': 2}, ['mem', 1]]  # malformed request
    with pytest.raises(ValueError):
        is_allocation_feasible(resources, requests)

"""TODO: Add at least 5 additional test cases to test your implementation."""
def test_resource_feasible_equality():
    # Resources and requests are equal in capacity
    # Constraint: total demand <= capacity
    # Reason: Check edge case with equality
    resources = {'cpu': 5}
    requests = [{'cpu': 5}]  
    assert is_allocation_feasible(resources, requests) is True

    def test_negative_resource_capacity():
    # System must return false when a negative capacity is given
    # Constraint: capacity !< 0
    # Reason: Check negative value handling
    resources = {'cpu': 5}
    requests = [{'cpu': -5}, {'cpu': 10}]  
    assert is_allocation_feasible(resources, requests) is False

    def test_zero_request_handling():
    # Resources and requests can be a zero value
    # Constraint: capacity >=0
    # Reason: Check edge case with 0 handling
    resources = {'cpu': 5}
    requests = [{'cpu': 0}, {'cpu' : 5}]  
    assert is_allocation_feasible(resources, requests) is True

    def test_zero_resource_handling():
    # Resources and requests can handle zero values
    # Constraint: capacity >= 0
    # Reason: Check edge case with zero handling
    resources = {'cpu': 5, 'vram' : 0}
    requests = [{'cpu' : 5}]  
    assert is_allocation_feasible(resources, requests) is True