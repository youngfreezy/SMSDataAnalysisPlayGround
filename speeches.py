import numpy as np

# P(J) jill stein
p_j = 0.5

# P(F/J) saying the word freedom
p_j_f = 0.1

# P(I/J) saying the word immigration
p_j_i = 0.1

#saying both

p_j_text = p_j * p_j_i * p_j_f

print(p_j_text)

p_g = 0.5

p_g_f = 0.7

p_g_i = 0.2

p_g_text = p_g * p_g_i * p_g_f

print(p_g_text)


total_probability = p_g_text + p_j_text

print('Probability of words freedom and immigration being said by either candidate are: ', format(total_probability))

p_j_fi = p_j_text / total_probability
print('The probability of Jill Stein saying the words Freedom and Immigration: ', format(p_j_fi))

p_g_fi = p_g_text / total_probability
print('The probability of Gary Johnson saying the words Freedom and Immigration: ', format(p_g_fi))