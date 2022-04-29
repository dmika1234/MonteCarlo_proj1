from tests import *
import pandas as pd


results = pd.DataFrame({'test': ['Monobit', 'Block', 'Runs',
                                 'chi-square', 'KS', 'Second-level1', 'Second-level2'],
                        'p_value': np.zeros(7)})

np.random.seed(2022)
gen = RC4(32)
n = 2 ** 15
R = 1000
# Single testing
res = gen.generate_numbers(n=n, key=np.random.randint(0, 31, 5))
resb = convert_int_tobin(res, 32)
ress = list_tobit_string(resb)
results.loc[0, 'p_value'] = monobit_test(resb, 32)
results.loc[1, 'p_value'] = block_test(resb, n / 32)
results.loc[2, 'p_value'] = runs_test(ress)
results.loc[3, 'p_value'] = chi_square_test(res)
results.loc[4, 'p_value'] = ks_test(resb)
# Second-level testing
# One long sequence
res2 = gen.generate_numbers(n=n * R, key=np.random.randint(0, 31, 10))
resb2 = convert_int_tobin(res2, 32)
p_vals1 = np.zeros(R)
for i in np.arange(R):
    p_vals1[i] = monobit_test(resb2[(0 + i):(R * n - 1)], 32)

results.loc[5, 'p_value'] = second_level_test(p_vals1)
# Multiple keys
p_vals2 = np.zeros(R)
for i in np.arange(R):
    key = np.random.randint(0, 31, 3)
    res3 = gen.generate_numbers(n=n, key=key)
    resb3 = convert_int_tobin(res2, 32)
    p_vals2[i] = monobit_test(resb3, 32)

results.loc[6, 'p_value'] = second_level_test(p_vals2)

# Saving results
path_to_save = '../Results/rc4_testing.csv'
results.to_csv(path_to_save, index=False)
print(f'Results saved in {path_to_save}.')
