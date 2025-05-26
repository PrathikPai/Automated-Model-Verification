from pacti.contracts import PolyhedralIoContract

#H - conserved quantity of the system

# values came from a specific system 
H0 = 6.95 #initial H value
x_max = 6.82 #max prey population
y_max = 7.78 #max predator population
epsilon = 1e-3 #tolerance level

contract_lotka_volterra = PolyhedralIoContract.from_strings(
    input_vars = [],
    output_vars = ["x", "y", "H"],
    assumptions = [],
    guarantees = ["x >= 0",
                  "y >= 0",
                  f"x <= {x_max}",
                  f"y <= {y_max}",
                  f"H >= {H0 - epsilon}",
                  f"H<= {H0 + epsilon}"
                  ]
)

print(contract_lotka_volterra)
