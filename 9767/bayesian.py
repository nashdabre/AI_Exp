from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Define the Bayesian Network structure
model = BayesianModel([('Burglary', 'Alarm'),
                       ('Earthquake', 'Alarm'),
                       ('Alarm', 'MaryCalls'),
                       ('Alarm', 'JohnCalls')])

# Define the conditional probability distributions
cpd_burglary = TabularCPD(variable='Burglary', variable_card=2, values=[[0.999], [0.001]])
cpd_earthquake = TabularCPD(variable='Earthquake', variable_card=2, values=[[0.998], [0.002]])

cpd_alarm = TabularCPD(variable='Alarm', variable_card=2,
                       values=[[0.999, 0.71, 0.06, 0.05],
                               [0.001, 0.29, 0.94, 0.95]],
                       evidence=['Burglary', 'Earthquake'],
                       evidence_card=[2, 2])

cpd_mary_calls = TabularCPD(variable='MaryCalls', variable_card=2,
                            values=[[0.99, 0.3],
                                    [0.01, 0.7]],
                            evidence=['Alarm'],
                            evidence_card=[2])

cpd_john_calls = TabularCPD(variable='JohnCalls', variable_card=2,
                            values=[[0.95, 0.1],
                                    [0.05, 0.9]],
                            evidence=['Alarm'],
                            evidence_card=[2])

# Add the conditional probability distributions to the model
model.add_cpds(cpd_burglary, cpd_earthquake, cpd_alarm, cpd_mary_calls, cpd_john_calls)

# Check the model for consistency
assert model.check_model()
#print(model.check_model())

# Perform inference
inference = VariableElimination(model)

q= inference.query(variables=['Alarm'])
print(q)

# Calculate the probability of Alarm given evidence that John didn't here the alarm
q = inference.query(variables=['Alarm'], evidence={'JohnCalls': 0})
print(q)

#comput probability of alram given evidence that mary heard the alarm
q = inference.query(variables=['Alarm'], evidence={'MaryCalls': 1})
print(q)


