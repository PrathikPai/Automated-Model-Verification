from pacti.contracts import PolyhedralIoContract

#P - population
K = 100 #carrying capacity

contract_logistic = PolyhedralIoContract.from_strings(
    input_vars = [],
    output_vars = ["P"],
    assumptions = [],
    guarantees = ["P >= 0", f"P <= {K}"]
)

print(contract_logistic)
