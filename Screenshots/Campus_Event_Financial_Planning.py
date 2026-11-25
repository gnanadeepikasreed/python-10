
# Campus Event Financial Planning

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Get event expenses
venue_cost = float(input("Enter venue cost: "))
equipment_cost = float(input("Enter equipment cost: "))
catering_cost = float(input("Enter catering cost: "))
transport_cost = float(input("Enter transport cost: "))
certificate_cost = float(input("Enter certificate cost per participant: "))

# Get participant and sponsorship details
participants = int(input("Enter expected number of participants: "))
sponsorship = float(input("Enter sponsorship amount: "))
registration_fee = float(input("Enter registration fee per participant: "))

# Calculate fixed costs
fixed_cost = (venue_cost + equipment_cost +
              catering_cost + transport_cost)

# Calculate total certificate cost
total_certificate_cost = certificate_cost * participants

# Calculate total event cost
total_cost = fixed_cost + total_certificate_cost

# Calculate participant contribution
participant_contribution = participants * registration_fee

# Calculate total available funds
total_funds = participant_contribution + sponsorship

# Calculate sponsorship shortfall
if total_funds < total_cost:
    shortfall = total_cost - total_funds
else:
    shortfall = 0

# Calculate remaining amount
remaining_amount = total_funds - total_cost

# Calculate minimum registrations needed to break even
if registration_fee > certificate_cost:
    required_registrations = (fixed_cost - sponsorship) / (
        registration_fee - certificate_cost
    )

    if required_registrations < 0:
        required_registrations = 0

    # Round up to the next whole participant
    minimum_registrations = int(required_registrations)

    if minimum_registrations < required_registrations:
        minimum_registrations = minimum_registrations + 1

else:
    minimum_registrations = -1


# Display financial report
print("\n===== EVENT FINANCIAL REPORT =====")

print("Venue Cost:", venue_cost)
print("Equipment Cost:", equipment_cost)
print("Catering Cost:", catering_cost)
print("Transport Cost:", transport_cost)
print("Certificate Cost:", total_certificate_cost)

print("Fixed Cost:", fixed_cost)
print("Total Event Cost:", total_cost)

print("Participant Contribution:", participant_contribution)
print("Sponsorship Amount:", sponsorship)
print("Total Available Funds:", total_funds)

if shortfall > 0:
    print("Sponsorship Shortfall:", shortfall)
    print("Event Status: Additional funds required")
else:
    print("Sponsorship Shortfall: 0")
    print("Event Status: Budget Covered")

if remaining_amount > 0:
    print("Remaining Amount:", remaining_amount)
elif remaining_amount < 0:
    print("Deficit Amount:", abs(remaining_amount))
else:
    print("Budget is exactly balanced")

if minimum_registrations == -1:
    print("Break-even is not possible with the given registration fee.")
else:
    print("Minimum Registrations Needed to Break Even:",
          minimum_registrations)

print("\n===== END OF REPORT =====")
