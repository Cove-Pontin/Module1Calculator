'''
CS3250 - Software Development Methods and Tools - Fall 2025
Instructor: Thyago Mota
Student:
Description: Activity 01 - Calculator
'''
import math

class Calculator: 

    DELTA = 0.0000000001

    @staticmethod
    def add(a, b):
        c = a + b;
        return c
    
    @staticmethod
    def subtract(a, b):
        c = a - b
        return c

    @staticmethod
    def multiply(a, b):
        c = a * b
        return c

    @staticmethod
    def divide(a, b): 
        c = a / b
        return c
