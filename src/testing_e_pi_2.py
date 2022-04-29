import numpy as np
from tests import *
import pickle
import pandas as pd


# Loading data
exp_e = pickle.load(open('../Data/binary_expansion_e.pkl', "rb"))
exp_pi = pickle.load(open('../Data/binary_expansion_pi.pkl', "rb"))
exp_sqrt2 = pickle.load(open('../Data/binary_expansion_sqrt2.pkl', "rb"))

# DataFrame to store results
results = pd.DataFrame({'test': ['Monobit', 'Block', 'Second-level'],
                        'e': np.zeros(3),
                        'pi': np.zeros(3),
                        'sqrt2': np.zeros(3)})
# Single testing
# Monobit
results.loc[0, 'e'] = monobit_test(exp_e['numbers'], exp_e['Modulus'])
results.loc[0, 'pi'] = monobit_test(exp_pi['numbers'], exp_pi['Modulus'])
results.loc[0, 'sqrt2'] = monobit_test(exp_sqrt2['numbers'], exp_sqrt2['Modulus'])
# Block
results.loc[1, 'e'] = block_test(exp_e['numbers'], M=1005)
results.loc[1, 'pi'] = block_test(exp_pi['numbers'], M=1005)
results.loc[1, 'sqrt2'] = block_test(exp_sqrt2['numbers'], M=1004)
# Second-level testing
splitted_e = split_bit_str(list_tobit_string(exp_e['numbers']), 2000)
res_e = np.array(list(map(monobit_test, splitted_e)))
results.loc[2, 'e'] = second_level_test(res_e)

splitted_pi = split_bit_str(list_tobit_string(exp_pi['numbers']), 2000)
res_pi = np.array(list(map(monobit_test, splitted_pi)))
results.loc[2, 'pi'] = second_level_test(res_pi)

splitted_sqrt2 = split_bit_str(list_tobit_string(exp_sqrt2['numbers']), 2000)
res_sqrt2 = np.array(list(map(monobit_test, splitted_sqrt2)))
results.loc[2, 'sqrt2'] = second_level_test(res_sqrt2)


# Saving results
path_to_save = '../Results/irrational_testing.csv'
results.to_csv(path_to_save, index=False)
print(f'Results saved in {path_to_save}.')
