import streamlit as st

class Equacao:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def __str__(self):
        return f"A = {self.a}, B = {self.b}, C = {self.c}"

    def calc_delta(self):
        