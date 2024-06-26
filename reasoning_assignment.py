# -*- coding: utf-8 -*-
"""Reasoning_assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vf4thnIpWieAhuR6D_mp94Rbdq3PUEsU

# Team Members

*   Mostafa Aly Hashem , 20210394
*   Adham Tarek Abdelaziz, 20210051
"""

def Implication_Elimination(expression):
  if expression == "∀x P(x) -> ∀x R(x)":
    result = "¬(∀x P(x)) ∨ ∀x R(x)"
  elif expression == "∀x ¬P(x) -> ∀x R(x)":
    result = "¬(∀x ¬P(x)) ∨ ∀x R(x)"
  elif expression == "∀x P(x) -> ∀x ¬R(x)":
    result = "¬(∀x P(x)) ∨ ∀x ¬R(x)"
  elif expression == "∀x ¬P(x) -> ∀x ¬R(y)":
    result = "¬(∀x ¬P(x)) ∨ ∀x ¬R(x)"
  return result

expr1 = "∀x P(x) -> ∀x R(x)"
expr2 = "∀x ¬P(x) -> ∀x R(x)"
expr3 = "∀x P(x) -> ∀x ¬R(x)"
expr4 = "∀x ¬P(x) -> ∀x ¬R(y)"
res1=Implication_Elimination(expr1)
res2=Implication_Elimination(expr2)
res3=Implication_Elimination(expr3)
res4=Implication_Elimination(expr4)
print(res1)
print(res2)
print(res3)
print(res4)

def Add_Not(expression):
  final_result = f"¬({expression})"
  return final_result

print(Add_Not("¬(∀x P(x)) ∨ ∀x R(x)"))
print(Add_Not("¬(∀x ¬P(x)) ∨ ∀x R(x)"))
print(Add_Not("¬(∀x P(x)) ∨ ∀x ¬R(x)"))
print(Add_Not("¬(∀x ¬P(x)) ∨ ∀x ¬R(x)"))

def move_negation_inward(expression):
  if expression == "¬(¬(∀x P(x)) ∨ ∀x R(x))":
    expression = "¬(∃x ¬P(x) ∨ ∀x R(x))"
  elif expression == "¬(¬(∀x ¬P(x)) ∨ ∀x R(x))":
    expression = "¬(∃x P(x) ∨ ∀x R(x))"
  elif expression == "¬(¬(∀x P(x)) ∨ ∀x ¬R(x))":
    expression = "¬(∃x ¬P(x) ∨ ∀x ¬R(x))"
  elif expression == "¬(¬(∀x ¬P(x)) ∨ ∀x ¬R(x))":
    expression = "¬(∃x P(x) ∨ ∀x ¬R(x))"
  return expression

def Apply_DeMorgan(expression):
  # ¬¬ = ""
  # ¬ ∀x = ∃x
  # ¬ ∃x = ∀x
  # ¬ (- ∨ -) = (¬ - ∧ ¬ -)
  if expression == "¬(∃x ¬P(x) ∨ ∀x R(x))":
    expression = "(∀x P(x) ∧ ∃x ¬R(x))"
  elif expression == "¬(∃x P(x) ∨ ∀x R(x))":
    expression = "(∀x ¬P(x) ∧ ∃x ¬R(x))"
  elif expression == "¬(∃x ¬P(x) ∨ ∀x ¬R(x))":
    expression = "(∀x P(x) ∧ ∃x R(x))"
  elif expression == "¬(∃x P(x) ∨ ∀x ¬R(x))":
    expression = "(∀x ¬P(x) ∧ ∃x R(x))"
  return expression

expr = "∀x ¬P(x) -> ∀x R(x)"
step1 = Implication_Elimination(expr)
step2 = Add_Not(step1)
step3 = move_negation_inward(step2)
step4 = Apply_DeMorgan(step3)
print(step4)
# "(∀x ¬P(x) ∧ ∃x ¬R(x))"

def standardize_variable_scope(expression):
  if expression == "(∀x P(x) ∧ ∃x ¬R(x))":
    expression = "(∀x P(x) ∧ ∃y ¬R(y))"
  elif expression == "(∀x ¬P(x) ∧ ∃x ¬R(x))":
    expression = "(∀x ¬P(x) ∧ ∃y ¬R(y))"
  elif expression == "(∀x P(x) ∧ ∃x R(x))":
    expression = "(∀x P(x) ∧ ∃y R(y))"
  elif expression == "(∀x ¬P(x) ∧ ∃x R(x))":
    expression = "(∀x ¬P(x) ∧ ∃y R(y))"
  return expression

def to_prenex_form(expression):
  if expression == "(∀x P(x) ∧ ∃y ¬R(y))":
    expression = "∀x ∃y P(x) ∧ ¬R(y)"
  elif expression == "(∀x ¬P(x) ∧ ∃y ¬R(y))":
    expression = "∀x ∃y ¬P(x) ∧ ¬R(y)"
  elif expression == "(∀x P(x) ∧ ∃y R(y))":
    expression = "∀x ∃y P(x) ∧ R(y)"
  elif expression  == "(∀x ¬P(x) ∧ ∃y R(y))":
    expression = "∀x ∃y ¬P(x) ∧ R(y)"
  return expression

def skolemize(expression):
  # y = f(x) for ∀x ∃y P(x,y) = P(x,f(x)) "Skolem function"
  # ∃y P(y) = P(a) --> Skolem Constant
  if expression == "∀x ∃y P(x) ∧ ¬R(y)":
    expression = "∀x P(x) ∧ ¬R(a)"
  elif expression == "∀x ∃y ¬P(x) ∧ ¬R(y)":
    expression = "∀x ¬P(x) ∧ ¬R(a)"
  elif expression == "∀x ∃y P(x) ∧ R(y)":
    expression = "∀x P(x) ∧ R(a)"
  elif expression == "∀x ∃y ¬P(x) ∧ R(y)":
    expression = "∀x ¬P(x) ∧ R(a)"
  return expression

def eliminate_universal(sentence):
  if sentence == "∀x P(x) ∧ ¬R(a)":
    sentence = "P(x) ∧ ¬R(a)"
  elif sentence == "∀x ¬P(x) ∧ ¬R(a)":
    sentence = "¬P(x) ∧ ¬R(a)"
  elif sentence == "∀x P(x) ∧ R(a)":
    sentence = "P(x) ∧ R(a)"
  elif sentence == "∀x ¬P(x) ∧ R(a)":
    sentence = "¬P(x) ∧ R(a)"
  return sentence

def convert_to_cnf(expression):
  step1 = Implication_Elimination(expression)
  step2 = Add_Not(step1)
  step3 = move_negation_inward(step2)
  step4 = Apply_DeMorgan(step3)
  step5 = standardize_variable_scope(step4)
  step6 = to_prenex_form(step5)
  step7 = skolemize(step6)
  step8 = eliminate_universal(step7)
  return step8

def split_clauses(expression):
    clauses = expression.split("∧")
    clauses = [clause.strip() for clause in clauses]
    return clauses

# printing the set of clauses
expression1 = convert_to_cnf("∀x P(x) -> ∀x R(x)")
expression2 = convert_to_cnf("∀x ¬P(x) -> ∀x R(x)")
expression3 = convert_to_cnf("∀x P(x) -> ∀x ¬R(x)")
expression4 = convert_to_cnf("∀x ¬P(x) -> ∀x ¬R(y)")
expr1 = split_clauses(expression1)
expr2 = split_clauses(expression2)
expr3 = split_clauses(expression3)
expr4 = split_clauses(expression4)
print(expr1)
print(expr2)
print(expr3)
print(expr4)