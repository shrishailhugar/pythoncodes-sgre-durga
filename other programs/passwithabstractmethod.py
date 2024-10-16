from abc import *
class LoanPercentage:
    @abstractmethod
    def get_loan_percenatage(self):
        pass
class HomeLoan(LoanPercentage):
    def get_loan_percenatage(self):
        return 10
class VehicleLoan(LoanPercentage):
    def get_loan_percenatage(self):
        return 15

obj_home=HomeLoan()
obj_vehice=VehicleLoan()
print(obj_home.get_loan_percenatage())
print(obj_vehice.get_loan_percenatage())