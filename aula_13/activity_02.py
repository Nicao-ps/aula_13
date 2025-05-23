import numpy as np

house_values = np.array([150, 180, 200, 220, 250, 280, 300, 320, 400, 1500])
print(house_values * 1000)

meann = np.mean(house_values)
print('\nMédia: R$ ' + '{:.2f}'.format(meann * 1000))

mediann = np.median(house_values)
print('\nMediana: R$ ' + '{:.2f}'.format(mediann * 1000))

q2 = np.quantile(house_values, 0.50)
print('\n2º Quartil: R$ ' + '{:.2f}'.format(q2 * 1000))
