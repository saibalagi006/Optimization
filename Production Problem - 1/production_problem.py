import xpress as xp


# Create a new Xpress problem object
p = xp.problem("SimpleMIP")

# Define the decision variables
x_a = p.addVariable(name='x_A', vartype=xp.continuous)
x_b = p.addVariable(name='x_B', vartype=xp.integer)

# Define the objective function: Maximize profit
p.setObjective(20 * x_a + 30 * x_b, sense=xp.maximize)

# Add constraints:
labor_constraint = 2 * x_a + 4 * x_b <= 100
material_constraint = 5 * x_a + 3 * x_b <= 120
p.addConstraint(labor_constraint, material_constraint)
labor_constraint.name = 'labor_constraint'
material_constraint.name = 'material_constraint'


# --- 3. SOLVE THE PROBLEM ---
print("Solving the Mixed-Integer Problem...")
p.solve()

print("value of x_a is ",p.getSolution(x_a))
print("value of x_b is ",p.getSolution(x_b))
