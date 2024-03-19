# #Operadores booleanos
# '''
# Operación     Significado
# <             estrictamente menor que
# <=            menor o igual que
# >             estrictamente mayor que
# >=            mayor o igual que
# ==            igual que
# !=            diferente que
# is            igualdad a nivel de identidad (Son el mismo objeto)
# is not        desigualdad a nivel de identidad (no son el mismo objeto)
# '''
# proposicion = not ((10 > 2 + 2) and (5 < 3 or 6 > 1))
# #                       true           false   true
# #                       true            true
# #                               true
# #                               False
# print(proposicion)







#   Resultado     Resultado     A and B     A or B    A ^ B (XOR)
#   Prueba A      Prueba B
#   ----------+--------------+-----------+---------+---------
#   True          True          True        True      False
#   True          False         False       True      True
#   False         True          False       True      True
#   False         False         False       False      False







# x = not ( (3 > 7) and ( 4 > 1 + 1) or (5 < 10 - 3)) #
# #   not      F    and  (     T      or      T  )
# #   not      F    and              T
# #   not             F
# #           T
# #   x = true




